# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""strategic_cw_preservation.py — does the SINCERE Condorcet winner survive strategy?

THE QUESTION, AND WHY IT IS NOT THE ONE NEXT DOOR. condorcet_efficiency_simulation.py
measures P(method elects the CW | a CW exists) on SINCERE ballots. That number is a
property of the count. This script measures what happens when voters lie, which is a
property of the count AND of the incentive it creates:

    sincere      P(elects the sincere CW | a unique sincere CW exists), honest ballots
    held         the same, after an adaptive strategic bloc has done its worst
    paid         P(the attack changed the winner to someone the BLOC likes better)
    backfired    P(the attack changed the winner to someone the BLOC likes WORSE)

The four are the point. A single "how often does the sincere CW win under strategy"
rate — the shape of the claim this script was written to test — silently merges three
completely different events: the method missing while everyone is honest, an attack
succeeding, and an attack blowing up in the attackers' faces. Those carry opposite
policy weight, so they are counted apart. `held`, `paid` and `backfired` partition the
attacked elections (if the CW still wins, the bloc's payoff change is exactly zero, so
no election can land in two columns).

FORMAL COMPLIANCE IS NOT THE THING BEING MEASURED. A Condorcet/Smith-compliant rule
stays perfectly compliant with the ballots it was handed even after burial has
rearranged the pairwise structure those ballots report. That is not a defect in the
criterion; it is what a criterion IS — a property of the map from CAST BALLOTS to a
winner. No method ever sees a sincere preference. Gibbard-Satterthwaite already
guarantees none of them is strategy-proof. The interesting question was never "does
compliance confer strategy-proofness" (it cannot) but "what does an attack COST" —
which is the `paid` / `backfired` pair, not the `held` column.
See 07_Concepts/topics/compliance_vs_strategic_preservation.md.

THE ATTACK MODEL. For each election with a unique sincere CW:

  * every non-CW candidate X is tried as the CHALLENGER, in turn;
  * the BLOC for X is every voter who sincerely prefers X to the CW;
  * the bloc submits one of two strategies, keeping the rest of the ballot sincere:
        burial       rank the CW dead last / score them 0
        compromise   rank X top / score them 5  (consolidate behind the challenger)
  * the attacker keeps the BEST of the C-1 challengers by its objective.

Trying every challenger and keeping the best is what makes this ADAPTIVE, and it is
deliberately generous: it grants the attackers perfect polling, perfect within-bloc
discipline, and free coordination at any bloc size. The numbers are therefore an upper
bound on what strategy can achieve, not a forecast of what voters would do.

*** THE OBJECTIVE IS THE WHOLE BALLGAME — --objective ***
  utility   (default) the bloc submits the strategy only if the resulting winner is
            BETTER FOR THE BLOC than the sincere CW. This is a rational bloc.
  displace  the bloc submits any strategy that removes the CW, whatever it costs them.
            This is an adversary maximising damage, not a voter maximising utility.

Search under `displace` and you will find burials everywhere; search under `utility`
and margin-based rules turn most of them down, because a mis-aimed burial elects the
buried candidate or a worse third. A simulation that reports only the `displace` number
is reporting how much damage is REACHABLE, and reading it as how much is LIKELY.

THREE CONTROLS, NOT RESULTS (printed so the harness can be audited):
  * Ranked Robin's `sincere` column must read 100.0%. Copeland is Condorcet-efficient
    by construction; anything less means the pairwise code and the method code disagree
    and every other number in the run is worthless.
  * Plurality's winner must be BIT-IDENTICAL before and after BURIAL, in every trial. It
    reads one mark and burial never moves a ballot's top choice, so the attack cannot
    reach it. If this ever fails, the burial is touching something it should not be.
  * RCV-IRV, under a burial by a bloc that SHARES A FAVOURITE, must never newly elect
    that favourite. This is later-no-harm made testable, and the proof is short: the
    burial only takes effect once those ballots transfer, which only happens once their
    favourite is eliminated — and an eliminated candidate cannot win. So if the shared
    favourite wins the buried election, the burial never altered the count at all.

*** THE CONTROL THAT IS *NOT* THERE, AND WHY IT MATTERS ***
It is widely repeated that later-no-harm makes IRV burial-proof. What LNH actually
delivers is the narrow theorem above: burial cannot promote *the burier's own
favourite*. It does NOT make IRV inert under burial. A coalition whose members do NOT
share a favourite — everyone who prefers some challenger X to the Condorcet winner —
can and does unseat the CW from IRV by burial, because each member's buried ballot
takes effect at exactly the moment their own favourite is eliminated, and the CW
starves on transfers they would sincerely have received. This harness measures that,
and IRV is not immune to it. So the fair statement is two-sided, and both sides are
printed here rather than whichever one suits the argument:
  * burial is HARDER against IRV than against a Condorcet rule — it needs a coalition
    willing to lose its own favourites first, and it can never elect your favourite; but
  * "IRV satisfies later-no-harm, therefore burial does not work on IRV" is FALSE as
    stated, and this script's IRV column is the counterexample.

*** THIS SCRIPT DEFINES NO METHOD OF ITS OWN. *** Every rule is imported from
condorcet_efficiency_simulation.py (which in turn imports STAR from
star_vs_rr_divergence.py, the model held to the real LH engine by
STARVote_LH_tabulation_engine/tests/test_sim_star_model.py). There is deliberately one
model of each method in this folder.

Usage:  uv run 06_Other/simulations/strategic_cw_preservation.py
        uv run 06_Other/simulations/strategic_cw_preservation.py --selftest
        uv run 06_Other/simulations/strategic_cw_preservation.py --objective displace
        uv run 06_Other/simulations/strategic_cw_preservation.py --strategy compromise
        uv run 06_Other/simulations/strategic_cw_preservation.py --price
        uv run 06_Other/simulations/strategic_cw_preservation.py --trials 4000 --seed 7
"""
import argparse
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from condorcet_efficiency_simulation import (   # noqa: E402  - path set above
    METHODS,
    condorcet_winner,
    winners,
)
from star_vs_rr_divergence import gen, pairwise, scores_from_util   # noqa: E402

STRATEGIES = ["burial", "compromise"]
# Burial never moves a ballot's top choice, and Plurality reads nothing else, so its
# column under burial is a CONTROL and not a result. RCV-IRV is deliberately NOT in
# this tuple — see the header: later-no-harm stops burial promoting your own favourite,
# it does not stop a mixed-favourite coalition burying the Condorcet winner out.
BURIAL_INERT = ("Plurality",)


# --- who attacks, and with what ----------------------------------------------
def bloc_for(true_util, cw, challenger):
    """Voters who sincerely prefer `challenger` to the Condorcet winner.

    This is the only coalition with a motive: everyone in it would rather the
    challenger won, so everyone in it gains if the attack lands. Voters who honestly
    prefer the CW are never conscripted — an attack that needs them is not an attack,
    it is a different electorate.
    """
    return np.flatnonzero(true_util[:, challenger] > true_util[:, cw])


def cast_ballots(true_util, sincere_scores, bloc, cw, challenger, strategy):
    """The ballots the bloc actually submits. Everything outside the strategy is sincere.

    Returns (cast_util, cast_scores). `cast_util` is the SUBMITTED RANKING expressed as
    a utility matrix — the ranked rules read nothing but its order, so shoving a
    candidate below the row minimum is exactly "ranked last". It is NOT the voters'
    preferences: those stay in `true_util`, which is what the CW and every bloc payoff
    are computed from. Confusing the two is the single easiest way to write a strategy
    simulation that scores lies as if they were sincere.
    """
    cast_util = true_util.copy()
    cast_scores = sincere_scores.copy()
    if strategy == "burial":
        cast_util[bloc, cw] = true_util[bloc].min(axis=1) - 1.0
        cast_scores[bloc, cw] = 0
    elif strategy == "compromise":
        cast_util[bloc, challenger] = true_util[bloc].max(axis=1) + 1.0
        cast_scores[bloc, challenger] = 5
    else:                                                  # pragma: no cover - guarded by argparse
        raise ValueError(f"unknown strategy {strategy!r}")
    return cast_util, cast_scores


def bloc_payoff(true_util, bloc, candidate):
    """The attacking bloc's mean SINCERE utility for a candidate.

    Sincere, always — the bloc lied on its ballot, not to itself. This is what decides
    whether an attack paid or backfired, and under --objective utility it is what
    decides whether the bloc submits the ballot at all.
    """
    return float(true_util[bloc, candidate].mean())


# --- one election, one method, adaptively attacked ----------------------------
def attack(true_util, sincere_scores, cw, cutoff, strategy, objective):
    """Best attack the strategists can find, per method.

    Returns {method: (winner, bloc_size)} where `winner` is the outcome after the
    attack the bloc chose to submit, and bloc_size is that attack's coalition (0 if the
    bloc submitted nothing). Every non-CW challenger is tried and the best kept — the
    "adaptive" part, and the reason these are upper bounds.
    """
    C = true_util.shape[1]
    honest = winners(true_util, sincere_scores, cutoff)
    # Submitting nothing is always an option, and it is worth exactly zero by
    # definition — the baseline every attack is judged against is HONESTY, not the
    # Condorcet winner. That distinction is not pedantic: judging against the CW scores
    # a do-nothing "attack" on a method that already missed the CW as a success, which
    # hands the worst methods the best strategy numbers.
    best = {m: (w, 0, 0.0) for m, w in honest.items()}
    for challenger in range(C):
        if challenger == cw:
            continue
        bloc = bloc_for(true_util, cw, challenger)
        if bloc.size == 0:
            continue                                       # nobody wants this challenger
        cast_util, cast_scores = cast_ballots(
            true_util, sincere_scores, bloc, cw, challenger, strategy)
        got = winners(cast_util, cast_scores, cutoff)
        for m in METHODS:
            # THIS bloc's payoff, on ITS sincere utilities, for lying versus for telling
            # the truth. Recovering a "bloc" from the winner afterwards instead would be
            # circular — the voters who prefer the new winner always gain by
            # construction, so every attack would score as a success and none as a
            # backfire.
            gain = (bloc_payoff(true_util, bloc, got[m])
                    - bloc_payoff(true_util, bloc, honest[m]))
            if objective == "displace":
                # Unseat the CW at any cost. Nothing to displace if honesty already
                # missed them. Among attacks that displace, still take the best one.
                accept = (honest[m] == cw and got[m] != cw
                          and (best[m][0] == cw or gain > best[m][2]))
            else:
                # A rational bloc submits only what beats voting honestly.
                accept = gain > 1e-12 and gain > best[m][2]
            if accept:
                best[m] = (got[m], int(bloc.size), gain)
    return best


def run_cell(rng, model, V, C, trials, cutoff, strategy, objective):
    """One (model, C, V) cell. Returns per-method rates plus the mean successful bloc.

    Denominator throughout: elections with a UNIQUE sincere Condorcet winner. Cycles are
    excluded because there is no sincere CW to preserve — folding them in would measure
    the electorate rather than the method, exactly as in the sincere sweep next door.
    """
    have_cw = 0
    stat = {m: {"sincere": 0, "held": 0, "paid": 0, "backfired": 0,
                "bloc": [], "moved": 0} for m in METHODS}
    for _ in range(trials):
        true_util = gen(rng, model, V, C)
        sincere_scores = scores_from_util(true_util)
        cw = condorcet_winner(true_util)
        if cw < 0:
            continue
        have_cw += 1
        honest = winners(true_util, sincere_scores, cutoff)
        got = attack(true_util, sincere_scores, cw, cutoff, strategy, objective)
        for m in METHODS:
            stat[m]["sincere"] += honest[m] == cw
            w, n, gain = got[m]
            if w == cw:
                stat[m]["held"] += 1                       # the sincere CW survived
                continue
            if w != honest[m]:
                stat[m]["moved"] += 1                      # the attack moved it, not the rule
                stat[m]["bloc"].append(n / V)
            if gain > 1e-12:
                stat[m]["paid"] += 1                       # the attackers came out ahead
            elif gain < -1e-12:
                stat[m]["backfired"] += 1                  # they made their own life worse
    if not have_cw:
        return 0.0, {m: None for m in METHODS}
    out = {}
    for m in METHODS:
        s = stat[m]
        out[m] = {
            "sincere": s["sincere"] / have_cw,
            "held": s["held"] / have_cw,
            "paid": s["paid"] / have_cw,
            "backfired": s["backfired"] / have_cw,
            "bloc": (float(np.mean(s["bloc"])) if s["bloc"] else float("nan")),
        }
    return have_cw / trials, out


# --- the sweep ----------------------------------------------------------------
def sweep(rng, trials, cutoff, models, cands, voters, strategy, objective):
    head = (f"{'model':<10}{'C':>3}{'V':>6} {'CW ex':>7} | {'method':<12}"
            f"{'sincere':>9}{'held':>8}{'paid':>8}{'backfired':>11}{'bloc':>7}")
    print(head)
    print("-" * len(head))
    for model in models:
        for C in cands:
            for V in voters:
                cw_rate, res = run_cell(rng, model, V, C, trials, cutoff,
                                        strategy, objective)
                for i, m in enumerate(METHODS):
                    r = res[m]
                    lead = (f"{model:<10}{C:>3}{V:>6} {cw_rate*100:6.1f}%" if i == 0
                            else " " * 26)
                    flag = "  (control: burial cannot reach it)" \
                        if strategy == "burial" and m in BURIAL_INERT else ""
                    bloc = "     —" if np.isnan(r["bloc"]) else f"{r['bloc']*100:5.0f}%"
                    print(f"{lead} | {m:<12}{r['sincere']*100:8.1f}%{r['held']*100:7.1f}%"
                          f"{r['paid']*100:7.1f}%{r['backfired']*100:10.1f}%{bloc}{flag}")
                print()


# --- what does an attack COST? -------------------------------------------------
def price(rng, trials, cutoff, models, cands, voters):
    """The question the hit-rate hides: how expensive is a successful attack?

    Three numbers per method, over the elections where an attack was available at all:

      reachable   share where SOME adaptive burial unseats the sincere CW if the bloc
                  does not care what it costs them   (--objective displace)
      rational    the same share when the bloc submits the ballot only if lying beats
                  telling the truth FOR THE BLOC  (--objective utility)
      bloc        mean size of the coalition a successful rational attack needed,
                  as a share of the electorate

    reachable - rational is the DETERRENT: burials that exist on paper and that no
    rational coalition would cast, because the manufactured cycle hands the win to the
    buried candidate or to someone worse. It is invisible to any measure that reports
    only how often the sincere CW ends up losing.
    """
    print("The price of a successful burial. 'reachable' assumes the attackers do not")
    print("care what it costs them; 'rational' requires the attack to leave the")
    print("attacking coalition better off than voting honestly did.\n")
    head = (f"{'model':<10}{'C':>3}{'V':>6} | {'method':<12}"
            f"{'reachable':>11}{'rational':>10}{'deterred':>10}{'bloc':>7}")
    print(head)
    print("-" * len(head))
    for model in models:
        for C in cands:
            for V in voters:
                # Same stream position for both objectives: the two runs must see the
                # SAME electorates or "deterred" is a difference of two samples.
                seed = rng.integers(0, 2**31 - 1)
                _, hard = run_cell(np.random.default_rng(seed), model, V, C, trials,
                                   cutoff, "burial", "displace")
                _, soft = run_cell(np.random.default_rng(seed), model, V, C, trials,
                                   cutoff, "burial", "utility")
                for i, m in enumerate(METHODS):
                    # Both are the same event — "the CW won honestly and lost after the
                    # attack" — measured under the two acceptance rules, on the SAME
                    # electorates. Their difference is therefore a deterrent and not a
                    # difference of two samples.
                    reach = hard[m]["sincere"] - hard[m]["held"]
                    rat = soft[m]["sincere"] - soft[m]["held"]
                    lead = f"{model:<10}{C:>3}{V:>6}" if i == 0 else " " * 19
                    bloc = "     —" if np.isnan(soft[m]["bloc"]) else f"{soft[m]['bloc']*100:5.0f}%"
                    print(f"{lead} | {m:<12}{reach*100:10.1f}%{rat*100:9.1f}%"
                          f"{(reach - rat)*100:9.1f}%{bloc}")
                print()


# --- known-answer checks -------------------------------------------------------
def selftest():
    """Everything here has an answer known before the code runs."""
    ok = True
    rng = np.random.default_rng(31337)

    # 1. Ranked Robin is Condorcet-efficient by construction: the sincere column is 100%.
    _, res = run_cell(rng, "spatial2d", 51, 4, 300, 4, "burial", "utility")
    rr = res["RankedRobin"]["sincere"]
    ok &= abs(rr - 1.0) < 1e-9
    print(f"  RankedRobin sincere efficiency = {rr*100:.1f}%  (expect 100.0) "
          f"{'ok' if abs(rr - 1.0) < 1e-9 else 'UNEXPECTED'}")

    # 2. Burial keeps every ballot's top choice intact, and Plurality reads nothing
    #    else, so its winner must be bit-identical before and after. A failure here
    #    means the burial is reaching part of the ballot it has no business touching,
    #    and every other number in the run is suspect.
    rng = np.random.default_rng(4242)
    inert = 0
    tried = 0
    for _ in range(400):
        u = gen(rng, "spatial1d", 41, 5)
        sc = scores_from_util(u)
        cw = condorcet_winner(u)
        if cw < 0:
            continue
        tried += 1
        honest = winners(u, sc, 4)
        got = attack(u, sc, cw, 4, "burial", "displace")
        inert += got["Plurality"][0] == honest["Plurality"]
    ok &= inert == tried
    print(f"  Plurality  unchanged by burial   : {inert}/{tried} "
          f"{'ok' if inert == tried else 'UNEXPECTED'}")

    # 3. LATER-NO-HARM, MADE TESTABLE. A bloc that SHARES a favourite F cannot elect F
    #    under IRV by burying the Condorcet winner. Their buried ballots only transfer
    #    once F is eliminated, and an eliminated candidate cannot win — so if F wins the
    #    buried election, the burial changed nothing at all. This is the precise content
    #    of "later-no-harm protects IRV from burial", and it is much narrower than the
    #    slogan: it says nothing about a coalition whose members have DIFFERENT
    #    favourites, which the sweep shows unseats the CW from IRV routinely.
    rng = np.random.default_rng(20260814)
    viol = 0
    checked = 0
    for _ in range(600):
        u = gen(rng, "spatial1d", 41, 4)
        sc = scores_from_util(u)
        cw = condorcet_winner(u)
        if cw < 0:
            continue
        honest_irv = winners(u, sc, 4)["RCV-IRV"]
        for fav in range(u.shape[1]):
            if fav == cw:
                continue
            bloc = np.flatnonzero(u.argmax(1) == fav)      # a SHARED-favourite bloc
            if bloc.size == 0:
                continue
            cu, cs = cast_ballots(u, sc, bloc, cw, fav, "burial")
            checked += 1
            # F may only win the buried election if F already won the honest one.
            if winners(cu, cs, 4)["RCV-IRV"] == fav and honest_irv != fav:
                viol += 1
    ok &= viol == 0
    print(f"  IRV: shared-favourite burial never elects that favourite : "
          f"{checked - viol}/{checked} {'ok' if viol == 0 else 'UNEXPECTED'}")

    # 4. The bloc must be the voters who prefer the challenger, and nobody else.
    u = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 0.0]])
    b = bloc_for(u, 0, 1)
    ok &= b.tolist() == [1]
    print(f"  bloc_for picks only challenger-preferrers -> {b.tolist()} (expect [1]) "
          f"{'ok' if b.tolist() == [1] else 'UNEXPECTED'}")

    # 5. Burial must actually move the ballot: the buried candidate ends up last for
    #    every bloc member, and nothing else in their ranking changes.
    u = np.array([[0.9, 0.5, 0.1], [0.2, 0.8, 0.3]])
    cu, cs = cast_ballots(u, scores_from_util(u), np.array([1]), 0, 1, "burial")
    buried_last = bool(cu[1].argmin() == 0) and cs[1, 0] == 0
    untouched = bool((cu[0] == u[0]).all())
    ok &= buried_last and untouched
    print(f"  burial sinks the CW for the bloc only -> {buried_last and untouched}  "
          f"{'ok' if buried_last and untouched else 'UNEXPECTED'}")

    # 6. A rational bloc never submits a ballot that leaves it worse off, so under
    #    --objective utility no method can record a backfire. Backfires are what the
    #    'displace' objective buys, and that asymmetry is the point of having both.
    _, soft = run_cell(np.random.default_rng(99), "faction2d", 51, 4, 300, 4,
                       "burial", "utility")
    zero = all(soft[m]["backfired"] == 0.0 for m in METHODS)
    ok &= zero
    print(f"  no backfires under --objective utility -> {zero}  "
          f"{'ok' if zero else 'UNEXPECTED'}")

    print("\nSELFTEST", "PASSED" if ok else "FAILED")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--trials", type=int, default=1500, help="elections per cell")
    ap.add_argument("--seed", type=int, default=20260814)
    ap.add_argument("--approval-cutoff", type=int, default=4, metavar="N")
    ap.add_argument("--models", nargs="+",
                    default=["noise", "spatial1d", "spatial2d", "faction2d"])
    ap.add_argument("--candidates", nargs="+", type=int, default=[3, 5])
    ap.add_argument("--voters", nargs="+", type=int, default=[101])
    ap.add_argument("--strategy", choices=STRATEGIES, default="burial",
                    help="burial (sink the CW) or compromise (consolidate behind a "
                         "challenger). Burial is the attack Condorcet rules are open "
                         "to; compromise is the one IRV is open to. Run both.")
    ap.add_argument("--objective", choices=["utility", "displace"], default="utility",
                    help="what the bloc maximises: its own payoff (default, rational) "
                         "or removal of the CW at any cost (adversarial upper bound)")
    ap.add_argument("--price", action="store_true",
                    help="instead of the sweep, contrast the two objectives: how many "
                         "burials are reachable, how many a rational bloc would cast, "
                         "and how big a coalition a successful one needs")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        return selftest()
    if a.price:
        price(np.random.default_rng(a.seed), a.trials, a.approval_cutoff,
              a.models, a.candidates, a.voters)
        return 0

    print(f"Sincere-CW preservation under {a.strategy.upper()}, "
          f"--objective {a.objective}.  {a.trials} elections/cell, seed {a.seed}, "
          f"approval cutoff >= {a.approval_cutoff}.")
    print("Denominator: elections with a UNIQUE sincere Condorcet winner "
          "(cycles excluded — nothing to preserve).")
    print("sincere = honest ballots. held = the sincere CW still wins. paid/backfired "
          "= an attack\nwas submitted and beat / lost to voting honestly, "
          "FOR THE ATTACKERS. bloc = its mean size.")
    print("RankedRobin's sincere column is a CONTROL and must read 100.0%.\n")
    sweep(np.random.default_rng(a.seed), a.trials, a.approval_cutoff,
          a.models, a.candidates, a.voters, a.strategy, a.objective)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
