# Split Cycle — the method that hands the tie back, claim-checked

*Wesley H. Holliday and Eric Pacuit propose a new Condorcet method in ["Split Cycle: A New Condorcet-Consistent Voting Method Independent of Clones and Immune to Spoilers"](https://arxiv.org/abs/2004.02350) (arXiv:2004.02350; **Public Choice** 197, 1–62, 2023). The claim is specific and checkable: among clone-independent methods, **only** Split Cycle also satisfies a criterion they define called* immunity to spoilers, *plus positive and negative involvement. So we ran it — and built an election where the older, better-known Schulze method gets spoiled by a candidate that* not one voter *ranks above the winner.*

**Level 301.** Prerequisite: [cycle resolution](../../RCV_Ranked_Robin/cycle_resolution.md) (why Minimax, Ranked Pairs and Schulze exist at all). Where this sits in the family: [the Condorcet reading list](condorcet_reading_list.md) puts it in **Fishburn's C2 tier** — rules that read the pairwise *margins*, not just who-beat-whom.

**Set expectations first.** Split Cycle has been adopted by no jurisdiction and is on no ballot measure. Neither STAR nor Ranked Robin is affected by anything on this page — neither is a C2 method. This page is here because the paper is **the clearest modern statement of what the older cycle rules actually do**, and because its central counterexample is the kind of claim this library exists to run rather than repeat.

---

## The rule, in one sentence

> **In every cycle of majority defeats, discard that cycle's weakest defeat. Elect whoever is left undefeated.**

That's it. When a [Condorcet winner](README.md) exists, nothing is discarded and Split Cycle elects them, like every other Condorcet method. When preferences cycle, the weakest link in each loop is treated as the one the electorate is least sure about, and dropped.

Two consequences follow immediately, and both matter:

1. **Split Cycle can return more than one winner.** If discarding leaves two candidates undefeated, it reports both. This is deliberate: the authors' position is that the ballots did not separate them, and a method that names one anyway is applying a convention, not reading the voters.
2. **Its winner set contains Schulze's and Ranked Pairs'.** Split Cycle never contradicts them — it declines to narrow. Every disagreement between Split Cycle and those two is Split Cycle saying "you broke a tie I don't think the ballots break."

Worked side by side against the other rules, on a 40-voter cycle where Schulze says Ana and Ranked Pairs says Bruno: [cycle resolution](../../RCV_Ranked_Robin/cycle_resolution.md).

## The claim we checked: "immunity to spoilers"

This is the paper's new criterion, and it is much **narrower** than the everyday phrase — read the definition before using the term:

> **Immunity to spoilers** *(the paper's informal statement)*: if `a` would win without `b` in the election, and **more voters prefer `a` to `b` than prefer `b` to `a`**, then it is not the case that when `b` joins, both `a` and `b` lose.

The formal version (their Definition 4.1) says `b` **spoils** the election for `a` when all four of these hold: `a` wins without `b`; the margin of `a` over `b` is positive; `a` does not win with `b` present; and `b` does not win either. The companion notion — `b` *steals* from `a` when `b` itself wins — combines with it into **stability for winners**, which Split Cycle satisfies and Schulze and Ranked Pairs do not.

**The majority-preference clause is load-bearing**, and it's why the criterion is defensible rather than absurd: if most voters prefer the newcomer to `a`, then `b` may quite legitimately cost `a` the win. Only the *perverse* case is ruled out — where the newcomer loses to `a` head-to-head and still knocks them out.

## The counterexample, tabulated

The paper proves Schulze fails this (their Proposition 4.10). Rather than transcribe their profile, we searched for our own with `pref_voting` and took the smallest one found: **40 voters, five national parks.**

→ **[the case file](../../../method_comparisons/split_cycle/cases/split_cycle_schulze_spoiler_c5_b40.yaml)** · [folder](../../../method_comparisons/split_cycle/README.md)

```
11 : Everglade > Denali > Cascade > Bryce > Arches
11 : Arches > Denali > Cascade > Everglade > Bryce
10 : Cascade > Bryce > Arches > Denali > Everglade
 8 : Everglade > Cascade > Bryce > Arches > Denali
```

**Cascade beats Bryce 40–0.** Every single voter ranks Cascade above Bryce. Bryce wins under no method in any field — she is, by any ordinary meaning of the word, irrelevant.

Now run the two fields:

| | Copeland (Ranked Robin) | Minimax | Ranked Pairs | **Schulze** | **Split Cycle** |
|---|---|---|---|---|---|
| **Without Bryce** | Arches, Cascade, Denali | Everglade | Cascade | **Cascade** | **Cascade** |
| **With Bryce** | Cascade, Denali | Everglade | Cascade | **Everglade** | **Cascade, Everglade** |

**Schulze flips from Cascade to Everglade** because Bryce joined — and Bryce doesn't win, and no voter prefers her to Cascade. That is a spoiler by the paper's definition, exactly as claimed. **Split Cycle keeps Cascade in both fields**, so no spoiler effect occurs — that is stability for winners doing its job.

Reproduce both rows:

```bash
uv run STARVote_LH_tabulation_engine/tools_adam/pref_voting_tabulation_engine/cycle_resolution_report.py method_comparisons/split_cycle/cases/split_cycle_schulze_spoiler_c5_b40.yaml --drop Bryce
```

(Drop the `--drop Bryce` for the full field. The [LH engine](../../tabulation_engines/LH_starvote/) runs only the Copeland column — that's Ranked Robin — so the case's `_tabulated` mirror shows the pairwise matrix and a Copeland tie, and `pref_voting` supplies the rest.)

## Reading it fairly — four things the case does *not* show

The repo's [reading-these-fairly discipline](../../../method_comparisons/paradoxes_and_whoops/reading_these_fairly.md) applies to arguments we find *congenial* too, and this one flatters a method we don't teach:

1. **It needs a knotted election.** Five candidates, no Condorcet winner, and a Smith set containing *every* candidate. Cycles are rare to begin with; cycles this tangled are rarer. A criterion failure that requires this much structure is a real defect but not an everyday risk.
2. **Ranked Pairs is not convicted here.** On this profile Ranked Pairs elects Cascade in both fields. The paper proves it fails the criterion too (Proposition 4.12), on a different profile we did not reproduce — so treat that as cited, not demonstrated.
3. **The price is real.** Split Cycle avoids the spoiler by *returning two winners* in the full field. A public election needs one name, so a real deployment would bolt a tiebreak onto the back — and whatever that tiebreak is, it inherits the properties Split Cycle just refused to assume. "Immune to spoilers" is a property of the set, not of whatever picks from it.
4. **Immunity to spoilers is not IIA.** The criterion says nothing about cases where the majority *prefers the newcomer*. This library's sharpest [STAR spoiler case](../../../01_STAR/iia_cycle_spoiler/README.md) — where deleting Ben flips STAR from Alice to Carla — is **not** a violation of it, because Ben beats Carla head-to-head. Split Cycle's criterion would not have flagged our own best example. That's a limit worth stating plainly, in both directions.

## Does any of this touch STAR or Ranked Robin?

No, and it's worth being explicit about why, because "Condorcet method fails a criterion" arguments get recycled loosely:

- **Ranked Robin** is Copeland — a **C1** method that reads only who-beat-whom, with a margins tiebreak. It is not Schulze and does not inherit Schulze's failure. Its own honest limits are [documented separately](../../RCV_Ranked_Robin/RCV_RR_honest_limits.md).
- **STAR** is not a Condorcet method at all ([why](../../STAR_Voting/properties_and_limits/STAR_three_winner_notions.md)), so a criterion defined over pairwise margins in a cycle isn't the right lens. STAR's analogous weakness is a different one, tabulated at [the IIA cycle spoiler](../../../01_STAR/iia_cycle_spoiler/README.md).

What the paper *does* offer this library is precision. It is the clearest available account of the difference between "the ballots chose" and "the rule chose," and that distinction — not Split Cycle the method — is the part worth teaching.

## Related

- [Cycle resolution](../../RCV_Ranked_Robin/cycle_resolution.md) — Minimax / Ranked Pairs / Schulze / Split Cycle, with the disagreement case
- [Condorcet reading list](condorcet_reading_list.md) — where this paper sits, and the C1/C2/C3 taxonomy
- [Topic: Condorcet efficiency](README.md) · [Smith set](../smith_set.md) · [clone independence](../../RCV_Ranked_Robin/rr_clone_independence.md)
- The arguments *against* privileging the Condorcet winner: [Edelman, tabulated](edelman_condorcet_myth.md) · [ordered majority rule](ordered_majority_rule_irv.md)
- [Cross-checking with pref_voting](../../tabulation_engines/cross_checking_with_pref_voting.md)
