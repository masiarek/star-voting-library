# BV27 — Lackner & Skowron steering committee on BetterVoting (Multi-Winner Approval, k=4)

*The book's running example (Lackner & Skowron, Example 2.1) run on **BetterVoting's Approval engine**: 7 candidates, 12 approval ballots, 4 seats. The point of interest is the **4th seat**, where `d` and `f` tie at 2 approvals — exactly the "AV returns two tied committees" of the book's Example 2.2. BetterVoting's random draw seated **F**, giving `{A,B,C,F}`; this repo's published-priority LH engine seats **D**, giving `{A,B,C,D}`. Both are valid AV committees.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/jt6r76) · **[results ↗](https://bettervoting.com/jt6r76/results)** (election `jt6r76`).

Reference files: LH approval original [`approval_bloc_4seats_c7_b12_lackner_skowron.yaml`](cases/approval_bloc_4seats_c7_b12_lackner_skowron.yaml) · frozen export [`bv27_jt6r76_lackner_approval_committee_bv_export.json`](cases/bv27_jt6r76_lackner_approval_committee_bv_export.json). Backs sheet row **BV27**. Created via [`create_bv_test_election.py`](../../../STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py).

## The election

Multi-Winner Approval (bloc), 7 candidates `A–G`, **4 seats**, 12 approval ballots:

```
3 × {A,B}   3 × {A,C}   2 × {A,D}   1 × {B,C,F}   1 × {E}   1 × {F}   1 × {G}
```

Approval counts: **A = 8**, B = 4, C = 4, D = 2, F = 2, E = 1, G = 1. Three seats are clear — A, B, C. The 4th is a **2–2 tie between D and F**.

## View 1 — BetterVoting

Elected **A, B, C, F** (`nTallyVotes: 12`, `nAbstentions: 0` — all ballots counted). BetterVoting's export reports the seat-4 tie explicitly:

```
elected      : A, B, C, F
tied         : F (score 2) , D (score 2)     ← the 4th-seat tie, both with 2 approvals
tieBreakType : "random"                       ← the draw seated F (tieBreakOrder F=1, D=6)
```

**QA note (a *good* result):** BV correctly labels this `tieBreakType: "random"` and surfaces the tied pair — unlike some STAR cases where a lot-decided seat was mislabeled `"none"` (cf. BV130-r2, BV131). The count is also right (12 of 12, no flat-ballot drop). What remains is the general reproducibility gap: a random draw means a re-run could seat **D** instead (cf. [#1063](https://github.com/Equal-Vote/bettervoting/issues/1063) / [#1417](https://github.com/Equal-Vote/bettervoting/issues/1417)).

## View 2 — the LH engine (published-priority tiebreak)

The same profile through the LH Approval engine, which breaks ties by a **published candidate priority order** (A>B>…>G) rather than a random draw:

<!-- report:approval_bloc_4seats_c7_b12_lackner_skowron -->
```text
--- Approval Voting (4 winners) ---
 Tabulating 12 ballots (any non-zero score = approval).

Ballots:
   columns = A, B, C, D, E, F, G      (1 = approve; 0 = not approved)
     3 × 1,1,0,0,0,0,0
     3 × 1,0,1,0,0,0,0
     2 × 1,0,0,1,0,0,0
     1 × 0,1,1,0,0,1,0
     1 × 0,0,0,0,1,0,0
     1 × 0,0,0,0,0,1,0
     1 × 0,0,0,0,0,0,1

   A -- 8 (67%) -- Elected
   B -- 4 (33%) -- Elected
   C -- 4 (33%) -- Elected
   D -- 2 (17%) -- Elected
   F -- 2 (17%)
   E -- 1 (8%)
   G -- 1 (8%)
  Note: D, F each have 2 approvals and tie for the last 1 seat.
        Candidate priority order (D > F) broke the tie: D elected, F not elected.

[Approval Distribution] (how many candidates each ballot approved)
   22 approvals across 12 ballots — average 1.8 of 7 (range 1–3).
     approved 1: 3 ballots
     approved 2: 8 ballots
     approved 3: 1 ballot

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
      |   A    |   B    |   C    |   D    |   F    |   E    |   G    |
   -------------------------------------------------------------------
   A  |   --   |  38%   |  38%   |  25%   |   0%   |   0%   |   0%   |
   B  |  75%   |   --   |  25%   |   0%   |  25%   |   0%   |   0%   |
   C  |  75%   |  25%   |   --   |   0%   |  25%   |   0%   |   0%   |
   D  |  100%  |   0%   |   0%   |   --   |   0%   |   0%   |   0%   |
   F  |   0%   |  50%   |  50%   |   0%   |   --   |   0%   |   0%   |
   E  |   0%   |   0%   |   0%   |   0%   |   0%   |   --   |   0%   |
   G  |   0%   |   0%   |   0%   |   0%   |   0%   |   0%   |   --   |

Winners — Approval Voting (4 winners)
  A, B, C, D
```
<!-- /report -->
## The finding

Both engines agree on the tabulation — `a,b,c` plus a **genuine 2–2 tie for seat 4**. They differ only in *how the tie is broken*: BetterVoting draws at **random** (here → F, the book's committee `W₂ = {a,b,c,f}`), while LH uses a **pre-published priority order** (→ D, the book's `W₁ = {a,b,c,d}`). This is the multi-winner on-screen report of the single-winner random-vs-published-lot theme ([BV `jfk7pd`](../../../01_STAR/03_Criteria/tie_break_dead_rung/lot_random_vs_published_jfk7pd/lot_random_vs_published_jfk7pd.md)): the *committee* is reproducible only once the tiebreak order is fixed.

It also makes the book's point tangible: `{a,b,c,d}` leaves **3** voters wholly unrepresented, `{a,b,c,f}` leaves **2** — so even among the tied AV committees, one is "kinder," and it's the coin toss that decides which you get. The proportional rules (PAV → `{a,b,c,f}`) resolve this on purpose rather than by luck.

## See also

- The education built on this election: [ABC rules — a gentle intro (101)](../../01_Learn/Multiwinner_Approval/abc_rules_intro.md) · [ABC rules & the utilitarian–egalitarian spectrum (301)](../../01_Learn/Multiwinner_Approval/abc_rules_spectrum.md).
- [Shadow STAR of this same profile](lackner_skowron_shadow_star.md) — Bloc STAR / Allocated / SSS / RRV on the 5/0 reading.
- [Approval multi-winner](../../01_Learn/Multiwinner_Approval/approval_multiwinner.md).
