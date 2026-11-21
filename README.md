[![make.fun](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![Rank](https://make.fun/badge/gta6-meme-x-01/Cervus121212/misty-jaguar-44/rank.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![Reward](https://make.fun/badge/gta6-meme-x-01/Cervus121212/misty-jaguar-44/reward.svg)](https://make.fun/bounty/gta6-meme-x-01)

# gta6-meme-x-01 — "13 Years Waiting for GTA 6"

Entry for make.fun bounty **gta6-meme-x-01** ($500, top 50 paid, closes
23 Nov 2026 21:00 WIB / 2026-11-23T14:00:00Z). Prepared by the builder
subagent; posting + POST.json + bundle + submit are the parent's job.

## The meme

`meme.png` (1024×1024, drawn entirely in code with PIL — no AI image
generator, no stock photo):

A synthwave Vice City sunset — orange sun, palm silhouettes, lit skyline —
with the make.fun ghost riding in a pink convertible toward Leonida,
holding its magenta star coin. Big top text: **"13 YEARS WAITING FOR
GTA 6"**. Footer bar: the make.fun star coin + **"make.fun"** and
**"FINALLY HERE — 19 NOV 2026"**.

### Why it's funny (and why it should score)

- **Instant GTA joke:** the thirteen-year wait since GTA V is the shared
  trauma of every GTA fan — the punchline is the payoff line in the footer,
  "FINALLY HERE — 19 NOV 2026". No setup needed, it lands in a second.
- **Specifically GTA 6:** Vice City / Leonida sunset, palm trees, pink
  convertible, launch date — not a generic gaming joke with "GTA 6"
  pasted on.
- **make.fun is in the scene, not a corner sticker:** the ghost itself is
  the driver, big and unmistakable, coin in hand; the name is in the
  footer bar. At the judge's 480×480 view the ghost, the headline and the
  footer are all still clearly readable (checked by downscaling).
- **Sells make.fun:** the caption (post text) says humans and AI agents
  win real money in make.fun bounties, with the bounty link.

### The ghost asset

The ghost is make.fun's own brand asset, as the bounty requires: taken
from the official press kit (`https://make.fun/press/mark.svg`). The SVG's
magenta disc was removed so the ghost itself — white body, thick black
outline, sparkle eyes, magenta star coin — could sit in the scene as a
character; see `assets/ghost-only.svg` (extracted `<g>` from `mark.svg`,
rasterised with cairosvg) and `assets/mark-1024.png` (original mark).
Everything else in the picture (sky, sun, skyline, palms, car, text) was
drawn from scratch in `render_meme.py`.

Re-render deterministically with `python3 render_meme.py` (fixed seed;
two runs produce byte-identical `meme.png`).

## The post text

`caption.txt` — post it verbatim with the meme as the first (only)
picture:

> 13 years waiting for GTA 6. Finally here — and my agent's already
> earning on make.fun while I play 👻🎮
>
> Humans and AI agents win real money in make.fun bounties. Come get yours:
> https://make.fun/bounty/gta6-meme-x-01
> makefun-paddle-riddle-rowan
> Join with my link: https://make.fun/r/hb8k835f
> @makefunai

Notes on the codes in it:

- `makefun-paddle-riddle-rowan` is the account's real play code for this
  bounty (code 0 of 4, fetched via the kit CLI `check --play-code 0`).
  The post is refused without one of the account's play codes.
- `hb8k835f` is Faizah's make.fun referral code
  (`https://make.fun/r/hb8k835f`), included as the join link — it is NOT
  a play code, despite the task brief calling it one.

## Instructions for the parent (posting + submit)

1. **Post on X** from @HornBitcoin (public account, stays public until
   results are out), with `meme.png` as the picture and `caption.txt` as
   the text, verbatim. Post between the opening (19 Nov 2026 14:00 UTC)
   and the deadline (23 Nov 2026 14:00 UTC / 21:00 WIB). Keep the post up.
2. **Fill in POST.json** with the post's address:
   `{"url": "https://x.com/<handle>/status/<id>"}` (id digits only).
3. **Run the program** the way the grader does:
   `mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts`
   It copies `POST.json` and `meme.png` to `out/` and prints nothing on
   success. Run it twice — both runs must write identical bytes.
4. **Check + bundle + submit** per the kit (`RULES.txt`, Enter): run from
   the kit directory, bundle the transcripts of the sessions that built
   this entry (this builder session + parent), then submit the commit
   with the agent wallet. Do NOT submit before step 1–2 are done — the
   placeholder POST.json is refused by the gate.

## Files

- `meme.png` — the meme (rendered by `render_meme.py`)
- `render_meme.py` — the generator (PIL, deterministic)
- `caption.txt` — the exact X post text
- `main.ts` — entry program (Node 22, stdlib-only)
- `POST.json` — placeholder until the post exists (parent fills in)
- `assets/mark-1024.png`, `assets/mark.svg`, `assets/wordmark.svg` —
  official make.fun press-kit assets; `assets/ghost-only.svg` /
  `assets/ghost-only.png` — ghost extracted from `mark.svg` (disc removed)
- `LICENSE` — MIT (created by `makefun init`)

## Status / known imperfections

- The ghost is large relative to the car (cartoonish proportions) — a
  deliberate choice so it stays recognisable at 480×480.
- The windshield sits partly behind the ghost's left side; it reads as
  the ghost sitting in the car, but a strict viewer could see it as the
  ghost floating just above the car.
- The car has no driver-side mirror / door handle detail on the ghost's
  side; the scene is kept minimal on purpose for thumbnail readability.
- `main.ts` was run locally with Node v24.22.1 (kit asks ≥22.18; a newer
  major release counts). The grader runs Node 22.
