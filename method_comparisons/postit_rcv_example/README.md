# The Post-it RCV example — Equal Vote's whiteboard demo, live (BV2176 / BV2177 / BV2178)

The 20-voter election from Equal Vote's video **["Updated: How does RCV work? — With Post-its!"](https://youtu.be/Vte4nly_Neg)**, reproduced, stress-tested, and extended as **three live BetterVoting elections**. RCV-IRV elects **Purple**, exactly as counted on the whiteboard — but Blue, eliminated in round 2, beats Purple head-to-head 10–9, and **STAR elects Blue** by actually holding that runoff. From there the set widens: all seven BV methods on the same ballots elect **four different candidates**, and a two-ballot flip makes the video's round-2 hypothetical real. <!-- terminology-ok: bare RCV is inside the quoted video title -->

**Start here → [Is the video fair and balanced?](postit_video_fair_and_balanced.md)** — the claim-check lesson: what the video gets right (the count; the ignored 10–9 head-to-head), where a critic pushes back (the electorate is a Condorcet cycle with *no* rightful winner; the 0–5 scores are invented — order-consistent with the ranks, verified, but the *gap sizes* decide STAR's answer: generous 5/4/3 → Blue, stingy 5/2/1 → Purple), and five portable lessons.

**▶ Live on BetterVoting:**

- **BV2176** (the video's election, 3 races) — [vote](https://bettervoting.com/p8dp28) · **[results ↗](https://bettervoting.com/p8dp28/results)** (election `p8dp28`)
- **BV2177** (all seven BV methods, 7 races) — [vote](https://bettervoting.com/v8r66y) · **[results ↗](https://bettervoting.com/v8r66y/results)** (election `v8r66y`)
- **BV2178** (the round-2 switch, made real, 4 races) — [vote](https://bettervoting.com/8kg698) · **[results ↗](https://bettervoting.com/8kg698/results)** (election `8kg698`)

| Case page (read these) | What it shows |
|---|---|
| [BV2176 — the Post-it RCV example](bv2176_p8dp28_postit_rcv_example.md) | The video, live: IRV → Purple (7/6/4/3 → 8/7/4 → 9–8); STAR → Blue (44–44 finalist tie breaks head-to-head, runoff 10–9 — a Runoff Reversal); Ranked Robin → the first live sighting of the [LH-vs-BV tiebreak-ladder divergence](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md) (Green on BV, Blue in LH) |
| [BV2177 — seven ways, four winners](bv2177_v8r66y_seven_methods.md) | The same 20 ballots under STAR, Ranked Robin, Approval, IRV, Choose-One, STV, STAR-PR: **all four candidates win somewhere** — incl. Approval's threshold trap (approve ≥1/≥4/=5 → Pink/Blue/Purple) and STAR-PR-at-1-seat being Score voting (Purple, no runoff) |
| [BV2178 — the switch, made real](bv2178_8kg698_switch_made_real.md) | Two of six Green>Blue>Pink voters flip their top two → IRV really does eliminate Green in round 2 and lands the video's exact hypothetical (Blue 10, Purple 9); Blue becomes a clean 3–0 Condorcet winner; only Choose-One still says Purple |

## Races and sources

| Race | Page | src | LH winner | BV winner |
|---|---|:--:|:--:|:--:|
| BV2176/77 — STAR | [page](postit_rcv_example_pages/bv2176_p8dp28_star.md) | [`.yaml`](bv2176_p8dp28_star.yaml) | Blue | Blue |
| BV2176/77 — RCV-IRV (& STV 1-seat) | [page](postit_rcv_example_pages/bv2176_p8dp28_irv.md) | [`.yaml`](bv2176_p8dp28_irv.yaml) | Purple | Purple |
| BV2176/77 — Ranked Robin | [page](postit_rcv_example_pages/bv2176_p8dp28_ranked_robin.md) | [`.yaml`](bv2176_p8dp28_ranked_robin.yaml) | **Blue** | **Green** |
| BV2177 — Approval (any support) | [page](postit_rcv_example_pages/bv2177_v8r66y_approval.md) | [`.yaml`](bv2177_v8r66y_approval.yaml) | Pink | Pink |
| BV2177 — Choose-One | [page](postit_rcv_example_pages/bv2177_v8r66y_plurality.md) | [`.yaml`](bv2177_v8r66y_plurality.yaml) | Purple | Purple |
| BV2177 — STAR-PR, 1 seat | (BV-only: LH's allocated needs ≥ 2 seats) | — | — | Purple |
| BV2178 — STAR | [page](postit_rcv_example_pages/bv2178_8kg698_star.md) | [`.yaml`](bv2178_8kg698_star.yaml) | Blue | Blue |
| BV2178 — RCV-IRV | [page](postit_rcv_example_pages/bv2178_8kg698_irv.md) | [`.yaml`](bv2178_8kg698_irv.yaml) | Blue | Blue |
| BV2178 — Ranked Robin | [page](postit_rcv_example_pages/bv2178_8kg698_ranked_robin.md) | [`.yaml`](bv2178_8kg698_ranked_robin.yaml) | Blue | Blue |
| BV2178 — Choose-One | (in the STAR mirror's divergence block) | — | Purple | Purple |

Related: [LH vs BV on Ranked Robin ties](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md) · [center squeeze](../center_squeeze/) (the same "eliminated the head-to-head winner" mechanic with a clean Condorcet winner) · up: [method_comparisons — same ballots, different methods](../)

# file: README.md
