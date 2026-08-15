---
tags:
  - criteria
  - strategy
  - simulation
---

# Formal compliance vs. strategic preservation of the sincere winner

*A voting criterion is a property of the map from **cast ballots** to a winner. "The candidate who would beat everyone under **sincere** preferences wins" is a property of the electorate **and of how the voters chose to behave**. These are different objects, and the second is not a stronger version of the first. This page separates them, measures the gap, and shows why a popular-sounding conclusion — that formal Smith/Condorcet compliance therefore "doesn't discriminate between methods" — does not survive the decomposition.*

**Level: 301 · deep dive** — Curriculum [301](../curriculum/CURRICULUM_301.md). The simulation: [`strategic_cw_preservation.py`](../../06_Other/simulations/strategic_cw_preservation.py) ([folder README](../../06_Other/simulations/README.md)). Companions: [Condorcet efficiency, measured](condorcet/condorcet_efficiency_measured.md) (the same question with everyone honest) · [burial](burial/README.md) · [PVSI](pvsi_strategic_incentive.md) · [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) · [the Smith set](smith_set.md).

---

## The argument this page answers

Stated at its strongest, because it deserves that:

> A [Smith](smith_set.md)-compliant method will of course keep electing from the Smith set of the ballots actually cast. But strategic [burial](burial/README.md) can change that reported Smith set. So a method can be perfectly Smith-compliant and still fail to elect the candidate who would have been the [Condorcet winner](condorcet/README.md) under sincere preferences. Conditioning on elections that *have* a unique sincere Condorcet winner, sophisticated Condorcet rules preserve that winner only about 70% of the time under adaptive strategy — and simple [RCV-IRV](../../06_Other/RCV_IRV/concepts/README.md) does about as well. So formal compliance may be much less informative than we assume.

**The first half is correct, and worth conceding without hedging.** A criterion cannot be about sincere preferences, because no method ever sees one. Compliance is evaluated on the ballots in the box. [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) already guarantees that no method is strategy-proof, so "compliance does not confer strategy-proofness" was never in dispute — it is a theorem, not a discovery. Advocates who talk as though Smith compliance protects the *electorate's* preferred candidate rather than the *ballots'* are overstating, and this repo has been guilty of the same shorthand.

**The second half is where it breaks**, and the reason is a measurement artifact that a single preservation rate cannot show. "The sincere Condorcet winner did not win" merges three events with opposite policy weight:

| Event | What it requires | What it says about the method |
|---|---|---|
| The method missed the CW **on honest ballots** | nobody lied | a defect of the count itself |
| An attack **succeeded** | a coordinated bloc lied and profited | a defect of the incentive |
| An attack **backfired** | a bloc lied and made its own life worse | a *deterrent* — the method punishing manipulation |

Collapse those into one rate and the rate converges across methods — not because the methods are alike, but because the ones that are bad on honest ballots have nothing left to lose. The rest of this page measures each event separately.

## How it is measured

[`strategic_cw_preservation.py`](../../06_Other/simulations/strategic_cw_preservation.py) samples voter utilities, derives every ballot from them ([simulate utilities, not ballots](simulate_utilities_not_ballots.md)), and keeps the sincere preferences separately from the ballots actually submitted. For each election with a unique sincere Condorcet winner it tries **every** non-CW candidate as a challenger, forms the bloc of every voter who sincerely prefers that challenger to the CW, has them submit a strategy, and keeps the best attack the bloc can find.

That is deliberately generous to the attackers: perfect polling, perfect within-bloc discipline, free coordination at any size, and a free search over every available target. **The numbers below are an upper bound on what strategy can achieve, not a forecast of what voters would do.**

Four columns, and the last two are the point:

- **sincere** — P(the method elects the sincere CW | one exists), honest ballots. The baseline.
- **held** — the same, after the best attack.
- **paid** — an attack was submitted and left *the attackers* better off than voting honestly would have.
- **backfired** — an attack was submitted and left them *worse* off.

The acceptance test is what separates the two objectives the script offers. Under **`--objective utility`** (the default) a bloc submits a strategic ballot only if lying beats telling the truth *for that bloc* — a rational coalition. Under **`--objective displace`** it submits anything that unseats the CW, whatever the cost. Reporting only the second is reporting how much damage is *reachable* and reading it as how much is *likely*.

Three cells of the harness are controls rather than results, and they are printed so the code can be audited: Ranked Robin's `sincere` column must read exactly 100.0% (Copeland is Condorcet-efficient by construction); Plurality's winner must be bit-identical before and after burial (burial never moves a ballot's top mark, and Plurality reads nothing else); and under burial by a bloc that *shares* a favourite, RCV-IRV must never newly elect that favourite. `--selftest` asserts all three.

## Burial: the convergence is real, and it is a baseline artifact

2,000 elections per cell, seed 20260814, 101 voters, rational bloc.

```
model       C     V   CW ex | method        sincere    held    paid  backfired   bloc
-------------------------------------------------------------------------------------
spatial1d   5   101   98.4% | RankedRobin    100.0%   39.0%   61.0%       0.0%   39%
                           | STAR            83.9%   15.5%   68.7%       0.0%   39%
                           | Score           72.6%    6.0%   66.6%       0.0%   35%
                           | Approval        66.2%   16.1%   50.1%       0.0%   40%
                           | RCV-IRV         65.5%   47.1%   18.7%       0.0%   40%
                           | Plurality       44.0%   44.0%    0.0%       0.0%     —  (control)

spatial2d   5   101   99.1% | RankedRobin    100.0%   37.4%   62.6%       0.0%   38%
                           | STAR            92.7%   27.5%   65.2%       0.0%   39%
                           | Score           85.5%   11.9%   73.6%       0.0%   36%
                           | Approval        80.9%   31.6%   49.3%       0.0%   39%
                           | RCV-IRV         84.3%   49.0%   35.4%       0.0%   35%
                           | Plurality       62.0%   62.0%    0.0%       0.0%     —  (control)

faction2d   5   101   96.9% | RankedRobin    100.0%   65.7%   34.3%       0.0%   37%
                           | STAR            94.5%   47.3%   47.2%       0.0%   39%
                           | Score           83.5%   26.1%   57.5%       0.0%   34%
                           | Approval        79.9%   44.8%   35.2%       0.0%   37%
                           | RCV-IRV         85.6%   71.4%   14.2%       0.0%   35%
                           | Plurality       73.5%   73.5%    0.0%       0.0%     —  (control)
```

Reproduce with:

```bash
uv run 06_Other/simulations/strategic_cw_preservation.py --trials 2000
```

**1. The convergence reproduces.** Look only at `held` in the 1-D row: Ranked Robin 39.0%, RCV-IRV 47.1%, Plurality 44.0%. Three methods with nothing in common land within eight points of each other. Anyone running this experiment and reporting one number per method would find exactly the "everything converges to 65–75%" pattern, and would be reporting it accurately.

**2. And the decomposition dissolves it.** Read the same rows with the `sincere` column beside them. Ranked Robin arrives at 39.0% from **100%** — every point it lost, it lost to somebody lying. RCV-IRV arrives at 47.1% from **65.5%** — most of its shortfall is the count missing the Condorcet winner while every ballot is honest, which is [center squeeze](center_squeeze/README.md) and not strategy at all. Plurality arrives at 44.0% from **44.0%**: it lost *nothing* to the attack, because burial cannot reach a method that reads one mark, and it is nevertheless the worst method in the table.

That is the whole answer to the argument at the top of this page. **A shared `held` rate is not evidence that the methods are equally good; it is evidence that a method already bad on honest ballots has less left for an attacker to take.** A metric on which Plurality ties Ranked Robin is a metric that has stopped measuring the thing anyone cares about.

**3. The attack is enormous.** The `bloc` column is the mean size of a winner-moving coalition: **34–40% of the entire electorate**, perfectly disciplined and perfectly informed, is what it took. That is the cost the `held` column charges nothing for.

## What a preservation rate hides: the price

The forum argument's own better question — *how difficult, risky, or dependent on coordination is it to displace the sincere CW?* — is answerable, and it is a different table. `--price` runs the same electorates under both objectives, so the difference is a deterrent and not a difference of two samples.

```
model       C     V | method        reachable  rational  deterred   bloc
------------------------------------------------------------------------
noise       5   101 | RankedRobin      100.0%    100.0%      0.0%   45%
                    | STAR              84.2%     84.2%      0.0%   46%
                    | Score             76.6%     76.6%      0.0%   47%
                    | Approval          59.6%     59.6%      0.0%   47%
                    | RCV-IRV           89.7%     89.7%      0.0%   44%
                    | Plurality          0.0%      0.0%      0.0%     —

spatial1d   5   101 | RankedRobin       89.0%     61.6%     27.4%   39%
                    | STAR              77.7%     69.2%      8.4%   39%
                    | Score             69.8%     68.6%      1.2%   35%
                    | Approval          54.5%     51.3%      3.2%   39%
                    | RCV-IRV           54.5%     17.8%     36.7%   40%
                    | Plurality          0.0%      0.0%      0.0%     —

spatial2d   5   101 | RankedRobin       84.8%     63.5%     21.3%   38%
                    | STAR              76.0%     64.7%     11.3%   39%
                    | Score             74.6%     73.3%      1.3%   35%
                    | Approval          52.1%     48.6%      3.5%   39%
                    | RCV-IRV           70.1%     36.8%     33.3%   35%
                    | Plurality          0.0%      0.0%      0.0%     —

faction2d   5   101 | RankedRobin       51.9%     35.6%     16.3%   37%
                    | STAR              56.3%     47.5%      8.8%   38%
                    | Score             62.4%     60.3%      2.0%   34%
                    | Approval          38.7%     36.0%      2.7%   38%
                    | RCV-IRV           35.3%     13.3%     22.1%   35%
                    | Plurality          0.0%      0.0%      0.0%     —
```

`reachable` is the share of elections where *some* burial unseats the sincere CW if the bloc does not care what it costs them; `rational` is the same when the bloc submits only what beats voting honestly; `deterred` is the difference — burials that exist on paper and that no self-interested coalition would cast, because the manufactured cycle hands the win to the buried candidate or to someone worse.

**4. RCV-IRV has the largest deterrent in every structured model** — 36.7 points in 1-D, 33.3 in 2-D, 22.1 in the factional model. Most burials that *work* against IRV are burials the attackers should not want. That is a real point in IRV's favour on this specific attack, it is the honest content of "later-no-harm makes IRV hard to bury," and it belongs in the table alongside everything else.

**5. Score voting has essentially no deterrent** — 1.2 to 2.0 points. Nearly every burial that displaces the CW under Score also pays. Adding STAR's [automatic runoff](../../01_STAR/01_Learn/README.md) to the identical ballot raises the deterrent to 8–11 points and the `held` column with it, which is the runoff earning its keep.

**6. Under impartial culture, the deterrent vanishes entirely — every cell reads 0.0%.** In an electorate with no structure there is nothing for a mis-aimed burial to hit, so every attack that works also pays, and every method's `reachable` equals its `rational`. This matters because impartial culture is the model in which these simulations are most often run and the one in which [IRV scores best](condorcet/condorcet_efficiency_measured.md). It is a model that simultaneously manufactures cycles at rates no real electorate shows (`CW exists` drops to 76% at five candidates, against 97–99% in every structured model) and switches off the single mechanism that makes burial risky. Results quoted from it should say so.

## Two burial regimes, and only one of them cares which completion rule you picked

A natural objection to the "which completion rule?" framing is that by the time the completion rule runs, it may be too late: if the burial has pushed the sincere Condorcet winner **out of the Smith set of the cast ballots**, then every Smith-compliant rule is obliged to elect someone else, and swapping Ranked Pairs for Minimax or Benham or a fresh second round cannot rescue anything. That is a real and sharply-stated mechanism, and it is measurable — `--smith` splits successful burials into the two regimes:

- **ejected** — the CW is gone from the reported Smith set. No completion rule can help. The choice is irrelevant.
- **inside** — the CW is still in the reported Smith set and the completion rule picked someone else out of it. This is the regime where the choice of completion is the whole ballgame, and where the [Alaska 2022 burial](../../method_comparisons/condorcet_burial_alaska/README.md) lives: margin-based rules shrug that attack off, a Hare/runoff completion falls for it.

Field size is swept because that is the variable the two regimes should trade on — a wider field gives a burial far more room to build a Smith set that excludes the CW outright. 1,200 elections per cell, 71 voters, rational bloc.

```
model       C     V |  displaced  ejected  inside |  ejected as % of displaced
------------------------------------------------------------------------------
spatial1d   3    71 |      19.6%     4.6%   15.1% |                      23.4%
spatial1d   5    71 |      63.4%    11.8%   51.6% |                      18.7%
spatial1d   7    71 |      79.9%    18.2%   61.6% |                      22.8%
spatial1d   9    71 |      88.4%    22.8%   65.6% |                      25.8%

spatial2d   3    71 |      24.8%     8.9%   15.9% |                      36.0%
spatial2d   5    71 |      64.5%    18.5%   46.1% |                      28.6%
spatial2d   7    71 |      80.5%    24.3%   56.2% |                      30.2%
spatial2d   9    71 |      90.6%    24.3%   66.3% |                      26.9%

faction2d   3    71 |      10.4%     2.9%    7.5% |                      28.2%
faction2d   5    71 |      34.5%     7.1%   27.4% |                      20.5%
faction2d   7    71 |      48.6%    10.8%   37.8% |                      22.3%
faction2d   9    71 |      57.7%    12.6%   45.2% |                      21.8%
```

```bash
uv run 06_Other/simulations/strategic_cw_preservation.py --smith --candidates 3 5 7 9 --voters 71
```

**Ejection is the minority regime at every field size tested, including nine candidates.** Between 19% and 36% of successful burials eject the CW from the reported Smith set; the other two-thirds to four-fifths leave the CW sitting inside it, where the completion rule decides. And the ejected *share* barely moves with the field — 23% to 26% in 1-D from three candidates to nine — even as the raw displacement rate climbs from 19.6% to 88.4%. A wider field makes burial far easier; it does not much change *where* the burial lands.

The honest limit of this result: the attack measured here is a single coordinated bloc ranking the CW last. It is not an adaptive search over rank *and* score offsets by several factions best-responding to each other. Ejection is plainly something a more powerful search can buy — the question is how much, and that is the sharp form of the disagreement rather than a rhetorical one. Anyone reporting that burial routinely ejects the sincere winner from the Smith set should report the ejection rate next to the displacement rate, because the two come apart.

## Compromise: two exact controls, and what they prove

Running the other strategy — a bloc consolidating behind a challenger rather than sinking the CW — produces two cells that read exactly 100.0%, and neither is luck.

```
model       C     V   CW ex | method        sincere    held    paid  backfired   bloc
-------------------------------------------------------------------------------------
noise       5   101   76.1% | RankedRobin    100.0%  100.0%    0.0%       0.0%     —
                           | STAR            83.8%   38.1%   59.9%       0.0%   48%
                           | Score            75.8%    3.4%   96.5%       0.0%   46%
                           | Approval        64.6%    2.0%   98.0%       0.0%   45%
                           | RCV-IRV         90.9%   91.0%    0.1%       0.0%   46%
                           | Plurality       60.9%    0.0%  100.0%       0.0%   44%
```

**Ranked Robin holds 100.0% because it must.** The bloc already preferred the challenger to the CW, so raising the challenger to the top of their ballots changes no pairwise comparison between those two — the CW still beats the challenger, and still beats everyone else, so the Condorcet winner is unchanged and Copeland still elects them. **RCV-IRV holds ~91% for a related reason:** IRV's final round is itself a pairwise comparison, and a Condorcet winner who reaches it wins it. Consolidating behind a challenger delivers the challenger *to* that final round, where they lose.

**Plurality drops to 0.0%.** With no later rounds and no pairwise stage, consolidation is simply decisive.

Which yields the sharpest form of the criticism. **A "sincere-CW preservation" metric is sensitive to burial and to almost nothing else** — every method whose last stage is pairwise (Ranked Robin by construction, STAR by its runoff, IRV by its final round) is largely immune to the other direction of attack. So a study that tests burial and reports convergence has not shown that the methods are alike under strategy. It has shown that it tested the one attack on which they can be made to look alike, on a metric that is blind by construction to IRV's characteristic failure — because center squeeze happens on *honest* ballots and is therefore already priced into the `sincere` column the metric never looks at.

## A correction this page forced: what later-no-harm actually buys IRV

This library has repeated, in its [burial hub](burial/README.md) and elsewhere, that IRV is essentially immune to burial because it satisfies [later-no-harm](../GLOSSARY.md). Building the harness showed that shorthand is too strong, and the tables above are the counterexample: burial unseats the sincere Condorcet winner from RCV-IRV in 35–70% of structured-model elections when the attackers do not count the cost, and in 13–37% when they do.

The theorem later-no-harm actually delivers is narrower, and the harness asserts it every run as a control:

> **A bloc that shares a favourite F cannot elect F under IRV by burying the Condorcet winner.** Their buried ballots only take effect once they transfer, which only happens once F is eliminated — and an eliminated candidate cannot win. So if F wins the buried election, the burial never altered the count at all.

What that leaves untouched is a coalition whose members have **different** favourites. Everyone who prefers some challenger to the CW can bury the CW, and each member's buried ballot bites at exactly the moment their own favourite is eliminated, starving the CW of transfers they would sincerely have received. Nothing in later-no-harm prevents this, because no single voter is promoting their own favourite.

So the fair two-sided statement, which is what the burial hub now carries:

- Burial is **harder** against RCV-IRV than against a Condorcet rule — it needs a coalition willing to see its own favourites eliminated first, it can never elect your favourite, and it is the attack IRV deters most strongly.
- But *"IRV satisfies later-no-harm, therefore burial does not work on IRV"* is **false as stated**, and this page's IRV column is the counterexample.

## Caveats — read before quoting

- **These are upper bounds, not forecasts.** The attackers get free coordination, perfect polling, perfect discipline, and a free search over every challenger. Real burial needs a third of the electorate to rank someone they genuinely like dead last, on the strength of polling accurate enough to identify the target — and it [leaves fingerprints](burial/README.md), since a cycle appearing in a race whose polling showed a clean head-to-head winner *is* the anomaly.
- **One bloc attacks; nobody defends.** There is no counter-strategy by the CW's own supporters, and no second bloc. A defended election is a harder election to manipulate, so the true `held` numbers are higher than these.
- **The model swings the answer more than the method does**, as it does on [the sincere page](condorcet/condorcet_efficiency_measured.md). Every number here is conditional on the electorate model; that is why four models are printed and never one.
- **`held` is a hit rate and says nothing about severity.** A Smith-compliant method that fails still elects from the *reported* Smith set, which after a manufactured cycle usually still contains the sincere CW. Plurality's failures are unconstrained. Two methods can share a `held` rate and be electing very different candidates in the elections they miss; measuring that needs a utility scale, not a binary ([VSE](what_makes_a_good_winner.md)).
- **Approval's column is set by the cutoff rule**, a modelling choice rather than a fact about Approval, exactly as on the sincere page.

## What to ask of any study of this shape

The five questions that decide whether a "methods converge under strategy" result means anything:

1. **What is the sincere baseline for each method?** Without it, a method that is bad honestly is indistinguishable from a method that was successfully attacked.
2. **What is the profile generator?** Impartial culture flatters IRV, manufactures cycles, and removes the deterrent. Structured models do none of those.
3. **What are the strategic blocs maximizing?** Displacing the sincere winner, or their own payoff? The gap between those two objectives is 20–37 points for some methods and 1 point for others — it is not a detail.
4. **Which strategies were tested?** A burial-only study measures the one axis on which pairwise-completed methods can be made to look alike.
5. **How large a coalition, and how much information, did a successful attack need?** A method attacked successfully by 5% of voters and one attacked successfully by 40% are not tied.

Related: [burial](burial/README.md) · [strategic voting — the four kinds of insincere vote](strategic_voting.md) · [the strategic pathologies](strategic_pathologies.md) · [PVSI, the per-strategy incentive metric](pvsi_strategic_incentive.md) · [Condorcet efficiency, measured](condorcet/condorcet_efficiency_measured.md) · [Gibbard–Satterthwaite](gibbard_satterthwaite_theorem.md) · [Even Condorcet methods can be buried — Alaska 2022](../../method_comparisons/condorcet_burial_alaska/README.md) · [election simulation models](election_simulation_models.md).
