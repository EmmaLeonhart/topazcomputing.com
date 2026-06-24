"""Smoke tests for the topazcomputing.com static site."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent


def read(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def test_cname_is_topazcomputing():
    assert read("CNAME").strip() == "topazcomputing.com"


def test_index_has_brand_and_tagline():
    html = read("index.html")
    assert "Topaz" in html
    assert "Topaz&nbsp;Computing" in html or "Topaz Computing" in html
    assert "learns in real time" in html


def test_sutra_link_points_to_new_subdomain():
    html = read("index.html")
    assert "https://sutra.topazcomputing.com" in html
    assert "sutra.noldor.tech" not in html


def test_no_noldor_mention_in_shipped_files():
    for name in ("index.html", "404.html", "styles.css", "robots.txt", "sitemap.xml"):
        assert "noldor" not in read(name).lower(), f"'noldor' leaked into {name}"


def test_robots_points_to_sitemap():
    assert "https://topazcomputing.com/sitemap.xml" in read("robots.txt")


def test_sitemap_is_wellformed_with_homepage():
    root = ET.fromstring(read("sitemap.xml"))
    locs = [e.text for e in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    assert "https://topazcomputing.com/" in locs


def test_404_links_home():
    html = read("404.html")
    assert "https://topazcomputing.com/" in html


def test_story_page_exists_and_branded():
    html = read("story/index.html")
    assert "Emma" in html and "Leonhart" in html
    assert "Founder" in html
    assert "Sutra" in html
    # links back to the product home
    assert 'href="/"' in html


def test_homepage_links_to_story():
    assert 'href="/story/"' in read("index.html")


def test_sitemap_includes_story():
    root = ET.fromstring(read("sitemap.xml"))
    locs = [e.text for e in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    assert "https://topazcomputing.com/story/" in locs


def test_link_preview_tags_present():
    # Discord/Slack/iMessage previews need an absolute og:image + twitter card.
    for page in ("index.html", "story/index.html"):
        html = read(page)
        assert 'property="og:image"' in html, f"{page} missing og:image"
        assert "https://topazcomputing.com/logo-social.png" in html, f"{page} og:image not absolute"
        assert 'name="twitter:card"' in html, f"{page} missing twitter:card"
        assert 'name="theme-color"' in html, f"{page} missing theme-color"


def test_social_image_is_published():
    # The og:image file must exist AND be copied into the deployed _site.
    assert (ROOT / "logo-social.png").exists(), "logo-social.png missing from repo"
    deploy = (ROOT / ".github/workflows/deploy.yml").read_text(encoding="utf-8")
    assert "logo-social.png" in deploy, "deploy.yml does not publish logo-social.png"


def test_waitlist_signup_form_present():
    """The mailing-list signup must stay on the page (it went missing once; this
    guards it). It posts to the existing Google Form so sign-ups stay continuous."""
    html = read("index.html")
    assert 'id="waitlist"' in html, "waitlist section missing"
    # The live Google Form endpoint + email entry field — the original list.
    assert "1FAIpQLSe7ZXwFpOAVADmKkmOvcVsFAv1qhdJb_pwMP2c3mNMTvifdHw" in html, \
        "Google Form action missing — signups would not be collected"
    assert 'name="entry.900213640"' in html, "email field missing"
    assert 'type="email"' in html and "required" in html
