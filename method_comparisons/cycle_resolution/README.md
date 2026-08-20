# Cycle resolution, counted — where the Condorcet family stops agreeing

The tabulatable evidence behind [Cycle Resolution — why Minimax, Ranked Pairs, and Schulze exist](../../05_Ranked_Robin/01_Learn/cycle_resolution.md). When a [Condorcet winner](../../07_Concepts/topics/condorcet/README.md) exists, **every** Condorcet method elects them and there is nothing to argue about. When majority preference **cycles**, the family splits — and these elections are the split, made runnable.

All are **LH-only**: the LH engine's Ranked Robin is Copeland, and in a cycle Copeland usually ties. LH breaks that tie by Ranked Robin's published [degrees of ties](../../05_Ranked_Robin/03_Criteria/rr_tiebreaks/degrees_of_ties.md) — 1st Degree (margins among the finalists), then 2nd Degree (margins over the field), then lot — while BetterVoting has a rung only for a *two-way* tie and sends anything larger to a seeded shuffle nobody can derive from the ballots. A tie decided that way can't be frozen on BV, so these cases stay in the library.

**Two of the Ranked Robin winners on this page changed on 2026-08-19**, when the engine gained the 1st Degree rung it had been missing; both were two-way ties in which the old engine elected the candidate who had lost the finalists' own match. The rows below are current.

The last two rows are one election counted twice — 999 ballots converted from an outside engine's published cast vote record, which is why they break this folder's usual keep-it-small rule. See [RCV Lab](../../07_Concepts/tabulation_engines/rcv_lab.md) for where the data came from and what was verified against it.

| Case (source) | Ballots | What it shows |
|---|:--:|---|
| [page](cases/cases_pages/cycle_copeland_ties_c4_b21.md) · [`cycle_copeland_ties_c4_b21.yaml`](cases/cycle_copeland_ties_c4_b21.yaml) | 21 | Copeland ties **Alder, Birch, Cedar** at 2–1 each — the simple count can't pick. All four refined rules then agree on **Alder**, whose only defeat (margin 1) is the mildest in the cycle. |
| [page](cases/cases_pages/cycle_schulze_vs_ranked_pairs_c4_b40.md) · [`cycle_schulze_vs_ranked_pairs_c4_b40.yaml`](cases/cycle_schulze_vs_ranked_pairs_c4_b40.yaml) | 40 | The two "serious" cycle-resolvers **disagree outright**: Schulze elects **Ana**, Ranked Pairs elects **Bruno**, on identical ballots. Split Cycle returns **both**, on the grounds that the ballots don't separate them. Copeland ties Ana and Bruno too; Ranked Robin's 1st Degree reads their own match — Bruno by 4 — and sides with Ranked Pairs. *(It said Ana until 2026-08-19.)* |
| [page](cases/cases_pages/cycle_family_splits_c5_b77.md) · [`cycle_family_splits_c5_b77.yaml`](cases/cycle_family_splits_c5_b77.yaml) | 77 | Five candidates, Smith set = everyone, no Condorcet winner. Minimax, Schulze and Stable Voting pick **Ava**; **Ranked Pairs picks Ben**, and so does Ranked Robin — Copeland ties the two at three wins, and the 1st Degree reads the match they played, which Ben won 40–37. Split Cycle returns both. *(Ranked Robin said Ava until 2026-08-19: Ava's whole-field margin is +76 to Ben's +24, which is the 2nd Degree question and not the one the protocol asks first.)* Replaces an earlier unsourced "Heitzig" profile — this one is search-built and `pref_voting`-verified. |
| [page](cases/cases_pages/cycle_vote_on_the_rule_rr_c5_b999.md) · [`cycle_vote_on_the_rule_rr_c5_b999.yaml`](cases/cycle_vote_on_the_rule_rr_c5_b999.yaml) | 999 | **The candidates are the cycle-breaking rules, and the ballots cycle.** Minimax, Ranked Pairs, Schulze, Split Cycle, Stable Voting and RCV-IRV are *unanimous* for **Ranked Pairs** — Schulze and Minimax each voting for a rival over itself. Only **Copeland's Rule** can't decide (all three go 3–1), so Ranked Robin's 1st Degree tiebreak lands on **Schulze Method** instead (+103 among the three finalists). Converted from [RCV Lab's](../../07_Concepts/tabulation_engines/rcv_lab.md) published CVR. |
| [page](cases/cases_pages/cycle_vote_on_the_rule_irv_c5_b999.md) · [`cycle_vote_on_the_rule_irv_c5_b999.yaml`](cases/cycle_vote_on_the_rule_irv_c5_b999.yaml) | 999 | The same ballots as an RCV-IRV count, kept as the fidelity check: every tally reproduces [RCV Lab's](../../07_Concepts/tabulation_engines/rcv_lab.md) published report. Winner **Ranked Pairs** on 492 — a majority of the 886 ballots still live, and 49.2% of the 999 cast. |

## Running them

The LH engine tabulates the Copeland/Ranked Robin column and writes the `_tabulated` mirror:

```bash
python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/cycle_resolution/cases/cycle_schulze_vs_ranked_pairs_c4_b40.yaml
```

The other five rules have no LH implementation. This repo tool prints them all at once, via `pref_voting`:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/cycle_resolution_report.py method_comparisons/cycle_resolution/cases/cycle_schulze_vs_ranked_pairs_c4_b40.yaml
```

```
Pairwise margins (winner's margin over loser):
   Bruno beats Ana by 4
   Ana beats Chloe by 18
   Ana beats Diego by 12
   Bruno beats Chloe by 18
   Diego beats Bruno by 10
   Chloe beats Diego by 12

Condorcet winner: NONE — majority preference cycles.
Smith set: Ana, Bruno, Chloe, Diego

Winners by method:
   Copeland (= Ranked Robin)  [C1]  Ana, Bruno
   Minimax                    [C2]  Ana
   Ranked Pairs               [C2]  Bruno
   Schulze (beat path)        [C2]  Ana
   Split Cycle                [C2]  Ana, Bruno
   Stable Voting              [C2]  Ana
```

The `[C1]` / `[C2]` tags are [Fishburn's classification](../../07_Concepts/topics/condorcet/condorcet_reading_list.md): C1 rules read only who-beat-whom, C2 rules read the margins too.

Concept pages: [cycle resolution](../../05_Ranked_Robin/01_Learn/cycle_resolution.md) · [Split Cycle, claim-checked](../../07_Concepts/topics/condorcet/split_cycle.md) · [Ranked Robin](../../05_Ranked_Robin/01_Learn/ranked_robin.md) · [Smith set](../../07_Concepts/topics/smith_set.md) · up: [method_comparisons](../README.md)
