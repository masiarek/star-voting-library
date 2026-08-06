# "Single-elimination RCV," claim-checked — the method already has a name, and a record

**Level: 301 · for debaters**

**One line:** a conservative policy paper proposes a streamlined RCV in which voters rank two candidates and the count jumps straight to the top two — a model it presents as new, which is in fact the **Supplementary Vote** used for the Mayor of London until 2022; and on the paper's *own* five-candidate example the streamlining makes worse the exact flaw the paper concedes.

The paper: Adam Kissel, [*Can Ranked-Choice Voting Work? A Conservative Approach*](https://cardinalinstitute.com/publication/ranked-choice-voting-a-conservative-approach/) (Cardinal Institute for West Virginia Policy; the landing page titles it *Ranked-Choice Voting: A Conservative Approach*). What the method is: [RCV-IRV (Contingent & Supplementary Vote)](../../06_Other/RCV_IRV/concepts/variants/RCV-IRV-contingent-supplementary.md) · [Which RCV-IRV?](../../06_Other/RCV_IRV/concepts/variants/RCV_IRV_variants.md). Companions: [center squeeze](../../07_Concepts/topics/center_squeeze/README.md) · [exhausted ballots](../../06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md) · [summability](../../07_Concepts/topics/summability/README.md) · [false majorities](../../07_Concepts/topics/false_majorities.md).

---

## What the paper proposes

> 1. Rank your top two candidates. 2. If somebody has a majority, he wins. 3. If there is no majority, there is an instant runoff among the top two candidates. All the others are eliminated. 4. If a voter's candidate was eliminated, but she recorded one of the top two as her second choice, that second-choice vote now counts instead. 5. In this runoff, whichever candidate has more votes wins.

The paper calls this "single-elimination ranked-choice voting" and writes, "I call this model…" — presenting it as a new design. It is not new. Batch-eliminating everyone below the top two is the **Contingent Vote**; doing it with a ballot capped at two marks is the **Supplementary Vote**. Both are documented in this repo already: [RCV-IRV (Contingent & Supplementary Vote)](../../06_Other/RCV_IRV/concepts/variants/RCV-IRV-contingent-supplementary.md).

That is the single most useful correction in this claim-check, because it converts a thought experiment into an evidence question. The Supplementary Vote elected the **Mayor of London**, England's other directly-elected mayors, and Police & Crime Commissioners from 2000 until the [Elections Act 2022](https://www.legislation.gov.uk/ukpga/2022/37/part/1/crossheading/voting-system-for-elections-for-certain-offices/enacted) replaced it with first-past-the-post. The Contingent Vote (three marks) elects the President of Sri Lanka. A West Virginia legislator asking "has anyone tried this?" has two decades of answers.

## The claims, checked

| # | Claim | Verdict |
|--:|---|---|
| 1 | The model is a new proposal ("I call this model…") | ❌ **It's the Supplementary Vote** — 20+ years of use, repealed in England in 2022 |
| 2 | Eliminating a candidate who'd win a fuller count "seems quite rare" | ⚠️ **Unevidenced, and the direction is wrong** — the model *guarantees* the winner is a top-two first-choice finisher |
| 3 | Denying voters their second choice is "essentially the same in all forms of RCV" | ❌ **False** — true of elimination counts, not of [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) |  <!-- terminology-ok: verbatim quotation of the paper / the canon statement itself -->
| 4 | Fixing it needs "an even more complicated point system… at the expense of additional voter confusion" | ⚠️ **The fix is STAR, and it's one grid** — the ballot simplicity the paper asks for on p.13 |
| 5 | It is "much more likely to overcome the exhausted-ballot flaw than traditional RCV" | ❌ **Backwards** — 16% exhausted vs 0% on identical ballots, below |  <!-- terminology-ok: verbatim quotation of the paper / the canon statement itself -->
| 6 | The winner "wins regardless of whether he holds a majority of all votes" | ✅ **Correct, and the most honest paragraph in the paper** |
| 7 | Transparency and precinct-checkable, election-night results should govern the choice | ✅ **Right priority — and it argues past the paper's own proposal** |
| 8 | RCV lets voters "vote their conscience" and reveals true preferences | ⚠️ **Weaker under this model than under the full IRV it streamlines** |

---

## Claim 2 — "quite rare," and pointed the wrong way

The paper concedes that "single elimination RCV might eliminate a candidate who would win in a more complex RCV model," then sets the concern aside: "This event, however, seems quite rare." No evidence is offered, and the structural fact runs the other way.  <!-- terminology-ok: verbatim quotation of the paper / the canon statement itself -->

**The Contingent Vote's winner is always one of the top two on first choices. Full IRV's need not be.** That is not a tendency, it is the definition: step 3 eliminates everyone else before a single ballot transfers. Any candidate who would have climbed from third on transfers is mathematically ineligible under the paper's model.

Here is that difference on 100 ballots — an ordinary four-way mayor's race, no cycle, no ties ([full count](cases/cases_pages/mayor_c4_b100_streamlined_irv.md)):

```text
 33 × Ada   > Cora > Blake > Dean      Round 1:  Ada 33 · Blake 31 · Cora 20 · Dean 16
 31 × Blake > Cora > Ada   > Dean
 20 × Cora  > Blake > Ada  > Dean      Cora is every other bloc's SECOND choice.
 16 × Dean  > Cora > Blake > Ada
```

| Count | Winner | |
|---|---|---|
| Choose-One (plurality) | **Ada** | 33 of 100 |
| **Contingent Vote** (the paper's model) | **Blake** | Cora is cut in step one; Cora's and Dean's ballots go to Blake, 67–33 |
| **Supplementary Vote** (2-mark ballot) | **Blake** | 51–33, with **16 ballots exhausted** |
| RCV-IRV, full rounds | **Cora** | Dean out → Cora 36; Blake out → Cora 67 |
| [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) | **Cora** | 3–0: beats Ada 67–33, Blake 69–31, Dean 84–16 |
| **STAR** | **Cora** | leads scoring 356–280, wins the runoff 69–31 |

Cora is the **Condorcet winner** — she beats every rival head-to-head. Full IRV finds her from third place. The streamlined model cannot, ever. The paper's proposal is offered as a safer, simpler RCV; on its own stated criterion it is the version that loses the winner.

<details><summary><strong>The count, as the tool prints it</strong> — <code>contingent_vote_report.py</code></summary>

```text title="Abridged for the lesson — the runoff and comparison blocks only"
No majority (33 of 100, majority needs more than 50).
   Top two advance: Ada and Blake. Cora, Dean eliminated — all at once, in one step.

Instant runoff — every ballot to whichever finalist it ranks higher:
   Blake            67   ( 67.0% of ballots still counting,  67.0% of ballots cast)
   Ada              33   ( 33.0% of ballots still counting,  33.0% of ballots cast)
   exhausted         0   (ranked neither finalist —   0.0% of ballots cast)

Winner — Contingent Vote: Blake

Same ballots, other counts (all computed independently by pref_voting):
   Plurality (choose-one)        : Ada
   Contingent Vote               : Blake
   RCV-IRV (Hare, full rounds)   : Cora
   Ranked Robin (Copeland)       : Cora

   Condorcet winner (beats every rival head-to-head): Cora
   Contingent Vote ✗ does NOT elect it.
   (For contrast, full Hare IRV on these same ballots finds it: Cora.)
   Note: the ballots DO contain the answer — Cora wins every pairing on this
   very same data. This count just never asks.

 pref_voting plurality_with_runoff_put: Blake
 cross-check vs our contingent winner (Blake): AGREE ✓  (unique winner)
```
</details>

**Being fair about what this shows.** This profile was built to show the failure, and one constructed example does not establish a rate. This repo states rarity when it cuts against its own preferences — across [182 US RCV elections (2004–2022), exactly two](../alaska_2022/alaska_301.md) had a Condorcet failure — and the same discipline applies here: nobody in this repo has measured how often the Contingent Vote diverges from full IRV in real elections, and neither has the paper. What the example does establish is the *mechanism*, and the mechanism is not rare-by-construction: it fires whenever a broadly-acceptable candidate runs third, which is the ordinary shape of a race with a moderate in it.

## Claim 3 — "essentially the same in all forms of RCV" is the load-bearing error

The paper writes:

> This flaw—denying some voters the opportunity to have their second choices counted while giving that opportunity to others—is essentially the same in all forms of RCV.

The observation is correct and well-made about **elimination** counts, and the paper deserves credit for stating plainly what most RCV advocacy elides: in a polarized race with a compromise candidate C, "RCV would never count the second-choice votes of the A and B voters to reveal the relative popularity of C."

But "all forms of RCV" is false, and this is the repo's central terminology point: **RCV names a *ballot* (ranked); IRV names one *tabulation* of it** ([terminology canon](../../07_Concepts/tips/TIPS_terminology.md)). [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) — Condorcet/Copeland, on the identical ranked ballot — reads every ballot in every pairing. No voter's second choice is discarded, because nothing is ever eliminated.  <!-- terminology-ok: verbatim quotation of the paper / the canon statement itself -->

The proof is the same ballots counted twice. Run the paper's *own* five-candidate example ([p.5](#the-papers-own-example-run)) under Ranked Robin and C wins 4–0 ([full count](cases/cases_pages/kissel_five_way_c5_b1000_rr.md)):

```text title="Abridged for the lesson — the win–loss record only"
Win–loss record — Copeland score = wins + ½·ties:
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  C          4–0–0         4   +2020  A, B, D, E
    2  A          3–1–0         3   +1194  B, D, E
    3  B          2–2–0         2    +368  D, E
    4  D          1–3–0         1    +346  E
    5  E          0–4–0         0   -3928  —

Winner — Ranked Robin (RCV-RR): C
   beats every opponent head-to-head — the Condorcet winner.
```

Nothing about the ballots changed. Only the count did. If the paper's objection is that some voters' second choices go uncounted — and it is a good objection — then the remedy is a count that reads them, not a count that reads even fewer of them.

## The paper's own example, run

The paper prints a five-way field to argue that C's chances are hopeless anyway:

> A >30% · B 30% · C 20% · D <19% · E <1%
>
> …in such scenarios, the only way for C to win is if a large majority of the D voters choose C with too few choosing A or B to keep one of them ahead. This is unlikely.

Given ballots that match those percentages and a C who is the moderate second choice of both poles, that diagnosis is wrong. C's problem is not D's transfers. C **is** the majority-preferred candidate — beating A 511–489 and B 700–300 — and *every* elimination count misses it ([the cases](#the-cases)):

| Count | Winner | |
|---|---|---|
| Choose-One (plurality) | **A** | 306 of 1000 |
| **Contingent Vote** | **A** | 609–391 |
| **Supplementary Vote** (2-mark ballot) | **A** | 600–391, 9 exhausted |
| RCV-IRV, full rounds | **A** | E out, D out, then **C out** — A wins 609–391 |
| Ranked Robin | **C** | 4–0 |
| **STAR** | **C** | scoring 3221 to A's 2695; runoff **511–489** |

<!-- report:kissel_five_way_c5_b1000_star -->
```text
[Divergence from STAR]
  STAR                   = C
  Choose-One (Plurality) = A   (differs from STAR)
  RCV-IRV                = A   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
  Full round-by-round reports (generated for review):
  RCV-IRV rounds: cases_tabulated/kissel_five_way_c5_b1000_star_RCV-IRV_tabulated.txt

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 1000 ballots.
Count × A,B,C,D,E
  306 × 5,0,3,1,0
  300 × 0,5,3,1,0
  183 × 4,0,2,5,0
  111 × 3,1,5,0,0
   91 × 1,3,5,0,0
    9 × 1,0,3,4,5

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   C             -- 3221 -- First place
   A             -- 2695 -- Second place
   B             -- 1884
   D             -- 1557
   E             --   45
 C and A advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   C             -- 511 -- First place
   A             -- 489
   Equal Support --   0
 C wins.
   Runoff math:
     1000  ballots cast
   −    0  Equal Support (no preference between the two finalists)
     ────
     1000  voters with a preference  (majority = 501)
           C 511 (51%)  ·  A 489 (49%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 C
```
<!-- /report -->

This is the one place the paper's letters are kept instead of a named cast: the point is that these are *the paper's own numbers*, and a reader should be able to hold the two side by side.

## Claim 4 — the fix is one grid, not a complication

Having identified the flaw, the paper gestures at a remedy and waves it off:

> (An even more complicated point system, in which voters give their first choice most of the available points and other choices the remaining points, could reduce this flaw—at the expense of additional voter confusion.)

Two things. First, what's described — a fixed budget of points to distribute — is closer to **cumulative voting**, and budgeting *is* the confusing part. **STAR** doesn't budget: score each candidate 0–5 independently, the way you'd rate five restaurants. Nothing is divided up, nothing is ranked, and giving your favorite a 5 costs you nothing anywhere else.

Second, the paper asks for exactly STAR's ballot without noticing. On p.13 it argues that the two-column layout is a reason to prefer its model:

> Paper ballots similarly should show one grid for the first choice and a separate one for the second choice… In contrast, paper ballots under traditional RCV must use either a large, confusing grid or a large number of separate grids.

The STAR ballot is **one grid** — candidates down, 0–5 across, one mark per row, no rank ordering to get wrong and no way to overvote. And on both elections above it elects the candidate the paper says gets denied. The paper's ballot-design instinct and its method conclusion point in different directions.

## Claim 5 — the exhausted-ballot claim is backwards

> Nevertheless, in many cases, single-elimination RCV will push one of the top two candidates over the 50 percent threshold; single-elimination RCV is therefore much more likely to overcome the exhausted-ballot flaw than traditional RCV.  <!-- terminology-ok: verbatim quotation of the paper / the canon statement itself -->

Capping the ballot at two marks is what *causes* exhaustion; it cannot cure it. And batch elimination exhausts more than sequential elimination, because a ballot gets fewer chances to land on a candidate still standing. The mayor's race shows both effects on identical voters:

| Same 100 voters | Ballot | Exhausted |
|---|---|--:|
| RCV-IRV, full rounds, full rankings | 4 marks | **0** |
| RCV-IRV, full rounds, **2-mark ballot** | 2 marks | **0** |
| **Supplementary Vote** (the paper's model) | 2 marks | **16** |

The middle row is the sharp one: on the paper's *own* two-mark ballot, running ordinary IRV rounds instead of the batch jump exhausts nothing and elects the Condorcet winner. The exhaustion is not coming from the ballot. It is coming from the count.

The paper half-concedes this a page later — "it is easy to imagine most voters not choosing A or B as a second choice, with the C–H voters splitting their second choices evenly" — in the eight-candidate field on p.12 (A 15% … H 10%), where the C–H blocs are 61% of the electorate and most of their ballots would exhaust. That is the right worry; it belongs in the claim above, not against "traditional RCV." Background: [exhausted ballots](../../06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md), which already notes that the Supplementary Vote "exhausts the most."  <!-- terminology-ok: verbatim quotation of the paper / the canon statement itself -->

## Claim 6 — the paper is right, and unusually honest

> This candidate wins regardless of whether he holds a majority of all votes. … To get the benefits of instant runoffs, lawmakers and policy makers should be content with the plurality winner and should not argue that an RCV model represents a "majority" when it often does not.

Correct, and worth quoting to *both* camps. The runoff denominator excludes exhausted ballots, so the headline percentage is a majority of ballots *still counting*, not of ballots cast. In the mayor's race the Supplementary Vote winner takes 51 of 100 cast — but the number a press release would print is **60.7%**, the share of the 84 ballots still live.

This repo takes the same position and builds it into the engine: `show_runoff_percent` prints a self-reconciling line that states the decided-voter denominator *and* the total, so the gap never has to be inferred. See [false majorities](../../07_Concepts/topics/false_majorities.md) and the [automatic runoff](../../01_STAR/01_Learn/the_count/STAR_Automatic_Runoff.md).

## Claim 7 — the transparency argument is the paper's best, and it argues past the proposal

The integrity program — published, annotated source code; hashes before and after the count; no internet-connected tabulators; ballot records published after certification; chain-of-custody penalties; results on or immediately after election day — is method-independent good practice, and this repo has no quarrel with any of it.

But the paper under-sells its own strongest technical point, because it never names **[summability](../../07_Concepts/topics/summability/README.md)**. A method is summable when each precinct can publish a small fixed-size table and those tables *add* to the statewide result — no ballots travel, partial results mean something, and any citizen can re-add the published numbers.

- **Full RCV-IRV is not summable.** The elimination order depends on statewide totals, so every ballot must reach a central count. That is precisely the New York City experience the paper opens with. → [IRV isn't summable](../../06_Other/RCV_IRV/concepts/RCV_IRV_lack_of_summability.md)
- **The Contingent / Supplementary Vote *is* summable**, and the paper never says so. Each precinct publishes two things: first-choice counts, and the pairwise table (how many ballots rank *i* over *j*). Add them across precincts. The first-choice column gives the top two; the single pairwise cell for that pair gives the runoff; ballots cast minus those two numbers gives the exhausted count. Nothing else is needed.

So on the paper's own top priority the streamlined model genuinely beats the one it's replacing — a real argument, left on the table.

Follow it one step further, though, and it runs past the proposal. That pairwise table is the same artifact **[Ranked Robin](../../05_Ranked_Robin/01_Learn/RCV_RR_summability.md)** and **[STAR](../../01_STAR/01_Learn/properties_and_limits/STAR_summability.md)** publish. All three are precinct-summable and election-night-fast. The difference is only what the count does with the table it already has: the Contingent Vote reads one cell of it and discards the rest.

## Claim 8 — "vote your conscience" is weaker here, not stronger

> In contrast, RCV lets people feel comfortable choosing a likely-losing candidate.

Partly true, and true of full IRV. Under the paper's model it is weaker, for the reason in Claim 2: the winner is always one of the top two on **first choices**. So a voter whose favorite is polling third has a live reason to put a likely finalist first — not to help them win, but to decide *who the finalists are*. That is the plurality calculus the paper wants to abolish, moved from the final to the semifinal. Full IRV at least lets a third-place candidate climb; the Contingent Vote forecloses it.

The same cut applies to "Voters Reveal Their True Preferences." A two-mark ballot reveals less than a full ranking — the paper's own cap trims the benefit it claims. (The paper anticipates part of this with its E-voter example, and is right that the residual gaming is milder than plurality's.) Background: [strategic voting](../../07_Concepts/topics/strategic_voting.md).

## Smaller notes

- **Voter capacity, argued both ways.** Pages 3 and 8 lean on voters "many of whom lack basic literacy" and "the low levels of literacy, numeracy, and general education among much of the electorate." Page 11 says the same objection "rings hollow" because voters manage supermarkets and online retailers. Page 11 has the better argument; the paper shouldn't spend the other one.
- **Nielson (2017) is quoted accurately**, including the "[quotation corrected]" flag on the *Wall Street Journal* passage — more care than these citations usually get. Worth noting what it measures: a survey experiment in which subjects tried RCV **once**, without seeing results. That is evidence about *unfamiliarity*, which is the same thing the paper's own one-year-runway recommendation is designed to fix.
- **Multi-winner.** "If there are to be N winners, voters just choose their top N and then a fallback candidate" is **bloc voting**, and its defining property goes unmentioned: a cohesive 51% takes *all N seats*. The paper's conclusion that plurality-at-large "is sufficient" for school boards is a defensible cost judgment, but the choice being made is majority-sweep versus proportional representation, and that should be said out loud. → [electing more than one](../../07_Concepts/topics/electing_more_than_one.md)
- **NYC 2021** was 135,000 test ballots left in the system — a Board of Elections procedural failure, caught and corrected. The paper says so fairly ("That fiasco does not, however, invalidate the benefits of RCV"), which is more than most citations of it manage.

## What the paper gets right

Worth restating, because a claim-check that only subtracts is not much use:

1. **The compromise-candidate flaw is real and correctly described** — and stated more plainly than most RCV advocacy manages.
2. **"Don't call it a majority"** is right, and both camps should adopt it.
3. **The integrity program** is method-independent and sound.
4. **Election-night, precinct-checkable results** is the right priority — and it points at summable methods.
5. **The Contingent Vote is genuinely simpler** than full IRV to hand-count, explain, and put on paper. That is a real advantage and this page does not dispute it.

Where the argument goes wrong is one substitution: it treats "fewer rounds" as if it meant "less information discarded." It is the opposite. The rounds are where a compromise candidate's support becomes visible; deleting them deletes the only chance an elimination count had of seeing it. The methods that don't discard it — [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) and [STAR](../../01_STAR/README.md) — meet every one of the paper's five criteria above, and read the whole ballot.

## The honest cut against STAR

STAR is not exempt from this page's own standard. It fails the [majority criterion](../../07_Concepts/topics/majority_criterion/README.md) in a construction where a majority's generosity to a *second* rival lifts that rival past their favorite — demonstrated on the Center for Election Science's own example in [the majority illusion, counted](../ces_majority_illusion/). It also fails [Later-No-Harm](../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md). Those are real, and a debater using this page should know them before an opponent supplies them.

## The cases

Two elections, each counted three ways. All **LH-only** — they are constructed profiles built to isolate a mechanism, and the headline method (the Contingent Vote) is not one BetterVoting offers, so a BV election would reproduce only the side legs.

| Case | The job | Winner | Source |
|---|---|---|---|
| [Kissel's five-way (RCV-IRV)](cases/cases_pages/kissel_five_way_c5_b1000_irv.md) | the paper's own p.5 field, eliminated down | A | [`yaml`](cases/kissel_five_way_c5_b1000_irv.yaml) |
| [Kissel's five-way (Ranked Robin)](cases/cases_pages/kissel_five_way_c5_b1000_rr.md) | same ballots, every pairing counted | C | [`yaml`](cases/kissel_five_way_c5_b1000_rr.yaml) |
| [Kissel's five-way (STAR)](cases/cases_pages/kissel_five_way_c5_b1000_star.md) | same electorate, one 0–5 grid | C | [`yaml`](cases/kissel_five_way_c5_b1000_star.yaml) |
| [The mayor's race (RCV-IRV)](cases/cases_pages/mayor_c4_b100_streamlined_irv.md) | full rounds find the third-place winner | Cora | [`yaml`](cases/mayor_c4_b100_streamlined_irv.yaml) |
| [The mayor's race (Ranked Robin)](cases/cases_pages/mayor_c4_b100_streamlined_rr.md) | 3–0 round robin | Cora | [`yaml`](cases/mayor_c4_b100_streamlined_rr.yaml) |
| [The mayor's race (STAR)](cases/cases_pages/mayor_c4_b100_streamlined_star.md) | scoring 356–280, runoff 69–31 | Cora | [`yaml`](cases/mayor_c4_b100_streamlined_star.yaml) |

**Run the paper's method yourself.** Neither engine in this repo counted the Contingent Vote before this page; `contingent_vote_report.py` now does, and cross-checks itself against `pref_voting`'s independent `plurality_with_runoff_put`:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/contingent_vote_report.py method_comparisons/kissel_single_elimination_rcv/cases/mayor_c4_b100_streamlined_irv.yaml
```

Add `--ranks 2` for the Supplementary Vote — the paper's two-mark ballot, with the exhausted count:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/contingent_vote_report.py --ranks 2 method_comparisons/kissel_single_elimination_rcv/cases/mayor_c4_b100_streamlined_irv.yaml
```

**Lean disclosure:** the Cardinal Institute is a free-market state policy think tank, and the paper is written to persuade conservative legislators — its framing ("A Conservative Approach") says so openly, and the cover carries a disclaimer that the views are the author's. Per the repo's [sourcing tiers](../../CLAUDE.md) that makes it a fine source for a *proposal* and a weak one for *empirical verdicts* like "quite rare" — which is exactly where it needed evidence and didn't have any. It is also, by the standards of this genre, notably fair: it concedes its own method's central flaw, refuses the "majority" talking point, and quotes its critics accurately. This repo's own lean runs the other way — it advocates STAR — which is why the [cut against STAR](#the-honest-cut-against-star) is on the page. The same recipe applied to the other camp: [FairVote's STAR white paper](../fairvote_star_whitepaper/) · [CES's majority illusion](../ces_majority_illusion/).
