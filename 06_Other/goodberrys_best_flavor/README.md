# Goodberry's Best Flavor 2026 — a real STAR election

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/6tthfv) · **[results ↗](https://bettervoting.com/6tthfv/results)** (election `6tthfv`, Test ID BV2252).

A live, real-world STAR Voting election: **which Goodberry's Frozen Custard flavor is the best?** Not a constructed teaching case — an actual poll, minted with no seed ballots, collecting real votes from paper ballots printed at the Cary, NC shop and from anyone who scans the QR code.

Goodberry's sells **frozen custard**, not ice cream — the title says so on purpose. Its permanent menu board carries a couple dozen flavors, and a rotating daily calendar adds specials on top. That makes it a natural STAR ballot: **almost everyone likes several flavors**, and a choose-one poll would force each voter to throw away all but one of those opinions.

## The ballot

Ten flavors from the permanent menu board, spread across its families — custard classic, chocolate, nut, coffee, citrus, mix-in, and the Southern one Goodberry's is known for:

| # | Flavor | Why it's on the ballot |
|---|--------|------------------------|
| 1 | Banana Pudding | the Southern signature |
| 2 | Butter Pecan | the nut classic |
| 3 | Chocolate Malt | chocolate, the soda-fountain way |
| 4 | Cookie Dough | the mix-in favorite |
| 5 | Jamocha | the coffee lane |
| 6 | Key Lime | tart, unlike anything else on the list |
| 7 | Mint Chocolate Chip | the perennial top-five finisher |
| 8 | Peanut Butter | the other nut lane, and a second-choice magnet |
| 9 | Salted Caramel | the modern favorite |
| 10 | Sweet Cream | the base custard itself — the purist's vote |

**Write-ins are enabled**, so a voter whose favorite is Blueberry, Nutella, plain Chocolate, or a calendar special (Lavender Limoncello, Piña Colada, Tiramisu…) can still say so.

## How to vote

Score every flavor you have an opinion about, 0–5 stars. **Give your favorite 5.** Give anything you'd be unhappy with 0. Everything in between is fair game — you are rating, not ranking, so equal scores are allowed and normal.

Then STAR does two things:

1. **Scoring round** — add up all the stars; the two highest-scoring flavors become finalists.
2. **Automatic runoff** — every ballot counts once more, for whichever finalist it scored higher. The finalist preferred by more voters wins.

That second step is what a plain star-rating poll lacks: the winner is the flavor more people actually preferred, not merely the one that collected the most generous ratings.

## Paper ballots

`goodberrys_best_flavor_2026_ballots.pdf` — 30 print-ready STAR ballots, one per page, each with the 0–5 bubble grid and one big *Scan to vote online* QR pointing at `6tthfv` (the results URL prints as text in the footer). Built PDFs are generated artifacts (`*_ballots.pdf` is gitignored), so regenerate it from the frozen export with [`bv_ballot_sheet.py`](../../STARVote_LH_tabulation_engine/tools_adam/bv_ballot_sheet.py):

```bash
.venv/bin/python STARVote_LH_tabulation_engine/tools_adam/bv_ballot_sheet.py --bv-export 06_Other/goodberrys_best_flavor/cases/goodberrys_best_flavor_2026_bv_export.json --logo STARVote_LH_tabulation_engine/tools_adam/assets/NC_STAR_Logo1.jpg --notice "UNOFFICIAL FLAVOR POLL — COUNTED WITH STAR VOTING." --cover --verify-bv --out 06_Other/goodberrys_best_flavor/goodberrys_best_flavor_2026_ballots.pdf
```

`--cover` prints a **preamble page** ahead of the 30 ballots. It matters here: anyone who scans the ballot's QR lands on BetterVoting and reads the full election description before voting, so without a cover the paper voter and the phone voter get briefed differently. The cover carries that same text plus *how to vote* and *how it is counted*, and says in its footer that it is not a ballot so it can't be hand-counted by mistake. Change `--copies` for a bigger or smaller table (default 30). Paper and platform stay linked: the QR voters and the bubble-fillers are casting the same ballot into the same count. The full workflow (print → vote → hand-count → compare to BetterVoting) is in [running a paper-ballot demo](../../01_STAR/01_Learn/hands_on/running_a_paper_ballot_demo.md); the by-hand count is in [count STAR by hand](../../01_STAR/01_Learn/hands_on/count_star_by_hand.md).

## What to watch for when the votes come in

- **The score leader and the winner may differ.** With ten flavors, a polarizing one (Key Lime, Jamocha) can pile up 5s from its fans and 0s from everyone else, lead the scoring round, and then lose the runoff to a broadly-liked flavor. That reversal is the whole point of the "AR" in STAR — see [the runoff-reversal case](../../01_STAR/02_Examples/cases/cases_pages/bv2182_tg4779_faq_runoff_reversal.md).
- **Bullet voting costs you.** A ballot that scores one flavor 5 and leaves the rest blank has no say at all in a runoff between two other flavors — see [the bullet-vote case](../../01_STAR/02_Examples/cases/cases_pages/03a_c3_b3_style-bullet-vote.md).
- **Ten candidates, no vote-splitting.** Unlike choose-one, adding a tenth flavor similar to the ninth cannot split their support, which is exactly why a long menu is safe on one ballot.

## Files

| File | What it is |
|------|-----------|
| `goodberrys_best_flavor_2026_ballots.pdf` | the printable ballots (30 pages) — generated, not committed |
| [cases/goodberrys_best_flavor_2026_bv_export.json](cases/goodberrys_best_flavor_2026_bv_export.json) | frozen BV export at mint time (zero ballots — the poll had not started) |

Re-freeze the export once real votes are in, and the results are tabulatable in this repo's engine:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/fetch_bv_export.py 6tthfv -o 06_Other/goodberrys_best_flavor/cases/goodberrys_best_flavor_2026_bv_export.json --force
```
