# A win with no mandate — reading the *strength* of a result

**Level: 201 · deep dive**

**One line:** every method answers *who won*; a score ballot also answers *how much anybody wanted them*, and when the answer is "0.9 stars out of 5" that number is a published fact about the winner rather than a matter of opinion — the one piece of information a Choose-One count structurally cannot produce.

Companion pages: the table this reads from is [The Score Distribution table](reporting_LH/score_distribution.md); the two averages in it are [Score averages — which denominator, and why](score_averages.md); the same question one stage later is [Runoff percentages](../the_count/runoff_percentages.md).

---

## The scenario

Imagine a field where the candidates are disliked or simply unknown to most voters, and nearly every score cast is a 1 or a 0. Somebody still gets elected. The interesting question is not who — it is what the report can tell that winner, and what it can tell everyone thinking about running next cycle.

This case is built to be exactly that election: 100 ballots, four candidates, **82% of every score cast is a 1 or a 0**, with a scattering of die-hards who give a 4 or a 5.

<!-- report:weak_mandate_c4_b100 -->
```text
[Divergence from STAR]
  STAR     = Beth
  Approval = Colin   (differs from STAR)

--- STAR Voting Method (single winner) ---

[STAR Voting]
 Tabulating 100 ballots.
Count × Arlo,Beth,Colin,Dara
   15 ×    0,   1,    -,   0
    8 ×    2,   0,    -,   0
    6 ×    0,   2,    -,   0
    6 ×    1,   1,    -,   0
    5 ×    0,   1,    2,   0
    5 ×    1,   2,    -,   0
    5 ×    0,   0,    -,   0
    4 ×    0,   0,    -,   2
    3 ×    1,   0,    -,   1
    3 ×    1,   1,    -,   1
    3 ×    2,   0,    -,   1
    3 ×    1,   0,    -,   0
    3 ×    1,   5,    -,   0
    3 ×    0,   0,    0,   0
    3 ×    2,   1,    -,   0
    2 ×    1,   0,    -,   2
    2 ×    0,   0,    4,   0
    2 ×    0,   1,    0,   0
    2 ×    1,   0,    2,   0
    2 ×    0,   1,    5,   0
    2 ×    1,   4,    -,   0
    2 ×    0,   0,    -,   5
    2 ×    1,   1,    2,   0
    1 ×    0,   0,    5,   0
    1 ×    1,   1,    4,   0
    1 ×    5,   0,    -,   0
    1 ×    0,   1,    -,   2
    1 ×    0,   1,    -,   1
    1 ×    2,   1,    -,   1
    1 ×    1,   0,    -,   4
    1 ×    0,   1,    4,   0
    1 ×    0,   0,    2,   0
  ('-' = left blank / abstained; '0' = scored zero — both count as 0 stars.)

[STAR Voting: Scoring Round]
 The two highest-scoring candidates advance to the next round.
   Beth          -- 88 -- First place
   Arlo          -- 68 -- Second place
   Colin         -- 51
   Dara          -- 39
 Beth and Arlo advance.

[STAR Voting: Automatic Runoff Round]
 The candidate preferred in the most head-to-head matchups wins.
   Beth          -- 43 -- First place
   Arlo          -- 27
   Equal Support -- 30
 Beth wins.
   Runoff math:
     100  ballots cast
   −  30  Equal Support (no preference between the two finalists)
     ───
      70  voters with a preference  (majority = 36)
           Beth 43 (61%)  ·  Arlo 27 (39%)

[STAR Voting: Winner — STAR Voting Method (single winner)]
 Beth
```
<!-- /report -->

## Three numbers that only a score ballot prints

The scoring round of that report, pulled out on its own — this is the table the rest of this page reads:

```text title="Abridged for the lesson — the Score Distribution block and the Condorcet lines only"
[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  Abs  | Total  Avg all  Avg rated
Arlo        1   0   0  15  33  51    0  |    68      0.7        0.7
Beth        3   2   0  11  43  41    0  |    88      0.9        0.9
Colin       3   4   0  10   0   5   78  |    51      0.5        2.3
Dara        2   1   0   7  11  79    0  |    39      0.4        0.4

[Condorcet Winner]
  Condorcet Winner: Beth — matches the STAR winner

[Condorcet Loser]
  Condorcet Loser: Colin — loses every head-to-head matchup — elected by Approval!
```

**1. The mandate itself: `Avg all` = 0.9.** Beth won with **88 stars out of a possible 500**. She is the legitimate winner — she leads the scoring round and she wins the head-to-head runoff against the runner-up — and she is also, on the record, the choice of an electorate that would rather have had somebody else. Both things are true at once, and the report says both without editorializing. A Choose-One tally would print `Beth — 34 votes, elected` and be finished; the *ceiling* of a Choose-One ballot is one mark, so there is no room on it for "and nobody was happy about it."

**2. The size of the shrug: 30 Equal Support.** Thirty of the hundred ballots scored the two finalists *identically* and therefore expressed no preference between them. They are not spoiled and not abstentions — they are counted in full in the scoring round, and the runoff line names them rather than hiding them in a denominator. A third of the electorate looked at the two people who could actually win and had nothing to choose between them.

**3. Unknown is not the same as disliked — and only the `Abs` column can tell.** Colin totals 51 stars and finishes third, close to Dara's 39. Read the row and they are nothing alike:

| | Total | `Avg all` | `Abs` | `Avg rated` |
|---|---:|---:|---:|---:|
| **Colin** | 51 | 0.5 | **78** | **2.3** |
| **Dara** | 39 | 0.4 | 0 | 0.4 |

Dara was rated by everyone and rated badly. Colin was **left blank by 78 voters**, and among the 22 who had an opinion he scored 2.3 — the strongest real support anywhere in this election. The scoring round is right to rank him third: being unrated is not the same as being liked, and a candidate 78% of voters cannot identify has not earned the seat. But the two columns together say something the winner's total never could — *there was a candidate people liked, and the problem was reach, not appeal.* That is precisely the signal that argues for more and better-campaigned candidates next time, and it is invisible to any method that records only an order.

## What the report does *not* do

It does not act on any of this. There is no threshold below which STAR declines to elect, no "none of the above" rung, and no re-run trigger; 0.9 out of 5 elects exactly as firmly as 4.6 out of 5. The number is **information for the people reading the result**, not a rule inside the count. A body that wants a floor has to write one into its own bylaws — a quorum, a minimum-support requirement, a NOTA option — and the score report is what makes such a rule *checkable* rather than rhetorical.

It also does not tell you whether a low-enthusiasm result is a problem. That is the [values question](../../../07_Concepts/topics/what_makes_a_good_winner.md), not a statistic. An election in which every candidate is mediocre and the report says so is working correctly.

## The threshold trap: where you draw the approval line decides this election

The divergence block above reports **Approval = Colin**, who is also the [Condorcet](reporting_LH/matrix.md) *loser* — he loses every head-to-head matchup. That is worth unpacking rather than scoring a point with, because it is mostly an artifact and partly a real warning.

The engine's divergence line projects score ballots onto an approval ballot at **3 stars or more**. In a field where 82% of marks are 0 or 1, that threshold discards almost the whole electorate:

| approval line | Arlo | Beth | Colin | Dara | winner |
|---|---:|---:|---:|---:|---|
| **3+ stars** (the divergence block's reading) | 1 | 5 | **7** | 3 | Colin, on 7 ballots out of 100 |
| **any non-zero score** | 49 | **59** | 17 | 21 | Beth |

Same ballots, same voters, opposite winners — the entire result rides on where the line is drawn. The honest reading: this is **not** a demonstration that [Approval](../../../04_Approval/README.md) elects Condorcet losers. Real Approval voters are asked to approve directly, and voters facing a field like this one would approve their least-bad option rather than approve nobody; they would behave like the second row, not the first. What it *does* show is a genuine property of any threshold method in a no-enthusiasm field: when hardly anyone feels strongly, a small bloc that does can carry the seat, and the voter has to decide where "approve" starts with no guidance from the ballot. STAR's runoff asks a question that has an answer on every ballot — *of these two, which did you score higher?* — which is why 70 voters still separate the finalists here even though only 12 of them ever wrote a 3 or better.

## Does a bigger field help or hurt?

Both, and the report is how you tell which one happened.

- **More candidates raise the ceiling.** The best available option can only be someone who ran. A field of two disliked incumbents cannot produce a 4-star winner no matter how the ballots are counted, and Colin's `2.3` rated average exists only because he was on the ballot at all.
- **More candidates do not divide a score ballot.** Every voter scores every candidate independently, so adding a fifth name takes nothing away from the other four — no vote-splitting, no spoiler, no reason for anyone to stay out of the race. That is the structural difference from Choose-One, where each added candidate shaves the winner's share until a mandate can vanish entirely: [the pineapple progression](../../../method_comparisons/minority_winner_progression/README.md) grows a menu from 3 options to 11 and watches the winner's slice shrink to a quarter.
- **What more candidates *do* cost is attention.** Colin is the whole lesson: 78 blanks is what a crowded or low-information ballot does to a newcomer. A bigger field spreads name recognition thinner, so `Abs` climbs and `Avg all` falls for everyone — which reads on the report as a *weaker* electorate-wide result even when the field itself improved.

So: recruit more candidates, and read `Avg rated` next to `Avg all` before concluding the field was bad. A low `Avg all` with a low `Avg rated` is a field voters knew and rejected. A low `Avg all` with a high `Avg rated` is a field voters never got to know.

## See also

- [Preference vs support](../../../07_Concepts/scores_and_ranks/preference_vs_support.md) — the general form of this page: a mandate and a resignation can produce the same ranking.
- [Abstention vs zero vs NOTA](../properties_and_limits/abstention_vs_zero_vs_nota.md) — what a blank actually means on a STAR ballot.
- [Full count for this case](cases/cases_pages/weak_mandate_c4_b100.md) · [`_tabulated` mirror](cases/cases_tabulated/weak_mandate_c4_b100_tabulated.txt)
