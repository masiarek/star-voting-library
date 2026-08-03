# The case for approval voting — Hamlin & Hua (2023), §4 claim-checked

*The companion article to [the foundational STAR paper](../../01_STAR/01_Learn/reference/wolk_quinn_ogren_2023.md) — same journal, same issue, the next ten pages. Approval's advocacy organisation makes its case in an academic venue, and section 4 answers the four critiques it expects: the majority criterion, later-no-harm, bullet voting, expressiveness. This page runs it through the same [claim-check recipe](../../method_comparisons/fairvote_star_whitepaper/) used on every camp — concede the kernel, test what's testable, flag the overreach, disclose the lean. The §4.1 example is fully runnable, so most of this page is engine output rather than argument.*

**Level: 301.** · [DOI 10.1007/s10602-022-09381-x](https://doi.org/10.1007/s10602-022-09381-x) · runnable companions: [Approval and the majority criterion](../../method_comparisons/approval_majority_criterion/README.md).

> **Hamlin, A. & Hua, W. (2023).** "The case for approval voting." *Constitutional Political Economy* **34(3): 335–345.**

---

## Why this one matters here

Volume 34, issue 3 of *Constitutional Political Economy* carries both sides of the cardinal-voting argument back to back: **Wolk, Quinn & Ogren at 310–334** making the case for STAR, **Hamlin & Hua at 335–345** making the case for Approval. This library already claim-checks [the first](../../01_STAR/01_Learn/reference/wolk_quinn_ogren_2023.md) — including where its own numbers overreach. Doing the same to the second is not even-handedness for its own sake; it is the only way the first page keeps its credibility.

It also closes a real gap. This repo has asserted that Approval fails the [majority criterion](../../07_Concepts/topics/majority_criterion/README.md) — it's a row in the criterion table — while only ever *working* STAR's version of the failure. Section 4.1 supplies the missing demonstration, chosen by the approval side itself.

## §4.1 — the majority criterion, counted

The paper's example, reproduced with its own labels ([case 01](../../method_comparisons/approval_majority_criterion/cases/cases_pages/hh41_01_approval_as_printed.md)):

| voters | preference | approval ballot assumed |
|--:|---|---|
| 60 | A > B > C | A + B |
| 30 | B > C > A | B + C |
| 10 | C > B > A | C + B |

```text
--- Approval Voting (single winner) ---
 Tabulating 100 ballots (any non-zero score = approval).

   B -- 100 (100%) -- Elected
   A -- 60 (60%)
   C -- 40 (40%)
```

A is the first choice of 60% and loses. The paper states this plainly and does not hedge it — which is to its credit, and is why the section is worth engaging with rather than rebutting.

**One fact the section doesn't mention about its own example.** It opens by observing that a [Condorcet winner](../../07_Concepts/topics/condorcet/) need not exist. True in general — but this profile has one, and it is A ([case 02](../../method_comparisons/approval_majority_criterion/cases/cases_pages/hh41_02_preferences_ranked_robin.md)):

```text
Round-Robin — every pair, head-to-head (For – Against):
   A  beats B   60 – 40
   A  beats C   60 – 40
   B  beats C   90 – 10
```

So the loser here isn't only "the candidate a majority ranked first." It is the candidate a majority prefers to *each* rival, head to head. The general caveat about Condorcet winners is doing rhetorical work that this particular electorate doesn't support.

## The kernel — what's solid (concede it)

- **The example is correct as printed**, and conceded without spin. Advocacy writing that publishes its own method's clearest failure is doing something right.
- **"Frequency × severity, not pass/fail" is the correct framework** — and it is this library's own. It's exactly what stops [the majority-criterion page](../../07_Concepts/topics/majority_criterion/README.md) treating "STAR fails the majority criterion" as a knockout, and what the [criteria table](../../07_Concepts/topics/criteria_at_a_glance.md) is built on. A criterion checklist with no frequencies attached is a debating device, not an evaluation.
- **The severity claim checks out.** §4.1 argues that for B to be genuinely worse than A, the 60 would have to strongly prefer A and barely accept B, and the rest would have to barely disapprove of A — and that such a scenario has no large utility gap. Write those stipulations on a 0–5 ballot (5 / 3 at the approval line / 2 just under it) and the scoring round says [A 380, B 370](../../method_comparisons/approval_majority_criterion/cases/cases_pages/hh41_04_stipulated_utilities_star.md) — ten points in five hundred. **They're right: the gap is tiny.**
- **§4.2's answer to later-no-harm is the same one this repo gives for STAR.** "At worst, a candidate acceptable to the voter still wins" is precisely the [later-no-harm-is-a-bug-not-a-feature](../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md) argument, made by STAR's own co-inventor. A STAR advocate cannot accept it there and reject it here.
- **§4.3's bullet-voting data is real, and it settles a bad argument.** 2.3 marks per ballot in Fargo 2020, ~1.6 in St. Louis 2021, 2.23–3.15 in the French surveys, ~2 in the German study. "Everyone will just bullet vote" is an empirical claim, and the empirics say no. Note the two US figures are the Center for Election Science's own data from campaigns it ran — self-collected, though nothing suggests they're wrong.
- **§4.4's claims 1, 2 and 4 are true and are this repo's own critiques of ranked ballots.** Approval can express [equal support](../../07_Concepts/GLOSSARY.md); it never forces truncation; and it never discards recorded ballot information mid-count — unlike IRV, which does exactly that ([exhausted ballots](../../06_Other/RCV_IRV/concepts/RCV_IRV_exhausted_ballots.md), [no summability](../../06_Other/RCV_IRV/concepts/RCV_IRV_lack_of_summability.md)).

## Read it critically — where §4 doesn't hold

**1. The defence needs data the ballot cannot produce.** To argue "the utility discrepancy is small," you need utilities. §4.4's own claim 5 concedes what an approval ballot records: *a threshold*, not a degree of preference. So §4.1's rebuttal is sound reasoning that can only be *checked* on a score ballot — the ballot type the paper is arguing against. [Case 04](../../method_comparisons/approval_majority_criterion/cases/cases_pages/hh41_04_stipulated_utilities_star.md) performs that check on the paper's own stipulation, and it splits: the gap is tiny (they're right), and the majority favorite still wins (they're wrong that this rescues the result) —

```text
Scoring Round
   A             -- 380 -- First place
   B             -- 370 -- Second place
   C             -- 170

Automatic Runoff Round
   A             -- 60 -- First place
   B             -- 40
   Equal Support --  0
 A wins.
```

**2. Compression doesn't just lose the gap — it inverts and magnifies it.** Same voters, same opinions. At full resolution: A 380, B 370, a coin flip. Compressed to checkmarks: **B 100, A 60** — a landslide the other way. A method that reports a 40-point margin where the underlying opinions differ by 2% is not merely failing to see a small difference; it is confidently reporting a large one that isn't there. That is a sharper statement of the expressivity critique than [our own limits page](approval_honest_limits.md#1-no-preference-strength-or-order) makes.

**3. The frequency leg of their own test goes unargued.** §4.1 proposes judging violations by frequency *and* severity, then argues only severity. The frequency question here is: how often does a majority approve a second candidate? Their §4.3 answers it — **1.6 to 3.15 approvals per ballot** — which is to say, usually. The paper's bullet-voting section is a good answer to one critique and, unremarked, the frequency estimate that undercuts its answer to another.

**4. §4.1 and §4.2 are the same event, presented as two.** The 60 voters' approval of B is a *later* preference that harms their favorite — a later-no-harm failure — and it is *why* the majority favorite loses. This library already makes that identification for STAR ("[they are one phenomenon](../../07_Concepts/topics/majority_criterion/README.md#the-same-fork-as-later-no-harm)"); it holds identically here. Which means §4.2's answer is really §4.1's answer given a second time, and the paper's four critiques are closer to three.

**5. The violation lives in the threshold, not in the electorate.** Move one line — the 60 approve only A — and [A wins 60–40](../../method_comparisons/approval_majority_criterion/cases/cases_pages/hh41_05_majority_bullet_votes.md) with nobody's opinion changed. The outcome is decided by where 60 voters draw a line they were given no rule for drawing. That is [honest limits §2](approval_honest_limits.md#2-the-approval-threshold-dilemma-the-central-critique), and the paper's §4.3 (voters approve widely) and §4.1 (approving widely costs the majority its favorite) are the two horns of it.

**6. A runoff on approval ballots doesn't fix this.** Worth stating because it's the obvious next thought, and [case 03](../../method_comparisons/approval_majority_criterion/cases/cases_pages/hh41_03_marks_read_pairwise.md) shows why not:

```text
Automatic Runoff Round
   B             -- 40 -- First place
   A             --  0
   Equal Support -- 60
 B wins.
   Voters with a preference: 40 of 100 (60 Equal Support).
```

Sixty percent of the electorate has no voice in the deciding round, because they approved both finalists. The information wasn't outvoted; it was never written down. (Which is also why [Approval + Top-Two](approval_top_two.md) must be a *second election*, not an automatic runoff.)

**7. §4.4's comparison class excludes the method that wins on it.** Claim 5 — approval reveals a threshold "whereas ordinal methods show neither a threshold of support nor the degree of preference" — is true as stated and quietly sets the comparison against *ordinal* methods only. A 0–5 score ballot shows both. Their own 2^C expressiveness metric says the same thing once you extend it: at three candidates, **8** possible approval ballots against **216** for a 0–5 ballot; and from four candidates up, approval (16) has fewer than strict rankings (24). Similarly claim 4 — no data discarded in the tally — separates Approval from IRV but not from Score or STAR, which also discard nothing. Both claims are real advantages over the methods named and silent on the one nearest neighbour.

**8. Disclose the lean.** Both authors are the Center for Election Science — Hamlin co-founded it and was its executive director, Hua its director of research. CES is the Approval Voting advocacy organisation. This is advocates presenting their own method, exactly as [Wolk, Quinn & Ogren](../../01_STAR/01_Learn/reference/wolk_quinn_ogren_2023.md) are advocates presenting theirs, and both should be read the same way.

## Where the fairness cuts back

STAR fails the majority criterion too, and this repo works that failure in full: [BV95a / BV95b](../../01_STAR/03_Criteria/majority_criterion/README.md). Nothing above should be read as "Approval fails a criterion STAR passes" — the honest statement is about the trigger:

| | what it takes for the majority's favorite to lose |
|---|---|
| **Approval** | the majority approves **one** other candidate |
| **STAR** | the majority gives real support to **two** other candidates |
| **RCV-IRV / Choose-One** | never (they pass the criterion outright) |

That's the [Relaxed Majority Criterion](../../07_Concepts/topics/majority_criterion/README.md#the-relaxed-majority-criterion-equal-votes-answer), and it is a difference of degree. Note also that case 04 shows STAR electing the majority favorite in *this* profile — it does not show STAR always does.

## Test it — the runnable companions here

| The paper's claim | Run it |
|---|---|
| §4.1's example (approval elects B over a 60% majority favorite) | [case 01](../../method_comparisons/approval_majority_criterion/cases/cases_pages/hh41_01_approval_as_printed.md) |
| §4.1's opening caveat about Condorcet winners | [case 02](../../method_comparisons/approval_majority_criterion/cases/cases_pages/hh41_02_preferences_ranked_robin.md) — this profile has one, and it's A |
| §4.1's "no meaningfully large utility discrepancy" | [case 04](../../method_comparisons/approval_majority_criterion/cases/cases_pages/hh41_04_stipulated_utilities_star.md) — true (380 v 370), and A still wins |
| §4.3's bullet-voting frequencies, applied to §4.1 | [case 05](../../method_comparisons/approval_majority_criterion/cases/cases_pages/hh41_05_majority_bullet_votes.md) |
| "approval voting is not an ordinal method" (§4.1) | [case 03](../../method_comparisons/approval_majority_criterion/cases/cases_pages/hh41_03_marks_read_pairwise.md) · [Black Curtain](../../method_comparisons/black_curtain/condorcet_compression.md) |
| §4.4 expressiveness, against a score ballot | [scores vs ranks](../../07_Concepts/scores_and_ranks/scores_vs_ranks.md) · [preference vs support](../../07_Concepts/scores_and_ranks/preference_vs_support.md) |
| The critiques as the *neutral* literature states them | [Approval in the theory literature](approval_in_the_literature.md) (Zwicker, 2016) |

## The honest bottom line

Section 4 is a good-faith engagement with the real objections, and its evaluative framework — frequency and severity, not checkboxes — is the right one and the one this library uses. Its bullet-voting evidence should end that particular argument, and its later-no-harm answer is one STAR advocates already make for themselves.

What doesn't survive is the §4.1 defence, and it fails on its own terms. The severity claim is correct — the utility gap in that example really is negligible — but demonstrating it requires a ballot that records degrees, which is the ballot the paper argues against; the frequency claim is left unmade while §4.3 supplies numbers that cut the other way; and the example the section chose to concede turns out to have an unambiguous pairwise majority winner that the checkmark cannot see. Run at higher resolution, the same electorate is a near-tie between A and B. Run through checkmarks, it reports a 40-point win for the wrong one. Approval's own paper picked the example; the arithmetic is what it is.

---

*See also: [Approval — honest limits](approval_honest_limits.md) · [Approval in the theory literature](approval_in_the_literature.md) · [the majority criterion](../../07_Concepts/topics/majority_criterion/README.md) · [the runnable case set](../../method_comparisons/approval_majority_criterion/README.md) · [claim-checking as a habit](../../method_comparisons/fairvote_star_whitepaper/).*

# file: hamlin_hua_2023.md
