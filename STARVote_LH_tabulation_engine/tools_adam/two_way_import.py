#!/usr/bin/env python3
"""Import a BetterVoting export into LH *two ways* and compare the winners.

The point: on a **lot-decided tie** (a "dead rung" — the ballots tie at every
deterministic rung, so only the tie-break order decides), the winner depends
entirely on which lot order you use. This tool tabulates the same BV export two
ways with the LH engine:

  1. BV / "old" approach  — the tie-break order BetterVoting actually DREW at
     count time (its `perm` / `tieBreakOrder`, mapped to `lot_numbers:` by the
     repo converter). Reproduces BetterVoting's own elected winner.
  2. Published / "new" approach — a deterministic, pre-published lot order you
     choose (default: the reverse of BV's draw, which flips the winner of a full
     tie). This is the fix BV issue #1063 asks for.

If the election really is lot-decided, the two winners DIFFER — same ballots,
different result, purely from the tie-break order. If the ballots actually
decided it, both agree (and the tool says so).

Usage
-----
  python two_way_import.py <bv_export.json>
  python two_way_import.py <bv_export.json> --published "Ada, Ben"
  python two_way_import.py <bv_export.json> --out-dir 06_Other/_demo_dropbox

Writes `<base>_bv_order.yaml` and `<base>_published_order.yaml` next to the JSON
(or into --out-dir), runs the LH engine on each, and prints the comparison.
Works on any BV export, e.g. one dropped in `06_Other/_demo_dropbox/`.
"""
from __future__ import annotations

import argparse
import importlib.util
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ENGINE_DIR = HERE.parent                      # STARVote_LH_tabulation_engine/
REPO = ENGINE_DIR.parent                      # repo root
ENGINE = ENGINE_DIR / "starvote_larry_hastings.py"
CONVERTER = REPO / "YAML_library" / "1_positive" / "01_convert_json_yaml.py"

sys.path.insert(0, str(ENGINE_DIR))
sys.path.insert(0, str(HERE))
from scenario_eval import scenario_winners  # noqa: E402

LOT_FLAG = "[Lot-decided tie — rare]"


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _convert_to_yaml(json_path: Path) -> Path:
    """Run the repo converter on a copy of the JSON in an isolated temp dir and
    return the produced YAML path (with BV's lot order + winner embedded)."""
    converter = _load_module("bv_converter", CONVERTER)
    engine = _load_module("starvote_larry_hastings", ENGINE)
    tmp = Path(tempfile.mkdtemp(prefix="two_way_"))
    src = tmp / json_path.name
    shutil.copy(json_path, src)
    converter.convert_election_data(str(src), engine, embed_report=False,
                                    include_candidates=False)
    produced = sorted((tmp / "_generated").glob("*.yaml"),
                      key=lambda p: p.stat().st_mtime, reverse=True)
    if not produced:
        raise SystemExit("error: converter produced no YAML (bad or unsupported export).")
    return produced[0]


def _race(data: dict) -> dict:
    elec = data.get("election", data)
    races = elec.get("races") or [elec]
    return races[0]


def _run_flag(path: Path) -> bool:
    proc = subprocess.run([sys.executable, str(ENGINE), str(path)],
                          capture_output=True, text=True)
    return LOT_FLAG in proc.stdout


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Import a BV export into LH two ways and compare winners.")
    p.add_argument("json", help="path to the BetterVoting .json export")
    p.add_argument("--published", default=None,
                   help='pre-published lot order, e.g. "Ada, Ben" '
                        "(default: reverse of BV's drawn order)")
    p.add_argument("--out-dir", default=None,
                   help="where to write the two YAMLs (default: next to the JSON)")
    args = p.parse_args(argv)

    json_path = Path(args.json).resolve()
    if not json_path.exists():
        raise SystemExit(f"error: no such file: {json_path}")
    out_dir = Path(args.out_dir).resolve() if args.out_dir else json_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    base = json_path.stem

    # 1) Convert -> the BV-order YAML (BV's drawn lot order + winner).
    produced = _convert_to_yaml(json_path)
    data = yaml.safe_load(produced.read_text(encoding="utf-8"))
    race = _race(data)
    bv_lot = race.get("lot_numbers")
    if not bv_lot:
        raise SystemExit(
            "error: the export carries no tie-break order (no `perm` / `tieBreakOrder`),\n"
            "       so BV's draw can't be reconstructed. Re-export with the sequence\n"
            "       included (BV #1371) — otherwise there's nothing to compare.")

    bv_yaml = out_dir / f"{base}_bv_order.yaml"
    bv_yaml.write_text(produced.read_text(encoding="utf-8"), encoding="utf-8")

    # 2) Build the published-order variant.
    if args.published:
        pub_lot = [c.strip() for c in args.published.split(",") if c.strip()]
        missing = [c for c in pub_lot if c not in bv_lot]
        if sorted(pub_lot) != sorted(bv_lot):
            raise SystemExit(
                f"error: --published must be a permutation of {bv_lot}; got {pub_lot}"
                + (f" (unknown: {missing})" if missing else ""))
    else:
        pub_lot = list(reversed(bv_lot))   # guarantees a different first pick

    pub_data = yaml.safe_load(produced.read_text(encoding="utf-8"))
    _race(pub_data)["lot_numbers"] = pub_lot
    # Drop any embedded winner assertion — it was BV's; recompute below.
    _race(pub_data).pop("expected_results", None)
    pub_yaml = out_dir / f"{base}_published_order.yaml"
    pub_yaml.write_text(
        yaml.dump(pub_data, sort_keys=False, allow_unicode=True), encoding="utf-8")

    # 3) Tabulate both and compare.
    bv_winner = scenario_winners(bv_yaml)[0]
    pub_winner = scenario_winners(pub_yaml)[0]
    bv_flag = _run_flag(bv_yaml)
    pub_flag = _run_flag(pub_yaml)

    print("═" * 70)
    print("Two-way LH import of a BetterVoting export")
    print(f"  source: {json_path.name}")
    print(f"  candidates / tie stack: {bv_lot}")
    print("─" * 70)
    print(f"  1) BV / old approach   lot {bv_lot}")
    print(f"       → winner: {bv_winner}   {'[lot-decided]' if bv_flag else '[ballots decided]'}")
    print(f"     wrote {bv_yaml.name}")
    print(f"  2) published / new     lot {pub_lot}")
    print(f"       → winner: {pub_winner}   {'[lot-decided]' if pub_flag else '[ballots decided]'}")
    print(f"     wrote {pub_yaml.name}")
    print("─" * 70)
    if bv_winner != pub_winner:
        print(f"  ⚠ DIFFERENT WINNERS: BV drew {bv_winner}, the published order gives")
        print(f"    {pub_winner} — same ballots, decided entirely by the lot order.")
        print("    This is exactly why the lot must be deterministic (BV #1063).")
    else:
        print(f"  Both approaches agree ({bv_winner}). The ballots decided this one —")
        print("    it isn't a lot-decided tie, so the tie-break order doesn't matter here.")
    print("═" * 70)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
