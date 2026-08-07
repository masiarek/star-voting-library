# Reweighted Range Voting (RRV) — the divisor method in the family

*Don't spend ballots — **divide** them. After each seat, every ballot's weight is divided by a growing factor based on how much score it has already given to winners. It is the oldest cardinal-PR proposal and the simplest to tabulate, and it is the one member of this family that **does not pass the Hare Quota Criterion**.*

→ Family: [the three STAR-PR methods](README.md) · the theory underneath: [the math behind proportional STAR](the_math_behind_proportional_star.md) · the quota methods it differs from: [Allocated Score](allocated_score.md) · [SSS](sequentially_spent_score.md)

**Level: 301 · deep dive**

---

## How it counts

Seat the highest scorer. Then, rather than marking some voters represented and setting them aside, **re-weight every ballot at once**: a ballot's weight becomes `1 / (1 + sum_of_score_given_to_winners / max_score)` — a D'Hondt/Jefferson-style divisor. A ballot that gave a seated winner 5 stars is halved; one that gave 0 is untouched; everything else lands in between. Re-tally with the new weights and seat the next candidate.

Nobody is ever "used up," and no quota is ever computed. That single design choice is the whole story below.

`voting_method: rrv` plus `num_winners: k`.

## Watch it count

The same 63 ballots as the other two methods:

<!-- report:02c_c5_b63_proportional-rrv -->
```text
[Divergence from STAR]
  STAR                   = Ben
  Choose-One (Plurality) = Alice   (differs from STAR)
  Approval               = Alice   (differs from STAR)

--- Reweighted Range Voting Method (3 winners) ---

[Reweighted Range Voting]
 Tabulating 63 ballots to fill 3 seats.
Count × Alice,Ben,Cara,Dan,Eve
   18 ×     5,  4,   3,  0,  0
   15 ×     0,  0,   0,  5,  4
   12 ×     4,  5,   3,  0,  0
    9 ×     3,  4,   5,  0,  0
    9 ×     0,  0,   0,  4,  5

[Reweighted Range Voting: Round 1: Score round]
 The highest-scoring candidate wins a seat.
   Ben           -- 168 -- First place
   Alice         -- 165
   Cara          -- 135
   Dan           -- 111
   Eve           -- 105
 Ben wins a seat.

[Reweighted Range Voting: Round 1: Reweighing Ballots]
 Reweighted 39 ballots:
   27 ballots reweighted from 1 to 5/9.
   12 ballots reweighted from 1 to 1/2.

[Reweighted Range Voting: Round 2: Score round]
 The highest-scoring candidate wins a seat.
   Dan           -- 111 -- First place
   Eve           -- 105
   Alice         --  89
   Cara          --  73
 Dan wins a seat.

[Reweighted Range Voting: Round 2: Reweighing Ballots]
 Reweighted 24 ballots:
   15 ballots reweighted from 1 to 1/2.
   9 ballots reweighted from 1 to 5/9.

[Reweighted Range Voting: Round 3: Score round]
 The highest-scoring candidate wins a seat.
   Alice         -- 89 -- First place
   Cara          -- 73
   Eve           -- 55
 Alice wins a seat.

[Reweighted Range Voting: Winners — Reweighted Range Voting Method (3 winners)]
 Alice
 Ben
 Dan
```
<!-- /report -->

**Alice, Ben, Dan** — the same slate the quota methods reach. A clean two-coalition electorate is exactly the case where the family difference is invisible. For the case where it is *not*, see the divergence below.

## Where the methods actually part company

On the **Lackner & Skowron shadow election** — the running example used across the multi-winner literature, 7 candidates and 12 ballots, four seats — the identical ballots give:

- **[Allocated Score](../../02_Examples/cases/cases_pages/lackner_skowron_shadow_star_pr_c7_b12.md) → A, B, C, D**
- **[RRV](../../02_Examples/cases/cases_pages/lackner_skowron_shadow_star_pr_rrv_c7_b12.md) → A, B, C, F**

Three seats agree; the fourth does not. That last seat is the quota-versus-divisor question made concrete, and it is the case to reach for when someone asks whether the choice between these tabulations is merely academic.

## Where it stands, honestly

**RRV is a divisor method, and the trade cuts both ways.** Classical apportionment theory (Pukelsheim, ch. 9) proves a **Coherence Theorem**: a method is coherent — every subset of the winners, re-solved on its own, gives the same answer — *if and only if* it is a divisor method. So RRV is coherent, house-size monotone and vote-ratio monotone, and structurally immune to the family of paradoxes that quota methods are prone to — including the **[Alabama paradox this library demonstrates for Allocated Score](../../03_Criteria/alabama_paradox/README.md)**. That is a real advantage, and it should not be buried under the criterion failure below.

**What it pays for that: it does not guarantee quota.** A faction holding a quota's worth of voters cannot always force a seat by voting as a bloc, so RRV **fails the [Hare Quota Criterion](../what_proportional_means.md)** — which is why some classify it as **semi-proportional** rather than proportional. Structurally it belongs to the Thiele school, which equalizes satisfaction rather than allocating quotas; the criterion failure is a different answer to what "proportional" should mean, not a bug.

**It is not on Equal Vote's shortlist, and that is consistent rather than incidental.** Their committee's three finalists are Allocated Score, SSS and Sequential Monroe. RRV is the one that doesn't pass the quota criterion. Their summary of the trade, with the lean stated: RRV is the mathematically simplest tabulation and the oldest cardinal-PR proposal, but tends toward more utilitarian and less diversified winners, and is less transparent to non-mathematicians.

**One more sensitivity worth knowing:** because the divisor is computed from score *relative to the maximum*, RRV is more exposed than its siblings to the ballot's granularity — [changing the score scale can flip the winner](../../../07_Concepts/scores_and_ranks/scale_granularity_flips_the_winner.md).

## Scenarios in this library

Two case files use `rrv`, and between them they make the whole point — one where RRV agrees with the quota methods and one where it doesn't:

| Scenario | What it shows | Read · run |
|---|---|---|
| **The 63-ballot baseline** | The count above. Same slate as [Allocated](allocated_score.md) and [SSS](sequentially_spent_score.md) — the family difference stays invisible on a clean two-coalition race. | [page](../../02_Examples/cases/cases_pages/02c_c5_b63_proportional-rrv.md) · [yaml](../../02_Examples/cases/02c_c5_b63_proportional-rrv.yaml) |
| **Shadow — Lackner & Skowron** | The divergence: **A, B, C, F** where Allocated Score seats D, on identical ballots. | [page](../../02_Examples/cases/cases_pages/lackner_skowron_shadow_star_pr_rrv_c7_b12.md) · [yaml](../../02_Examples/cases/lackner_skowron_shadow_star_pr_rrv_c7_b12.yaml) |

## Related

- **The quota methods:** [Allocated Score](allocated_score.md) — the recommended STAR-PR · [Sequentially Spent Score](sequentially_spent_score.md)
- **The shared theory:** [the math behind proportional STAR](the_math_behind_proportional_star.md) — quotas, divisors, Balinski–Young
- **The criterion it fails:** [what "proportional" actually means](../what_proportional_means.md)
- **Pure Score without seats:** [Range / Score Voting](../../../06_Other/Range/concepts/range_voting.md)
