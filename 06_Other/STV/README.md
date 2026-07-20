# 06_Other/STV — proportional multi-winner ranked (STV)

Single Transferable Vote: the proportional, multi-winner tabulation of the ranked ballot. One runnable example — three seats, seven candidates — showing quota, surplus transfer, and elimination.

| Case | Page | YAML |
|---|---|---|
| STV — 3 seats, 7 candidates (proportional RCV) | [page](cases/cases_pages/03a_stv_3seats.md) | [`03a_stv_3seats.yaml`](cases/03a_stv_3seats.yaml) |
| **The sole-survivor STV crash** — a live BetterVoting bug, bisected with five public elections and diagnosed in BV's `IRV.ts` (BV2203–BV2205) | [lab notebook](bv_stv_sole_survivor_crash/README.md) | [flag probe](bv_stv_sole_survivor_crash/cases/bv2203_gvtg2h_flag_probe.yaml) · [control](bv_stv_sole_survivor_crash/cases/bv2204_39py93_control_standing_hopefuls.yaml) · [minimal](bv_stv_sole_survivor_crash/cases/bv2205_8xwx43_minimal_sole_survivor.yaml) |

Full audit mirror in `STV_tabulated/`. Concepts: [proportional representation](../../00_start_here/proportional_representation/README.md) — and don't fold STV into "RCV" = IRV; it's the *multi-winner* count of the same ballot ([terminology](../../00_start_here/tips/TIPS_terminology.md)).
