# One dial, three winners — Kim's (A,B)-scoring family, made runnable

**Level: 301 · deep dive**

Semin Kim's **"Ordinal versus cardinal voting rules: A mechanism design approach"** (*Games and Economic Behavior* 104, 2017, pp. 350–371, [DOI](https://doi.org/10.1016/j.geb.2017.04.012)) asks whether a ballot that records *how much* can beat a ballot that records only *which* — and, unusually, asks it while holding the voters to honesty constraints rather than assuming honesty. This folder runs the family of rules his answer lives in.

The theory lives on the concept page → **[Ordinal vs. cardinal, as mechanism design](../../07_Concepts/topics/ordinal_vs_cardinal_mechanism_design.md)**.

## The dial

With three candidates, Kim works in what Myerson (2002) named the **(A,B)-scoring rules**: every voter hands in a score vector that is a permutation of `(1, A, 0)` or `(1, B, 0)`, with `0 ≤ A ≤ B ≤ 1`. One number — what a voter's **second** choice is worth — and the familiar rules fall out of where you set it:

| (A, B) | The rule | The ballot says |
|---|---|---|
| `(0, 0)` | **Plurality** | my favorite, and nothing else |
| `(½, ½)` | **Borda** | my favorite, then my second at half credit |
| `(1, 1)` | **Negative voting** (anti-plurality) | the one I *don't* want |
| `(0, 1)` | **Approval** | *I* decide whether my second counts |

The first three are ordinal — a ranking is enough to fill them in. The fourth is not, and that gap is the whole paper.

## The cases

One electorate throughout: **36 voters, three flavors, fixed rankings.**

| Voters | Ranking |
|:--:|---|
| 12 | Almond > Berry > Cocoa |
| 8 | Berry > Almond > Cocoa |
| 7 | Cocoa > Almond > Berry |
| 9 | Cocoa > Berry > Almond |

| Case | (A, B) | Winner | What it shows |
|---|:--:|:--:|---|
| [The middle is worth nothing](cases/cases_pages/kim_scoring_a0_plurality.md) | `(0,0)` | **Cocoa** | plurality — and two blocs handing in identical papers | 
| [The middle is worth half](cases/cases_pages/kim_scoring_ahalf_borda.md) | `(½,½)` | **Almond** | Borda — which Kim proves is the *optimal* ordinal rule here |
| [The middle is worth everything](cases/cases_pages/kim_scoring_a1_negative.md) | `(1,1)` | **Berry** | negative voting — fewest last places wins |
| [Approval, lukewarm seconds](cases/cases_pages/kim_approval_lukewarm_seconds.md) | `(0,1)` | **Almond** | the voters set the dial — and one intensity pattern |
| [Approval, intense seconds](cases/cases_pages/kim_approval_intense_seconds.md) | `(0,1)` | **Berry** | *identical rankings*, different intensities, different winner |

Sources: [`kim_scoring_a0_plurality.yaml`](cases/kim_scoring_a0_plurality.yaml) · [`kim_scoring_ahalf_borda.yaml`](cases/kim_scoring_ahalf_borda.yaml) · [`kim_scoring_a1_negative.yaml`](cases/kim_scoring_a1_negative.yaml) · [`kim_approval_lukewarm_seconds.yaml`](cases/kim_approval_lukewarm_seconds.yaml) · [`kim_approval_intense_seconds.yaml`](cases/kim_approval_intense_seconds.yaml)

## Three winners, nobody changed their mind

On this repo's 0–5 ballot the vector `(1, A, 0)` is written ×4, so the three ordinal settings are `(4,0,0)`, `(4,2,0)` and `(4,4,0)`. Here are the three scoring rounds side by side — the same 36 people, three different results:

| | Almond | Berry | Cocoa | Winner |
|---|--:|--:|--:|:--:|
| **A = 0** (plurality) | 48 | 32 | **64** | Cocoa |
| **A = ½** (Borda) | **78** | 74 | 64 | Almond |
| **A = 1** (negative) | 108 | **116** | 64 | Berry |

Cocoa leads the first count by 16 points and finishes last in the second. Berry finishes *last* under plurality with 32 and *wins* under negative voting. Not one voter revised an opinion, and not one ranking moved — a designer turned a dial.

That instability is the standard objection to scoring rules and it is old news (it is Saari's territory). What Kim does with it is the new part: he argues the dial should not be the **designer's** to set. His incentive-compatible optimum hands it to the **voter**.

### Each setting destroys something different

Worth watching in the ballot blocks, because it is the mechanism behind the table:

- **At A = 0** the two Cocoa blocs — 7 who rank Almond second, 9 who rank Berry second — hand in *identical* papers and collapse into one row of 16. A Choose-One ballot cannot tell them apart.
- **At A = 1** the collapse moves: the 12 `Almond > Berry` voters and the 8 `Berry > Almond` voters both mark `(4,4,0)`, merging into a row of 20.
- **At A = ½** nothing collapses. Three distinct marks, four distinct rows, and — the only file where this happens — **zero Equal Support** in the runoff.

STAR's automatic runoff tracks that exactly. At both ends of the dial the ballot has already thrown the information away, so the runoff has nothing to add and simply confirms the scoring round (8 and 20 voters respectively register Equal Support). Only in the middle file does the runoff have real data, and there it agrees with the scoring round too — Almond beats Berry 19–17.

<!-- report:kim_scoring_ahalf_borda -->
```text
[Divergence from STAR]
  STAR                   = Almond
  Choose-One (Plurality) = Cocoa   (differs from STAR)
  Approval               = Cocoa   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 36 ballots.
Count × Almond,Berry,Cocoa
   12 ×      4,    2,    0
    9 ×      0,    2,    4
    8 ×      2,    4,    0
    7 ×      2,    0,    4

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Almond        -- 78 -- First place
   Berry         -- 74 -- Second place
   Cocoa         -- 64
 Almond and Berry advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Almond        -- 19 -- First place
   Berry         -- 17
   Equal Support --  0
 Almond wins.
   Runoff math:
     36  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     36  voters with a preference  (majority = 19)
           Almond 19 (53%)  ·  Berry 17 (47%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Almond
```
<!-- /report -->

> **Read the divergence block in the `A = 1` file with care.** It reports `Choose-One (Plurality) = Almond`, which is *not* the plurality answer to this election — the plurality answer is Cocoa, and it is [file 1](cases/cases_pages/kim_scoring_a0_plurality.md). Every ballot in the negative-voting file has two candidates tied at 4, so "this ballot's top choice" is decided by candidate priority order rather than by the voter. The engine flags this itself ("36 of 36 ballots (100%) had equal non-zero scores"). It is an artifact of reading a Choose-One count off a ballot that was never a Choose-One ballot.

## Why Borda is the one to beat

Borda gets a rough ride in this library — the [Dark Horse](../dark_horse_borda/README.md) folder is about the trap it sets — so it is worth being precise about the role it plays here. In Kim's environment it is not one setting among many. His **Proposition 1** characterizes every Pareto-efficient ordinal rule as a scoring rule whose scores are *the expected values of the ranked positions* given the voter's ranking, and **Corollary 1** picks out the utilitarian-best one. When a voter's middle value is uniform on `(0, 1)`, that expectation is exactly ½.

So `(1, ½, 0)` is the **best an ordinal ballot can do** in this environment, and Theorem 2's cardinal rule is claimed to beat it — not to beat plurality, which would be no achievement.

## The half a ranking cannot record

The two approval files are the payoff. They carry the **same 36 rankings** as everything above. The only difference is *which voters feel strongly about their second choice* — and that is not a fact any ranked ballot records.

| | Almond | Berry | Cocoa | Winner |
|---|--:|--:|--:|:--:|
| **Lukewarm seconds** — only the 7-voter bloc approves two | **19** | 8 | 16 | Almond |
| **Intense seconds** — the 12- and 9-voter blocs approve two | 12 | **29** | 16 | Berry |

<!-- report:kim_approval_intense_seconds -->
```text
--- Approval Voting (single winner) ---
 Tabulating 36 ballots (any non-zero score = approval).

Ballots:
   columns = Almond, Berry, Cocoa      (1 = approve; 0 / blank / marker = not approved)
    12 × 1,1,0
     8 × 0,1,0
     7 × 0,0,1
     9 × 0,1,1

   Berry  -- 29 (81%) -- Elected
   Cocoa  -- 16 (44%)
   Almond -- 12 (33%)

[Approval Distribution] (how many candidates each ballot approved)
   57 approvals across 36 ballots — average 1.6 of 3 (range 1–2).
     approved 1: 15 ballots
     approved 2: 21 ballots

[Co-Approval Matrix]
 Of the voters who approved the ROW candidate, the % who ALSO approved the COLUMN candidate.
           | Berry  | Cocoa  | Almond |
   ------------------------------------
   Berry   |   --   |  31%   |  41%   |
   Cocoa   |  56%   |   --   |   0%   |
   Almond  |  100%  |   0%   |   --   |

Winner — Approval Voting (single winner)
  Berry
```
<!-- /report -->

Kim draws the line in one sentence: plurality, Borda and negative voting count as ordinal rules because a ranking suffices to implement them, whereas approval — in his words — "requires more than information about ordinal preferences."

So across this folder one fixed set of rankings elects **Cocoa**, **Almond** or **Berry** depending on a dial — and when the voters hold the dial, it still elects **Almond** or **Berry** depending on something no ranking contains.

## What this folder does *not* show

Three honest limits, because the cases are easy to over-read:

1. **Approval is not Kim's optimum.** `(0, 1)` is the extreme corner of the family. His rule pulls both vectors inward to a pair chosen so that a voter sitting exactly on the intensity threshold is *indifferent* between them — which is what makes honest reporting a best response. In the paper's two-agent uniform example the threshold is `β* = 1/√2`, giving `(A, B) ≈ (0.354, 0.854)`. Approval here is the **shape** of his answer, not the answer.
2. **Nothing here demonstrates incentive compatibility.** These files are tallies. IC is a claim about what a voter would gain by lying, and it lives in the paper's Bayesian model — a common prior, symmetric alternatives, everyone else honest — none of which a ballot file can exhibit.
3. **STAR is not in Kim's design space at all.** Every rule in this family maximizes a *sum*. STAR's [automatic runoff](../../01_STAR/01_Learn/the_count/STAR_Automatic_Runoff.md) is a majoritarian correction applied *after* the sum, so it is not an (A,B)-scoring rule, and the paper neither supports nor refutes it. The STAR winners printed in these files agree with the scoring rounds for the reasons given above, not because the paper says they should.

## Related

- [Ordinal vs. cardinal, as mechanism design](../../07_Concepts/topics/ordinal_vs_cardinal_mechanism_design.md) — the concept page this folder supports: Kim's three results, claim-checked
- [Cardinal utility](../../07_Concepts/topics/cardinal_utility.md) — what a score is reaching for, and Hillinger's rival account of the same question
- [The Gibbard–Satterthwaite theorem](../../07_Concepts/topics/gibbard_satterthwaite_theorem.md) — the impossibility Kim escapes by weakening the incentive requirement
- [Hillinger's evaluative voting](../hillinger_evaluative_voting/README.md) — the other paper in this library that argues every rule is already cardinal, and differs only in what it forbids
- [Dark Horse Borda](../dark_horse_borda/README.md) — Borda's failure mode, for balance against the role it plays here
- [Approval in the theory literature](../../04_Approval/01_Learn/approval_in_the_literature.md) — what a checkmark means, which is the question the two approval files turn on
- [Scores vs. ranks](../../07_Concepts/scores_and_ranks/scores_vs_ranks.md) — the same distinction at the ballot level, without the theory
