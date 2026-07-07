# BV2145 — Felsenthal Example 2 (1 of 2): the runoff eliminates the Condorcet winner

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/6fj2kg) · **[results ↗](https://bettervoting.com/6fj2kg/results)** (election `6fj2kg`).

17 voters, three candidates. Ada beats *both* rivals head-to-head — yet the plurality-with-runoff procedure eliminates her before the runoff even starts, and Ben wins. Three races on the same ranked electorate show the contrast: Runoff/IRV → **Ben**; Ranked Robin → **Ada**; STAR → **Ada**. Part 2 ([BV2146](bv2146_krk2px_felsenthal_ex2_monotonicity.md)) adds the non-monotonicity twist.

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010 (Leverhulme Trust *Voting Power in Practice* workshop, Château du Baffy, Normandy). Appendix §A2 ("Demonstrating Paradoxes Afflicting the Plurality with Runoff Procedure"), **Example 2**. Felsenthal lists this procedure as vulnerable to the Condorcet winner, lack-of-monotonicity, reinforcement, no-show, twin, and SCC paradoxes; this example demonstrates the Condorcet winner, non-monotonicity (part 2), and SCC.

## The election

17 voters rank three candidates (Felsenthal's *a, b, c* → cast as **Ada, Ben, Cleo**):

```
No. of voters    Preference ordering
      3          Ada  > Ben  > Cleo
      2          Ada  > Cleo > Ben
      4          Ben  > Ada  > Cleo
      2          Ben  > Cleo > Ada
      4          Cleo > Ada  > Ben
      2          Cleo > Ben  > Ada
```

Head-to-head: **Ada beats Ben 9–8** and **Ada beats Cleo 9–8** — Ada is the Condorcet winner, and the full social ordering is Ada > Ben > Cleo (Ben beats Cleo 9–8). But first choices are **Ada 5, Ben 6, Cleo 6** — Ada is last on the first count.

With three candidates, plurality-with-runoff and RCV-IRV are the same procedure: eliminate the first-count loser, then a head-to-head between the survivors. The BV race is therefore an IRV race.

## The paradoxes

The **[Condorcet winner paradox](../../00_start_here/voting_paradoxes/condorcet_winner_paradox.md)**: the runoff eliminates Ada on first choices, and Ben beats Cleo 9–8. The electorate's pairwise favorite never reaches the runoff — the same center-squeeze mechanism as [BV2137](../center_squeeze_bv2137/bv2137_ywckmg_center_squeeze.md), at Felsenthal's minimal scale.

The **[SCC / spoiler](../../00_start_here/voting_paradoxes/spoiler_scc.md)** (conditional): had Cleo withdrawn before the vote, Ada would have won the *first* round outright — 9 of 17 first choices, a majority. Cleo can't win, but her presence hands the election to Ben.

## View 1 — BetterVoting

Live results: **[bettervoting.com/6fj2kg/results ↗](https://bettervoting.com/6fj2kg/results)**. BV elects **Ben** (IRV), **Ada** (Ranked Robin), **Ada** (STAR) — matching the LH engine on all three races, no tiebreaks anywhere.

## View 2 — LH engine

Runoff/IRV race ([bv2145_6fj2kg_irv.yaml](bv2145_6fj2kg_irv.yaml)):

```
 Tabulating 17 ballots (ranked ballots).

ROUND 1
Candidate      Votes  Status
-----------  -------  --------
Ben                6  Hopeful
Cleo               6  Hopeful
Ada                5  Rejected

FINAL RESULT
Candidate      Votes  Status
-----------  -------  --------
Ben                9  Elected
Cleo               8  Rejected
Ada                0  Rejected

Winner(s) — RCV / Instant-Runoff Voting (single winner)
  Ben
```

Ranked Robin ([bv2145_6fj2kg_ranked_robin.yaml](bv2145_6fj2kg_ranked_robin.yaml)) elects **Ada** — 2 pairwise wins (9–8, 9–8), the Condorcet winner. STAR ([bv2145_6fj2kg_star.yaml](bv2145_6fj2kg_star.yaml)) with the 5/3/1 rank→score map: **Ada 53, Ben 51, Cleo 49**; Ada wins the automatic runoff **9–8**. Full detail: [IRV mirror](felsenthal_paradoxes_tabulated/bv2145_6fj2kg_irv_tabulated.txt) · [RR mirror](felsenthal_paradoxes_tabulated/bv2145_6fj2kg_ranked_robin_tabulated.txt) · [STAR mirror](felsenthal_paradoxes_tabulated/bv2145_6fj2kg_star_tabulated.txt).

## Agreement

| Race | BetterVoting | LH engine | Agree? |
|---|---|---|---|
| Runoff (IRV) | Ben | Ben | ✓ |
| Ranked Robin | Ada | Ada | ✓ |
| STAR (ranks→scores) | Ada | Ada | ✓ |

Frozen export: [bv2145_6fj2kg_bv_export.json](bv2145_6fj2kg_bv_export.json) · Part 2: [BV2146 — the non-monotonicity flip](bv2146_krk2px_felsenthal_ex2_monotonicity.md).
