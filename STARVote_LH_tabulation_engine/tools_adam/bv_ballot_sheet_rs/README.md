# bv_ballot_sheet (Rust / Typst)

A **Rust port** of [`bv_ballot_sheet.py`](../bv_ballot_sheet.py) that prints STAR paper ballots (PDF) from a BetterVoting export — **Option B** from the feasibility chat: compose a [Typst](https://typst.app) document and render it to PDF with the **embedded Typst compiler**, so there's **no headless browser** (no playwright/Chromium) and **no Python** at runtime.

## Why

The Python tool needs Python + uv + playwright + a Chromium download. This is a **single self-contained binary** — build once, hand a teacher one file, run it anywhere. Fonts are bundled (via `typst-assets`); QR codes are generated in-process and injected into the Typst document as in-memory files.

## Pipeline

```
BV export JSON  --serde_json-->  { title, candidates, id, descriptions }
     URLs       --qrcode-->       QR SVGs
  data + template --typst-as-lib--> PagedDocument --typst-pdf--> PDF
```

## Build & run

```sh
cargo build --release
./target/release/bv_ballot_sheet \
    --bv-export "../../../06_Other/_demo_dropbox/<election>-<id>.json" \
    --title "Best Ice Cream Flavor" --serials \
    --logo ../assets/NC_STAR_Logo1.jpg \
    --chapter "STAR Voting NC (facebook.com/groups/starvotingnc)" \
    --copies 30 --out ballots.pdf
```

**With a logo:** `--logo <FILE>` (SVG/PNG/JPG) drops your chapter logo into the header in place of the drawn "STAR VOTING" wordmark — the image is embedded straight into the PDF (no external file needed at print time). For a color print, use `../assets/NC_STAR_Logo1.jpg`; for black-and-white, `../assets/BW_long_form.jpg`.

## Same design as the Python tool

- **One input route:** `--bv-export FILE` (create on BV → export → print). No `--candidates`/`--yaml`.
- **PDF only**, one ballot per page.
- **Two QRs** (vote + results); `--no-qr` to suppress.
- Official-style layout: notice banner, STAR VOTING header, bulleted instructions, Worst/Best + 0–5 grid with digit-in-bubble cells, zebra stripes, finalist footer, election id + results URL.

## Status / parity with the Python tool

Implemented: `--bv-export`, `--title`, `--question`, `--copies`, `--serials`, `--no-qr`, `--chapter` (promo), `--logo` (embed a header logo image), `--out`.

Not yet ported (easy follow-ups): `--verify-bv`, `--per-page`, `--write-ins`, `--qr-size`, `--promo` without a chapter, `--notice`/`--no-notice`. The **Python tool remains the reference / full-featured version**; this is a working proof that the Rust/Typst path produces the same ballot with zero runtime dependencies.

Cosmetic note: uses Typst's bundled serif font (Libertinus) rather than the Python tool's system sans — a faithful sans match would bundle a sans `.ttf`.
