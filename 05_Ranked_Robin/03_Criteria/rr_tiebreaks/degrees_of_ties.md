# Degrees of ties — how Ranked Robin is supposed to break one

**Level: 301 · deep dive**

*Ranked Robin has a tie-break protocol of its own, published, worked and four rungs deep. Neither engine in this repo implemented it. They failed in **opposite** ways, which is why the disagreement between them looked for two years like a difference of opinion about the method rather than a bug on one side — and the side that was wrong was ours.*

## The ladder

The Equal Vote Coalition's protocol ([electowiki, *Ranked Robin* → Degrees of ties](https://electowiki.org/wiki/Ranked_Robin#Degrees_of_ties)) starts where the tally ends. Tie for the most pairwise victories, and the tied candidates become **finalists**:

| Rung | The question it asks | Pool |
|---|---|---|
| **1st Degree** | greatest sum of win margins over **the other finalists** | the tie itself |
| **2nd Degree** | greatest sum of win margins over **all candidates** | the whole field |
| 3rd Degree | of candidates still level, the least polarising — fewest votes for **and** against | the whole field |
| 4th Degree | greatest sum of shortest-beatpath strengths among the tied | the whole field |

A win margin is just the pairwise result read as one number: the votes ranking you higher minus the votes ranking the other higher. Sum those over a pool and you get a figure that can be positive or negative, and that always sums to zero across the pool — which is the protocol's own argument that the 1st Degree winner is *majority preferred among finalists*, since somebody in the tie must be above zero.

*(The ladder starts from "a tie for the most pairwise victories" — and what counts as a victory is itself unsettled when a matchup is drawn. That question sits below everything on this page and is taken up at the end: [what counts as a win](#the-rung-below-the-ladder-what-counts-as-a-win).)*

**Two things about this ladder are easy to miss, and both change winners.**

**The pool moves between the rungs.** The 1st Degree asks only about the finalists' matches with each other. The 2nd Degree asks about their matches with everybody. Those are different questions with different answers, and the protocol deliberately asks the narrow one first.

**For exactly two finalists, the 1st Degree *is* the head-to-head.** Two candidates, one match between them, so the sum of margins over "the other finalists" is a single number and its sign is who won that match. This is the rung that matters most in practice, because two-way ties are the common case — and it means an engine that breaks a two-way tie head-to-head is already doing the 1st Degree, whether or not it says so.

The spec stops recommending itself after the 2nd Degree: it defines the 3rd and 4th but says plainly that for public elections a lot or a re-run is better for voter trust than tie-breaking mechanics nobody can follow. So a faithful implementation is **1st Degree → 2nd Degree → lot**, which is exactly what this engine now does.

## Where the two engines were

| | Copeland tie → | and then → | and then → |
|---|---|---|---|
| **The protocol** | 1st Degree (finalists) | 2nd Degree (whole field) | lot |
| **This engine**, before 2026-08-19 | *(no such rung)* | total margin over the whole field | published lot |
| **BetterVoting** `RankedRobin.ts` | head-to-head, **but only when exactly two are tied** | *(no such rung)* | seeded shuffle |

Read the table by column and the shape of each bug is visible. BetterVoting implements the 1st Degree, correctly, in the only case it handles — and has nothing at all for three or more tied candidates, so those fall straight past both degrees to the shuffle. This engine had the 2nd Degree and used it as though it were the first, so it answered the whole-field question in cases where the protocol had already been decided by the narrow one.

The two failures overlap on nothing, which is why the engines' answers differed so often and so confidently.

## What each bug costs

### BetterVoting: every three-candidate cycle goes to lot

Not a corner case. With three candidates and no drawn matchups, **every** Condorcet cycle is a three-way Copeland tie — the scores must sum to 3, and no candidate can be alone at the top without beating both others — so the two-way rung can never fire on one, and the shuffle is the entire cycle path. Filed as [bettervoting#1469](https://github.com/Equal-Vote/bettervoting/issues/1469).

Eleven ballots make the point:

<!-- ballots:rr_degrees_three_way_cycle -->
Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Dre>Edith>Frank
Dre>Edith>Frank
Edith>Frank>Dre
Edith>Frank>Dre
Edith>Frank>Dre
Edith>Frank>Dre
Frank>Dre>Edith
Frank>Dre>Edith
Frank>Dre>Edith
Frank>Dre>Edith
Frank>Dre>Edith
```
<!-- /ballots -->

The cycle is lopsided — Frank beats Dre 9–2 while the other two matches are won by 3 and by 1 — so the 1st Degree is not close: Frank +6, Edith −2, Dre −4, on eleven ballots. Frank is the only finalist above zero.

<!-- report:rr_degrees_three_way_cycle -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 11 ballots (ranked ballots).

Ballots:
     2 × Dre > Edith > Frank
     4 × Edith > Frank > Dre
     5 × Frank > Dre > Edith

Round-Robin — every pair, head-to-head (For – Against):
   Dre    beats Edith   7 – 4
   Frank  beats Dre     9 – 2
   Edith  beats Frank   6 – 5

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |    Dre    |  Edith   |  Frank   |
---------------------------------------------
    Dre > |    ---    |7 - 0 - 4 |2 - 0 - 9 |
  Edith > | 4 - 0 - 7 |   ---    |6 - 0 - 5 |
  Frank > | 9 - 0 - 2 |5 - 0 - 6 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  Frank      1–1–0         1      +6            +6  Dre
    2  Edith      1–1–0         1      -2            -2  Frank
    3  Dre        1–1–0         1      -4            -4  Edith

Winner — Ranked Robin (RCV-RR): Frank
   *** 3 candidates tie for the most wins (Dre, Edith, Frank) — a Condorcet cycle (no candidate beats all others). Resolved by the 1st Degree tiebreaker: Frank has the greatest sum of win margins over the other finalists (+6). (This is where Minimax / Ranked Pairs / Schulze differ — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.)
```
<!-- /report -->

BetterVoting reports whichever of the three sits first in its shuffled candidate order, and in its sandbox that is simply the order they were typed in: enter the same election as Edith, Frank, Dre and the page says Edith won.

### This engine: the whole field decided ties the finalists had already decided

The narrow question and the wide one come apart as soon as a finalist has run up a score against somebody who isn't in the tie:

<!-- ballots:rr_degrees_finalists_vs_field -->
Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
8:Ben>Dane>Cleo>Alma
9:Cleo>Alma>Ben>Dane
9:Alma>Ben>Cleo>Dane
```
<!-- /ballots -->

<!-- report:rr_degrees_finalists_vs_field -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 26 ballots (ranked ballots).

Ballots:
     8 × Ben > Dane > Cleo > Alma
     9 × Cleo > Alma > Ben > Dane
     9 × Alma > Ben > Cleo > Dane

Round-Robin — every pair, head-to-head (For – Against):
   Ben   beats Dane   26 –  0
   Ben   beats Cleo   17 –  9
   Alma  beats Ben    18 –  8
   Cleo  beats Dane   18 –  8
   Alma  beats Dane   18 –  8
   Cleo  beats Alma   17 –  9

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
         |     Ben      |    Dane     |    Cleo     |    Alma     |
-------------------------------------------------------------------
   Ben > |     ---      |26 -  0 -  0 |17 -  0 -  9 | 8 -  0 - 18 |
  Dane > |  0 -  0 - 26 |    ---      | 8 -  0 - 18 | 8 -  0 - 18 |
  Cleo > |  9 -  0 - 17 |18 -  0 -  8 |    ---      |17 -  0 -  9 |
  Alma > | 18 -  0 -  8 |18 -  0 -  8 | 9 -  0 - 17 |    ---      |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  Alma       2–1–0         2     +12            +2  Ben, Dane
    2  Cleo       2–1–0         2     +10             0  Alma, Dane
    3  Ben        2–1–0         2     +24            -2  Cleo, Dane
    4  Dane       0–3–0         0     -46             —  —

Winner — Ranked Robin (RCV-RR): Alma
   *** 3 candidates tie for the most wins (Ben, Cleo, Alma) — a Condorcet cycle (no candidate beats all others). Resolved by the 1st Degree tiebreaker: Alma has the greatest sum of win margins over the other finalists (+2). (This is where Minimax / Ranked Pairs / Schulze differ — see 05_Ranked_Robin/01_Learn/cycle_resolution.md.)
```
<!-- /report -->

Alma, Ben and Cleo cycle and tie at two wins each. Ben's total margin is +24 against Alma's +12 — but nearly all of Ben's number is one matchup, 26–0 against Dane, who lost everything and was never a finalist. Ask the 1st Degree question and Alma leads at +2. Ask the 2nd Degree question first, as this engine did, and a candidate who lost to Alma head-to-head wins the tie on the strength of how hard he beat somebody irrelevant to it.

**On two finalists the same bug shows up as overriding the head-to-head**, and that is the version that actually fired on this repo's cases: **11 of the 100 Ranked Robin cases changed winner** when the ladder was corrected, and **every one of them was a two-way tie whose head-to-head was decisive**. In each, the old engine elected the candidate who had lost the finalists' own match.

## The four cases that were filed as engine disagreements

Four of the eleven are BV-backed, and in all four the corrected engine now agrees with the winner BetterVoting published:

| Case | Old LH winner | Now (and BV's live result) |
|---|---|---|
| [BV2270 — the two-way tie](bv2270_8h4bvh_head_to_head_vs_margin.md) | Birch | **Alder** |
| [BV2138 — no Condorcet winner](../../../method_comparisons/no_condorcet_bv2138/README.md) | Abby | **Brad** |
| [BV2176 — the Post-it example](../../../method_comparisons/postit_rcv_example/bv2176_p8dp28_postit_rcv_example.md) | Blue | **Green** |
| [BV2143 — clone teaming](../clone_independence/README.md) | A1 | **C** |

Two of those pages existed *because* of the disagreement. They are worth keeping and worth re-reading: a divergence between two independent implementations is real evidence that one of them is wrong, and this repo spent two years treating it as a difference of convention. The lesson that survives is the one about method definitions — **"break the tie by margins" is not a rule until you say margins over what.**

## A note on the source

The protocol's own worked example of clone teaming does not follow it. [electowiki's clone-independence section](https://electowiki.org/wiki/Ranked_Robin) argues that a faction can convert a coin flip into a win by running clones, and concludes that after cloning "A1 wins after the tiebreaker". On those ballots the finalists are A1 and C, and C beats A1 head-to-head 21–12 — so the 1st Degree elects **C**, and the teaming attack backfires. The clones do still change the outcome (before cloning the count ends in a tie the degrees cannot separate), so clone independence still fails by crowding; what fails with it is the claim that teaming pays. It pays only against the total-margin reading, which is the 2nd Degree — the same mistake this engine was making. Worked in full in [clone independence](../clone_independence/README.md).

## The rung below the ladder — what counts as a win

Everything above starts from the same sentence: *"If there is a tie for the greatest number of pairwise victories…"* Read it again with a **drawn** matchup in mind, and it stops being obvious. A draw is not a victory. Is it nothing, or is it half of one?

The two answers are not equivalent, and the protocol and its implementations are on opposite sides.

**What the spec says.** The primary rule is not a tie-break at all — it is the whole tabulation, stated in one line: *"Elect the candidate who pairwise beats the greatest number of candidates."* Read literally that counts wins and ignores draws, and the source means it literally: in [its own four-degree example](bv2141_3r3yf7_four_degree_tie.md), Ava beats three candidates, draws with Bianca 29–29 and loses one — and the page scores her **3**.

**What every implementation does.** All three engines this repo can reach score that same Ava **3.5**, because they use the standard Copeland tally, `wins + ½·draws`. Our own report prints it on exactly the example electowiki scores as 3:

```text title="Abridged for the lesson — not verbatim engine output"
    #  Candidate  W–L–T  Copeland  Margin
    1  Ava        3–1–1       3.5     +55
    2  Bianca     3–1–1       3.5     +55
```

BetterVoting's `RankedRobin.ts` awards the same half point, and so does `pref_voting`'s independent Copeland. Nobody implements the sentence as written.

### It can change the winner

On the four-degree example the disagreement is invisible in the outcome — Ava and Bianca have identical records, so they tie at 3 and at 3.5 alike, and the same two candidates go into the ladder. That is luck, not a general fact. Change the *shape* of the records and the two readings elect different people:

<!-- ballots:rr_degrees_what_counts_as_a_win -->
Each row is one voter's ranking, most-preferred first (`N:` prefix = N identical ballots).

```text
Aaron>Bella>Dana>Caleb
Dana>Aaron>Caleb>Bella
Bella>Dana>Aaron>Caleb
Caleb>Bella>Dana>Aaron
```
<!-- /ballots -->

Four voters, four different favourites, no equal rankings anywhere — the two drawn matchups are just the electorate splitting 2–2, which is how a small round robin ordinarily produces one.

<!-- report:rr_degrees_what_counts_as_a_win -->
```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 4 ballots (ranked ballots).

Ballots:
     1 × Aaron > Bella > Dana > Caleb
     1 × Dana > Aaron > Caleb > Bella
     1 × Bella > Dana > Aaron > Caleb
     1 × Caleb > Bella > Dana > Aaron

Round-Robin — every pair, head-to-head (For – Against):
   Aaron  ties  Bella   2 – 2
   Dana   beats Aaron   3 – 1
   Aaron  beats Caleb   3 – 1
   Bella  beats Dana    3 – 1
   Bella  ties  Caleb   2 – 2
   Dana   beats Caleb   3 – 1

--- Pairwise (Round-Robin) Matrix ---
Head-to-head / pairwise comparison — the Ranked Robin tally
Legend: For - Equal Support - Against   (row vs column)
          |   Aaron   |  Bella   |  Dana    |  Caleb   |
--------------------------------------------------------
  Aaron > |    ---    |2 - 0 - 2 |1 - 0 - 3 |3 - 0 - 1 |
  Bella > | 2 - 0 - 2 |   ---    |3 - 0 - 1 |2 - 0 - 2 |
   Dana > | 3 - 0 - 1 |1 - 0 - 3 |   ---    |3 - 0 - 1 |
  Caleb > | 1 - 0 - 3 |2 - 0 - 2 |1 - 0 - 3 |   ---    |

Win–loss record — Copeland score = wins + ½·ties (highest score wins; ties broken by the Ranked Robin degrees, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  vs finalists  Beats
    1  Bella      1–0–2         2      +2            +2  Dana
    2  Dana       2–1–0         2      +2            -2  Aaron, Caleb
    3  Aaron      1–1–1       1.5      +0             —  Caleb
    4  Caleb      0–2–1       0.5      -4             —  —

Winner — Ranked Robin (RCV-RR): Bella
   *** 2 candidates tie on the highest Copeland score (2): Bella, Dana — tied on the tally, not a cycle (some of them beat others head-to-head, but no loop closes). Resolved by the 1st Degree tiebreaker: Bella has the greatest sum of win margins over the other finalists (+2).
```
<!-- /report -->

Read the **W–L–T** column, because that is where the whole question lives:

| | record | wins + ½·draws | wins only |
|---|---|---|---|
| **Bella** | 1–0–2 — **never beaten** | **2.0** — tied for top | 1 — third |
| **Dana** | 2–1–0 — beaten by Bella | **2.0** — tied for top | **2** — top, alone |

Under the convention the engines use, Bella and Dana tie, both become finalists, and the 1st Degree separates them on their own matchup, which Bella won 3–1. **Bella is elected.** Under the sentence as written, there is no tie to break: Dana has two victories to Bella's one and **Dana is elected outright**, with the ladder never running at all.

### Why this repo reads it as loose drafting

Notice which way the literal reading errs. It elects **Dana, who lost a matchup, over Bella, who lost none.** A rule that seats a candidate ahead of someone nobody beat is doing something a round-robin scorer is not supposed to do, and it is far easier to believe the sentence was written for the ordinary case — where every matchup is decided and the two readings agree exactly — than that anyone intended that outcome.

The half-point also has an argument of its own that the wins-only reading cannot match: `wins + ½·draws` and `wins − losses` are affine transforms of each other, so they always produce the *same ranking*. Raw wins is the odd rule out, agreeing with neither. That is the reasoning already written into this engine's `ranked_robin_tally`, and it is why a drawn matchup being worth half a win is the standard Copeland tally rather than a house choice.

**So: this repo scores a draw as half a win, and says so wherever it prints a Copeland column.** But that is a judgement about a published definition, not a finding, and the definition it departs from is the method's own. It is recorded here as an open question rather than settled, and it is not filed as a defect against anyone: three independent implementations agreeing against a one-line summary is much more likely to be imprecise drafting than a bug replicated three times. What would close it is Equal Vote saying which they meant — the same posture this repo takes on [what to call the method](../../01_Learn/what_to_call_this_method.md), where the field is genuinely unresolved and our preference is an argument rather than a ruling.

**If it were ever settled the other way**, the cost is bounded and knowable: nothing changes on any election whose every matchup was decided, and among the cases here only those with a drawn matchup *and* differently-shaped records at the top could move.

## Why not just run Copeland again?

The rung directly after the tie is a **margin**, and that is worth pausing on, because there is an obvious-looking alternative the protocol does not take: run Copeland a second time. Score each tied candidate by the Copeland scores of the opponents they *defeated*, and let whoever beat the stronger field take it. That is a real published rule — **second-order Copeland** — and it carries a selling point margins cannot match: it makes manipulating the count NP-hard, so a party trying to reverse-engineer the ballots it needs has a genuinely hard problem to solve.

It also does not work, at exactly the field size where a tie is most likely to arrive.

Enumerate every way three candidates' matchups can come out — win, draw or loss on each of the three pairs, 27 patterns in all — and **six** of them tie for the Copeland lead. A second Copeland round separates **none** of the six:

| Pairwise outcome | Copeland | 2nd-order | net | |
|---|---|---|---|---|
| A>B · A=C · C>B | A 1.5, C 1.5 | A 0, C 0 | A 0, C 0 | still tied |
| A>B · C>A · B>C *(cycle)* | A 1, B 1, C 1 | A 1, B 1, C 1 | A 0, B 0, C 0 | still tied |
| A=B · A>C · B>C | A 1.5, B 1.5 | A 0, B 0 | A 0, B 0 | still tied |
| A=B · A=C · B=C *(all draws)* | A 1, B 1, C 1 | A 0, B 0, C 0 | A 0, B 0, C 0 | still tied |
| B>A · A>C · C>B *(cycle)* | A 1, B 1, C 1 | A 1, B 1, C 1 | A 0, B 0, C 0 | still tied |
| B>A · C>A · B=C | B 1.5, C 1.5 | B 0, C 0 | B 0, C 0 | still tied |

Both score columns are shown because the literature carries two readings of the second-order score — the Copeland scores of the opponents you beat, or that minus the scores of the opponents who beat you — and on this evidence the choice never matters, which is its own small result. The reason is plain enough to check by hand: with three candidates, two contenders level on Copeland have beaten the same *number* of opponents, and the only opponent outside the tie is the lone third candidate, so their defeated sets carry identical weight. A second round has nothing to read that the first round did not already spend.

Widen the field and the rule does start to bite, because the tied candidates can at last have beaten *different* people — it settles 38% of four-candidate ties and 76% of five-candidate ties. But that is backwards from where the help is wanted. Ties concentrate in small fields, and the three-candidate cycle — the case BetterVoting still sends straight to its shuffle ([#1469](https://github.com/Equal-Vote/bettervoting/issues/1469)) — is precisely the one a second Copeland round can never touch.

[The eleven-ballot cycle above](#bettervoting-every-three-candidate-cycle-goes-to-lot) is the runnable instance, and it is the same one BetterVoting sends to its shuffle: Dre, Edith and Frank each finish 1–1–0, each beats exactly one opponent, and every opponent beaten is worth the same Copeland 1. Second-order Copeland returns three 1s and stops. The 1st Degree returns Frank, +6.

So margins are what is left, and the ladder's shape stops looking like a preference and starts looking like the only option: margins read information the win counts throw away, and they are available at every field size, including the one where second-order Copeland goes silent.

The enumeration is exhaustive rather than sampled, and it loses nothing by working on pairwise patterns instead of ballots — by [McGarvey's theorem](../../../07_Concepts/topics/tournament_solutions.md) every complete pattern is produced by some electorate, and the three patterns above that contain a draw need only an even one. Reproduce it with [`second_order_copeland_sweep.py`](../../../STARVote_LH_tabulation_engine/tools_adam/second_order_copeland_sweep.py):

```bash
.venv/bin/python STARVote_LH_tabulation_engine/tools_adam/second_order_copeland_sweep.py --show 3
```

*Second-order Copeland is not a straw man — it stood in the Wikipedia article on Copeland's method until 2021, when it was removed on the grounds that it "[has] the drawback of not being likely to resolve ties in the first place. In particular, if a tie arises in a 3-way election, then a second Copeland round never resolves it" ([Talk:Copeland's method](https://en.wikipedia.org/wiki/Talk:Copeland%27s_method), Colin.champion, 22 January 2021). The claim was asserted there without a demonstration; the table above is the demonstration, and it holds under both readings of the score.*

## Where the ladder still ends in a lot

Correcting the rungs does not make Ranked Robin decisive, and a fix that always decided would be the wrong fix. [BV2141](bv2141_3r3yf7_four_degree_tie.md) is electowiki's own "needs all four degrees" example: Ava and Bianca tie at 3 wins, tie at 0 on the 1st Degree and at +55 on the 2nd, and only the 4th Degree beatpath separates them — which the protocol does not recommend using. That case still ends at the lot, on both engines, and it is the regression test that keeps the fix honest.

## Related

- [rr_tiebreaks — the case set](README.md) · [Ranked Robin tie-breaks: LH vs BetterVoting](../../01_Learn/rr_tiebreak_lh_vs_bv.md)
- [Cycle resolution — why Minimax, Ranked Pairs and Schulze exist](../../01_Learn/cycle_resolution.md)
- [Ranked Robin (the method)](../../01_Learn/ranked_robin.md) · [clone independence](../clone_independence/README.md)
- Upstream: [bettervoting#1469](https://github.com/Equal-Vote/bettervoting/issues/1469) · [#1063 deterministic tie-breaking](https://github.com/Equal-Vote/bettervoting/issues/1063) · [our tracker row](../../../07_Concepts/about_this_repo/upstream_bug_reports.md)

# file: degrees_of_ties.md
