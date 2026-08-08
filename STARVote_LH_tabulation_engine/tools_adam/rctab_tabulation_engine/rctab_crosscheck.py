#!/usr/bin/env python3
"""
rctab_crosscheck.py — run a repo case through RCTab and diff it against ours.

`rctab_convert.py` writes the CSV + config; this runs the real tabulator on them,
parses its machine-readable `_detailed_report.json`, and reports the round-by-round
count next to what this repo's engine says.

WHAT AGREEMENT HERE IS WORTH
----------------------------
RCTab is federally tested under the VVSG and state-certified; it is the software
that counts real elections. So a match is evidence our arithmetic is the arithmetic
jurisdictions actually run. It is NOT evidence that instant runoff picks good
winners — certifying an implementation says nothing about the method, and every
center-squeeze / exhausted-ballot critique in this repo survives RCTab counting
perfectly.

THE TWO SWEEPS (why this tool exists at all)
--------------------------------------------
Winners agreeing is the boring half. The interesting half is HOW each engine
reaches an arbitrary decision when the ballots genuinely don't settle it:

  --row-permutations   re-runs the case under every ordering of the ballot rows.
                       An ANONYMOUS rule ignores who cast which ballot, so the
                       winner must not move. The vendored pyrankvote's does.
  --candidate-orders   re-runs it under different declared candidate orders, which
                       is what `tiebreakMode: useCandidateOrder` breaks ties by.
                       RCTab's winner DOES move here — but the lever is a value
                       written in the config and echoed in the audit log, where
                       ours is the order the YAML's ballot rows happen to be typed.

Both engines are arbitrary. Only one is auditable. That's the finding.

Usage:
    RCTAB_HOME=/path/to/rcv \\
      uv run STARVote_LH_tabulation_engine/tools_adam/rctab_tabulation_engine/rctab_crosscheck.py FILE.yaml
    ... --row-permutations          # anonymity check (capped; 6 ballots = 720 runs)
    ... --candidate-orders alpha,reverse,ballot
    ... --batch-elimination --tiebreak useCandidateOrder

RCTAB_HOME must point at an unpacked RCTab (the folder holding bin/RCTab). Get one
from https://github.com/BrightSpots/rcv/releases — the macOS/Linux zips bundle their
own JDK 21, so nothing else is needed. Verify the published .sha512 before unpacking.
"""
import argparse
import glob
import itertools
import json
import os
import shutil
import subprocess
import sys
import tempfile

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from rctab_convert import add_args, convert  # noqa: E402

MAX_PERMUTATIONS = 720  # 6! — beyond this the sweep is not a sane thing to run


def find_rctab():
    """The launcher, from RCTAB_HOME — an unpacked release OR a macOS .app bundle.

    The release zips unpack to `<home>/bin/RCTab`, but the macOS build is shipped as
    `RCTab.app`, where the launcher is `Contents/MacOS/RCTab` and there is no bin/ at
    all. Accept both, and accept being pointed at either the .app or its parent, so
    RCTAB_HOME can be whatever the user actually has on disk.
    """
    home = os.environ.get("RCTAB_HOME")
    if not home:
        raise SystemExit(
            "RCTAB_HOME is not set. Point it at an unpacked RCTab or a macOS RCTab.app:\n"
            "  export RCTAB_HOME=/path/to/rcv            # release zip (has bin/RCTab)\n"
            "  export RCTAB_HOME=/path/to/RCTab.app      # macOS bundle\n"
            "Download from https://github.com/BrightSpots/rcv/releases (the zips bundle a JDK)."
        )
    candidates = [
        os.path.join(home, "bin", "RCTab"),                      # unpacked release
        os.path.join(home, "Contents", "MacOS", "RCTab"),         # RCTAB_HOME=…/RCTab.app
        os.path.join(home, "RCTab.app", "Contents", "MacOS", "RCTab"),  # its parent folder
    ]
    for launcher in candidates:
        if os.path.isfile(launcher) and os.access(launcher, os.X_OK):
            return launcher
    raise SystemExit(
        f"no RCTab launcher under {home} — is RCTAB_HOME right? Looked for:\n  "
        + "\n  ".join(candidates)
    )


def rctab_version(launcher):
    """The app's own version string, for the config's tabulatorVersion.

    RCTab refuses a config whose tabulatorVersion is newer than itself ("Unable to
    process a config file with version 2.1.0 using older version 2.0.0"), so the
    converter has to be told which one is on this machine rather than assuming.
    """
    try:
        out = subprocess.run([launcher, "--cli", "--help"], capture_output=True,
                             text=True, timeout=120)
        for line in (out.stdout + out.stderr).splitlines():
            if line.startswith("RCTab version "):
                return line.split("RCTab version ", 1)[1].strip()
    except Exception:
        pass
    return None


def run_rctab(launcher, cfg_path, operator="star-voting-library crosscheck"):
    """Run one tabulation; return (parsed detailed report | None, stdout)."""
    workdir = os.path.dirname(cfg_path)
    out = subprocess.run(
        [launcher, "--cli", os.path.basename(cfg_path), "--name", operator],
        cwd=workdir, capture_output=True, text=True,
    )
    blob = out.stdout + out.stderr
    reports = sorted(glob.glob(os.path.join(workdir, "output", "*", "*_detailed_report.json")))
    if not reports:
        return None, blob
    with open(reports[-1], encoding="utf-8") as fh:
        return json.load(fh), blob


def winners_of(report):
    """Every candidate RCTab elects, in the order the rounds elect them.

    Multi-seat matters here: an STV report elects across several rounds, and may elect
    more than one in the SAME round under multiWinnerAllowMultipleWinnersPerRound, so
    stopping at the first `elected` (which is all a single-winner count ever has) would
    silently report a 3-seat contest as a 1-seat one and "agree" with nothing.
    """
    if not report:
        return []
    elected = []
    for rnd in report.get("results", []):
        for tr in rnd.get("tallyResults", []):
            if "elected" in tr and tr["elected"] not in elected:
                elected.append(tr["elected"])
    return elected


def winner_of(report):
    """First elected candidate, or None — the single-winner view the sweeps compare on."""
    got = winners_of(report)
    return got[0] if got else None


def tiebreak_lines(blob):
    return [ln.split(" INFO: ", 1)[-1] for ln in blob.splitlines() if "tie-breaker" in ln]


def expected_from_yaml(path):
    """What THIS repo's engine reports — the answer the test suite guards."""
    try:
        import yaml
        with open(path, encoding="utf-8") as fh:
            doc = yaml.safe_load(fh) or {}
        return doc.get("expected_winners") or []
    except Exception:
        return []


def _num(v):
    """Tally values arrive as strings, and under STV they are FRACTIONAL ('5.9995').

    int() on those raises — which single-winner IRV never revealed, because whole-vote
    transfers keep every tally an integer. Sort on the float; print what RCTab wrote.
    """
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def print_rounds(report):
    for rnd in report.get("results", []):
        tally = rnd.get("tally", {})
        line = "  ".join(f"{c} {v}" for c, v in sorted(tally.items(), key=lambda kv: -_num(kv[1])))
        acts = []
        for tr in rnd.get("tallyResults", []):
            if "elected" in tr:
                acts.append(f"ELECTED {tr['elected']}")
            if "eliminated" in tr:
                moved = ", ".join(f"{k}+{v}" for k, v in (tr.get("transfers") or {}).items())
                acts.append(f"eliminated {tr['eliminated']}" + (f" → {moved}" if moved else ""))
        print(f"    round {rnd['round']} (threshold {rnd.get('threshold','?')}):  {line}"
              + (f"   [{'; '.join(acts)}]" if acts else ""))


def sweep_rows(launcher, args, cfg_path, csv_path):
    """Anonymity check: same ballots, every row order."""
    import csv as csvmod
    rows = list(csvmod.reader(open(csv_path, encoding="utf-8")))
    hdr, body = rows[0], rows[1:]
    perms = list(itertools.permutations(range(len(body))))
    if len(perms) > MAX_PERMUTATIONS:
        print(f"\n  row-permutation sweep SKIPPED: {len(body)} ballots = {len(perms)} orderings "
              f"(cap {MAX_PERMUTATIONS}). Anonymity is not sampled here — no claim is made.")
        return None
    winners = {}
    with tempfile.TemporaryDirectory() as tmp:
        for i, perm in enumerate(perms):
            sub = os.path.join(tmp, f"p{i}")
            os.makedirs(sub)
            shutil.copy(cfg_path, os.path.join(sub, os.path.basename(cfg_path)))
            with open(os.path.join(sub, os.path.basename(csv_path)), "w",
                      newline="", encoding="utf-8") as fh:
                w = csvmod.writer(fh)
                w.writerow(hdr)
                w.writerows([body[j] for j in perm])
            rep, _ = run_rctab(launcher, os.path.join(sub, os.path.basename(cfg_path)))
            winners.setdefault(winner_of(rep), []).append(i)
    print(f"\n  ROW-ORDER SWEEP — {len(perms)} orderings of the same {len(body)} ballots:")
    for wnr, which in sorted(winners.items(), key=lambda kv: -len(kv[1])):
        print(f"    {wnr or '(no winner)'}: {len(which)}/{len(perms)}")
    if len(winners) == 1:
        print("    ✅ STABLE — the winner does not depend on ballot row order (anonymous).")
    else:
        print("    ❌ UNSTABLE — the winner moves with row order. That is an anonymity failure.")
    return winners


def sweep_candidate_orders(launcher, args, cands, spec):
    """The declared-tiebreak lever: same ballots, different candidate orders."""
    orders = []
    for name in [s.strip() for s in spec.split(",") if s.strip()]:
        if name == "alpha":
            orders.append(("alpha", sorted(cands)))
        elif name == "reverse":
            orders.append(("reverse", sorted(cands, reverse=True)))
        elif name == "ballot":
            orders.append(("ballot", list(cands)))
        elif name == "all":
            for p in itertools.permutations(sorted(cands)):
                orders.append((",".join(p), list(p)))
        else:
            orders.append((name, [c.strip() for c in name.split("|")]))
    print(f"\n  CANDIDATE-ORDER SWEEP — tiebreakMode={args.tiebreak}:")
    seen = {}
    with tempfile.TemporaryDirectory() as tmp:
        for label, order in orders:
            sub = os.path.join(tmp, label.replace(",", "_").replace("|", "_"))
            os.makedirs(sub, exist_ok=True)
            local = argparse.Namespace(**vars(args))
            local.outdir = sub
            local.candidate_order = ",".join(order)
            _csv, cfg = convert_quiet(local)
            rep, _ = run_rctab(launcher, cfg)
            w = winner_of(rep)
            seen.setdefault(w, 0)
            seen[w] += 1
            print(f"    {', '.join(order):<28} → {w or '(no winner)'}")
    if len(seen) > 1:
        print(f"    ⚠️  {len(seen)} different winners — the tiebreak decides this election.")
        print("       RCTab's lever is a config value, echoed in the audit log. Ours is row order.")
    else:
        print("    the declared order does not change the winner here.")
    return seen


def convert_quiet(args):
    """convert() but without its stdout chatter."""
    buf, sys.stdout = sys.stdout, open(os.devnull, "w")
    try:
        return convert(args)
    finally:
        sys.stdout.close()
        sys.stdout = buf


def main():
    p = add_args(argparse.ArgumentParser(description=__doc__.split("\n")[1]))
    p.add_argument("--row-permutations", action="store_true",
                   help="re-run under every ballot row order (anonymity check)")
    p.add_argument("--candidate-orders", metavar="SPEC",
                   help="comma list of alpha|reverse|ballot|all, or explicit 'A|B|C' orders")
    p.add_argument("--keep", action="store_true", help="keep the RCTab output tree")
    p.add_argument("--pin-version", action="store_true",
                   help="use --tabulator-version as given instead of detecting the installed app")
    args = p.parse_args()

    launcher = find_rctab()
    # Match the config to the installed app unless the caller pinned a version: RCTab
    # hard-fails on a config newer than itself, and the converter's default tracks the
    # newest release, not whatever is on this machine.
    if not args.pin_version:
        detected = rctab_version(launcher)
        if detected:
            args.tabulator_version = detected
    stem = os.path.splitext(os.path.basename(args.yaml))[0]
    print(f"\n=== {stem} ===")
    print(f"  RCTab      : {args.tabulator_version}  ({launcher})")
    csv_path, cfg_path = convert_quiet(args)
    cands = [c["name"] for c in json.load(open(cfg_path, encoding="utf-8"))["candidates"]]
    print(f"  candidates : {', '.join(cands)}   ({args.candidate_order} order)")
    print(f"  rules      : tiebreak={args.tiebreak}  batchElimination={args.batch_elimination}")

    report, blob = run_rctab(launcher, cfg_path)
    if report is None:
        sev = [ln for ln in blob.splitlines() if "SEVERE" in ln]
        raise SystemExit("  RCTab produced no report:\n    " + "\n    ".join(sev[:6] or [blob[-500:]]))

    print("\n  RCTab count:")
    print_rounds(report)
    rc_winners = winners_of(report)
    for ln in tiebreak_lines(blob):
        print(f"    ⚖  {ln}")

    with open(cfg_path, encoding="utf-8") as fh:
        rules = json.load(fh)["rules"]
    seats = int(rules.get("numberOfWinners") or 1)

    ours = expected_from_yaml(args.yaml)
    print(f"\n  RCTab      : {', '.join(rc_winners) if rc_winners else '(no winner)'}")
    print(f"  this repo  : {', '.join(ours) if ours else '(no expected_winners)'}")
    if seats > 1:
        thr = ("floor(V/(S+1))+1, hand-count Droop" if not rules["nonIntegerWinningThreshold"]
               else "V/(S+1)+10^-d, exact Droop")
        print(f"  quota rule : {thr}   ({seats} seats)")

    if not ours:
        pass
    elif seats > 1:
        # Multi-seat: compare the SEATED SET. Order is not meaningful — STV fills seats
        # in count order, and expected_winners is authored in whatever order reads best —
        # but membership and COUNT both are. A short set is a real disagreement.
        if set(rc_winners) == set(ours):
            print("  ✅ AGREE — same seated set.")
        else:
            only_rc = sorted(set(rc_winners) - set(ours))
            only_us = sorted(set(ours) - set(rc_winners))
            print("  ❌ DISAGREE — investigate before quoting either number.")
            if only_rc:
                print(f"     RCTab seats, we don't : {', '.join(only_rc)}")
            if only_us:
                print(f"     we seat, RCTab doesn't: {', '.join(only_us)}")
            if len(rc_winners) != seats:
                print(f"     NOTE: RCTab elected {len(rc_winners)} of {seats} seats.")
    elif winner_of(report) in ours:
        print("  ✅ AGREE")
    else:
        print("  ❌ DISAGREE — investigate before quoting either number.")

    if args.candidate_orders:
        sweep_candidate_orders(launcher, args, cands, args.candidate_orders)
    if args.row_permutations:
        sweep_rows(launcher, args, cfg_path, csv_path)

    if not args.keep:
        shutil.rmtree(os.path.join(os.path.dirname(cfg_path), "output"), ignore_errors=True)
        for log in glob.glob(os.path.join(os.path.dirname(cfg_path), "rcv_*.log")):
            os.remove(log)
    print()


if __name__ == "__main__":
    main()
