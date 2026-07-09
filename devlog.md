# topazcomputing.com — Devlog

## 2026-07-09

- **Refreshed the hosted pitch deck PDF** — Ask slide now states the real round
  (raising ~$250K on an uncapped SAFE; YC + investors + cyber.fund tracks),
  replacing the [PENDING-EMMA] placeholder. Same unlisted URL.
- **Fixed the deploy workflow to actually publish `/materials/`.** The prior
  commit added the deck PDF to the repo but the live URL 404'd: `deploy.yml`
  assembles `_site` from an explicit file allowlist and did not copy
  `materials/`, so the file was in the repo but never in the deployed artifact
  (caught by a live-fetch check, not assumed). Added
  `mkdir -p … _site/materials` + `cp -r materials/. _site/materials/` to the
  assemble step. After this deploy the deck URL resolves.

## 2026-07-08

- **Hosted the Topaz investor pitch deck (PDF) unlisted at `/materials/topaz-pitch-deck.pdf`.**
  Added for the CDL application's optional deck-link field (Emma's pick: unlisted
  PDF on the site rather than Google Drive). The deck was rebuilt fresh in the
  funding-and-networking repo (trajectory framing: websites → edge/autonomous;
  sutra-dev v0.9.4; funnel-maker ICP; $57M–$120M/yr serviceable market range),
  then exported to PDF and dropped here. `robots.txt` gets `Disallow: /materials/`
  so the path is public-if-you-have-the-URL but not crawled/indexed — the
  "unlisted" property. Not linked from any page. Link for the application:
  https://topazcomputing.com/materials/topaz-pitch-deck.pdf

**This file is where "done" lives.** `queue.md` is delete-only: when a queue
item is finished, the item is **deleted from `queue.md`** and a dated entry
is **appended here**, in the same commit as the work, then pushed. Never
tick a box in place — a checked box left in `queue.md` is the failure mode
this file exists to prevent.

Also record releases (tag + a one-line note), notable milestones, and
anything else worth a chronological trail. Newest entries at the bottom.

This is the **same convention as the cleanvibe repo's own `devlog.md`** —
every cleanvibe-scaffolded project gets one for the same reason.

See `CLAUDE.md` § "Workflow Rules" and `queue.md`'s preamble.

---

## 2026-06-19 — cleanvibe onboarding started

Onboarded with `cleanvibe clone` (cleanvibe v1.13.1). This is an
**existing repository**, so the very first onboarding task is to **backfill
the rest of this devlog from `git log`** (tagged releases, milestone
commits, merged feature branches). After that, every finished queue item
appends a new dated entry here.

## 2026-06-19
- Landing page: added a "What we're building" stack section presenting the project family under the Topaz umbrella (Sutra language, Topaz OS [formerly Yantra], self-optimizing pages). Real artifacts only; no em-dashes. Site tests green.

## 2026-06-20
- Added /demo/ : a self-contained, client-side self-optimizing-button demo (no server, no torch) ported from the Sutra trainable-button (exact theta_to_style + BUTTON_AXES; owner-preference + click-through steering). Verified in a browser (state advances, button morphs). Linked from the homepage. This is the production shape: client-side, real-time. Deploys via Pages to topazcomputing.com/demo/.

## 2026-06-21
- Landing-page copy rewrite (Emma: "wording too defensive, learning algorithms vague"). Removed the defensive openers ("Adaptive AI is not new", "The depth is real", "not a roadmap promise") and rewrote each section to assert the claim first. Made the learning mechanism concrete in "The first product": page compiled to a differentiable program -> every visual choice is a continuous parameter -> dense behavioral signal (scroll/hover/dwell) -> follows the gradient like a neural net -> searches a continuous design space rather than picking among human variants. Renamed "Why it matters"->"Why now" and "What we're building"->"The stack underneath". Aligned the OS line to the unbranded investor framing ("an operating system written in Sutra", dropped the "Topaz OS" product name). Tests green (7 passed).

## 2026-06-21
- Added /story/ — a founder-story page (story/index.html) for Emma Leonhart, reusing the site chrome + styles. Branding-forward and confident: self-taught deep-tech founder, shipped a language + paper + OS prototype solo, "crystal not cloud", networked in via Google Scholar + Discord + cold outreach. Real facts only. NO deadname, NO trans/identity content (Emma: identity is irrelevant, the work is what matters). Wired into deploy.yml (assemble copies story/ into _site), sitemap.xml (+ /story/ and /demo/), and a homepage "Who's building it" link. Added 3 smoke tests. Tests green (10 passed).

## 2026-06-22
- Fixed the Discord/Slack/iMessage link preview for topazcomputing.com. The homepage had og:title/description/url but NO og:image, no twitter card, and no theme-color, so embeds rendered bare. Added og:image (absolute https URL to logo-social.png, 1200x1200), og:image:width/height/alt, og:site_name, twitter:card=summary_large_image + twitter:image, and theme-color #a9742c (the topaz gold that colors Discord's embed accent bar). Same preview block added to /story/. CRITICAL FIX: deploy.yml wasn't copying logo-social.png into _site at all, so the og:image would have 404'd; added `cp logo-social.png logo.png _site/`. Added smoke tests asserting the preview tags + that the image is actually published.

## 2026-06-23
- Restored the mailing-list signup, which never made it onto topazcomputing.com (it was on the original Yantra site and got dropped). Added a "Request early access" section (`index.html`, `#waitlist`) that posts to the SAME Google Form the original list used (form 1FAIpQLSe7ZXwFpOAVADmKkmOvcVsFAv1qhdJb_pwMP2c3mNMTvifdHw, email field entry.900213640), so existing sign-ups stay continuous and new ones land in the same Sheet. Hidden-iframe target keeps the visitor on the page; inline "thanks" message on submit. Styled to the Topaz palette (cream/ink, topaz-gold button) in `styles.css`. Added a smoke test asserting the form + Google Form action + email field are present, so it can't silently disappear again. Tests green (13 passed).
