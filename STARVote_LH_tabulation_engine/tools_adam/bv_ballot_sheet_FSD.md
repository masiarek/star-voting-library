# FSD — Paper-Ballot Demo Toolkit (`bv_ballot_sheet.py`)

*Functional Specification (as-built). A dev/maintainer-facing spec for the printable-ballot tool and the paper-ballot demo workflow. The teacher-facing how-to is [`running_a_paper_ballot_demo.md`](../../00_start_here/STAR_Voting/running_a_paper_ballot_demo.md); this doc records **what** it does, **why** the design choices were made, and — importantly — **what it deliberately does not do**.*

**Status:** front-end (ballot generation) built, self-tested, in use. Return-path (OCR) is a documented roadmap, not built. Real-world print + QR-scan validation is pending (owner: user — see §7).

---

## 1. Goal

Let a teacher / workshop leader / demo runner turn a STAR election into **printable paper ballots**, so a room can vote on paper, **hand-count**, and compare the result to BetterVoting and/or the LH engine. The teaching payoff: three independent counts (paper, platform, engine) that agree — the repo's "don't believe it, check it" story, made tangible.

## 2. Scope

**In scope (built):** generate print-ready ballots from a STAR election; link them to a BetterVoting election (id, results URL, QR); optional serial "receipts", write-in rows, and a custom QR target for offline demos.

**Out of scope — deliberately (the guard):**
- **OCR / scan-to-YAML** (the *return* path). Needs a vision engine; specified in §6 as the roadmap, not built. Rationale: an unverified OCR pipeline that silently misreads a score is worse than none.
- **Threading serials through BetterVoting's vote API** for digital "confirm counted." BV doesn't carry them and it isn't needed — the serial demo is complete on paper (§5.3). A truly *digital* verifiable count is **end-to-end verifiability (E2E-V)**, a cryptography research area, flatly out of scope.
- **Extra ballot *options* — parked "someday, if asked":** other ballot *types* (Approval checkboxes, ranked-order grids), tear-off receipt stubs, localization (`--lang`), custom logos/branding, and multi-race-per-sheet ballots. Each is real polish or added capability but adds no *lesson* the single-race STAR paper ballot doesn't already teach; multi-race printing complicates both the sheet and the hand-count, and the "run 4 separate demos and compare" framing teaches the same thing with no code. (Revisit *only* if there's a concrete need — e.g. teaching the meta method-comparison **on paper**.)
- The compass for every call above: **"does this add education, or just engineering?"** Education → build; engineering-only → drop.

## 3. Workflow supported

```
1. Make the election on BetterVoting → get the BV id (bettervoting.com/<id>)
2. Print matching paper ballots      → bv_ballot_sheet.py → HTML → PDF
3. Vote on paper                      → fill 0–5 bubbles
4. Hand-count                         → add columns · runoff (count_star_by_hand.md)
5. Compare to BetterVoting            → bettervoting.com/<id>/results
6. (roadmap) OCR paper → YAML         → LH engine
```
The tool owns step 2. Steps 4–5 are the [count-by-hand](../../00_start_here/STAR_Voting/count_star_by_hand.md) and [teacher](../../00_start_here/STAR_Voting/teaching_star_voting.md) pages. Step 1 can use [`create_bv_test_election.py`](./create_bv_test_election.py).

**The five workflows this enables** (all supported today; the loop above is the fullest one):

| # | Workflow | Election defined in | Vote | Counted by | QR |
|---|---|---|---|---|---|
| 1 | **Pure paper, offline** (the simplest) | manual / a YAML | paper only | by hand | none (or `--qr-url`) |
| 2 | **Paper + BV — the "compare" demo** | a BV election | paper and/or online | hand-count *vs.* BV | → the BV election |
| 3 | **Create → print** | `create_bv_test_election.py` → id | paper and/or online | hand-count *vs.* BV | → BV |
| 4 | **Meta method-comparison** | `meta_pets` (4 races) | online (or paper STAR) | winner changes per method | → `meta_pets` |
| 5 | **Paper → LH engine** | manual / YAML | paper | transcribe → the engine | optional |

#1 and #2 are the two that matter; #3 is #2 with the create step (the only worthwhile *smoothing* is having `create_bv_test_election.py` print the ready-to-run `bv_ballot_sheet.py` command — not yet done); #4 is a teaching framing (pair with `criteria_at_a_glance.md`); #5 is the offline-verify path.

**Workflow #2 is really *hybrid* (validated on real hardware).** The same election runs on paper **and** online at once: paper voters fill bubbles, QR voters scan and vote on BetterVoting. The payoff for the teacher is **less work, not more** — online votes need **no transcription** (BV tabulates them the instant they're cast), so you can push most of the room to the QR and keep only a handful of paper ballots to demonstrate the hand-count. This also reframes the return path (§6): OCR only ever matters for the paper ballots you *choose* to keep; every QR voter has already closed the loop.

## 4. Functional requirements — the tool

**FR-1 Inputs (candidates + title), any one of:**
- `--yaml FILE` — a repo election YAML; minimal parse pulls `election_title`, `bv_election_id` (if present), and the candidate header under `ballots:`. No PyYAML dependency.
- `--bv-export FILE` — a frozen `*_bv_export.json`; extracts title, `election_id`, candidate names, and the election + first-race **descriptions**.
- `--candidates "A,B,C"` [`--title` `--bv-id` `--question` `--description` `--race-description`] — manual.

**FR-2 Output — the extension picks the format:**
- **`.txt` → plain ASCII** (strictly 7-bit — enforced by `--selftest`). **Zero dependencies**, prints from anywhere (`lpr ballots.txt`, or any editor). One ballot per page via the **form-feed** char (`\f`). `( )` circles to mark; no QR (the results URL is printed instead). The purest, most portable ballot — and the best fit for the "keep it simple" guard when styling isn't needed.
- **`.pdf` → print-ready PDF** rendered straight via headless Chromium (the already-declared **`playwright`** dep — `playwright install chromium` once). **Graceful fallback:** no playwright / no browser binary → it writes the `.html` beside it and tells you to Print → PDF.
- **`.html` (default) → styled, self-contained** (embedded CSS, optional inline-SVG QR data-URI; no other external assets). Print to PDF from any browser.

The trade-off is deliberate: **ASCII** = zero-dep and universal but plain (no QR); **HTML/PDF** = styled with a scannable QR but pulls in optional libraries. All three produce the same ballot content and honor `--per-page`.

**FR-2a Pagination:** `--per-page N` is *real* (a print `page-break-after` every N ballots, never a trailing blank page). **Default is 1** — one ballot per page, the right choice for ballots handed to voters individually (secret ballot). Set `--per-page 2+` to pack multiple per sheet to save paper.

**FR-3 Per-ballot content (styled after the official Equal Vote STAR ballot):** a **demonstration notice** (FR-9); a **STAR VOTING wordmark** header (star-with-check facsimile + "SCORE · THEN · AUTOMATIC · RUNOFF"); the election **title**, optional **description blurb** (italic), and **question**; the four **bulleted instructions** ("Give your favorite candidate(s) five stars", etc.) plus a fine-print overvote line; the **score grid** — **Worst/Best** labels, **star-outline column headers** 1–5 (0 plain), **digit-in-bubble** cells, **zebra-striped** candidate rows; the **finalist explanation** ("The two highest scoring candidates are finalists…"); a footer with serial + BV id + results URL; and an optional **promo line** (FR-10). The ASCII (`.txt`) output mirrors this as faithfully as 7-bit allows (wordmark, bullets, Worst/Best, `(0)…(5)` bubbles, explanation).

**FR-3a Descriptions:** a `--bv-export` automatically carries the election's `description` (→ the blurb) and the first race's `description` (→ the question line) onto the ballot; `--description` / `--race-description` override or supply them for the YAML/manual paths (the minimal YAML parser doesn't read block-scalar descriptions). Both print in all three formats.

**FR-10 Promo footer (optional, off by default):** `--promo` adds a small footer line — `Learn more: starvoting.org · equal.vote · bettervoting.com`; `--chapter "TEXT"` appends a local chapter (e.g. `STAR Voting NC (facebook.com/groups/starvotingnc)`) and implies `--promo`. **Off by default** so the base ballot matches the clean official design; **links are parameters, not the election description** (see §5.5).

**FR-11 Custom logo (optional):** `--logo FILE` embeds a local image (SVG/PNG/JPG) as a self-contained data URI in the header, **replacing** the drawn STAR-wordmark facsimile — so a user can drop in the real Equal Vote logo or a chapter logo. HTML/PDF only (ignored for `.txt`, which keeps the text wordmark). Missing/unreadable file → a warning and graceful fallback to the facsimile. Bounded on purpose: **one** header logo, not a general image-insertion system (that would be engineering past the lesson).

**FR-9 Demonstration notice (on by default):** every ballot carries a standing notice — default `"EDUCATION ONLY - a STAR Voting teaching demo, not a secret ballot."` — because this tool *only* makes demo ballots. It also does real work: it makes the optional **serial number** read as a teaching device rather than surveillance (a numbered *real* ballot would break the secret ballot; the notice preempts the immediate — and correct — objection). `--notice "..."` overrides the text; `--no-notice` omits it (discouraged). Kept 7-bit ASCII so it survives unchanged into the `.txt` output. Rendered as a bordered banner (HTML) / dashed banner (ASCII) at the top of each ballot.

**FR-4 QR code (optional):** top-right of each ballot.
- Points to `bettervoting.com/<bv-id>` by default; to `--qr-url <URL>` if given (works with no BV election).
- Implemented via the pure-Python **`segno`** library (declared in `pyproject.toml`). **Graceful fallback:** no segno → no QR, tool still runs on plain `python3`. `--no-qr` to force off.

**FR-5 Serial receipts (optional, `--serials`):** number each ballot ("Ballot #N — keep this to verify it was counted"). See §5.3 for the verifiability design + secret-ballot caveat.

**FR-6 Write-in rows (optional, `--write-ins N`):** N blank "Write-in: ___" rows with a 0–5 grid. Front-end only — *tallying* write-ins (name matching across ballots) is an OCR-step concern (§6), not the printer's.

**FR-7 Layout:** `--copies N`, `--per-page N` (real page-breaks, default 1), `--out FILE` (`.pdf` → direct PDF, else HTML). Print CSS avoids splitting a ballot across pages.

**FR-8 Self-test (`--selftest`):** known-answer checks — candidate presence, BV id + results URL, ballot count, bubble-grid arithmetic, HTML escaping, serials, write-in rows, and the QR path (whichever of present/absent applies). Exit non-zero on failure.

## 5. Key design decisions & rationale

**5.1 Ballot is self-sufficient; BV is an enhancement.** With `--bv-id` → id, results URL, QR. Without → generic STAR heading, no QR — still a valid **LH-only** ballot. So the tool serves both BV-backed and offline demos with no forced complexity.

**5.2 Flag mistakes by reusing the repo's existing markers — don't invent a scheme.** The marker vocabulary (see [CLAUDE.md](../../CLAUDE.md)) already maps ambiguous input to `0`-with-a-flag:

| On paper | Meaning | YAML |
|---|---|---|
| one bubble | valid 0–5 | that digit |
| **≥2 bubbles in a row** (e.g. 2, 4 *and* 5) | overvote / ambiguous | **`?`** (spoiled — counts 0, reported) |
| no bubble | no score | `0` (or `-` blank) |
| stray / illegible | unreadable | `?` + run-log note |

So "voter marked 2, 4 and 5 for one candidate" → `?` in that column; the engine already scores it 0 and surfaces it as spoiled. The ballot *warns the voter up front*.

**5.3 Serials teach verifiability — with the secret-ballot tension as the lesson.** Publishing the list of counted serials demonstrates **counted-as-cast**. But a serial linkable to a voter breaks ballot secrecy (coercion) — which is *why* real systems need E2E-V (crypto receipts that confirm your vote counted without revealing how you voted). The tool prints serials; the [demo page](../../00_start_here/STAR_Voting/running_a_paper_ballot_demo.md) frames the tension. **Keep serials unlinked to identity in any real use; do not build BV/digital serial plumbing (§2).** The **default demonstration notice (FR-9)** is the on-ballot half of this safeguard: it states in print that the sheet is a teaching demo, not a secret ballot — so a numbered ballot can't be mistaken for (or objected to as) a real one.

**Why serials default OFF (a considered call, not an accident).** The pull is real in both directions:
- *For ON:* every demo would surface verifiability + the secret-ballot tension (the richest discussion the tool enables); numbered sheets aid hand-count reconciliation ("all 30 back, none duplicated"); and now that every ballot is stamped "EDUCATION ONLY," the main risk of ON is largely defused.
- *For OFF:* the core STAR lesson (score → runoff) stays the focus; no privacy footgun if a demo is reused casually; and in a classroom, ballots handed out in seating order **plus** numbers are deanonymizable.

The decider is a **default-design principle**: *a default is used by the person who isn't thinking about it.* A serial only pays off **paired with the discussion** ("what breaks if we post a name→number list?"); a teacher who wants that types `--serials`, and that deliberate act is the signal they'll frame it. An ON default instead hands numbered ballots to the teacher who *didn't* plan the lesson — propagating the double-edged artifact without the framing that makes it safe. So: **the safe, on-topic thing is the default; the richer-but-double-edged thing is a conscious opt-in.** Serials OFF, notice ON, and the teacher docs actively *invite* `--serials` when verifiability is the lesson. **Keep serials unlinked to identity in any real use; do not build BV/digital serial plumbing (§2).**

**5.4 QR is conditional, not decorative.** It only appears when there's something to open (a BV election, or an explicit `--qr-url`). No BV, no `--qr-url` → no QR. Avoids a QR that points nowhere.

**5.5 Match the official ballot; links are parameters, not description.** The layout deliberately mirrors Equal Vote's recognizable STAR ballot (wordmark, bulleted instructions, Worst/Best, star headers, stripes, finalist footer) — familiarity buys credibility for a teaching artifact. Two calls fall out of that goal:
- **The default logo is a facsimile, not the trademark.** A self-contained file can't embed Equal Vote's actual logo asset, and every ballot is stamped EDUCATION ONLY, so we draw a star-with-check lookalike in inline SVG rather than pass off their mark. A user who *has the right* to the real logo (or a chapter logo) supplies it with `--logo FILE` (FR-11) — the decision to use a real mark is theirs, made explicitly.
- **Promo links are `--promo` / `--chapter` parameters, kept OFF by default — not folded into the description.** Reasons: (1) the description is *election-specific* content (what the vote is about); links are *boilerplate promotion*, identical across elections — mixing them would pollute the BV description field and repeat on every export; (2) the official ballot carries **no** URLs, so links-off is what keeps ours faithful; (3) a teacher promoting locally flips them on deliberately (`--promo --chapter "…"`), which is exactly when the promotion is wanted. On paper the links are read-and-type text (short domains), not clickable — so a compact one-liner beats a wall of full URLs.

## 6. Return-path (OCR) — roadmap spec, NOT built

Restated in the repo's terms (the *goal*, not the letter of the original suggestion):
1. Read each ballot image; locate candidate rows and the 0–5 bubble grid.
2. Per row, count filled bubbles → **1** = that score · **0** = `0` · **≥2** = `?` (spoiled).
3. Below a confidence threshold, or unreadable → `?` + log for human review.
4. Emit standard `voting_method: STAR` YAML (candidate header + one scored/marked row per ballot) **plus a run log** naming every flagged ballot.
5. Tabulate in the LH engine, which already reports spoiled ballots — loop closed.

**Open design questions for whoever builds it:** OCR engine choice (local **tesseract** preferred over a cloud API — offline, no key); bubble detection vs. handwriting; write-in *name matching* ("Bob"="bob"="Bobby"); deskew/threshold robustness. **Build discipline:** a **synthetic-ballot round-trip self-test** (render ballots with known scores → OCR → assert match) *before* it's trusted on real scans. Until built, transcribe by hand using the §5.2 table.

## 7. Verification status

- **Verified (automated):** `--selftest` passes (structure, bubbles, serials, write-ins, **pagination** (per-page breaks, no trailing blank), QR present/absent, and the **`--bv-export` schema** — a frozen UI export nests everything under a capitalized `Election` key). Reads the lunch YAML (picks up candidates + title + `fyy886`), the live `bettervoting.com/pet` election (7 candidates, QR → `/pet`), and a **real frozen export** (`mptvrm`: title + `election_id` + candidates + results URL + QR all extracted). *(The capitalized-`Election` case is why the earlier best-effort guess missed title/id until a real export was tested — now covered.)*
- **Verified (manual, this pass):** `--out mptvrm_ballots.pdf` produced a **30-page PDF, one ballot per page** (confirmed `/Count 30`) via headless Chromium; `--out mptvrm_ballots.txt` produced a **strictly-7-bit-ASCII 30-page** text file (30 form-feed pages, zero deps) — both from the real export.
- **Verified (real hardware, owner: user — 2026-07):** the full loop ran end to end on the `mptvrm` PDF — (a) the **QR scanned** on a phone and opened the live election; (b) the ballot **printed cleanly** (banner, bubble grid, QR, serial line all legible, one per page); (c) the voter **cast an online ballot via the QR** and it landed in the BV tally (re-exported as a fresh `_bv_export.json`). The earlier "pending, needs a human" items are now cleared.
- **Insight from that run (see §3, workflow #2):** the QR makes this a **hybrid** demo — some vote on paper, some scan-and-vote online. Online votes need **no transcription** (BV tabulates them instantly), so the more of the room that uses the QR, the *less* scanning/typing for the teacher; paper is then optional, kept only to demonstrate the hand-count.
- **Return path proven end-to-end (owner: user — 2026-07).** A hand-marked ballot photo (`mptvrm` #1, deliberately messy: a slash, an ✗, a check, one faint) was read correctly (ala 2, bob 4, tome 5), tabulated in the LH engine (→ tome), **and cast back into the live BV election** via `POST /API/Election/{id}/vote` (HTTP 200; BV `nTallyVotes` 1→2, BV STAR winner tome — agrees with LH). So all three legs — paper→engine, paper→BV, and scan→BV — are demonstrated. The lesson the messy marks confirmed: a valid human mark is a **slash/✗/check, not a filled bubble**, so any future OCR must detect mark *intent* (not fill-darkness) and flag low-confidence marks (`?`) for review. Note: the API cast is what the test tooling uses; a classroom normally enters paper ballots via the BV vote page/QR — a bulk paper→BV uploader is explicitly **not** built (engineering past the lesson).

## 8. Invocation

```bash
# from a repo YAML (auto-picks title, candidates, bv id)
python3 tools_adam/bv_ballot_sheet.py --yaml 01_STAR/_main/bv2184_fyy886_lunch_vote.yaml --copies 30

# the friendly live pet election, with receipts + a write-in
python3 tools_adam/bv_ballot_sheet.py --candidates "Bird,Cat,Python,Dog,Fish,Rabbit,Rat" \
    --title "What Makes the Best Pet?" --bv-id pet --serials --write-ins 1 --copies 25

python3 tools_adam/bv_ballot_sheet.py --selftest        # known-answer checks
```

**Dependencies:** stdlib only, except the *optional* `segno` (QR; declared in `pyproject.toml`, degrades gracefully).

## 9. Related

- Teacher how-to: [`running_a_paper_ballot_demo.md`](../../00_start_here/STAR_Voting/running_a_paper_ballot_demo.md)
- Hand-count: [`count_star_by_hand.md`](../../00_start_here/STAR_Voting/count_star_by_hand.md) · Teaching guide: [`teaching_star_voting.md`](../../00_start_here/STAR_Voting/teaching_star_voting.md)
- BV election creation: [`create_bv_test_election.py`](./create_bv_test_election.py) · Marker conventions & house rules: [`CLAUDE.md`](../../CLAUDE.md)
