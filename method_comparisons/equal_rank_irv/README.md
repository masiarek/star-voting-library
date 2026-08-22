# Equal ranks on an IRV ballot — the two ways to generalize instant runoff

*Mark two candidates equal on a US ranked ballot and you have spoiled it. That is a fact about every jurisdiction that runs instant runoff — and it is a **design choice, not a mathematical necessity**. IRV extends to ballots with ties in exactly two natural ways, and a 2024 result proves the two are not equally good: one of them keeps every property that makes instant runoff worth having, and the other — the one actually deployed — keeps none of them.*

**Level: 301 · deep dive**

→ the method: [RCV-IRV (Hare)](../../06_Other/RCV_IRV/concepts/RCV-IRV-Hare.md) · the ballot: [weak ranks](../../07_Concepts/scores_and_ranks/weak_ranks.md) · the variant page: [RCV-IRV with equal ranks](../../06_Other/RCV_IRV/concepts/variants/RCV-IRV-equal-rank.md) · the axiom it turns on: [independence of clones](../../05_Ranked_Robin/01_Learn/rr_clone_independence.md)

---

## The two rules

Both work exactly like ordinary instant runoff — score every candidate, eliminate the lowest, repeat — and both agree with it perfectly on a ballot with no ties. They differ on one question: **what is a tie worth?**

| | A ballot whose top surviving choices are `Aida=Bram` gives… | Where it is used |
|---|---|---|
| **Approval-IRV** | **one full point to each** — Aida 1, Bram 1 | Described by Janson (2016) from Phragmén's 1903 principle; not deployed |
| **Split-IRV** | **one point split between them** — Aida ½, Bram ½ | **In real use**: John Muir Trust (since 1998), London Mathematical Society (since 1999), R's `vote` package |

Split-IRV is the intuitive one — it encodes "every voter has a single vote" — and it is the one people reach for. It is also the one that breaks.

## What the theorem says

Théo Delemazure and Dominik Peters, [*Generalizing Instant Runoff Voting to Allow Indifferences*](https://arxiv.org/abs/2404.11407) (EC'24), work inside the class of **elimination scoring rules** — every rule of the shape "score the ballots somehow, drop the lowest, repeat" — and prove Approval-IRV is the *unique* member of that class with the properties IRV is sold on.

| | Approval-IRV | Split-IRV |
|---|---|---|
| **Independence of clones** — running a near-identical candidate can't change who wins | ✅ (Thm 3.2) | ❌ |
| **Respect for cohesive majorities** — if a majority all rank *x* first, the winner must be someone one of them ranked first | ✅ (Thm 3.5) | ❌ |
| **Indifference monotonicity** — raising the winner to *tie* your favorite can't defeat them | ✅ | ❌ |
| **Generalized PSC** (the multi-winner version, Approval-STV vs Split-STV) | ✅ (Thm 5.4) | ❌ |

Independence of clones is the one that matters most politically: it is [IRV's central claim over Choose-One voting](../../06_Other/RCV_IRV/concepts/why_rcv_irv.md) — that a similar candidate entering the race can't spoil it. Tideman proved strict-ballot IRV has it. **Split-IRV throws it away**, so an organization that allows equal ranks the intuitive way has quietly given up the reason it adopted the method.

## The cases

Every file below is a real 0-5 score election this engine counts, because **a score ballot already is a weak order** — two 5s are an equal-first exactly as `Aida=Bram` is. So one file carries the paper's profile *and* gives STAR's answer on the same voters, with nothing invented. The Approval-IRV and Split-IRV columns come from [`approval_irv_report.py`](../../STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/approval_irv_report.py); nothing else in this repo, and nothing on BetterVoting, counts either rule.

| Case | The point | Approval-IRV | Split-IRV | STAR | source |
|---|---|---|---|---|---|
| [Five voters, two answers](cases/cases_pages/equal_rank_five_voters.md) | The smallest election here where the two rules disagree. Aida is shared-first on two ballots, which under Split-IRV is what eliminates her. | **Aida** | Bram | **Aida** | [`yaml`](cases/equal_rank_five_voters.yaml) |
| [A bare majority tops Amira — Basil still wins](cases/cases_pages/equal_rank_majority_alternative.md) | Why "elect a candidate a majority ranks first" is the *wrong* axiom: 102 of 200 rank Amira first, but 98 strictly prefer Basil and only 8 the reverse. | **Basil** | Amira | **Basil** | [`yaml`](cases/equal_rank_majority_alternative.yaml) |
| [Costa joins Chen's ticket](cases/cases_pages/equal_rank_clone_with.md) · [and withdraws](cases/cases_pages/equal_rank_clone_without.md) | Independence of clones, as a matched pair. One clone enters and Split-IRV's winner flips from Alma to the Chen/Costa ticket. | **Alma** both | Chen/Costa → **Alma** | **Alma** both | [`yaml`](cases/equal_rank_clone_with.yaml) · [`yaml`](cases/equal_rank_clone_without.yaml) |
| [38 of 74 rally to Alice — consecutive scores](cases/cases_pages/equal_rank_cohesive_consecutive.md) · [and wide gaps](cases/cases_pages/equal_rank_cohesive_wide_gaps.md) | Respect for cohesive majorities, and the encoding trap. Same 74 voters, same preference order, two legitimate uses of the 0-5 scale. | Bilal/Cato both | **Delia** both ❌ | **Alice** → **Delia** ❌ | [`yaml`](cases/equal_rank_cohesive_consecutive.yaml) · [`yaml`](cases/equal_rank_cohesive_wide_gaps.yaml) |

Run any of them:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/approval_irv_report.py method_comparisons/equal_rank_irv/cases/equal_rank_majority_alternative.yaml
```

## The flagship case, counted

<!-- ballots:equal_rank_majority_alternative -->
*(No ballot art for `equal_rank_majority_alternative` — draw it with `build_style_ballot_images.py --from-yaml method_comparisons/equal_rank_irv/cases/equal_rank_majority_alternative.yaml`.)*

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Count:Amira,Basil,Cora,Dmitri
94:5,5,2,0    # Amira and Basil equal-first, then Cora, then Dmitri
8:5,4,2,0     # the only bloc that strictly prefers Amira to Basil
50:0,4,5,2    # Cora first, Basil a strong second
48:0,4,2,5    # Dmitri first, Basil a strong second
```
<!-- /ballots -->

102 of the 200 voters put Amira in their top class — 94 who rate her equal-first with Basil, 8 who put her alone on top. A rule promising "elect someone a majority ranked first" would have to elect Amira. Read the same ballots the other way and **98 voters strictly prefer Basil to Amira, against 8 the other way.** Basil is the Condorcet winner.

Split-IRV halves those 94 equal-first ballots, which drops Basil to last (47 points against Amira's 55) and eliminates him in round one. Approval-IRV gives both a full point, and Basil wins. **So does STAR:**

<!-- report:equal_rank_majority_alternative -->
```text
[Divergence from STAR]
  STAR                   = Basil
  Choose-One (Plurality) = Amira   (differs from STAR)
  RCV-IRV                = Amira   (differs from STAR)
  Note: 94 of 200 ballots (47%) had equal non-zero scores, so their ranks
        were decided by candidate priority order. The RCV-IRV result may be
        an artifact of score-to-rank tie-breaking rather than a deep
        difference.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/equal_rank_majority_alternative_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 200 ballots.
Count × Amira,Basil,Cora,Dmitri
   94 ×     5,    5,   2,     0
   50 ×     0,    4,   5,     2
   48 ×     0,    4,   2,     5
    8 ×     5,    4,   2,     0

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Basil         -- 894 -- First place
   Cora          -- 550 -- Second place
   Amira         -- 510
   Dmitri        -- 340
 Basil and Cora advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Basil         -- 150 -- First place
   Cora          --  50
   Equal Support --   0
 Basil wins.
   Runoff math:
     200  ballots cast
   −   0  Equal Support (no preference between the two finalists)
     ───
     200  voters with a preference  (majority = 101)
           Basil 150 (75%)  ·  Cora 50 (25%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Basil
```
<!-- /report -->

## What this says about STAR

Three things, and the third one cuts the other way.

**1. STAR never had this problem.** The paper's whole difficulty — how do you let a voter say "these two are equal" — does not arise on a 0-5 ballot, which has expressed weak orders since the day it was drawn. What the paper is doing is the serious axiomatic work needed to buy, for ranked ballots, an expressiveness the score ballot gives away for free. That is worth saying without triumph: it is a real result about a real ballot most of the world actually uses.

**2. Where the paper's own axioms point, STAR usually goes.** On the two profiles built to separate good behavior from bad, STAR lands with Approval-IRV and against Split-IRV — Aida in the five-voter case, Basil in the majority-alternative case. Neither is a fluke of the scores chosen: across 20,000 random strictly-decreasing 0-5 encodings of each profile, STAR elects Basil **98.5%** of the time (and never anyone else) and Aida **92.9%**.

**3. But STAR fails respect for cohesive majorities, and the fourth case is the witness.** 38 of 74 voters rank Alice in their top class, so the axiom permits Alice, Bilal or Cato and forbids Delia. Give those voters consecutive scores and STAR elects Alice; give them the same preference order with wide gaps and **STAR elects Delia** — the one candidate the majority excluded. Both files are ordinary 0-5 ballots inducing the identical weak order. Approval-IRV satisfies the axiom on both.

That third point has a companion worth reading beside it: respect for cohesive majorities is **generalized PSC at one seat and one candidate**, and Allocated Score fails the multi-winner version too — see [solid coalitions and STAR-PR](../../03_STAR_PR/03_Criteria/solid_coalitions/README.md). And STAR is in wide company here: the paper's Proposition 3.4 proves **no rule that reads only pairwise margins can satisfy the axiom**, which rules out Schulze, Ranked Pairs and Minimax. Approval-IRV's claim to it is genuinely unusual.

**And a fourth thing, about method.** The Alice/Delia pair is the clearest demonstration in this library of something easy to say and hard to feel: **a weak order does not determine a STAR result.** Translating any ordinal profile into scores adds information, and on that profile the added information decides the election. Every ordinal case in this repo that gets scored is making an assumption; this pair is where the assumption is visible. It is also why the STAR percentages quoted above were measured across thousands of encodings rather than asserted from one.

## Why anyone would want this on a real ballot

The paper's motivation is not axiomatic, it is operational — equal-rank ballots are already being cast, by voters who did not mean to spoil anything.

- **San Francisco, 2019 mayoral.** Of 206,117 ballots, **899 (0.4%)** could be read as a weak order with at least one genuine tie. The authors read the county's published CVR JSON and ballot images to count them.
- **Scotland, 2017 local elections.** **1.6%** of ballots were rejected for having multiple top choices.
- **Portland, Maine, 2021 city council.** McCune reports the race was close enough that **a different treatment of overvotes would have changed the winner.**
- **It is not evenly spread.** In San Francisco the weak-order rate correlates *negatively* with precinct median household income (r = −0.4, p < 0.001) — matching earlier findings on invalid-ballot and overvote rates in San Francisco and New York City. Whatever else a ban on equal ranks is, it is not neutral about who it disqualifies.

Against which the paper is honest about the costs, and so is this page: Approval-IRV **inherits IRV's real problems** — it is still non-monotonic in the ordinary sense, still not Condorcet-consistent, still [center-squeezable](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md). Allowing equal ranks fixes the *ballot*, not the *count*. And more permissive ballot instructions are themselves a source of voter error, which could give back some of what it saves.

## One discrepancy, recorded

This library runs the figures it cites, and one of them does not count as printed. Of the paper's Figure 11 the text says *"Approval-IRV selects a."* Counted, Approval-IRV eliminates d, then **a**, and ends in a 64–64 tie between b and c — `Bilal, Cato` in [our cast](cases/equal_rank_cohesive_consecutive.yaml). **Theorem 3.5 is untouched**: b and c are both inside the set the axiom permits, so respect for cohesive majorities holds exactly as proved. It is the illustrative sentence that names the wrong candidate, not the theorem. Our count agrees with the paper on Figures 3, 9 and 10, and the round-by-round table is in the report so it can be checked rather than believed.

## Related

- [RCV-IRV with equal ranks](../../06_Other/RCV_IRV/concepts/variants/RCV-IRV-equal-rank.md) — the variant page, in the RCV-IRV family
- [Weak ranks](../../07_Concepts/scores_and_ranks/weak_ranks.md) · [strict vs. weak ranks](../../07_Concepts/scores_and_ranks/strict_vs_weak_ranks.md) — the ballot
- [Exhausted ballots](../../06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md) — the other way an IRV ballot stops counting
- [Solid coalitions and STAR-PR](../../03_STAR_PR/03_Criteria/solid_coalitions/README.md) — the multi-winner half of the same axiom

*Source: Théo Delemazure & Dominik Peters, ["Generalizing Instant Runoff Voting to Allow Indifferences"](https://arxiv.org/abs/2404.11407) — Proceedings of the 25th ACM Conference on Economics and Computation (EC'24), [ACM DL](https://dl.acm.org/doi/10.1145/3670865.3673501), [author PDF](https://dominik-peters.de/publications/approval-irv.pdf). **Lean: neutral academic social choice** — the authors are theorists at CNRS/Paris Dauphine with no campaign affiliation, and the paper is explicit that Approval-IRV inherits IRV's known defects. Prior art it credits: Janson (2016) on Phragmén's principle; Meek, Warren and Hill in *Voting Matters* for the Split construction; Aziz & Lee (2020) for generalized PSC and the Expanding Approvals Rule. Glossary: [`independence of clones`](../../07_Concepts/GLOSSARY.md) · [`overvote`](../../07_Concepts/GLOSSARY.md).*
