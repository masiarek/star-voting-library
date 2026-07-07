# Felsenthal Example 6 — Approval can elect a Pareto-dominated candidate (LH-only)

**No BetterVoting election on purpose:** the paradox turns on a *random* Aria/Beau tie, and a random BV result can't be frozen into a repeatable case — the same reason as the [RR tiebreak study](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md). This is an LH-only reference pair.

## Source

Dan S. Felsenthal, *"Review of Paradoxes Afflicting Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be Elected"*, University of Haifa / LSE, revised 26 May 2010; Appendix §A3, **Example 6** — due to **Felsenthal & Maoz (1988: 123, Example 4)**.

## The election

3 voters, four candidates, each approving their top **three**:

```
Voter    Ranking                        Approves
  1      Aria > Beau > Cole > Dean      {Aria, Beau, Cole}
  2      Cole > Aria > Beau > Dean      {Cole, Aria, Beau}
  3      Dean > Aria > Beau > Cole      {Dean, Aria, Beau}
```

Approval totals: **Aria 3, Beau 3**, Cole 2, Dean 1 — an Aria/Beau tie. Broken randomly, there is a 0.5 chance **Beau** is elected. But *every single voter* prefers Aria to Beau: Aria **Pareto-dominates** Beau (and is the Condorcet winner — beats Beau 3–0, Cole 2–1, Dean 2–1). A method that can elect Beau here can elect a candidate *unanimously* considered worse than an available alternative — the Pareto-dominated paradox. The top-three cutoff is the culprit: it puts Aria and Beau in the same approval bucket on all three ballots, erasing a unanimous preference.

## The LH pair

[felsenthal_ex6_pareto_approval.yaml](felsenthal_ex6_pareto_approval.yaml) pins the lot order **adversarially** (`[Beau, Aria, Cole, Dean]`) to exhibit exactly the branch Felsenthal warns about — the LH echo shows the 3–3 tie resolving to **Beau**, the Pareto-dominated candidate. (This required a small engine fix: the Approval path now honors `lot_numbers`, where it previously fell back to ballot column order.) The companion [felsenthal_ex6_ranked_robin.yaml](felsenthal_ex6_ranked_robin.yaml) counts the same rankings pairwise and elects **Aria** outright.

Mirrors: [approval](felsenthal_paradoxes_tabulated/felsenthal_ex6_pareto_approval_tabulated.txt) · [rr](felsenthal_paradoxes_tabulated/felsenthal_ex6_ranked_robin_tabulated.txt). Tag: `pareto` in the [paradox registry](../../00_start_here/YAML_test_case_index/PARADOX_index.md).
