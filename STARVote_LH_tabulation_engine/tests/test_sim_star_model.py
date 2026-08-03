"""
test_sim_star_model.py
======================
Keeps the simulation's fast STAR model honest against the real engine.

`06_Other/simulations/star_vs_rr_divergence.py` cannot call the LH engine once
per trial (the sweep runs ~135k elections), so it reimplements STAR in numpy.
That shortcut bit once: the original model resolved every tie by numpy index
order, which disagrees with the engine's tie-break rungs, and it mislabelled a
dumped sample — `cycle_C10_fewV29_bloc_2` was published as "STAR elects A" when
the engine elects C (fixed 2026-07-26).

So the model is only allowed to exist if it agrees with the engine. This test
runs both on deliberately tie-heavy random profiles (few voters, narrow score
range) plus the 30 committed samples, and fails the moment they diverge.

Scope: this checks the MODEL against the engine. Whether the samples' prose and
answer keys match the engine is a separate question, covered more thoroughly by
test_star_vs_rr_labels.py (title, description, key, mirror and README row).
"""
import importlib.util
import random
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SIM = REPO_ROOT / "06_Other" / "simulations" / "star_vs_rr_divergence.py"
SAMPLES = REPO_ROOT / "05_Ranked_Robin" / "02_Examples" / "star_vs_rr_divergence"

np = pytest.importorskip("numpy", reason="the simulation model is numpy-based")


def _load_sim():
    if not SIM.exists():
        pytest.skip("star_vs_rr_divergence.py not present")
    spec = importlib.util.spec_from_file_location("star_vs_rr_divergence", SIM)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _engine_winner(scores, names):
    """The real thing: starvote's star(), with the engine's own lot fallback."""
    import starvote

    import_path = REPO_ROOT / "STARVote_LH_tabulation_engine"
    spec = importlib.util.spec_from_file_location(
        "starvote_larry_hastings", import_path / "starvote_larry_hastings.py"
    )
    lh = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lh)

    ballots = [{n: int(row[i]) for i, n in enumerate(names)} for row in scores]
    winners = starvote.election(
        method=starvote.star,
        ballots=ballots,
        seats=1,
        # no lot_numbers -> falls back to ballot-key (column) order, which is
        # exactly what the model's min-index lot models.
        tiebreaker=lh.LotNumberTiebreaker(silent=True),
        verbosity=0,
        maximum_score=5,
        print=lambda *a, **k: None,
    )
    return winners[0]


def _names(c):
    return [chr(ord("A") + i) for i in range(c)]


@pytest.mark.parametrize("voters,cands", [(5, 3), (7, 4), (9, 5), (15, 3), (12, 7)])
def test_model_matches_engine_on_random_profiles(voters, cands):
    """Tie-heavy profiles: few voters and a narrow score range make ties common,
    which is precisely where an index-order shortcut drifts from the engine."""
    sim = _load_sim()
    names = _names(cands)
    rng = random.Random(f"star-model-{voters}-{cands}")

    for trial in range(60):
        # Narrow the range on some trials to manufacture ties on purpose.
        hi = 5 if trial % 3 else 2
        scores = np.array(
            [[rng.randint(0, hi) for _ in range(cands)] for _ in range(voters)]
        )
        if scores.sum() == 0:  # engine has nothing to work with
            continue
        model = names[sim.star_winner(scores)]
        engine = _engine_winner(scores, names)
        assert model == engine, (
            f"simulation model and LH engine disagree on:\n"
            f"{names}\n" + "\n".join(",".join(map(str, r)) for r in scores) + "\n"
            f"model={model} engine={engine}\n"
            "Fix star_winner() in 06_Other/simulations/star_vs_rr_divergence.py "
            "to match starvote's star() tie-break rungs."
        )


def test_model_matches_the_dumped_samples():
    """The 30 published samples: the model must reproduce every committed winner."""
    sim = _load_sim()
    yamls = sorted(SAMPLES.glob("*.yaml"))
    if not yamls:
        pytest.skip("no star_vs_rr_divergence samples present")

    for y in yamls:
        text = y.read_text()
        block = text.split("ballots: |-", 1)[1].split("\nexpected_winners")[0]
        lines = [ln.strip() for ln in block.strip().splitlines() if ln.strip()]
        header = lines[0]
        weighted = header.startswith("Count:")
        names = (header.split(":", 1)[1] if weighted else header).split(",")

        rows = []
        for ln in lines[1:]:
            if weighted:
                count, vals = ln.split(":", 1)
                rows += [[int(v) for v in vals.split(",")]] * int(count)
            else:
                rows.append([int(v) for v in ln.split(",")])

        model = names[sim.star_winner(np.array(rows))]
        mirror_text = (
            SAMPLES / "star_vs_rr_divergence_tabulated" / f"{y.stem}_tabulated.txt"
        ).read_text()
        engine = re.search(r"^  STAR +=\s*(\S+)", mirror_text, re.M).group(1)

        assert model == engine, (
            f"{y.name}: model says {model}, the engine's own mirror says {engine}."
        )
