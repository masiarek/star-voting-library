# The valuable Condorcet loser — what a majority runoff costs, priced by theorem

*A runnable companion to Ebadian, Latifian & Shah, **"The Distortion of Approval Voting with Runoff"** (AAMAS 2023) — the closest published relative to STAR's score-then-runoff shape, and a result that **cuts against the runoff**: in the adversarial (unit-sum) distortion model, adding a majority runoff to approval voting makes its worst case **worse**, not better — Θ(m) → Θ(m²) — because a runoff structurally blocks a candidate the paper's proof pivots on: the **valuable Condorcet loser**, adored by a large minority, ranked below everyone by the rest, and still the highest-welfare candidate in the race. This page states the paper's results honestly, then makes that pivotal scenario countable on nine ballots — where **Score elects Amy and STAR's runoff (correctly, majoritarianly) rejects her**. Read next to [Metric distortion](../../07_Concepts/topics/distortion.md), where the *same* runoff is the insurance step: two models, two verdicts, and the model decides.*

**Level: 301 · deep dive** Companions: [Distortion (umbrella)](../../07_Concepts/topics/distortion.md) · [Metric distortion](../../07_Concepts/topics/distortion.md) · [What makes a good winner? — majoritarian vs. utilitarian](../../07_Concepts/topics/what_makes_a_good_winner.md#the-deepest-split-majoritarian-vs-utilitarian) · [Where do you draw the line? (ex13)](../../01_STAR/05_Practice/ex13_draw_the_line.md).

---

## What the paper proves (the honest summary)

The setting is the **unit-sum** distortion model — each voter's utilities sum to 1, no geometry assumed (the adversarial model on the [umbrella page](../../07_Concepts/topics/distortion.md), *not* the metric one). Voters cast approval ballots by approving everything above a utility threshold τ; a *pair-selection rule* picks two finalists from the approvals; a majority runoff between the finalists picks the winner. That's the shape St. Louis, Missouri has used for real since 2021 — in its first approval-runoff mayoral election, 44,571 voters approved among four candidates, and 58,237 voters settled the top two in the runoff round. The paper asks: what is the *optimal* way to pick the two finalists, and what does the runoff stage do to the guarantee? Their results table (m = number of candidates):

| | No runoff | **Majority runoff** | Proportional runoff |
|---|---|---|---|
| Deterministic rules | Θ(m) | **Θ(m²)** | Θ(m) |
| Randomized rules | Θ(√m) | **Θ(m)** | O(m), Ω(m^0.6) |

Three findings worth carrying:

1. **The majority runoff is the culprit — by a factor of m.** Single-stage approval achieves Θ(m) deterministically; bolt on a majority runoff and the best achievable becomes Θ(m²) (their Theorems 5.2–5.5). The failure is *structural*, not a matter of picking finalists badly: even a pair-selection rule **with access to the exact utilities** can't beat Ω(m), because a Condorcet loser can never survive a majority runoff no matter how valuable she is (their Example 5.1 — the instance made countable below).
2. **The approval threshold is load-bearing.** For τ > 1/(m−1), *any* deterministic rule has unbounded distortion (everyone may approve nobody); the optimum sits at τ = 1/m, and their experiments put the empirically best threshold at about **2/m**. Theory's version of the repo's cutoff lesson: [where you draw the approval line has outcome power](../../01_STAR/05_Practice/ex13_draw_the_line.md).
3. **Their fix keeps the two-round shape but drops the majority rule:** a *proportional runoff* (each finalist wins with probability equal to her share of the runoff vote) restores Θ(m) — at the price of a randomized winner, which real public elections don't accept. The honest reading: within this model, the welfare cost *is* the majority check itself, not the second round.

**Lean disclosure:** peer-reviewed CS (AAMAS), no stake in the US reform fight — the neutral tier. Its blind spot is the usual one for worst-case theory: adversarial instances, tractability-driven models, nothing about usability or legitimacy — and a randomized "proportional runoff" is a theorist's device, not a proposal any election office would run.

## The pivotal scenario, on nine ballots

The paper's Example 5.1 is a *utility profile*; here it is as a countable election — [`vcl_c4_b9_score_vs_runoff`](cases/cases_pages/vcl_c4_b9_score_vs_runoff.md) ([yaml](cases/vcl_c4_b9_score_vs_runoff.yaml)). Four voters adore **Amy** and score everyone else zero; five voters score Amy zero and spread mild support across **Ben, Cora, Dan** (one of them leans Ben, so every count below is deterministic):

```
Amy,Ben,Cora,Dan
  5,  0,  0,  0   × 4 voters   (the devoted minority)
  0,  2,  2,  2   × 4 voters   (the spread-the-love majority)
  0,  3,  2,  1   × 1 voter    (same bloc, leans Ben)
```

One electorate, three defensible winners, all from the same arithmetic:

- **Score totals: Amy 20, Ben 11, Cora 10, Dan 9.** Amy is the **utilitarian winner** — nearly double the runner-up. Pure Score voting elects her.
- **Head-to-head: Amy loses every matchup 4:5.** She is the **Condorcet loser**; Ben (who beats Amy 5:4 and edges Cora and Dan 1:0 with eight Equal Support) is the **Condorcet winner**.
- **STAR: finalists Amy (20) and Ben (11); runoff Ben 5, Amy 4 → Ben.** A textbook [Runoff Reversal](../../01_STAR/02_Examples/runoff_overturns_leader/README.md) — the score leader with the most total support loses the majority check. And any *approval-with-runoff* rule does the same or worse: whichever pair reaches the runoff, Amy can't win it, exactly the paper's point.

The embedded LH report, with the engine calling all of it:

<!-- report:vcl_c4_b9_score_vs_runoff -->
```text
[Divergence from STAR]
  STAR     = Ben
  Approval = Amy   (differs from STAR)

[Runoff Reversal]
 - Score Round Winner(s) = (Amy)
 - Runoff Round Winner   = (Ben)
  Candidate Amy earned the highest total score, but
  Candidate Ben won the automatic runoff — not a malfunction,
  STAR working as designed: the runoff elects the finalist preferred
  by the majority (of voters with a preference).

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 9 ballots.
Count × Amy,Ben,Cora,Dan
    4 ×   5,  0,   0,  0
    4 ×   0,  2,   2,  2
    1 ×   0,  3,   2,  1

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Amy           -- 20 -- First place
   Ben           -- 11 -- Second place
   Cora          -- 10
   Dan           --  9
 Amy and Ben advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Ben           -- 5 -- First place
   Amy           -- 4
   Equal Support -- 0
 Ben wins.
   Runoff math:
     9  ballots cast
   − 0  Equal Support (no preference between the two finalists)
     ─
     9  voters with a preference  (majority = 5)
           Ben 5 (56%)  ·  Amy 4 (44%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Ben
```
<!-- /report -->
Want the whole count? see the full LH report → [`cases_pages/vcl_c4_b9_score_vs_runoff.md`](cases/cases_pages/vcl_c4_b9_score_vs_runoff.md).

(That `elected by Approval!` line is itself a τ lesson: LH's approval conversion approves scores ≥ 3, so Amy wins approval 4:1 — while a voter approving everything ≥ 1 would elect Ben 5:4. The winner flips on the threshold, which is finding 2 in miniature.)

Distortion, concretely: the elected Ben carries welfare 11 against Amy's 20 — a ratio of **1.8 on nine ballots**. The paper's construction scales this same shape up: as the field grows, the majority-runoff loss grows like m, which is where Θ(m²) comes from.

## What this means for STAR (both directions, per [reading these fairly](../paradoxes_and_whoops/reading_these_fairly.md))

**Against the runoff (this paper's model):** STAR's automatic runoff is a majority check, and this paper prices what a majority check *costs* in the adversarial worst case — it structurally excludes the valuable Condorcet loser, the candidate who maximizes total satisfaction while losing every pairwise vote. When STAR advocacy says the runoff "protects against a weak winner," this is the counter-scenario: sometimes the candidate the runoff blocks was the *strongest* by total support. That's not a bug report — it's the [majoritarian-vs-utilitarian choice](../../07_Concepts/topics/what_makes_a_good_winner.md#the-deepest-split-majoritarian-vs-utilitarian) made explicit, and STAR *chooses* the majoritarian answer in its second round, by design.

**For the runoff (the metric model):** the [metric page](../../07_Concepts/topics/distortion.md) proves the mirror image — under the spatial assumption, "majority prefers W" *geometrically bounds* W's welfare loss at 3×, so the runoff is an insurance step. Both theorems are true; they disagree because the models do. In a spatial electorate the beloved-of-a-minority, despised-by-the-rest profile that drives Θ(m²) barely occurs (a candidate close to 4 voters and maximally far from 5 others strains the geometry the majority ballots imply); in the unit-sum adversarial world it's the *first* profile the adversary reaches for. **Never quote a distortion verdict on the runoff without naming the model** — the repo's standing simulation rule, now with a theorem-grade example on each side.

**And the gap that stays open:** none of this yields a distortion number *for STAR* — the paper analyzes approval ballots into a runoff, a cruder first round than STAR's 0–5 scores (the authors' own framing of why the first stage matters: richer first-round information changes what pair-selection can do). The umbrella page's [open-gap note](../../07_Concepts/topics/distortion.md) stands: nearest relative, not a bound.

## Sources

- Ebadian, Latifian & Shah, [*The Distortion of Approval Voting with Runoff*](https://www.ifaamas.org/Proceedings/aamas2023/pdfs/p1752.pdf) (AAMAS 2023) · [full version with proofs](https://www.cs.toronto.edu/~nisarg/papers/distortion-approval-runoff.pdf).
- Delemazure, Lang, Laslier & Sanver, *Approval with Runoff* (IJCAI 2022) — the rule's introduction and the axiomatic study this paper quantifies.
- The umbrella's source list: [Distortion — Sources](../../07_Concepts/topics/distortion.md#sources), including the IJCAI-21 survey.
