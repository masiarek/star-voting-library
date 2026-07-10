# The Post-it RCV example — Equal Vote's whiteboard demo, live (BV2176)

The 20-voter election from Equal Vote's video **["Updated: How does RCV work? — With Post-its!"](https://youtu.be/Vte4nly_Neg)**, reproduced as a live BetterVoting election with **three races on the same electorate** (STAR on the video's 0–5 scores, RCV-IRV and Ranked Robin on its ranked ballots). RCV-IRV elects **Purple**, exactly as counted on the whiteboard — but Blue, eliminated in round 2, beats Purple head-to-head 10–9, and **STAR elects Blue** by actually holding that runoff. The Ranked Robin race is a bonus lesson: a Condorcet cycle leaves Green and Blue tied 2–1, and the two engines' tiebreak ladders — both deterministic here — part ways: **Green** on BetterVoting (head-to-head rung), **Blue** in LH (margin rung). The first live election to exhibit [that documented divergence](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md). <!-- terminology-ok: bare RCV is inside the quoted video title -->

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/p8dp28) · **[results ↗](https://bettervoting.com/p8dp28/results)** (election `p8dp28`, Test ID **BV2176**)

Start with the case page: **[bv2176_p8dp28_postit_rcv_example.md](bv2176_p8dp28_postit_rcv_example.md)** — the ballots, the video's rounds, the runoff RCV-IRV never held, and both engines' reports.

| Page (read this) | What it shows | src |
|---|---|:--:|
| [STAR — Blue](postit_rcv_example_pages/bv2176_p8dp28_star.md) | Scores 46/38/44/44; the 44–44 second-finalist tie breaks head-to-head (Blue 10–3 Pink); runoff **Blue 10–9 Purple** — a Runoff Reversal | [`.yaml`](bv2176_p8dp28_star.yaml) |
| [RCV-IRV — Purple](postit_rcv_example_pages/bv2176_p8dp28_irv.md) | The video's whiteboard count: 7/6/4/3 → 8/7/4 → **Purple 9, Green 8**, 3 ballots exhausted | [`.yaml`](bv2176_p8dp28_irv.yaml) |
| [Ranked Robin — Green (BV) / Blue (LH)](postit_rcv_example_pages/bv2176_p8dp28_ranked_robin.md) | A genuine cycle, Green and Blue tied 2–1; BV's head-to-head rung → Green, LH's margin rung → Blue — both deterministic, live | [`.yaml`](bv2176_p8dp28_ranked_robin.yaml) |

Related: [LH vs BV on Ranked Robin ties](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md) · [center squeeze](../center_squeeze/) (the same "eliminated the head-to-head winner" mechanic with a clean Condorcet winner) · up: [method_comparisons — same ballots, different methods](../)

# file: README.md
