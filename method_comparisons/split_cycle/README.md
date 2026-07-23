# Split Cycle vs. Schulze — a spoiler nobody voted for

The tabulatable evidence behind [Split Cycle — the method that hands the tie back, claim-checked](../../00_start_here/topics/condorcet/split_cycle.md). Holliday & Pacuit ([arXiv:2004.02350](https://arxiv.org/abs/2004.02350); *Public Choice* 197, 2023) claim that among clone-independent methods only **Split Cycle** is immune to spoilers, and that **Schulze** is not. This is that claim, run.

| Case (source) | Ballots | What it shows |
|---|:--:|---|
| [`split_cycle_schulze_spoiler_c5_b40.yaml`](cases/split_cycle_schulze_spoiler_c5_b40.yaml) | 40 | **Cascade beats Bryce 40–0** — not one voter prefers Bryce. Bryce wins nothing, ever. Yet Schulze elects **Cascade** without her on the ballot and **Everglade** with her on it. Split Cycle keeps Cascade in both fields. |

Reproduced independently (this is **not** the paper's own profile — it's the smallest one a `pref_voting` search turned up), and **LH-only**: neither the LH engine nor BetterVoting implements Schulze or Split Cycle, and LH's Copeland result here is a tie.

## Running it

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/cycle_resolution_report.py method_comparisons/split_cycle/cases/split_cycle_schulze_spoiler_c5_b40.yaml
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/cycle_resolution_report.py method_comparisons/split_cycle/cases/split_cycle_schulze_spoiler_c5_b40.yaml --drop Bryce
```

| | Copeland (Ranked Robin) | Minimax | Ranked Pairs | **Schulze** | **Split Cycle** |
|---|---|---|---|---|---|
| **Without Bryce** | Arches, Cascade, Denali | Everglade | Cascade | **Cascade** | **Cascade** |
| **With Bryce** | Cascade, Denali | Everglade | Cascade | **Everglade** | **Cascade, Everglade** |

**Read it fairly** — the lesson page states the limits, and they're real: this needs a five-candidate election with no Condorcet winner and a Smith set of *everyone*; Ranked Pairs isn't convicted by this particular profile; Split Cycle's escape is to return **two** winners, which a public election would then have to break somehow; and the criterion is narrower than IIA — it wouldn't flag [this library's own STAR spoiler case](../../01_STAR/iia_cycle_spoiler/README.md). Nothing here is evidence about STAR or Ranked Robin.

Concept pages: [Split Cycle, claim-checked](../../00_start_here/topics/condorcet/split_cycle.md) · [cycle resolution](../../00_start_here/RCV_Ranked_Robin/cycle_resolution.md) · [Condorcet reading list](../../00_start_here/topics/condorcet/condorcet_reading_list.md) · up: [method_comparisons](../README.md)
