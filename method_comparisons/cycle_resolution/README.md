# Cycle resolution, counted — where the Condorcet family stops agreeing

The tabulatable evidence behind [Cycle Resolution — why Minimax, Ranked Pairs, and Schulze exist](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md). When a [Condorcet winner](../../00_start_here/topics/condorcet/) exists, **every** Condorcet method elects them and there is nothing to argue about. When majority preference **cycles**, the family splits — and these two elections are the split, made runnable.

Both are **LH-only**: the LH engine's Ranked Robin is Copeland, and in a cycle Copeland usually ties, which LH breaks by margin then lot and BetterVoting breaks *at random*. A tie-deciding result can't be frozen on BV, so these cases stay in the library.

| Case (source) | Ballots | What it shows |
|---|:--:|---|
| [`cycle_copeland_ties_c4_b21.yaml`](cases/cycle_copeland_ties_c4_b21.yaml) | 21 | Copeland ties **Alder, Birch, Cedar** at 2–1 each — the simple count can't pick. All four refined rules then agree on **Alder**, whose only defeat (margin 1) is the mildest in the cycle. |
| [`cycle_schulze_vs_ranked_pairs_c4_b40.yaml`](cases/cycle_schulze_vs_ranked_pairs_c4_b40.yaml) | 40 | The two "serious" cycle-resolvers **disagree outright**: Schulze elects **Ana**, Ranked Pairs elects **Bruno**, on identical ballots. Split Cycle returns **both**, on the grounds that the ballots don't separate them. |
| [`cycle_family_splits_c5_b77.yaml`](cases/cycle_family_splits_c5_b77.yaml) | 77 | Five candidates, Smith set = everyone, no Condorcet winner. **Ranked Pairs alone picks Ben**; Ranked Robin (margin tiebreak), Minimax, Schulze and Stable Voting all pick **Ava**; Split Cycle returns both. Replaces an earlier unsourced "Heitzig" profile — this one is search-built and `pref_voting`-verified. |

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

The `[C1]` / `[C2]` tags are [Fishburn's classification](../../00_start_here/topics/condorcet/condorcet_reading_list.md): C1 rules read only who-beat-whom, C2 rules read the margins too.

Concept pages: [cycle resolution](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md) · [Split Cycle, claim-checked](../../00_start_here/topics/condorcet/split_cycle.md) · [Ranked Robin](../../00_start_here/RCV_Ranked_Robin/ranked_robin.md) · [Smith set](../../00_start_here/topics/smith_set.md) · up: [method_comparisons](../README.md)
