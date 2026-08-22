# Resignation monotonicity — a winner resigns; can the count throw out someone who stayed?

**Level: 301 · deep dive**

**One line:** the obvious demand is that re-running a count after a winner resigns must not unseat anybody else; the non-obvious finding is that **plain Approval is the only rule that can promise it** — every proportional rule tested here breaks it, including all three of this engine's score-based PR rules, and that is a theorem rather than an accident.

> **Not the "resignation" this repo already talks about.** Two pages use the word as a metaphor for a *weak mandate* — winning a race everyone wanted to leave ([preference vs support](../../07_Concepts/scores_and_ranks/preference_vs_support.md), [weak mandate](../../01_STAR/01_Learn/reporting/weak_mandate.md)). That is about how much a win is worth. This page is about a winner literally quitting after the count, and the two have nothing to do with each other.

## The axiom

A committee is elected. Before it sits, one of its members resigns — health, a new job, a grant recipient moving institutions, a workshop organiser who can no longer attend. The seat has to be filled from the candidates who remain, so the rule is re-run on the shortened ballot. The question is what happens to *everyone else*.

> **Definition** (Oh & Peters). For an instance `E = (N, C, (Aᵢ), k)` and a set `T ⊆ C`, write `E − T` for the instance with `T` struck from the candidate set and from every ballot. A winning committee `W ∈ R(E)` is **resignation monotone** if for every `T ⊆ W` there is a replacement set `T′ ⊆ C \ W` with `(W \ T) ∪ T′ ∈ R(E − T)`. A rule is resignation monotone when every committee it outputs is. — *Candidate Resignation Monotonicity in Approval-Based Committee Elections*, [arXiv:2608.06156](https://arxiv.org/abs/2608.06156), 6 Aug 2026, §3.

The paper's own framing of why this is not negotiable is worth keeping: *"A politician who won their seat would rightly object to being removed because a colleague resigned."* Note what the axiom does **not** ask — it says nothing about who gets the vacant seat. Fill it with anyone. It only forbids evicting the survivors.

**This is a different axiom from its two neighbours in this folder**, and they are close enough to conflate:

| | what changes | what must not happen |
|---|---|---|
| [Committee monotonicity](committee_monotonicity.md) | a **seat** is added | a sitting winner is dropped |
| [Support monotonicity](support_monotonicity.md) | a **ballot** gains an approval | the approved winner is dropped |
| **Resignation monotonicity** | a **candidate** leaves | the *other* winners are dropped |

And none of the three is the [monotonicity](../../07_Concepts/topics/monotonicity/README.md) that sinks IRV, which is a single-winner, ranked-ballot pathology.

## AV passes, and it is the only one that does

Approval scores each candidate independently of who else is elected. Strike a winner and the remaining scores are unchanged, so the other winners are still the top of the list and the vacant seat goes to whoever was next. That argument is the whole proof — and the paper's **Theorem 3.1** shows it is also the *only* such argument available: among Thiele methods and sequential Thiele methods, AV is the only resignation monotone rule. Footnote 1 sharpens it: every other Thiele method admits an instance where **all** its output committees fail, so no tie-breaking rescues them.

### Witness — five rules, five voters, two seats

Example 3.2. Five voters, four candidates, two seats:

```text
v1:{c1}   v2:{c1,c3}   v3:{c1,c4}   v4:{c2,c3}   v5:{c2,c4}
```

PAV, Chamberlin–Courant, Monroe, leximax-Phragmén and Minimax Approval Voting **each uniquely elect `{c1,c2}`**. Then `c1` resigns, and each of them **uniquely elects `{c3,c4}`** — so `c2`, who did nothing, is off the committee:

```text title="Abridged for the lesson — not verbatim engine output"
before          {c1,c2}
c1 resigns      {c3,c4}      <- c2 is gone, and there was no tie to blame
```

### Witness — the representation trap

Example 3.3 is the one that shows *why* this is structural rather than a quirk of one rule. Five voters, seven candidates, five seats: two voters share `c1` and split on a second name, three voters approve the same slate of four.

```text
v1:{c1,c2}   v2:{c1,c3}   v3:{c4,c5,c6,c7}   v4:{c4,c5,c6,c7}   v5:{c4,c5,c6,c7}
```

PAV, seq-Phragmén and the Method of Equal Shares all elect `{c1,c4,c5,c6,c7}`. `c1` resigns. One seat is free — and now [justified representation](../01_Learn/Multiwinner_Approval/README.md) demands a seat for `c2` **and** a seat for `c3`, because each of those voters is now a group large enough to deserve one and has exactly one candidate left to want. Two demands, one seat. Every JR-satisfying rule must break something, and what it breaks is the slate: none of the three returns all four of `c4…c7` under any tie-breaking.

That generalises to **Theorem 3.4: no resignation monotone rule satisfies JR** — the weakest proportionality axiom in the literature. Perfect representation goes the same way (Proposition 3.5): on `v1:{c1,c3} v2:{c1,c4} v3:{c2,c3} v4:{c2,c4}` both `{c1,c2}` and `{c3,c4}` are perfectly representative, and once `c1` resigns only `{c3,c4}` is.

**So the trade is not "some rules are careless".** Representation is *why* a rule fails: it is the property that makes a winner's seat depend on who else is seated, which is exactly the dependency resignation monotonicity forbids.

## The question this repo asked next: the score rules

The paper covers approval-based rules. This engine's proportional rules take **score** ballots — [Allocated Score](../../03_STAR_PR/README.md) (the STAR-PR rule [BetterVoting](https://bettervoting.com/) runs), Sequentially Spent Score, and Reweighted Range Voting. They are not in the paper, and the question is well-posed: an approval ballot is a score ballot that only uses 0 and 5, so the paper's whole domain sits inside theirs.

**All three fail.** Each has a witness found by exhaustive search over every approval profile of its size, and in each one the rule has **exactly one reachable committee before and after**, so no tie-breaking is doing the work.

### Allocated Score — the lone voter loses her seat

Two seats. Four of the five voters are one bloc: all of them back Bruno, and they split evenly on a second name. The fifth voter backs Ana and nobody else.

<!-- ballots:resign_star_pr_seated_c4_b5 -->
*(No ballot art for `resign_star_pr_seated_c4_b5` — draw it with `build_style_ballot_images.py --from-yaml 04_Approval/03_Criteria/cases/resign_star_pr_seated_c4_b5.yaml`.)*

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Ana,Bruno,Cleo,Dev
5,0,0,0     # the lone voter — Ana only
0,5,5,0     # bloc voter, Cleo wing
0,5,5,0     # bloc voter, Cleo wing
0,5,0,5     # bloc voter, Dev wing
0,5,0,5     # bloc voter, Dev wing
```
<!-- /ballots -->

Allocated Score does what proportional representation is *supposed* to do: one seat to the four-voter bloc (Bruno), one to the lone voter (Ana).

<!-- report:resign_star_pr_seated_c4_b5 -->
```text
--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 5 ballots to fill 2 seats.
Count × Ana,Bruno,Cleo,Dev
    2 ×   0,    5,   5,  0
    2 ×   0,    5,   0,  5
    1 ×   5,    0,   0,  0

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Bruno         -- 20 -- First place
   Cleo          -- 10
   Dev           -- 10
   Ana           --  5
 Bruno wins a seat.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 2+1/2 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 4 ballots at score 5.
 This allocation overfills the quota.  Returning fractional surplus.
 Allocating only 62.50% of these ballots.
 Keeping these ballots, but multiplying their weights by 3/8.
 4 ballots reweighted from 1 to 3/8.

[Allocated Score Voting: Round 2]
 The highest-scoring candidate wins a seat.
   Ana           -- 5     -- First place
   Cleo          -- 3+3/4
   Dev           -- 3+3/4
 Ana wins a seat.

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Ana
 Bruno
```
<!-- /report -->

Bruno resigns. Nobody re-marks a ballot; Ana's supporter never mentioned Bruno at all:

<!-- report:resign_star_pr_after_bruno_c3_b5 -->
```text
[Divergence from STAR]
  STAR    = Cleo
  RCV-IRV = Dev   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/resign_star_pr_after_bruno_c3_b5_RCV-IRV_tabulated.txt

--- Allocated Score Voting Method (2 winners) ---

[Allocated Score Voting]
 Tabulating 5 ballots to fill 2 seats.
Count × Ana,Cleo,Dev
    2 ×   0,   5,  0
    2 ×   0,   0,  5
    1 ×   5,   0,  0

[Allocated Score Voting: Round 1]
 The highest-scoring candidate wins a seat.
   Cleo          -- 10 -- Tied for first place
   Dev           -- 10 -- Tied for first place
   Ana           --  5
 There's a two-way tie for first.

*** No official tie-breaking lot numbers were provided.
    Ties are resolved using a fallback order: CSV column order.
    Lot-number priority order: ['Ana', 'Cleo', 'Dev']

[Tiebreaker: Lot Number Priority]
  Tie among: ['Cleo', 'Dev']
  Resolved: ['Cleo'] (selected by lot-number priority).

[Lot-decided tie — rare]
  ⚠ The ballots did not break this tie: Allocated Score Voting has one
    deterministic rung per seat — the round's weighted score total —
    and the tied candidates came back equal on it, so the pre-published
    LOT order chose among them — the result here was set by lot, not by
    the votes. No head-to-head or five-star rung runs on this path: a
    tie on the weighted total goes straight to the lot. Verify the tied
    candidates' totals in the round above.

[Allocated Score Voting: Round 1: Ballot allocation round]
 Allocating 2+1/2 ballots.

[Allocated Score Voting: Round 1: Ballot allocation round: Round 1]
 Allocating 2 ballots at score 5.

[Allocated Score Voting: Round 2]
 Tabulating 3 remaining ballots.
Count × Ana,Cleo,Dev
    2 ×   0,   5,  0
    2 ×   0,   0,  5
    1 ×   5,   0,  0

[Allocated Score Voting: Winners — Allocated Score Voting Method (2 winners)]
 Cleo
 Dev
```
<!-- /report -->

**Cleo and Dev — both wings of the bloc that just lost its own winner — take both seats, and Ana is out.**

The mechanism is visible in the two counts and worth stating plainly, because it is the same mechanism as Example 3.3. Bruno was *absorbing* the bloc's voting power: electing him spent their four ballots down to a remainder of ⅜ each, which left Cleo and Dev at 3¾ against Ana's untouched 5. Take Bruno away and that power was never spent, so the bloc buys both seats outright. **The thing that protected Ana's seat was the presence of a candidate she did not vote for.**

Sequentially Spent Score fails on the identical profile, for the identical reason.

### Reweighted Range Voting — a one-supporter winner evicted

Three seats, five voters. Fern and Gus each have a single supporter; Hana, Ivan and Juno share three overlapping ones.

<!-- ballots:resign_rrv_seated_c5_b5 -->
*(No ballot art for `resign_rrv_seated_c5_b5` — draw it with `build_style_ballot_images.py --from-yaml 04_Approval/03_Criteria/cases/resign_rrv_seated_c5_b5.yaml`.)*

Row 1 = candidate names; each later row is one voter's 0–5 scores (a `N ×` prefix = N identical ballots).

```text
Fern,Gus,Hana,Ivan,Juno
5,0,0,0,0     # Fern only
0,5,0,0,0     # Gus only
0,0,5,5,0     # Hana + Ivan
0,0,5,0,5     # Hana + Juno
5,0,5,5,5     # Fern + the whole Hana/Ivan/Juno slate
```
<!-- /ballots -->

RRV elects **Fern, Gus and Hana**. Hana resigns, and it elects **Fern, Ivan and Juno** — Gus is evicted, and the vacated seat goes to the slate that lost its own winner. RRV also fails on the paper's own Example 3.3, where it agrees with PAV on the committee and then loses all four survivors.

**RRV's failure is really the paper's theorem in disguise, and the other two are not.** On 0/1 ballots RRV *is* sequential PAV ([why](../01_Learn/Multiwinner_Approval/thiele_methods.md)), so Theorem 3.1 already covers it and the witness above is a re-derivation rather than news. Allocated Score and Sequentially Spent Score are a different animal — they follow the **quota / STV** lineage, spending ballots down as seats are filled, and are not Thiele methods at all. Nothing in the paper reaches them, which is why they needed their own witness.

| rule | resignation monotone? | witness |
|---|:--:|---|
| **Approval (AV / bloc)** | ✓ *(theorem)* | — Theorem 3.1 |
| **Allocated Score (STAR-PR)** | ✗ | [`resign_star_pr_seated_c4_b5.yaml`](cases/resign_star_pr_seated_c4_b5.yaml) → [`resign_star_pr_after_bruno_c3_b5.yaml`](cases/resign_star_pr_after_bruno_c3_b5.yaml) |
| **Sequentially Spent Score** | ✗ | the same profile |
| **Reweighted Range Voting** | ✗ | [`resign_rrv_seated_c5_b5.yaml`](cases/resign_rrv_seated_c5_b5.yaml) → [`resign_rrv_after_hana_c4_b5.yaml`](cases/resign_rrv_after_hana_c4_b5.yaml) |
| **Bloc STAR** | no violation found | exhaustive over 4 candidates, ≤6 voters — **evidence, not a theorem** |

## The tie-breaking trap, which is the reason this page exists at all

The score rules are **sequential**, so a tie inside the count is settled by a tie-breaking order, and running one of them *once* is not enough to establish anything.

On the paper's own Example 3.2, all three score rules look like they fail under this engine's default tie-break — and all three are perfectly well-behaved once the alternatives are enumerated, because after `c1` resigns the three remaining candidates are tied at 10 apiece and `{c2,c3}` and `{c2,c4}` are both reachable. A first pass at this page recorded three violations there. There are none.

So every verdict above is taken over **all** tie-breaking orders (every permutation of the candidates, via starvote's `predefined_permutation_tiebreaker`), and a violation is reported only when the survivors appear in **no** reachable committee. That distinction matters beyond this page: a resolute engine answering a question about an irresolute axiom will manufacture failures.

## What is established here, and what is not

- **Every ✗ is DEMONSTRATED.** Run the witness, watch a seated winner get evicted. Proof by counterexample, and complete.
- **AV's ✓ is CITED**, to Theorem 3.1 — not demonstrated, because "no profile anywhere violates this" is a universal claim no finite replay settles.
- **Bloc STAR's row is neither.** It is an exhaustive sweep of every 4-candidate profile up to 6 voters (94,872 of them, 1,591 flagged by the default tie-break, none surviving the full sweep) plus a random search at larger sizes. That is real evidence and it is not a proof; if you want one, it needs an argument about why Bloc STAR's score does not depend on the rest of the committee.
- **The three ✗ score rows are this repo's finding, not the paper's.** Oh & Peters do not discuss score rules. If the result matters to you, the witnesses are four runnable files and one script.

## Reproduce it

```bash
.venv/bin/python 06_Other/abcvoting_tabulation_engine/resignation_check.py --verbose
```

That replays the paper's three witnesses through [`abcvoting`](https://github.com/martinlackner/abcvoting) and the four score witnesses through `starvote`, and exits non-zero if any stops reproducing. `--search N` hunts for fresh violations on random profiles; `--sweep-bloc` runs the exhaustive Bloc STAR sweep. Gated by [`tests/test_resignation_monotonicity.py`](../../STARVote_LH_tabulation_engine/tests/test_resignation_monotonicity.py), which also checks that each "after" case file really is its "before" file minus one column.

The Approval control is runnable too — [`resign_av_holds_c7_b5.yaml`](cases/resign_av_holds_c7_b5.yaml) and [`resign_av_holds_after_kai_c6_b5.yaml`](cases/resign_av_holds_after_kai_c6_b5.yaml) are the paper's Example 3.3 counted by plain multi-winner Approval, which keeps all four survivors where PAV, seq-Phragmén and Equal Shares cannot.

## What the paper does about it

Two escapes, both worth knowing before anyone proposes one here:

- **Fractional committees.** If seats can be split, rules based on maximum flow in the election's payment network satisfy both resignation monotonicity and a proportionality axiom (GRP). Real boards do not have fractional members, so this is a theoretical route rather than a proposal.
- **The Maximum Payment Rule (MPR).** An integral rule satisfying a *relaxed* form — after a resignation there is **some** way to refill the seats that guarantees PJR+. It is NP-hard in general, tractable in structured domains, and on party-list instances it reduces to the largest remainder method. Neither this engine nor BetterVoting implements it.

The paper's last section is a different worry with the same shape: a **losing** candidate recruiting weak extra candidates to change the result. Resignation monotone rules that are independent of losers are immune, as are many sequential rules — but PAV can be manipulated this way. That is the same complaint as this repo's [spoiler](../../07_Concepts/topics/spoiler_effect.md) pages, one committee up.

---

**Related:** [the criteria table](README.md) · [committee monotonicity](committee_monotonicity.md) — a seat is added instead · [support monotonicity](support_monotonicity.md) — a ballot changes instead · [proportionality for solid coalitions](../../03_STAR_PR/03_Criteria/solid_coalitions/README.md) — the other place Allocated Score's quota-spending bites · [the ABC rules themselves](../01_Learn/Multiwinner_Approval/README.md).
