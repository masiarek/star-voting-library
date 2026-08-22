# Zero support — the election nobody voted in

**Level: 301 · deep dive**

**One line:** three ballots, five nominees, every score `0` — the degenerate limit of a tie, counted six ways, where the only thing that separates the methods is how loudly each one admits the lot decided.

Most tie probes in this library ask *"the ballots point two ways — now what?"* This one asks the harder question: **the ballots point nowhere at all.** Every candidate totals 0. Every head-to-head is Equal Support, 0–0. Every rung above the lot has nothing to count, because there is nothing on the paper to count. So whatever comes out is the [published lot order](../../07_Concepts/GLOSSARY.md) talking, and the only interesting behaviour left is whether the report says so.

It is not purely hypothetical. A committee ballot listing five names nobody recognises comes back close to this, and an electorate that deliberately withholds support comes back exactly like it — which is why the neighbouring lesson on [abstention vs. zero vs. NOTA](../../01_STAR/01_Learn/properties_and_limits/abstention_vs_zero_vs_nota.md) matters here: these voters did not *skip* the race. They showed up and scored everybody zero, which is a statement, and the engine has to turn a statement into a seat anyway.

The theory says it has to: [Ties Are Forced](../../07_Concepts/topics/ties/ties_are_forced.md) proves no anonymous, neutral, Paretian rule can always name one winner, so *something* must be spent. What this folder shows is which methods say what they spent.

## The ballots

<!-- ballots:zero_support_star -->
The ballots as marked — the filled bubble is the score given, and the score is the number in its column:

| # | Ballot as marked | Ada | Ben | Cleo | Dev | Elsa |
|:--:|:--|:--:|:--:|:--:|:--:|:--:|
| 1 | <img src="cases/img/zero_support_star_ballot_1.png" width="260" style="min-width:260px" alt="A 0–5 STAR ballot — voter 1 — turned out, then scored every nominee 0: Ada 0, Ben 0, Cleo 0, Dev 0, Elsa 0."> | 0 | 0 | 0 | 0 | 0 |
| 2 | <img src="cases/img/zero_support_star_ballot_2.png" width="260" style="min-width:260px" alt="A 0–5 STAR ballot — voter 2 — a deliberate 0 is not a blank ballot: Ada 0, Ben 0, Cleo 0, Dev 0, Elsa 0."> | 0 | 0 | 0 | 0 | 0 |
| 3 | <img src="cases/img/zero_support_star_ballot_3.png" width="260" style="min-width:260px" alt="A 0–5 STAR ballot — voter 3 — the third ballot says the same thing: Ada 0, Ben 0, Cleo 0, Dev 0, Elsa 0."> | 0 | 0 | 0 | 0 | 0 |
<!-- /ballots -->

## Six methods, one answer, six different levels of candour

Every method elects **Ada** — first on the lot — and for a two-seat count, Ada and Ben. That agreement means nothing at all: it is the lot order agreeing with itself. The column that carries information is **What the report says about it**.

| Method | Seats | Winner(s) | What the report says about it | Read · run |
|--------|-------|-----------|-------------------------------|---|
| STAR | 1 | Ada | Two `[Lot-decided tie — rare]` banners — one for the finalists, one for the runoff — each naming zero support as the cause | [page](cases/cases_pages/zero_support_star.md) · [yaml](cases/zero_support_star.yaml) |
| Bloc STAR | 2 | Ada, Ben | The same pair of banners, **per seat** — four in all | [page](cases/cases_pages/zero_support_bloc_star.md) · [yaml](cases/zero_support_bloc_star.yaml) |
| STAR-PR (Allocated Score) | 2 | Ada, Ben | One banner per seat; the PR ladder's own wording is pre-empted by the zero-support one, which is true on every path | [page](cases/cases_pages/zero_support_star_pr.md) · [yaml](cases/zero_support_star_pr.yaml) |
| Ranked Robin | 1 | Ada | One line: *"5 candidates tie on the highest Copeland score (2) … a **dead heat** (they draw head-to-head, not a cycle)"* | [page](cases/cases_pages/zero_support_ranked_robin.md) · [yaml](cases/zero_support_ranked_robin.yaml) |
| Approval | 1 | Ada | The quietest in the engine — a `Note:` and *"Candidate priority order … broke the tie"*, no banner | [page](cases/cases_pages/zero_support_approval.md) · [yaml](cases/zero_support_approval.yaml) |
| Choose-One (Plurality) | 1 | Ada | The loudest — a banner **and** `, by lot` appended to the winner line itself | [page](cases/cases_pages/zero_support_plurality.md) · [yaml](cases/zero_support_plurality.yaml) |

**page** is the generated report for that case — the whole count, banner wording included; **yaml** is the tabulatable source file you can run yourself:

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/zero_support_election/cases/zero_support_star.yaml
```

Two things worth taking away from that column.

**The banner names the cause, not just the mechanism (2026-08-21).** Until this folder was built, every lot banner on the STAR path ended with the same advice — *"Usually the 'dead rung': no tied candidate held a score-5 vote … Verify the tied candidates' 5-counts."* True of the common case and a wild goose chase here, where no ballot cast a score of anything. A tie among candidates whose best score from anybody is `0` now says so instead: *"had nothing to break it with … every rung was comparing zero with zero … a tie for lack of support, not a close race."* The check is deliberately **per tie, not per election** — see the one-point case below, where an election-level "degenerate" verdict would be wrong about half the result.

**Ranked Robin is the only one that names the SHAPE.** "Dead heat, not a cycle" is a real distinction — five candidates who all draw with each other are tied for a completely different reason than five candidates in a rock-paper-scissors loop, and only one of those two is a scoring failure. The engine's [shared classifier](../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md) is what lets it tell them apart here; the [Smith set](../../07_Concepts/topics/smith_set.md) block says the same thing a second way.

**Approval is the one to watch.** It has the shortest ladder in the library — approvals, then the floor, with no rung in between — so it reaches the lot faster than anything else, and it announces that in the smallest voice. A reader skimming the Approval report sees "Ada — 0 (0%) — Elected" and a note; a reader skimming the Plurality report cannot miss `by lot` sitting in the winner line. Same election, same decision procedure, very different odds that anybody notices. That asymmetry is the general lesson of [the silent tiebreak](../../07_Concepts/topics/ties/silent_tiebreak.md), reproduced here on ballots simple enough to check by eye.

**And a fourth engine declines to answer at all.** This repo cross-checks its Approval counts against Martin Lackner's [`abcvoting`](../../06_Other/abcvoting_tabulation_engine/README.md), which builds its profile out of approval **sets** — so a ballot approving nobody contributes no voter, three such ballots make a profile of length zero, and the library raises *"The given profile contains no voters"* rather than electing anyone. Three ballots were cast; one library counts them and one says there is no election here. Neither is wrong — they are answering different questions, and which question is the right one is a policy choice about what a blank-but-returned ballot means, not a bug in either. It is pinned by a test on purpose ([`test_abcvoting_crosscheck.py`](../../STARVote_LH_tabulation_engine/tests/test_abcvoting_crosscheck.py)), because a cross-check that skipped past its sharpest disagreement would be worth less than no cross-check.

## One point changes everything, and nothing

Change one number — voter 3 gives Ben a `1` — and the same folder produces the case that is genuinely harder to read. That single mark is the only support anybody expresses: **one point out of a possible 75** (3 voters × 5 nominees × 5 points). It settles the first seat outright and changes nothing whatever about the second.

<!-- ballots:one_point_bloc_star -->
The ballots as marked — the filled bubble is the score given, and the score is the number in its column:

| # | Ballot as marked | Ada | Ben | Cleo | Dev | Elsa |
|:--:|:--|:--:|:--:|:--:|:--:|:--:|
| 1 | <img src="cases/img/one_point_bloc_star_ballot_1.png" width="260" style="min-width:260px" alt="A 0–5 STAR ballot — voter 1 — turned out, then scored every nominee 0: Ada 0, Ben 0, Cleo 0, Dev 0, Elsa 0."> | 0 | 0 | 0 | 0 | 0 |
| 2 | <img src="cases/img/one_point_bloc_star_ballot_2.png" width="260" style="min-width:260px" alt="A 0–5 STAR ballot — voter 2 — a deliberate 0 is not a blank ballot: Ada 0, Ben 0, Cleo 0, Dev 0, Elsa 0."> | 0 | 0 | 0 | 0 | 0 |
| 3 | <img src="cases/img/one_point_bloc_star_ballot_3.png" width="260" style="min-width:260px" alt="A 0–5 STAR ballot — voter 3 — one point for Ben, the only mark in the election: Ada 0, Ben 1, Cleo 0, Dev 0, Elsa 0."> | 0 | 1 | 0 | 0 | 0 |
<!-- /ballots -->

Here is what [Bloc STAR](cases/cases_pages/one_point_bloc_star.md) does with it. Seat 1:

```text title="Abridged for the lesson — not verbatim engine output"
Round 1: Automatic Runoff Round
   Ben           -- 1 -- First place
   Ada           -- 0
   Equal Support -- 2
 Ben wins.
   Voters with a preference: 1 of 3 (2 Equal Support).
   Ben 1 (100%) vs Ada 0 (0%); majority = 1.
```

**Every number on that line is correct and the impression it leaves is not.** The decided-voters denominator is doing exactly its job — one voter expressed a preference between the two finalists, and Ben got that voter — so a single point renders as a 100% landslide with a majority of 1. The `2 Equal Support` is the only thing on the line holding the truth, which is why this repo insists the summary [self-reconciles](../../07_Concepts/GLOSSARY.md) rather than printing a bare percentage. Seat 2 then goes to the lot twice over: a four-way lot for the finalists, then a two-way lot for the seat.

That is the reverse of the all-zero six, and it is the more dangerous direction. **An all-zero report looks degenerate, so nobody mistakes it for a mandate; this one looks decisive.**

It is also where the tempting rule breaks. *"Refuse to count an election with nobody supporting anybody"* is easy to state while every score is `0`, and impossible to state here: seat 1 rests on a real preference, however tiny, that a returning officer should report, and seat 2 rests on nothing at all. One election, both answers, and no threshold separates them without being a policy number in disguise. Note the engine's existing [`quorum`](../../07_Concepts/GLOSSARY.md) does not help — it measures *turnout* against eligible voters, so three of three voters turned out and quorum passes while support is ~zero. Wrong axis. A support floor would have to be a separate, opt-in setting that the electing body's own rules choose, not something the tabulator imposes.

So the engine counts it, and the report says per seat which rung paid for it. That is the whole design position of this folder, stated on the one file where it costs something.

## Why there is no BetterVoting election for this

Every other cross-method probe in this folder tree is worth putting on [BetterVoting](https://bettervoting.com) so a reader can click through to a live count. This one is not, and the reason is itself a finding somebody already made: **BetterVoting files a ballot that scores every candidate equally as an abstention**, so all three of these ballots would be dropped before the tally and the race would report zero ballots cast. That is [bettervoting#1508](https://github.com/Equal-Vote/bettervoting/issues/1508), open since 2026-08-09, already reduced to a minimal live repro at [`hb4qvv`](https://bettervoting.com/hb4qvv/results) — so minting a second one here would add a permanent public election and no new information. Tracked with the rest in [upstream bug reports](../../07_Concepts/about_this_repo/upstream_bug_reports.md).

**The one-point case is not exempt from that bug — it is a nastier instance of it,** which is the actual reason it is not minted either. Only ballots 1 and 2 score every candidate the same, so BV would drop those two and keep voter 3, then report **1 ballot cast** where 3 were. The winner would very likely still be Ben, and that is the problem: the all-zero election fails loudly on BV (zero ballots, obviously broken), while this one fails quietly with a plausible winner and a turnout figure short by two thirds. The `2 Equal Support` that makes the runoff line honest is precisely what gets deleted, so BV's version of that line would read `1 of 1` — 100% of everybody, instead of 100% of the one voter who had a preference. A public election that looks right for the wrong reason teaches worse than no election at all.

## Where this came from

These six files are the smallest witness the [coarse-ballot tie sweep](../../07_Concepts/topics/ties/coarse_ballots_and_the_tie_ladder.md) produces for its `X-2` category — *a winner elected with zero support*. The sweep counts a quarter of a million small elections looking for tie shapes the library has no lesson for; this is the shape at the very bottom of it.

## See also

- [Ties & tie-breaking — the topic hub](../../07_Concepts/topics/ties/README.md) · [Ties Are Forced](../../07_Concepts/topics/ties/ties_are_forced.md) · [Why build "silly" tie elections?](../../07_Concepts/topics/ties/why_contrived_tie_cases.md)
- [Flat scores, ties & tie-breaking](../../01_STAR/09_Parked/Flat_scores_ties/README.md) — the same idea one level up: every ballot flat at 5 rather than at 0
- [Tiebreak ladders — every method, every engine](../../07_Concepts/tabulation_engines/tiebreak_ladders.md) — the ladders the table above is walking
- [Abstention vs. zero vs. NOTA](../../01_STAR/01_Learn/properties_and_limits/abstention_vs_zero_vs_nota.md) — why "scored everyone 0" is not "did not vote"
