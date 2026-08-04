# Condorcet's 1788 rebuttal to Borda — where the Condorcet criterion comes from

*Borda's pitch (1770) was that his rank-points rule fixed plurality's embarrassment: the plurality winner can lose a direct majority contest to someone else. Condorcet's reply was that Borda's rule has the same disease — and he produced the election that proves it. Both plurality **and** Borda elect Paul here, yet **Peter beats every opponent head-to-head**. This is the argument that became the [Condorcet criterion](../../07_Concepts/topics/condorcet/), and it is also the cleanest demonstration of what [STAR](../../01_STAR/01_Learn/README.md)'s second round is **for**.*

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/khcwm4) · **[results ↗](https://bettervoting.com/khcwm4/results)** (election `khcwm4`, Test ID **BV2250** — three races on the same 11 ballots: STAR, Ranked Robin, RCV-IRV).

→ Related: [Borda count](../../06_Other/other_ranked_methods/borda.md) · [Ranked Robin](../../05_Ranked_Robin/01_Learn/README.md) · [the dark horse](../dark_horse_borda/README.md) (Borda's *strategic* pathology, as opposed to this *sincere* one)

---

## The election

Three candidates and 11 voters. The names are Condorcet's own:

| Voters | Ranking |
|---:|---|
| 4 | Peter > Paul > James |
| 3 | Paul > James > Peter |
| 2 | Paul > Peter > James |
| 2 | James > Peter > Paul |

**Plurality** counts first choices: Paul 5, Peter 4, James 2 → **Paul**.

**Borda** (2 / 1 / 0 points) → **Paul**:

```
Paul  = 4·1 + 3·2 + 2·2 + 2·0 = 14      ← Borda winner
Peter = 4·2 + 3·0 + 2·1 + 2·1 = 12
James = 4·0 + 3·1 + 2·0 + 2·2 =  7
```

**But every head-to-head contest says Peter:**

```
Peter  beats Paul    6 – 5
Peter  beats James   6 – 5
Paul   beats James   9 – 2
```

Peter is the **Condorcet winner** — and neither of the two methods on trial elects him. That is Condorcet's whole point: Borda diagnosed plurality's disease correctly and then caught it himself.

## Where each method lands

| Method | Winner | Elects the Condorcet winner? |
|---|---|---|
| [Choose-One (Plurality)](../../07_Concepts/topics/plurality.md) | Paul | ✗ |
| [**Borda**](../../06_Other/other_ranked_methods/borda.md) | **Paul** | **✗ — Condorcet's target** |
| [Approval](../../04_Approval/01_Learn/README.md) | Paul | ✗ |
| [RCV-IRV](../../06_Other/RCV_IRV/concepts/README.md) | Peter | ✓ |
| [Ranked Robin](../../05_Ranked_Robin/01_Learn/README.md) | Peter | ✓ |
| [STAR](../../01_STAR/01_Learn/README.md) | Peter | ✓ |

**Keep it fair — this is not an IRV failure case.** RCV-IRV gets it right: James is eliminated with 2 first choices, both his ballots transfer to Peter, and Peter wins 6–5 ([`condorcet_1788_irv.md`](cases/cases_pages/condorcet_1788_irv.md)). The methods that miss the Condorcet winner in this particular election are plurality, Borda and approval. (IRV's own Condorcet failures need a [center squeeze](../../06_Other/RCV_IRV/concepts/RCV_IRV_center_squeeze.md), which this profile doesn't contain.) The IRV race is on the live BetterVoting election deliberately, so nobody can accuse the demo of hiding it.

**BetterVoting agrees with the LH engine on all three races** — STAR, Ranked Robin and RCV-IRV each elect Peter, with the same pairwise counts (Peter over Paul 6–5, over James 6–5) and the same first-round IRV elimination of James. The frozen export is [`condorcet_1788_star_bv_export.json`](cases/condorcet_1788_star_bv_export.json).

## The STAR lesson: the scoring round *is* Borda, and then the runoff checks it

Ranks carry no intensity, so running this ranked profile under STAR means converting rank to score — exactly the fabrication the [Borda page](../../06_Other/other_ranked_methods/borda.md) warns about. We use an even 5 / 3 / 0 spacing, and the outcome is robust to the choice (5/4/0, 5/2/0, 5/1/0 and 4/2/0 all behave identically).

That conversion makes the point sharper rather than weaker: **under a uniform spacing, STAR's scoring round is a Borda count.** So STAR's first round reproduces Borda's answer exactly — Paul first — and then the automatic runoff runs the direct majority contest Condorcet demanded:

```text title="Abridged for the lesson — not verbatim engine output"
Scoring Round
   Paul          -- 37 -- First place       ← Borda's winner
   Peter         -- 32 -- Second place
   James         -- 19
 Paul and Peter advance.

Automatic Runoff Round
   Peter         -- 6 -- First place
   Paul          -- 5
   Equal Support -- 0
 Peter wins.
   Voters with a preference: 11 of 11 (no Equal Support).
   Peter 6 (55%) vs Paul 5 (45%); majority = 6.

[Runoff Reversal]
 - Score Round Winner(s) = (Paul)
 - Runoff Round Winner   = (Peter)

[Condorcet Winner]
  Condorcet Winner: Peter — matches the STAR winner

[Divergence from STAR]
  STAR                   = Peter
  Choose-One (Plurality) = Paul   (differs from STAR)
  Approval               = Paul   (differs from STAR)
```
**STAR is Borda's scoring step followed by Condorcet's check** — and on Condorcet's own counterexample to Borda, it returns Condorcet's answer. That two-step shape is STAR's [hybrid nature](../../01_STAR/01_Learn/the_count/STAR_hybrid_nature.md) in one election: the reversal is not a malfunction, it is a 238-year-old objection being answered on screen by the [automatic runoff](../../01_STAR/01_Learn/the_count/STAR_Automatic_Runoff.md).

Want the whole count? See the full LH reports → [`condorcet_1788_star.md`](cases/cases_pages/condorcet_1788_star.md) · [`condorcet_1788_ranked_robin.md`](cases/cases_pages/condorcet_1788_ranked_robin.md).

One more thing the pairwise table shows: **James is the [Condorcet loser](../../07_Concepts/topics/condorcet/)** — he loses every matchup. No method here elects him, but it is worth noticing that Borda ranks him *above* nobody while plurality's 2 first-choice votes are all he has.

## Reproduce it

```bash
.venv/bin/python STARVote_LH_tabulation_engine/starvote_larry_hastings.py method_comparisons/borda_condorcet_1788/cases/condorcet_1788_star.yaml
```

The LH engine has no Borda tabulator, so the Borda figures are cross-checked with [`pref_voting`](../../07_Concepts/tabulation_engines/cross_checking_with_pref_voting.md):

```bash
uv run python -c "
from pref_voting.profiles import Profile
from pref_voting.scoring_methods import borda, plurality
n={'Peter':0,'Paul':1,'James':2}; names=list(n)
rows=[(4,['Peter','Paul','James']),(3,['Paul','James','Peter']),(2,['Paul','Peter','James']),(2,['James','Peter','Paul'])]
P=Profile([tuple(n[c] for c in o) for _,o in rows], rcounts=[c for c,_ in rows])
print('borda scores ->', P.borda_scores())
print('borda        ->', [names[w] for w in borda(P)])
print('plurality    ->', [names[w] for w in plurality(P)])
print('condorcet    ->', names[P.condorcet_winner()])"
```

```
borda scores -> {0: 12, 1: 14, 2: 7}
borda        -> ['Paul']
plurality    -> ['Paul']
condorcet    -> Peter
```

## Notes on the source

The profile is the simplified 11-voter version of an example Condorcet described in **1788**, the form standard textbooks use when they introduce the Condorcet criterion. Condorcet formalized the head-to-head idea in **1785**; Borda had proposed his rank-points rule in **1770**, arguing from an example much like [Pliny the Younger's](../../06_Other/RCV_IRV/concepts/case_studies/RCV_IRV_history.md).

The candidate names are Condorcet's own (Peter / Paul / James) and are kept for fidelity to the source, even though Peter and Paul share an initial — which this repo's [naming rule](../../07_Concepts/tips/TIPS_canonical_elections.md) would otherwise avoid.

## Why Borda misses Peter — the mechanism, not just the result

Condorcet's objection isn't that Borda "got it wrong" here; it's that Borda reads the pairwise numbers through a **sum**, and a sum can be dominated by one lopsided pairing.

Peter's margins: **+1** over Paul, **+1** over James — he wins both, narrowly. Sum: **+2**.
Paul's margins: **−1** to Peter, **+7** over James. Sum: **+6**.

Paul *loses* the only matchup that decides a head-to-head champion, and still finishes ahead on Borda — because crushing James by 7 more than repays losing to Peter by 1. That is the whole disagreement in two lines of arithmetic. Borda asks *how much did you beat people by, on aggregate*; Condorcet asks *did you beat each of them*.

(The margins are exactly what a Borda score is made of: [`Borda(x) = ½·Σ M(x,y) + n(m−1)/2`](../../06_Other/other_ranked_methods/borda.md), and the constant is the same for everyone.)

Which is right is a values question, not a math question — and it's the same fork [Copeland vs Borda margins](../copeland_vs_borda_margins/) makes you choose at, with [the structural version](../../07_Concepts/topics/cycle_cocycle_decomposition.md) underneath. See also [what a method reads](../../07_Concepts/topics/what_a_method_reads.md).
