# 06_Other/STV — proportional multi-winner ranked (STV)

Single Transferable Vote: the proportional, multi-winner tabulation of the ranked ballot. One runnable example — three seats, seven candidates — showing quota, surplus transfer, and elimination.

→ Curriculum: **[301.2 — STV](../../07_Concepts/curriculum/CURRICULUM_301.md)**, its own rung (the score-ballot proportional family is the rung before it, [301.1](../../07_Concepts/curriculum/CURRICULUM_301.md)) · Level: **301 · deep dive**

| Case | Page | YAML |
|---|---|---|
| STV — 3 seats, 7 candidates (proportional RCV) | [page](cases/cases_pages/03a_stv_3seats.md) | [`03a_stv_3seats.yaml`](cases/03a_stv_3seats.yaml) |
| **The sole-survivor STV crash** — a live BetterVoting bug, bisected with five public elections and diagnosed in BV's `IRV.ts` (BV2203–BV2205) | [lab notebook](bv_stv_sole_survivor_crash/README.md) | [flag probe](bv_stv_sole_survivor_crash/cases/bv2203_gvtg2h_flag_probe.yaml) · [control](bv_stv_sole_survivor_crash/cases/bv2204_39py93_control_standing_hopefuls.yaml) · [minimal](bv_stv_sole_survivor_crash/cases/bv2205_8xwx43_minimal_sole_survivor.yaml) |

Full audit mirror in `STV_tabulated/`. Concepts: [proportional representation](../../03_STAR_PR/01_Learn/README.md) — and don't fold STV into "RCV" = IRV; it's the *multi-winner* count of the same ballot ([terminology](../../07_Concepts/tips/TIPS_terminology.md)).

**Wanted proportional at all?** STV is one answer to a question that comes first — majoritarian ("the N best") or proportional ("mirror the electorate"): [Electing more than one, simply](../../07_Concepts/topics/electing_more_than_one.md). The scored answer to the same question is [STAR-PR](../../03_STAR_PR/README.md), worked against STV on [one shared electorate](../../method_comparisons/stv_vs_star_pr/README.md).
