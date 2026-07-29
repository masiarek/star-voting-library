# Exercise 15 — Read the ballot, name the method

*Every other exercise in this set hands you the method and asks who wins. This one runs backwards. You get two filled-in profiles and no method name — just the marks. Name the method from the shape of the ballot, then count. Then the part the textbooks stop before: one of these two profiles has a property that guarantees its winner is also the **[Condorcet winner](../../00_start_here/topics/condorcet/)**, and the other has a winner so uncontested that no method in the library disagrees. Work out which is which, and why.*

**▶ Live on BetterVoting:** profile (a) — [vote](https://bettervoting.com/d4v2dh) · **[results ↗](https://bettervoting.com/d4v2dh/results)** (election `d4v2dh`, Test ID BV2258 — two races on the same 35 ballots: the Yes/No count, then the identical marks as 5/0 scores so the head-to-head view prints). Profile (b) — [vote](https://bettervoting.com/tfm64p) · **[results ↗](https://bettervoting.com/tfm64p/results)** (election `tfm64p`, Test ID BV2259). **BetterVoting's own count agrees with the engine on all three races** — Blair, Blair, Clara. Two elections rather than one because the profiles have different electorates (35 voters and 4), and every BV voter votes every race.

**You practice:** reading a ballot as evidence — what a set of marks can and cannot record — plus the vocabulary that names each shape: **dichotomous** vs **cardinal**, approval shares vs vote shares, and the guarantee that comes free on a [dichotomous profile](../../00_start_here/GLOSSARY.md#the-wider-field-computational-social-choice).

Work each part on paper before opening its solution. All three YAMLs are runnable and their answer keys are regression-tested.

---

## Profile (a) — 35 voters

The column headings are how many voters cast that ballot.

| | ×15 | ×8 | ×7 | ×5 |
|---|:---:|:---:|:---:|:---:|
| **Ada** | No | Yes | Yes | No |
| **Blair** | Yes | Yes | No | Yes |
| **Cosmo** | Yes | No | Yes | No |

## Profile (b) — 4 voters

| | Voter 1 | Voter 2 | Voter 3 | Voter 4 |
|---|:---:|:---:|:---:|:---:|
| **Alice** | 0 | 3 | 0 | 4 |
| **Bruno** | 2 | 5 | 1 | 3 |
| **Clara** | 5 | 5 | 5 | 4 |
| **Diego** | 4 | 3 | 4 | 2 |

## Your task

- **(a)** Which voting method produced profile (a)? Name **two** features of the ballot that rule out the alternatives.
- **(b)** Who wins profile (a), and with what share of the ballots? The three shares add up to far more than 100% — is something wrong?
- **(c)** Which method produced profile (b), and why is it called a **cardinal** method? (One sentence, and it should not be "because it uses numbers.")
- **(d)** Who wins profile (b)? Then the follow-up the prompt doesn't ask: can you tell from that table who each voter's **favorite** is?
- **(e)** Back to profile (a). Rank the three candidates by head-to-head wins — who beats whom. Compare that ranking to the approval totals from (b). Coincidence?
- **(f)** Does (e) mean Approval always elects the Condorcet winner? Answer carefully.

## Solutions

<details>
<summary><b>(a) Approval voting — and here's how the ballot tells you</b></summary>

**Approval voting.** Two features settle it:

1. **Each candidate is marked independently, with only two states.** No ranks (nothing says which Yes is better than another Yes), no magnitudes. That rules out every ranked method — [RCV-IRV](../../00_start_here/RCV_IRV/), [Ranked Robin](../../05_Ranked_Robin/concepts/ranked_robin.md), Borda — and every score method.
2. **Voters mark different *numbers* of candidates.** The ×15 bloc approves two, the ×5 bloc approves one. That rules out [Choose-One](../../00_start_here/topics/plurality.md) (exactly one mark) and k-approval (exactly k marks).

Independent, binary, unlimited marks — that is the definition of an approval ballot. The theorists' name for a profile of them is a **[dichotomous profile](../../00_start_here/GLOSSARY.md#the-wider-field-computational-social-choice)**: every voter's ballot is a ranking with exactly two levels and nothing said inside either one.

</details>

<details>
<summary><b>(b) Blair, 28 of 35 — and no, nothing is wrong with the percentages</b></summary>

Count the Yeses: Blair 15 + 8 + 5 = **28**, Cosmo 15 + 7 = **22**, Ada 8 + 7 = **15**.

```text
--- Approval Voting (single winner) ---
 Tabulating 35 ballots (any non-zero score = approval).

   Blair -- 28 (80%) -- Elected
   Cosmo -- 22 (63%)
   Ada   -- 15 (43%)

[Approval Distribution] (how many candidates each ballot approved)
   65 approvals across 35 ballots — average 1.9 of 3 (range 1–2).
     approved 1: 5 ballots
     approved 2: 30 ballots
```

80 + 63 + 43 = 186%, and that is exactly right. **An approval percentage is a share of *ballots*, not a slice of one pie** — "80% of voters approve Blair" and "63% approve Cosmo" are both true of the same 35 people, because a voter can say yes to both. Reading approval shares as vote shares is the single most common mistake with these results. The **approval distribution** line is what tells you how much doubling-up there was: 65 approvals across 35 ballots, so the average voter approved 1.9 of the 3.

Full report: [`ex15_approval_yes_no`](cases/cases_pages/ex15_approval_yes_no.md).

</details>

<details>
<summary><b>(c) Score (Range) voting — cardinal because each rating stands alone</b></summary>

**Score voting**, also called Range: rate every candidate on a fixed scale, add the columns, highest total wins.

It's **cardinal** because each candidate is judged **against the scale, not against the other candidates** — the ballot records *how much* a voter likes each one, independently, so it can say "these two are exactly equal" and "this one is far better than that one." An ordinal ballot can only say *which comes first*; it has no way to distinguish a hair's-breadth preference from a chasm. (Voter 2 rating Bruno and Clara both 5 is a statement no ranking can make.) → [scores vs ranks](../../00_start_here/scores_and_ranks/scores_vs_ranks.md) · [scoring methods vs ranked voting](../../00_start_here/topics/scoring-methods-vs-ranked-voting.md)

The giveaway that it isn't [STAR](../../00_start_here/STAR_Voting/STAR_start_here.md), by the way, is that nothing in the prompt mentions a runoff — the ballots are identical. **A ballot alone never fully identifies the method**; Score and STAR share this one, which is the whole point of [exercise 3](ex03_five_verdicts.md).

</details>

<details>
<summary><b>(d) Clara, 19 — and no, you cannot always read off a favorite</b></summary>

Column sums: Clara 5+5+5+4 = **19**, Diego 4+3+4+2 = **13**, Bruno 2+5+1+3 = **11**, Alice 0+3+0+4 = **7**.

```text
Scoring Round
   Clara         -- 19 -- First place
   Diego         -- 13 -- Second place
   Bruno         -- 11
   Alice         --  7
```

That scoring round **is** the Score-voting count — the file runs as STAR because the teaching CLI has no first-class `voting_method: Score`, and the totals it prints are the Score result. Here the runoff changes nothing:

```text
Automatic Runoff Round
   Clara         -- 4 -- First place
   Diego         -- 0
   Equal Support -- 0
```

Clara wins **4–0**, and she's the Condorcet winner too. The engine prints **no `[Divergence from STAR]` block at all** — Choose-One, RCV-IRV, Approval and Score all land on Clara. She is scored top or joint-top by every single voter, so there is nothing for the methods to disagree about. Worth keeping one of these around: [most curated elections in this library diverge](../../method_comparisons/divergence_review/INDEX.md), and it would be dishonest to only ever show those.

**Can you tell each voter's favorite?** Only for two of them. Voter 1 and voter 3 give Clara a clear 5. But voter 2 rates Bruno and Clara both 5, and voter 4 rates Alice and Clara both 4 — **tied at the top, with no tiebreaker on the ballot.** So you cannot reconstruct a Choose-One tally from these ballots without inventing information the voters didn't give you. (On profile (a) it's worse: an approval ballot has no top at all.) That asymmetry — score ballots can be read down to cruder ones, but never perfectly — is the [fidelity ladder](../../00_start_here/scores_and_ranks/fidelity_ladder.md).

Full report: [`ex15_score_profile`](cases/cases_pages/ex15_score_profile.md).

</details>

<details>
<summary><b>(e) Blair > Cosmo > Ada — the same order as the approval totals, and it is not a coincidence</b></summary>

Read the same 35 ballots pairwise ([`ex15_approval_pairwise`](cases/cases_pages/ex15_approval_pairwise.md) writes each approval as a 5 and each non-approval as a 0, which changes no head-to-head count — only the two-class order matters):

```text
--- Runoff (Preference) Matrix ---
Legend: For - Equal Support - Against
                 |      Ada     |  * Blair    |  * Cosmo    |
-------------------------------------------------------------
           Ada > |     ---      | 7 -  8 - 20 | 8 - 12 - 15 |
       * Blair > | 20 -  8 -  7 |    ---      |13 - 15 -  7 |
       * Cosmo > | 15 - 12 -  8 | 7 - 15 - 13 |    ---      |

[Condorcet Winner]
  Condorcet Winner: Blair — matches the STAR winner
```

Blair beats Ada 20–7 and Cosmo 13–7; Cosmo beats Ada 15–8. **Blair > Cosmo > Ada — exactly the order of the approval totals 28 > 22 > 15.**

Not luck. On a dichotomous profile, "more voters strictly prefer x to y" reduces to **"more voters approve x than approve y"** — so the head-to-head order *is* the approval order, a Condorcet winner is guaranteed to exist, and no cycle is possible. (Approval also coincides with [Borda](../../06_Other/other_ranked_methods/borda.md) on this domain, which is why the result is sometimes stated as *approval voting reconciles Borda and Condorcet*.)

Notice where the preferences went, though: Blair vs Cosmo is 13–7 with **15 Equal Support** — the ×15 bloc approved both and has no say in that matchup. That column is the compression, and it's the hinge of (f).

</details>

<details>
<summary><b>(f) No — and the gap is worth being precise about</b></summary>

What's true is: **Approval elects the Condorcet winner of the approval ballots.** Always, guaranteed, as (e) shows.

What does *not* follow: that it elects the Condorcet winner of what the voters actually think. Real approval ballots aren't cast by a dichotomous electorate — they're cast by people with richer opinions who compress them on the spot, and the compression can move the answer. The worked counterexample is five ballots long: in [Black Curtain #1](../../method_comparisons/black_curtain/condorcet_compression.md), Cal is the engine-confirmed Condorcet winner of the score ballots, Bob is the Condorcet winner of the same voters' approval ballots, and Bob wins — legitimately, because the three voters who prefer Cal approved both of them.

So the honest phrasing of the guarantee names its domain: *on a dichotomous profile*, Approval is Condorcet-consistent. Drop those four words and you've promised something the method can't deliver. → [Approval in the theory literature](../../04_Approval/concepts/approval_in_the_literature.md) · [Approval's honest limits](../../04_Approval/concepts/approval_honest_limits.md)

</details>

## The moral

Two profiles, two lessons about what marks can carry. A **Yes/No** ballot buys a guarantee — its winner beats everyone head-to-head, always — by throwing away every preference *inside* each group; the guarantee is real and it is about the ballots, not the voters. A **0–5** ballot keeps the intensity and the order, which is why it can be read down into an approval count, a ranking, or a runoff — and why the same marks support several different methods, so the ballot alone never names one.

## Run them

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 01_STAR/exercises/cases/ex15_approval_yes_no.yaml
```

| Case | Method | Winner | Shows |
|---|---|---|---|
| [`ex15_approval_yes_no`](cases/cases_pages/ex15_approval_yes_no.md) | Approval | **Blair** | The count, the shares, the approval distribution |
| [`ex15_approval_pairwise`](cases/cases_pages/ex15_approval_pairwise.md) | STAR (5/0) | **Blair** | The same ballots pairwise — approval order = Condorcet order |
| [`ex15_score_profile`](cases/cases_pages/ex15_score_profile.md) | STAR | **Clara** | The scoring round as the Score count; every method agrees |

## See also

- [Exercise 3 — one electorate, five verdicts](ex03_five_verdicts.md) — the same ballot, five methods, five answers
- [Exercise 13 — where do you draw the line?](ex13_draw_the_line.md) — the other half of the approval story: one honest electorate, three thresholds, three winners
- [Approval Voting](../../04_Approval/concepts/approval_voting.md) · [Approval in the theory literature](../../04_Approval/concepts/approval_in_the_literature.md)
- [Scores vs ranks](../../00_start_here/scores_and_ranks/scores_vs_ranks.md) · [the fidelity ladder](../../00_start_here/scores_and_ranks/fidelity_ladder.md)
- [When compression moves the Condorcet winner](../../method_comparisons/black_curtain/condorcet_compression.md) — part (f), worked in full

# file: ex15_read_the_ballot.md
