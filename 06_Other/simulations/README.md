# Simulations — measure it, don't guess it

This folder holds brute-force simulations that **measure** a claim instead of citing a number we can't defend. Two rules — each a 301-level lesson in its own right: **always report the model and parameters with any number**, and **never let an arbitrary tiebreaker silently inflate a result**. A third, more foundational one — **sample voter *utilities* and derive each ballot from them; never draw random ballots** — is why every script here starts from `sample_utilities()`: [Simulate utilities, not ballots](../../00_start_here/topics/simulate_utilities_not_ballots.md).

- **Favorite-Betrayal (FBC)** — `fbc_simulation.py` (below).
- **Runoff Reversal frequency** — `runoff_reversal_simulation.py` ([jump to section](#runoff-reversal-frequency-simulation)).
- **STAR vs Approval divergence** — `star_vs_approval_divergence.py`: how often sincere STAR and Approval elect *different* winners (spoiler: no single number — it depends on the electorate model and the approval cutoff). Full writeup + measured rates + worked examples: [How often do STAR and Approval disagree?](../../method_comparisons/star_vs_approval_divergence.md).

## Favorite-Betrayal (FBC) simulation

`fbc_simulation.py` measures, by brute force over many random elections, how often **STAR** and **RCV-IRV** actually satisfy the **Favorite Betrayal Criterion (FBC)** — and how often a favorite-betrayal vote pays off vs backfires.

## Why this exists

The debate doc once claimed STAR is *"~98% favorite-betrayal-proof."* That number had **no defensible source**: Equal Vote's criteria chart is binary pass/fail (STAR gets a ❌), and the ~91–98% figure that floats around is **Voter Satisfaction Efficiency** — an *accuracy* metric, a different thing entirely. Rather than cite a number we can't defend, this script **measures** one — and reports the modelling assumptions, because the result swings hugely with them.

## What it measures

1. **FBC-compliance frequency.** For each random election, compute the sincere STAR (or IRV) winner `W`. Then for every voter ask: holding everyone else sincere, is there *any* ballot in which they do **not** keep their true favorite (co-)top — a real betrayal — that elects someone they sincerely prefer to `W`? If even one voter has such a ballot, the election **fails** FBC. The betrayal search is **exhaustive** (every 0–5 ballot for STAR, every ranking for IRV), so this is a true best-response test, not a heuristic.

2. **Works : backfires ratio.** Over every `(voter, betrayal ballot)` pair, count how many strictly **help** the voter vs strictly **hurt** them (by sincere utilities). Reported per method. This is the brute-force cousin of Equal Vote's "honesty" stat — note it counts *all possible* betrayals, so it is a superset of the realistic strategies a real faction would attempt (read it as "if you betray blindly, how often does it pay?").

### Electorate models (both run by default)
- **spatial** — voters & candidates are points in issue space; utility = −distance. The realistic model (what [VSE / Bayesian Regret](../../00_start_here/topics/what_makes_a_good_winner.md#measuring-it-empirically-vse-bayesian-regret) uses).
- **impartial** — each utility is uniform[0,1], independent. An adversarial stress test that manufactures far more paradoxes; treat its FBC rate as a rough lower bound.

Sincere ballots are derived deterministically: STAR scores = per-voter min-max scaling of utilities onto 0–5; IRV ranks candidates by utility. Tie-breaks are fixed and documented in the script header. Everything is seeded (`--seed`).

## Running it

```bash
python3 fbc_simulation.py                 # default sweep, both models
python3 fbc_simulation.py --selftest      # known-answer checks only
python3 fbc_simulation.py --elections 3000 --voters 41 --candidates 3 --seed 7
```

`--selftest` confirms the tabulators are correct on known cases (clear STAR winner; a center-squeeze where IRV eliminates the center and STAR elects it).

## Representative results

3 candidates, 2-D spatial / impartial, seeded. (FBC % = elections with **no** profitable favorite betrayal; ratio = help : hurt over all betrayal ballots.)

| model | voters | STAR FBC % | RCV-IRV FBC % | STAR works:backfires | IRV works:backfires |
|-------|:---:|:---:|:---:|:---:|:---:|
| spatial   | 15 | 91.9% | 95.5% | 0.02 : 1 | 0.07 : 1 |
| spatial   | 41 | 96.2% | 97.2% | 0.02 : 1 | 0.13 : 1 |
| impartial | 15 | 79.4% | 89.6% | 0.04 : 1 | 0.08 : 1 |
| impartial | 41 | 80.8% | 90.8% | 0.04 : 1 | 0.09 : 1 |

## What this means for the "98%" claim

1. **"98%" is not reproducible as a distinctive STAR FBC property.** Under the realistic spatial model STAR lands in the low-to-mid 90s%; under impartial culture, ~80%. It is never a clean "98%."

2. **Both methods fail FBC at broadly similar low rates** by this existence test — and, on raw existence, STAR is *slightly worse* than IRV, not better. The reason is mechanical: FBC is an *existence* criterion, and STAR's score ballot offers ~36× more betrayal ballots (216 vs a handful of rankings) — more lottery tickets to find one that helps, even though almost none do. So **"STAR fails FBC less often than IRV" is not supported**; the honest statement is "neither is favorite-betrayal-proof."

3. **The real, robust difference is that betrayal reliably backfires in STAR.** Across every run, a STAR favorite-betrayal is far more likely to hurt the voter than an IRV one (STAR ~0.02–0.04 : 1 vs IRV ~0.07–0.13 : 1 help : hurt). That is the measurable version of "honest voting is your safest bet in STAR" — and it's the claim to make, instead of a bare percentage.

(Magnitudes here are **not** directly comparable to Equal Vote's published ~1:1 STAR vs ~3:1 IRV, which uses a realistic strategic-faction model, not an exhaustive ballot search. Only the *direction* — STAR less rewardingly manipulable — is shared.)

## Caveats (read before quoting)

- Small candidate field (default 3) — where center squeeze / favorite betrayal lives, but not the whole story.
- FBC tested for an **individual** pivotal voter, not a coordinated bloc; center squeeze in real polarized races is partly a bloc phenomenon.
- The works:backfires denominator includes every possible betrayal, so it understates how often a *well-chosen* strategy pays (and is not Quinn's VSE pipeline).
- Results are model-dependent. **Always report the model and parameters with the number.**

---

## Runoff Reversal frequency simulation

`runoff_reversal_simulation.py` measures how often a **Runoff Reversal** happens — the Scoring-Round leader losing the Automatic Runoff (the phenomenon taught in [Runoff Reversal](../../01_STAR/runoff_overturns_leader/)).

### Why this exists

A simulation once reported *"16.9% divergence"* under Impartial Culture with 5 candidates and **10 ballots**. That number is reproducible — and, on its own, misleading. This script makes three hidden assumptions visible:

1. **The model is white noise.** Impartial Culture makes every score independent and uniform, so `5,5,5,5,5` is as likely as a realistic ballot. Real electorates are *correlated*, and correlation makes the score leader and the majority winner agree far more often — so the realistic reversal rate is much lower.
2. **10 ballots is mostly ties.** At that size ~24% of elections have a tie for the top-two-by-score and ~14% have a tied runoff — nearly **40% are tie-ambiguous**.
3. **An arbitrary tiebreaker inflated the count.** The original picked the "score winner" by alphabetical order but broke STAR ties by *reverse* alphabetical order; when those two arbitrary rules disagreed it was logged as a "divergence." The genuine clean-reversal rate at that size is ~9–10%, not 17%.

### What it measures

Each election lands in exactly one of four buckets, so ties are **counted, not hidden**: `reversal` (clean), `runoff_tie`, `finalist_score_tie`, `no_reversal`. Two electorate models run by default — **impartial** (white-noise stress test) and **spatial** (realistic, correlated). Everything is seeded; `--selftest` checks the classifier on hand-built reversal / no-reversal / tie cases.

### Running it

```bash
python3 runoff_reversal_simulation.py --selftest
python3 runoff_reversal_simulation.py --elections 300000 --voters 21 --candidates 5
```

### Representative results (5 candidates, seed 42)

| model | voters | clean reversal | runoff tie | finalist score tie | no reversal |
|-------|:---:|:---:|:---:|:---:|:---:|
| impartial | 10  | 9.5%  | 14.3% | 23.6% | 52.6% |
| spatial   | 10  | 6.2%  | 12.2% | 14.0% | 67.6% |
| impartial | 21  | 13.2% | 11.0% | 16.8% | 59.0% |
| spatial   | 21  | 8.7%  | 6.2%  | 7.2%  | 77.9% |
| impartial | 101 | 18.6% | 5.7%  | 8.1%  | 67.5% |
| spatial   | 101 | 9.0%  | 1.8%  | 1.6%  | 87.7% |

### What this means

1. **There is no single "reversal rate."** It depends on the model (impartial ≈ 2× spatial) and on electorate size (it *rises* as ties vanish with more voters).
2. **Report the model.** Under the realistic spatial model with a real electorate (101 voters), clean Runoff Reversals are ~9% — not the ~17% the 10-ballot toy setup implied.
3. **It's still common enough to matter.** Even on the conservative spatial model it's ~1 election in 11 — which is exactly *why* Runoff Reversal is worth teaching. The runoff isn't catching a rare freak case; it's a regular, deliberate correction.

### Caveats (read before quoting)

- Sincere ballots only — no strategy.
- Spatial model is 2-D uniform; real issue spaces are lumpier (clusters, polarization).
- "Reversal" here is score-leader-vs-runoff only; it says nothing about the Condorcet winner (see [Three notions of "winner"](../../00_start_here/STAR_Voting/properties_and_limits/STAR_three_winner_notions.md)).
- **Always report the model, the size, and the tie split with the number.**

---

## STAR vs Ranked Robin divergence simulation

`star_vs_rr_divergence.py` — how often, and *why*, do STAR and [Ranked Robin](../../00_start_here/RCV_Ranked_Robin/README.md) (Copeland / Condorcet) elect different single winners?

### The mechanism

Same voter utilities feed both: STAR reads 0–5 **scores** (top-two by sum → pairwise runoff); RR reads the **ranking** (most head-to-head wins). A Condorcet winner who *reaches* STAR's runoff wins it (they beat any finalist head-to-head), so **STAR ≠ RR requires either a Condorcet *cycle*, or the Condorcet winner *missing* the score-based top-two** — a broadly-preferred but low-intensity compromise, everyone's tepid second choice. It is the [preference-vs-support](../../00_start_here/scores_and_ranks/preference_vs_support.md) split made statistical: RR rewards *order*, STAR rewards *how much* support each candidate has.

### Running it

```
uv run 06_Other/simulations/star_vs_rr_divergence.py --trials 3000
```

### Representative results (3000 trials/cell, seed 20260721)

| model | C | V | STAR≠RR | of which: cycle | of which: CW-missed-runoff |
|-------|:--:|:--:|:--:|:--:|:--:|
| **noise** | 3 | 51 | 14.5% | 8.5% | 1.0% |
| noise | 5 | 51 | 27.0% | 24.8% | 3.6% |
| noise | 10 | 51 | 34.7% | 47.2% | 3.2% |
| **spatial** | 3 | 51 | 3.9% | 0.3% | 0.1% |
| spatial | 3 | 501 | **1.2%** | 0.1% | 0.0% |
| spatial | 10 | 15 | 28.5% | 13.1% | 6.1% |
| spatial | 10 | 501 | 10.3% | 0.8% | 3.0% |
| **faction** | 3 | 501 | 1.7% | 0.9% | 0.1% |
| faction | 7 | 501 | 10.9% | 5.0% | 4.3% |
| faction | 10 | 501 | 14.8% | 7.9% | 5.2% |

### What this means

1. **Two completely different regimes.** Under **random noise**, divergence is high but almost entirely **cycle-driven** — cycles explode with candidate count (3→8%, 10→48%), and both methods are merely resolving an electorate with no real winner. Under **spatial / factional** models, cycles are rare (a centrist Condorcet winner usually exists), and the divergence that occurs is the *meaningful* kind: the compromise CW squeezed out of the score top-two.
2. **More candidates → more divergence, always.** With 2 candidates STAR = RR by definition; the gap widens monotonically with the field size in every model.
3. **Ballots cut opposite ways by model.** More voters *shrink* divergence under spatial/factional electorates (sampling noise fades, the structure dominates → the two methods converge on the centrist), but leave it roughly flat under pure noise. So **"fewer ballots → more divergence" is a property of *structured* electorates, not random ones.**
4. **Factions are where the real disagreement lives.** Factional/spatial models produce *lower* total divergence than noise, but a *higher share of it is the dark-horse mechanism* (CW-missed-runoff, 5–8% at 10 candidates) — polarized voters score the compromise centrist low, so RR's Condorcet winner never reaches STAR's runoff. That is the honest STAR-vs-RR philosophical disagreement (support vs. order), not a coin-flip electorate.

### Caveats (read before quoting)

- Sincere, **normalized** 0–5 scores (each voter min-maxes their utilities). Real voters don't perfectly normalize; different scoring assumptions move the numbers.
- RR = Copeland with a lowest-index tiebreak; LH breaks Copeland ties by margin then lot, so a knife-edge cell may differ slightly from the engine.
- "Divergence" counts *any* different winner, including ties resolved differently — report the model, size, and mechanism split with the number.
