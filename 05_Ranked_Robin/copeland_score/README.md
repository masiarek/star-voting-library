# Copeland score — why a drawn matchup is worth half a win

[Ranked Robin](../concepts/ranked_robin.md) is usually explained as "whoever wins the most head-to-head matchups wins." That is a shorthand, and it is very nearly always right. This page is about the case where it isn't — where the actual rule, the **Copeland score**, elects someone the shorthand would not.

## The rule

Every candidate plays every other candidate head-to-head. Score the results like a chess tournament:

| Result | Credit |
|---|---|
| win | 1 |
| **draw** | **½** |
| loss | 0 |

**Copeland score = wins + ½·ties.** Highest score wins. That half-point for a draw is the entire subject of this page.

You will also see Copeland written as **wins − losses**, and the repo's own [glossary](../concepts/glossary_ranked_robin.md) uses that form. The two are not in conflict: with every candidate playing the same number of matchups, `wins − losses = 2·(wins + ½·ties) − (n−1)`. That is an affine transform — multiply by two, shift by a constant — so the two formulas **always produce the same ranking**. Pick whichever you find easier to explain; the winner never changes.

What *is* different is the raw win count. Ignore draws entirely and you get a third ordering, one that can disagree with both. Raw wins is the odd one out — and since a report that prints "W–L–T" invites you to read the W column as the answer, it is worth seeing exactly how that goes wrong.

## When the shorthand breaks

If every matchup has a winner, there are no draws, so `wins + ½·ties` **is** the win count and the shorthand is exact. This is the common case, which is why the shorthand survives.

The moment one matchup is drawn, the two part company — and a single half-point is enough to decide an election.

## The case: the chess club elects a president

Thirty club members rank five candidates.

| Voters | Ranking |
|---:|---|
| 9 | Alice > Elena > Dmitri > Bruno > Carmen |
| 8 | Carmen > Bruno > Alice > Elena > Dmitri |
| 7 | Dmitri > Bruno > Carmen > Alice > Elena |
| 6 | Carmen > Alice > Dmitri > Elena > Bruno |

Every pair meets head-to-head:

```
Alice  beats Dmitri  23 – 7        Bruno  beats Carmen  16 – 14
Alice  beats Elena   30 – 0        Dmitri beats Bruno   22 – 8
Alice  ties  Bruno   15 – 15       Dmitri beats Carmen  16 – 14
Carmen beats Alice   21 – 9        Carmen beats Elena   21 – 9
Bruno  ties  Elena   15 – 15       Elena  beats Dmitri  17 – 13
```

Which gives the round-robin table:

```
Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Alice      2–1–1       2.5     +34  Dmitri, Elena
    2  Carmen     2–2–0         2     +20  Alice, Elena
    3  Dmitri     2–2–0         2      -4  Carmen, Bruno
    4  Bruno      1–1–2         2     -12  Carmen
    5  Elena      1–2–1       1.5     -38  Dmitri

Winner — Ranked Robin (RCV-RR): Alice
   the highest Copeland score (2.5 = wins + ½·ties).
```

## Why Alice wins

Read the W column alone and Alice looks unremarkable: **two wins, exactly like Carmen and Dmitri.** On raw wins this is a three-way tie at the top.

Now count the draw. Alice's tie with Bruno is worth ½, so Alice sits on **2.5** while Carmen, Dmitri and Bruno are all on exactly **2.0**. Nobody else has 2 wins *and* a draw. The half-point is not a tiebreaker here — it is the whole margin of victory.

And note what Alice's record actually contains: **a loss.** Carmen beat Alice 21–9, a thumping. Ranked Robin still elects Alice, because nobody in this election beat everybody — there is no [Condorcet winner](../concepts/ranked_robin_vs_condorcet.md) at all. The [Smith set](../../00_start_here/topics/smith_set.md) is all five candidates: the whole field is one big [cycle](../concepts/cycle_resolution.md). When no one beats everyone, Ranked Robin falls back to the best overall record — and the best overall record can belong to someone who lost a match.

## What the half-point costs

Here is the part worth being honest about. Run this same profile through the other Condorcet methods and **every one of them elects Carmen, not Alice**:

| Method | Winner |
|---|---|
| **Copeland (= Ranked Robin)** | **Alice** |
| Minimax | Carmen |
| Ranked Pairs | Carmen |
| Schulze | Carmen |
| Split Cycle | Carmen |
| Stable Voting | Carmen |

Copeland stands alone against the field. That is not a rounding artifact — it follows directly from what Copeland is allowed to look at.

Copeland reads only **who beat whom**. A win is a win; the size of it is invisible. So compare the two candidates' losses:

- **Alice** lost once — to Carmen, by **12 votes**.
- **Carmen** lost twice — to Dmitri by **2**, and to Bruno by **2**.

Copeland sees "one loss" versus "two losses" and prefers Alice. Every method in the right-hand column can see *margins*, and they see a candidate who was barely nudged out of two matchups versus one who was decisively beaten in another — and they prefer Carmen.

That is the [C1 / C2 distinction](../../00_start_here/topics/what_a_method_reads.md) exactly: Copeland is a [tournament solution](../../00_start_here/topics/tournament_solutions.md), reading only the arrows; the others read the numbers on the arrows. Neither is obviously correct — discarding margins is a deliberate choice that buys resistance to certain manipulations — but a profile like this one is where the choice becomes visible, and it is a fair thing for a critic to raise.

## Cross-checks

Verified two ways, per the repo's Ranked Robin practice:

- **LH engine** (this repo's tabulator) → Alice, Copeland 2.5
- **`pref_voting`** (Eric Pacuit's independent library, Copeland computed as wins − losses) → Alice, `AGREE ✓ (unique Copeland winner)`

Two different formulas, one winner — the affine-equivalence claim above, confirmed in practice rather than asserted.

There is no BetterVoting election behind this case; it is a pure engine-mechanics illustration. The result is fully deterministic (Alice is the unique Copeland leader, so no tiebreak rung is ever reached), so nothing here depends on a lot draw.

## Run it yourself

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py 05_Ranked_Robin/copeland_score/cases/copeland_half_credit_decides.yaml
```

Want the whole count — the full pairwise grid, the Smith-set audit, the ballot listing? See the full LH report → [`copeland_half_credit_decides`](cases/cases_pages/copeland_half_credit_decides.md), or the raw [`_tabulated` mirror](cases/cases_tabulated/copeland_half_credit_decides_tabulated.txt). Source: [`copeland_half_credit_decides.yaml`](cases/copeland_half_credit_decides.yaml).

## See also

- [Tiebreaks — dead heat → lot](../rr_tiebreaks/) — the sibling case, where the ½-credit produces a *tie* instead of a decisive winner and the full ladder (wins → margin → lot) has to finish the job
- [Ranked Robin vs. "the Condorcet winner"](../concepts/ranked_robin_vs_condorcet.md) — same animal, until there's a cycle
- [Honest limits](../concepts/RCV_RR_honest_limits.md) — where Ranked Robin is genuinely weak
- [A naming decoder](../concepts/condorcet_naming_decoder.md) — round-robin / Copeland / Condorcet / Ranked Robin, which word means what

*(Up: [05_Ranked_Robin](../README.md) · concept docs: [Ranked Robin (RCV-RR)](../concepts/README.md))*

# file: README.md
