# rr_vs_irv_plurality — Ranked Robin vs. IRV vs. plurality (same ballots)

Where the [Condorcet vs. Ranked Robin](../condorcet_vs_ranked_robin/) set asks *"is Ranked Robin the same as the Condorcet winner?"* (answer: yes, until a cycle), this set asks a different question: **on one ranked ballot set, do the common methods even agree on a winner?** They don't — and the gap is the lesson.

| Case (page) | What it shows | Plurality | RCV-IRV | Ranked Robin | src |
|------|---------------|:---:|:---:|:---:|:--:|
| [BV2131 — Tennessee capital](bv2131_tennessee_condorcet_center_vqyqkr.md) | one ballot set, three winners — the classic center-squeeze | Memphis | Knoxville | **Nashville** | [`.yaml`](bv2131_tennessee_condorcet_center_vqyqkr.yaml) |

**Tennessee in one line:** Nashville is nearly everyone's second choice, so it beats every rival head-to-head (the Condorcet winner Ranked Robin elects) — but it holds few first-choices, so plurality ignores it and IRV eliminates it before the final round.

Each case here is **triple-checked**: LH native `run_ranked_robin`, BetterVoting's `RankedRobin.ts` (frozen `_bv_export.json`), and `pref_voting`'s independent Copeland — all must agree on the winner. See each page's "Agreement" table.

**Concept docs:** [Ranked Robin (the method)](../../00_start_here/RCV_Ranked_Robin/ranked_robin.md) · [Condorcet efficiency (topic hub)](../../00_start_here/topics/condorcet/README.md) · why IRV is fragile here: center squeeze in [Ranked Robin vs. Condorcet](../../00_start_here/RCV_Ranked_Robin/ranked_robin_vs_condorcet.md).

# file: README.md
