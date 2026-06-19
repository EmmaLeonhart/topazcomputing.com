# topazcomputing.com

Main site for **Topaz Computing**, served at <https://topazcomputing.com> via GitHub Pages.

A static one-page landing (clean, minimal, light/dark via `prefers-color-scheme`).
This is the new primary domain; `noldor.tech` redirects here (path-preserving), and
Sutra lives at `sutra.topazcomputing.com`.

## Structure

- `index.html` — landing page (text wordmark + What we do / Why it matters / Sutra).
- `styles.css` — minimal styling, topaz-gold accent.
- `404.html` — branded not-found page.
- `CNAME` — `topazcomputing.com` (sets the GitHub Pages custom domain).
- `robots.txt`, `sitemap.xml` — SEO.
- `.github/workflows/deploy.yml` — assembles `_site/` and deploys to Pages on push to `main`.
- `.github/workflows/ci.yml` — runs the pytest checks.

## DNS (handled at the registrar)

Apex domain → GitHub Pages A records (`185.199.108–111.153`). The `CNAME` file +
repo Pages config set the custom domain to `topazcomputing.com`.

## Develop

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
python -m http.server 8000   # preview at http://localhost:8000
```

A logo/wordmark is TODO — the hero currently uses a text wordmark.
