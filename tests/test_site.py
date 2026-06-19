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
    assert "analog hardware and edge" in html


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
