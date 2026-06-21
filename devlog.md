# topazcomputing.com — Devlog

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
