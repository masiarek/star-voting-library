# Simulations — measure it, don't guess it

This folder holds brute-force simulations that **measure** a claim instead of citing a number we can't defend. Two rules — each a 301-level lesson in its own right: **always report the model and parameters with any number**, and **never let an arbitrary tiebreaker silently inflate a result**. A third, more foundational one — **sample voter *utilities* and derive each ballot from them; never draw random ballots** — is why every script here starts from `sample_utilities()`: [Simulate utilities, not ballots](../../07_Concepts/topics/simulate_utilities_not_ballots.md).

- **Favorite-Betrayal (FBC)** — `fbc_simulation.py` (below).
- **Runoff Reversal frequency** — `runoff_reversal_simulation.py` ([jump to section](#runoff-reversal-frequency-simulation)).
- **STAR vs Approval divergence** — `star_vs_approval_divergence.py`: how often sincere STAR and Approval elect *different* winners (spoiler: no single number — it depends on the electorate model and the approval cutoff). Full writeup + measured rates + worked examples: [How often do STAR and Approval disagree?](../../method_comparisons/star_vs_approval_divergence.md).
- **Condorcet efficiency** — `condorcet_efficiency_simulation.py`: how often does each of six methods elect the Condorcet winner? ([jump to section](#condorcet-efficiency-simulation)). Full writeup + the table: [Condorcet efficiency, measured](../../07_Concepts/topics/condorcet/condorcet_efficiency_measured.md). Its `--chart` and `--why` modes back a second page: [Why more candidates make every method miss](../../07_Concepts/topics/condorcet/why_more_candidates_miss.md), which explains the field-size effect and works it through [one 65-voter election at 3, 5 and 7 candidates](../../method_comparisons/crowded_field/README.md). Its `--expressiveness` and `--ballot-counts` modes back a third: [What the ballot can and cannot say](../../07_Concepts/scores_and_ranks/ballot_expressiveness_measured.md), which separates ballot resolution from tabulation rule and works it through [one 25-voter election on five different papers](../../method_comparisons/ballot_expressiveness/README.md).
- **Strategic preservation of the sincere winner** — `strategic_cw_preservation.py`: the same question as above, but with voters allowed to lie ([jump to section](#strategic-cw-preservation-simulation)). Separates the sincere baseline, successful attacks and *backfired* attacks, which a single "does the sincere Condorcet winner still win" rate merges. Full writeup + the tables: [Formal compliance vs. strategic preservation](../../07_Concepts/topics/compliance_vs_strategic_preservation.md).
- **Does the qualifying round throw away the consensus winner?** — `primary_method_simulation.py`: in a two-stage reform (open primary → top N → good general), how often does the *primary* discard the consensus candidate? Full writeup + measured rates: [Does the qualifying round throw away the consensus winner?](../../method_comparisons/qualifying_round_primary_method.md) ([mechanics](#qualifying-round-primary-method-simulation)).

## Favorite-Betrayal (FBC) simulation

`fbc_simulation.py` measures, by brute force over many random elections, how often **STAR** and **RCV-IRV** actually satisfy the **Favorite Betrayal Criterion (FBC)** — and how often a favorite-betrayal vote pays off vs backfires.

## Why this exists

The debate doc once claimed STAR is *"~98% favorite-betrayal-proof."* That number had **no defensible source**: Equal Vote's criteria chart is binary pass/fail (STAR gets a ❌), and the ~91–98% figure that floats around is **Voter Satisfaction Efficiency** — an *accuracy* metric, a different thing entirely. Rather than cite a number we can't defend, this script **measures** one — and reports the modelling assumptions, because the result swings hugely with them.

## What it measures

1. **FBC-compliance frequency.** For each random election, compute the sincere STAR (or IRV) winner `W`. Then for every voter ask: holding everyone else sincere, is there *any* ballot in which they do **not** keep their true favorite (co-)top — a real betrayal — that elects someone they sincerely prefer to `W`? If even one voter has such a ballot, the election **fails** FBC. The betrayal search is **exhaustive** (every 0–5 ballot for STAR, every ranking for IRV), so this is a true best-response test, not a heuristic.

2. **Works : backfires ratio.** Over every `(voter, betrayal ballot)` pair, count how many strictly **help** the voter vs strictly **hurt** them (by sincere utilities). Reported per method. This is the brute-force cousin of Equal Vote's "honesty" stat — note it counts *all possible* betrayals, so it is a superset of the realistic strategies a real faction would attempt (read it as "if you betray blindly, how often does it pay?").

### Electorate models (both run by default)
- **spatial** — voters & candidates are points in issue space; utility = −distance. The realistic model (what [VSE / Bayesian Regret](../../07_Concepts/topics/what_makes_a_good_winner.md#measuring-it-empirically-vse-bayesian-regret) uses).
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

`runoff_reversal_simulation.py` measures how often a **Runoff Reversal** happens — the Scoring-Round leader losing the Automatic Runoff (the phenomenon taught in [Runoff Reversal](../../01_STAR/02_Examples/runoff_overturns_leader/README.md)).

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
- "Reversal" here is score-leader-vs-runoff only; it says nothing about the Condorcet winner (see [Three notions of "winner"](../../01_STAR/01_Learn/properties_and_limits/STAR_three_winner_notions.md)).
- **Always report the model, the size, and the tie split with the number.**

---

## STAR vs Ranked Robin divergence simulation

`star_vs_rr_divergence.py` — how often, and *why*, do STAR and [Ranked Robin](../../05_Ranked_Robin/01_Learn/README.md) (Copeland / Condorcet) elect different single winners?

### The mechanism

Same voter utilities feed both: STAR reads 0–5 **scores** (top-two by sum → pairwise runoff); RR reads the **ranking** (most head-to-head wins). A Condorcet winner who *reaches* STAR's runoff wins it (they beat any finalist head-to-head), so **STAR ≠ RR requires either a Condorcet *cycle*, or the Condorcet winner *missing* the score-based top-two** — a broadly-preferred but low-intensity compromise, everyone's tepid second choice. It is the [preference-vs-support](../../07_Concepts/scores_and_ranks/preference_vs_support.md) split made statistical: RR rewards *order*, STAR rewards *how much* support each candidate has.

### Running it

```
uv run 06_Other/simulations/star_vs_rr_divergence.py --trials 3000
```

### Two models of STAR — the fast one, and the authority

The sweep tabulates ~135,000 elections, so it uses **`star_winner()`**: numpy, top-two by score sum, pairwise runoff — *including the engine's tie-break rungs* (head-to-head wins among the tied, then five-star counts, then lot). It is not an approximation: it agrees with the engine on every profile tested, and [`tests/test_sim_star_model.py`](../../STARVote_LH_tabulation_engine/tests/test_sim_star_model.py) keeps it that way. The full 3000-trial sweep still runs in well under a minute.

**`star_winner_engine()`** is the real LH tabulation, and remains what you should use for anything **written down** — not because the fast model is wrong, but because the engine is right *by construction* rather than by agreement, so it cannot drift if the rungs ever change.

Until 2026-07-26 the fast model settled every tie by column order, and that gap is what mislabelled one of the 30 samples. You can still measure the gap — it should now read 0.0% everywhere:

```
uv run 06_Other/simulations/star_vs_rr_divergence.py --audit-model 400
```

About **1% of elections overall**, but it climbs to ~5% at 10 candidates and 15 voters — precisely the corner the [30 divergence samples](../../05_Ranked_Robin/02_Examples/star_vs_rr_divergence/README.md) live in, and one of those 30 was in fact born mislabelled (`cycle_C10_fewV29_bloc_2` claimed "STAR A"; the engine elects C). Their labels now come from the engine and are held there by [`tools_adam/scripts/check_star_vs_rr_labels.py`](../../STARVote_LH_tabulation_engine/tools_adam/scripts/check_star_vs_rr_labels.py) + [`tests/test_star_vs_rr_labels.py`](../../STARVote_LH_tabulation_engine/tests/test_star_vs_rr_labels.py).

### Representative results (3000 trials/cell, seed 20260721)

| model | C | V | STAR≠RR | of which: cycle | of which: CW-missed-runoff |
|-------|:--:|:--:|:--:|:--:|:--:|
| **noise** | 3 | 51 | 14.7% | 8.5% | 1.0% |
| noise | 5 | 51 | 27.1% | 24.8% | 3.4% |
| noise | 10 | 51 | 35.0% | 47.2% | 3.0% |
| **spatial** | 3 | 51 | 3.9% | 0.3% | 0.1% |
| spatial | 3 | 501 | **1.2%** | 0.1% | 0.0% |
| spatial | 10 | 15 | 29.3% | 13.1% | 5.8% |
| spatial | 10 | 501 | 10.3% | 0.8% | 3.0% |
| **faction** | 3 | 501 | 1.7% | 0.9% | 0.1% |
| faction | 7 | 501 | 10.9% | 5.0% | 4.3% |
| faction | 10 | 501 | 14.8% | 7.9% | 5.1% |

*(Refreshed 2026-07-26, when `star_winner()` was corrected to use the engine's tie-break rungs — see the caveats. Five of the ten cells moved, by 0.1–0.8pp; the cycle column is unaffected, since cycles don't depend on how STAR breaks a tie. No conclusion below changes.)*

### What this means

1. **Two completely different regimes.** Under **random noise**, divergence is high but almost entirely **cycle-driven** — cycles explode with candidate count (3→8%, 10→48%), and both methods are merely resolving an electorate with no real winner. Under **spatial / factional** models, cycles are rare (a centrist Condorcet winner usually exists), and the divergence that occurs is the *meaningful* kind: the compromise CW squeezed out of the score top-two.
2. **More candidates → more divergence, always.** With 2 candidates STAR = RR by definition; the gap widens monotonically with the field size in every model.
3. **Ballots cut opposite ways by model.** More voters *shrink* divergence under spatial/factional electorates (sampling noise fades, the structure dominates → the two methods converge on the centrist), but leave it roughly flat under pure noise. So **"fewer ballots → more divergence" is a property of *structured* electorates, not random ones.**
4. **Factions are where the real disagreement lives.** Factional/spatial models produce *lower* total divergence than noise, but a *higher share of it is the dark-horse mechanism* (CW-missed-runoff, 3–7% at 10 candidates) — polarized voters score the compromise centrist low, so RR's Condorcet winner never reaches STAR's runoff. That is the honest STAR-vs-RR philosophical disagreement (support vs. order), not a coin-flip electorate.

### Caveats (read before quoting)

- Sincere, **normalized** 0–5 scores (each voter min-maxes their utilities). Real voters don't perfectly normalize; different scoring assumptions move the numbers.
- **STAR here matches the LH engine exactly.** `star_winner()` implements starvote's tie-break rungs — head-to-head wins among the tied, then five-star counts, then lot (lowest column index, the engine's own fallback when a file publishes no lot numbers). It did not always: until 2026-07-26 it resolved every tie by numpy index order, which disagreed with the engine on ~2% of tie-heavy profiles and mislabelled one of the [30 dumped samples](../../05_Ranked_Robin/02_Examples/star_vs_rr_divergence/README.md). [`test_sim_star_model.py`](../../STARVote_LH_tabulation_engine/tests/test_sim_star_model.py) now cross-checks the model against the real engine, so that drift cannot return silently.
- **RR is still a model, not the engine.** Copeland with a lowest-index tiebreak; LH breaks Copeland ties by margin then lot, so a knife-edge RR cell may still differ slightly from the engine.
- "Divergence" counts *any* different winner, including ties resolved differently — report the model, size, and mechanism split with the number.

---

## Qualifying-round (primary method) simulation

`primary_method_simulation.py` measures how often a **two-stage reform loses the consensus winner in its own primary** — and whether the method used for the qualifying round matters.

### Why this exists

Several reform packages narrow a crowded open field to the top N (usually 4) before running a good method in the general. [Consensus Choice](../../05_Ranked_Robin/01_Learn/ranked_robin_vs_consensus_choice.md) is the live example: step 1 is *"an open qualifying election ... [that] determines at least four of the strongest candidates,"* and the published materials **do not say which method that round uses**.

That gap produced a genuine disagreement among people who know the field, with **no published numbers on either side**:

- **It matters a lot** — if the primary doesn't eliminate vote-splitting, the general's accuracy is capped by whatever the primary already distorted.
- **It matters little** — with *four* candidates advancing, it's unlikely the consensus candidate fails to advance even under Plurality; four slots is a lot of slack.

This script measures it instead of arguing about it.

### The structural fact that makes this the whole question

If the general is a **Condorcet** method (Ranked Robin / Consensus Choice), a full-field Condorcet winner who *advances* **always wins** — they beat everyone head-to-head, so they beat every survivor, so they're the Condorcet winner of the surviving subset too. (This is checked as a self-test invariant, not assumed.)

So with a Condorcet general, **the qualifying round is the only place the consensus winner can be lost.** "How often does the primary drop the CW?" *is* the accuracy question — which is exactly why an unspecified primary method is not a footnote. (Run `--general star` and this stops holding: a CW can advance and still miss the score-based top two.)

### Running it

```bash
uv run 06_Other/simulations/primary_method_simulation.py --selftest
uv run 06_Other/simulations/primary_method_simulation.py
uv run 06_Other/simulations/primary_method_simulation.py --candidates 12 --advance 3 4 5
uv run 06_Other/simulations/primary_method_simulation.py --general star
```

`--selftest` checks four invariants: a Condorcet qualifying round never drops the CW; `N ≥ C` advances everyone; an advanced CW always wins a Condorcet general; and a hand-built 5-ballot center squeeze is dropped by a Plurality top-2.

### Results, and what they mean

**Full writeup, with the measured rates, the interpretation, and the caveats: [Does the qualifying round throw away the consensus winner?](../../method_comparisons/qualifying_round_primary_method.md)** — kept there rather than duplicated here so the numbers have one home.

The headline, for orientation (9 candidates, 501 voters, spatial model, top-4 advancing, Ranked Robin general): a **Plurality** qualifying round drops the Condorcet winner **17.3%** of the time; **Approval** drops it **0.4%**; **Score** 0.0%; a Condorcet qualifying round 0% by construction. Four slots is real slack but not enough, the fix is nearly free, and the *method* matters far more than the number of slots.

---

## Condorcet efficiency simulation

`condorcet_efficiency_simulation.py` — how often does each method elect the [Condorcet winner](../../07_Concepts/topics/condorcet/README.md)? The claim "STAR's Condorcet efficiency is very high" was asserted in four places in this repo with no reproducible number behind it; this script supplies one, and the answer is more qualified than the slogan.

### The definition, and the trap in it

**Condorcet efficiency = P(elects the CW | a CW exists).** The conditional is load-bearing. Elections with a **cycle** have no Condorcet winner, so no method can elect one — folding them into the denominator would drag every method down by the cycle rate and measure the *electorate*, not the method. Cycles are excluded and reported separately as the `CW exists` column, which is itself revealing: impartial culture manufactures cycles at rates (down to 63.6% CW-exists at 7 candidates) that no structured model comes close to.

### Ranked Robin is the control, not a result

Copeland is Condorcet-efficient by construction, so its column **must** read exactly 100.0%. It is printed so a reader can check the harness: any cell below 100.0% means the pairwise code and the method code disagree, and every other number in the run is suspect. `--selftest` asserts it.

### One STAR, not two

The script does **not** define its own STAR — it imports `star_winner()` from `star_vs_rr_divergence.py`, which implements the LH engine's tie-break rungs and is held to the real engine by [`test_sim_star_model.py`](../../STARVote_LH_tabulation_engine/tests/test_sim_star_model.py). A second copy would be a second thing to drift. The finalist set used for the mechanism split comes from the same helpers, so it matches the finalists STAR really advanced (an `argsort` shortcut silently disagrees exactly when the score round ties for second — which is the situation the grid-loss column is about).

### Running it

```
uv run 06_Other/simulations/condorcet_efficiency_simulation.py                  # the sweep
uv run 06_Other/simulations/condorcet_efficiency_simulation.py --selftest       # known answers
uv run 06_Other/simulations/condorcet_efficiency_simulation.py --mechanism      # why STAR misses
uv run 06_Other/simulations/condorcet_efficiency_simulation.py --chart          # the same rates, as bars
uv run 06_Other/simulations/condorcet_efficiency_simulation.py --why            # what a bigger field does
uv run 06_Other/simulations/condorcet_efficiency_simulation.py --expressiveness # ballot vs rule
uv run 06_Other/simulations/condorcet_efficiency_simulation.py --ballot-counts  # what each paper can say
uv run 06_Other/simulations/condorcet_efficiency_simulation.py --approval-cutoff 3
```

`--expressiveness` is the script's own control on its biggest caveat. The sweep hands ranked methods a strict ranking of every candidate and score methods six rungs, so part of the measured gap is the **paper** rather than the **count**. That mode varies the two independently — Copeland on a 0–5 ballot, STAR's rule at full resolution, and the ranked methods on a ballot capped at 5 or 3 ranks the way real jurisdictions cap them — and `--ballot-counts` gives the arithmetic half. Both back [What the ballot can and cannot say](../../07_Concepts/scores_and_ranks/ballot_expressiveness_measured.md), whose short version is that ~80% of STAR's gap at seven candidates is the ballot, that a *capped* ranked ballot is far less expressive than a 0–5 one, and that RCV-IRV cannot spend the resolution either way.

### Results, and what they mean

**Full writeup, with the table, the interpretation, and the caveats: [Condorcet efficiency, measured](../../07_Concepts/topics/condorcet/condorcet_efficiency_measured.md)** — kept there rather than duplicated here so the numbers have one home.

The headlines, for orientation:

1. **No single number.** The electorate model swings the answer by more than the gap between any two methods — RCV-IRV spans 96.7% to 47.0% across the sweep. STAR runs 74–99%.
2. **Under impartial culture, RCV-IRV beats STAR** (96.7% vs 89.7% at 3 candidates). Printed rather than buried — but the same model produces cycles in a third of elections, so it is not one either camp should argue from.
3. **On a 1-D spectrum the ordering reverses and widens** — at 7 candidates RCV-IRV elects the head-to-head winner **less than half the time** (47.0%) against STAR's 74–79%. That is [center squeeze](../../07_Concepts/topics/center_squeeze/README.md) as a statistic rather than an anecdote.
4. **Most of STAR's shortfall is the ballot, not the rule.** `--mechanism` splits the cases where the CW *reached* STAR's runoff and lost: about two-thirds are outright pairwise **reversals** on the 0–5 ballot, not ties. Rounding can never flip an individual ballot (scores are a monotone transform of utilities) but it flattens different voters at different rates, and that moves the aggregate. Score and Approval inherit the same effect.

### Caveats (read before quoting)

- **Sincere ballots only** — no strategy anywhere in this script.
- **Ballot resolution is not held constant across methods.** Ranked methods get full-resolution preferences; score methods get six rungs. Realistic (a 0–5 ballot genuinely cannot rank seven candidates), but part of the STAR-vs-RR gap at large fields is **ballot expressiveness, not tabulation rule**. This is the biggest caveat on the whole exercise.
- **Approval's column is a cutoff artifact** — there is no "Approval's Condorcet efficiency" without naming the cutoff rule. Sweep `--approval-cutoff`.
- **The CW is computed from utilities, not from any ballot** — reading it off the 0–5 ballot would grade STAR against a target its own ballot had shaped, and flatter Approval the same way.
- Scores are min-max normalized per voter; that assumption is what produces the grid-loss effect above.
- **Always report the model, the field size, and the voter count with the number.**

---

## Strategic CW preservation simulation

`strategic_cw_preservation.py` — when voters lie, does the **sincere** [Condorcet winner](../../07_Concepts/topics/condorcet/README.md) still win? The script next door measures Condorcet efficiency on honest ballots; this one lets an adaptive strategic bloc attack the same electorates, and reports four numbers instead of one.

### Why this exists

A recurring argument runs: a [Smith](../../07_Concepts/topics/smith_set.md)-compliant method stays compliant with the ballots it was handed even after [burial](../../07_Concepts/topics/burial/README.md) has rearranged the pairwise structure those ballots report, so formal compliance may not discriminate between methods once strategy is allowed — simulations show very different rules preserving the sincere Condorcet winner at similar rates. The first half is simply true, and [Gibbard–Satterthwaite](../../07_Concepts/topics/gibbard_satterthwaite_theorem.md) already guarantees no method is strategy-proof. This script exists to test the second half, and finds the convergence **reproduces and then dissolves**: it is an artifact of methods starting from different honest baselines, and on the metric that produces it Plurality ties Ranked Robin.

### What it measures

Per method, conditioning on a unique sincere Condorcet winner: `sincere` (honest baseline), `held` (the CW still wins after the best attack), `paid` (an attack beat honesty *for the attackers*), `backfired` (it lost to honesty). The last two are what a single preservation rate merges.

The attack model is deliberately generous — every non-CW candidate is tried as a challenger, the bloc is every voter who sincerely prefers that challenger, and the best attack is kept. Perfect polling, perfect discipline, free coordination. **The numbers are an upper bound on what strategy can achieve, not a forecast.**

`--smith` answers a separate question: when a burial succeeds, did it eject the sincere CW from the Smith set of the cast ballots (no completion rule can help) or leave them inside it (the completion rule decides)? Ejection turns out to be the minority regime — 19–36% of successful burials — at every field size from three candidates to nine.

`--objective` is the experiment: `utility` (default) means a rational bloc submits only what beats voting honestly; `displace` means it unseats the CW at any cost to itself. `--price` runs both on the same electorates and prints the difference as a **deterrent**.

### Controls, not results

Three cells have answers known before the code runs, and `--selftest` asserts all three: Ranked Robin's `sincere` column must read exactly 100.0%; Plurality's winner must be bit-identical before and after burial; and a bloc that *shares* a favourite must never elect that favourite under RCV-IRV by burying the CW (later-no-harm, made testable). Under `--strategy compromise` Ranked Robin holds exactly 100.0% for a fourth reason that is also a theorem — raising a challenger the bloc already preferred changes no pairwise comparison with the CW.

### Running it

```bash
uv run 06_Other/simulations/strategic_cw_preservation.py
uv run 06_Other/simulations/strategic_cw_preservation.py --selftest
uv run 06_Other/simulations/strategic_cw_preservation.py --price
uv run 06_Other/simulations/strategic_cw_preservation.py --strategy compromise
uv run 06_Other/simulations/strategic_cw_preservation.py --objective displace
```

### Caveats (read before quoting)

One bloc attacks and nobody defends, so real preservation rates are higher. Every number is conditional on the electorate model — and under impartial culture the deterrent vanishes entirely (every `deterred` cell reads 0.0%), which is worth knowing before quoting any strategy result computed on it. `held` is a hit rate and says nothing about *how bad* the winner is when a method misses. Full discussion: [Formal compliance vs. strategic preservation](../../07_Concepts/topics/compliance_vs_strategic_preservation.md).
