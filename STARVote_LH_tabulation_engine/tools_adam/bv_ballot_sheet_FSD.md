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

## 4. Functional requirements — the tool

**FR-1 Inputs (candidates + title), any one of:**
- `--yaml FILE` — a repo election YAML; minimal parse pulls `election_title`, `bv_election_id` (if present), and the candidate header under `ballots:`. No PyYAML dependency.
- `--bv-export FILE` — a frozen `*_bv_export.json`; best-effort recursive search for the title and candidate names.
- `--candidates "A,B,C"` [`--title` `--bv-id` `--question`] — manual.

**FR-2 Output:** a single **self-contained, print-ready HTML** file (embedded CSS, no external assets except an optional inline-SVG QR data-URI). Print to PDF from any browser. Chosen over LaTeX/JS toolchains because HTML is universal, dependency-light, and editable. **Direct PDF:** if `--out` ends in `.pdf`, the tool renders straight to a print-ready PDF via headless Chromium (the already-declared **`playwright`** dep — `playwright install chromium` once). **Graceful fallback:** no playwright / no browser binary → it writes the `.html` beside it and tells you to Print → PDF, so plain `python3` still works.

**FR-2a Pagination:** `--per-page N` is *real* (a print `page-break-after` every N ballots, never a trailing blank page). **Default is 1** — one ballot per page, the right choice for ballots handed to voters individually (secret ballot). Set `--per-page 2+` to pack multiple per sheet to save paper.

**FR-3 Per-ballot content:** title, question, STAR instructions (incl. the overvote warning), a **0–5 bubble grid** (one row per candidate), and a footer with the BV id + results URL.

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

**5.3 Serials teach verifiability — with the secret-ballot tension as the lesson.** Publishing the list of counted serials demonstrates **counted-as-cast**. But a serial linkable to a voter breaks ballot secrecy (coercion) — which is *why* real systems need E2E-V (crypto receipts that confirm your vote counted without revealing how you voted). The tool prints serials; the [demo page](../../00_start_here/STAR_Voting/running_a_paper_ballot_demo.md) frames the tension. **Keep serials unlinked to identity in any real use; do not build BV/digital serial plumbing (§2).**

**5.4 QR is conditional, not decorative.** It only appears when there's something to open (a BV election, or an explicit `--qr-url`). No BV, no `--qr-url` → no QR. Avoids a QR that points nowhere.

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
- **Verified (manual, this pass):** `--out mptvrm_ballots.pdf` produced a **30-page PDF, one ballot per page** (confirmed `/Count 30`) via headless Chromium from the real export.
- **Pending (needs a human — owner: user):** (a) the QR **actually scans** on a phone and opens the election; (b) the ballot **prints cleanly** (bubble alignment, ~2/page, no clipping, 7-row grids); (c) the **flow feels right** in a real room. These are structurally un-checkable in-repo; validate on real paper before treating the doc as final.

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
