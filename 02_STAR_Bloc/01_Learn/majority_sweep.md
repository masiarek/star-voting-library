# The majority sweep

**One line:** because every seat in a Bloc STAR race is decided by the *same* voters on the *same* unchanged ballots, a **cohesive majority can win every seat** — 55% of the electorate can take a council 5–0 and leave the other 45% with nothing. This is not a bug in the count; it is what "majoritarian" means, and it is the single fact that decides whether Bloc STAR is the right method for your body.

→ The fork this sits on one side of: [Electing more than one, simply](../../07_Concepts/topics/electing_more_than_one.md) · the method that refuses to do this: [STAR-PR](../../03_STAR_PR/01_Learn/README.md) · the mechanics: [Bloc STAR](bloc_star.md)

**Level: 201 · for voters**

---

## Why it happens

Nothing carries over between seats. Seat 2 is counted on the identical ballots that decided seat 1, minus one name. So if a group is both **large enough** and **agreed enough**, it wins every round for the same reason it won the first:

- **The scoring round.** Suppose a majority scores its own slate high and the rest 0. Every slate member's total is built from more than half the ballots; every outsider's total is built from fewer. The slate therefore occupies the top of the score order and keeps supplying both finalists until it runs out of candidates.
- **The runoff.** When a slate member does finally meet an outsider head-to-head, the same majority prefers the slate member. More than half of the voters, every time.

Both halves of STAR point the same way, every seat, because neither half ever hears that this bloc has already been served. Compare a proportional method, which does exactly that: [STAR-PR](../../03_STAR_PR/01_Learn/STAR_PR/README.md) reweights the ballots that won a seat so they count for less on the next one.

Two qualifiers keep this honest:

- **Cohesive is doing real work.** A 60% side that splits its scores unevenly across five candidates can lose seats to a disciplined 40% side. The sweep is a *capability*, not a guarantee — which is also why Bloc STAR rewards slate discipline (see [honest limits](bloc_honest_limits.md)).
- **A sweep needs a majority to sweep with.** Where no group has one, Bloc STAR splits the seats like anything else. In [BV1835](../02_Examples/bv1835_8h3yrx_score_leader_no_seat.md) two mirror-image camps of 49 take two seats each.

## Watch it happen — 60% takes 100%

A neighborhood association elects a **two-seat** board. The north side is 6 of 10 voters and runs Asa and Bram; the south side is 4 of 10 and runs Cleo and Dane. Every voter scores their own side 5 and 4, and the other side 0:

<!-- report:ex12_bloc_sweep -->
```text
--- Bloc STAR Voting Method (2 winners) ---

[Bloc STAR]
 Tabulating 10 ballots to fill 2 seats.
Count × Asa,Bram,Cleo,Dane
    6 ×   5,   4,   0,   0
    4 ×   0,   0,   5,   4

[Bloc STAR: Round 1: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Asa           -- 30 -- First place
   Bram          -- 24 -- Second place
   Cleo          -- 20
   Dane          -- 16
 Asa and Bram advance.

[Bloc STAR: Round 1: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Asa           -- 6 -- First place
   Bram          -- 0
   Equal Support -- 4
 Asa wins.
   Runoff math:
     10  ballots cast
   −  4  Equal Support (no preference between the two finalists)
     ──
      6  voters with a preference  (majority = 4)
           Asa 6 (100%)  ·  Bram 0 (0%)

──────────────────────────────────────────────────

[Bloc STAR: Round 2: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Bram          -- 24 -- First place
   Cleo          -- 20 -- Second place
   Dane          -- 16
 Bram and Cleo advance.

[Bloc STAR: Round 2: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Bram          -- 6 -- First place
   Cleo          -- 4
   Equal Support -- 0
 Bram wins.
   Runoff math:
     10  ballots cast
   −  0  Equal Support (no preference between the two finalists)
     ──
     10  voters with a preference  (majority = 6)
           Bram 6 (60%)  ·  Cleo 4 (40%)

[Bloc STAR: Winners — Bloc STAR Voting Method (2 winners)]
 Asa
 Bram
```
<!-- /report -->
The 60% takes 100% of the board. Note *where* the south side loses: not in round 1 — Cleo was never going to out-score Asa — but in **round 2**, where she reaches the runoff and loses it 6–4. The seat was close enough to be visible and never close enough to be winnable, which is the texture of a sweep. Run it yourself: [`ex12_bloc_sweep`](../../01_STAR/05_Practice/cases/cases_pages/ex12_bloc_sweep.md) ([yaml](../../01_STAR/05_Practice/cases/ex12_bloc_sweep.yaml)); the exercise that pairs it against a proportional count of the *same ten ballots* is [Exercise 12 — bloc vs. proportional](../../01_STAR/05_Practice/ex12_bloc_vs_proportional.md), where the south side's 40% earns one of the two seats.

## The same electorate, counted five ways

[Food-Truck Row](../../method_comparisons/food_truck_row/README.md) is the sharpest version: **one** 100-voter electorate, **two** seats, five counting rules, three different outcomes. A 57-voter savory majority running three trucks against a disciplined 43-voter sweet minority running two:

| | first choices | SNTV | **Bloc STAR** | Bloc Ranked Robin | STAR-PR | STV |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| *savory : sweet (57 : 43)* | | **0 : 2** | **2 : 0** | **2 : 0** | **1 : 1** | **1 : 1** |

Nothing about the voters changes across that row. Bloc STAR hands the majority both seats; the proportional methods split them; [SNTV](../../method_comparisons/multi_member_plurality/README.md) hands the *minority* both, because the majority's three trucks split its own vote. Read the row as three answers to three different questions, not as four wrong ones and a right one.

More of the same, at other sizes: the [Pets Governance](../../method_comparisons/pets_governance/README.md) council (3 seats, bloc vs. proportional, side by side) and the [Herb Garden Council](../../06_Other/ballot_style_lab/cases/cases_pages/07a_c5_b36_herb-council-bloc-3-seats.md) (3 seats, the majority sweeps).

## So when is a sweep the right answer?

The question to ask is **what the body is for**, not how it feels to the losing side.

**Use Bloc STAR when the winners are choices, or must act as one:**

- a slate of officers who have to govern together, where a hostile faction inside the group is a defect rather than representation;
- any at-large "pick the best few" race — three finalists, four logos, five grant recipients — where the candidates aren't standing *for* anybody;
- a small body where the alternative is worse: proportional methods need enough seats for a share to mean something, and at 2 seats a "fair share" is a very coarse instrument.

**Don't use it when the body is meant to represent people:**

- a legislature, a school board, a diverse committee, a union executive — anywhere a 45% minority holding zero seats would read as a failure of the election rather than a verdict of it;
- anywhere the winners will be understood as *delegates* of the groups that elected them;
- and, as a matter of law rather than taste, anywhere a racial or language minority is **clustered in one part of the jurisdiction** — there the sweep is what federal courts call vote dilution, and the seats being filled at-large is what makes it actionable ([at-large elections and the Voting Rights Act](at_large_and_the_vra.md)).

**The tell:** picture the cohesive-majority sweep and ask whether the result would look legitimate. If yes, Bloc STAR is doing its job. If it makes you wince, you wanted [proportional representation](../../03_STAR_PR/01_Learn/README.md) and should say so before the ballots are printed — this is a decision about the *rules*, and it cannot be fixed afterward by the count.

## See also

- [Bloc STAR](bloc_star.md) — the count itself
- [Over 50% — what a landslide actually buys](over_50_percent.md) — this page's mirror image: the same majoritarian logic when the majority runs only *one* candidate, and the second seat goes to a candidate most of them scored 0
- [The score leader can win no seat](score_leader_no_seat.md) — the *other* surprise, and not this one
- [Honest limits](bloc_honest_limits.md) — the sweep, plus everything else worth disclosing
- [STAR-PR](../../03_STAR_PR/01_Learn/STAR_PR/README.md) — quota and reweighting, the machinery that prevents a sweep
- [Electing a committee — a gentle intro](../../04_Approval/01_Learn/Multiwinner_Approval/abc_rules_intro.md) — the same fork on the approval side, counting only
