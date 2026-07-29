#!/usr/bin/env python3
"""bv_replay_tiebreak.py — recompute BetterVoting's "random" tiebreak order.

BetterVoting's Ranked Robin (and STAR) tiebreak of last resort is labelled
`tieBreakType: "random"`, which sounds like a coin flip whose reasoning is lost.
It is not. It is a SEEDED shuffle, and its own source says so:

    "Our random tiebreaker protocol is written to be deterministic to ensure that
     we get the same results regardless of how many times the tabulator is re-run"
        -- packages/backend/src/Tabulators/shuffleCandidatesForRandomTiebreak.ts

    seed = (rawVoteCount + hashStringToInt(raceId)) >>> 0
    getTinyRand(0, seed).shuffle(candidates)
    candidates.forEach((c, i) => c.tieBreakOrder = i)

The shuffled order ships in the results JSON as `perm`, with each candidate's
index stored as `tieBreakOrder`. This script is a Python port of that shuffle
(TinyRand v0, deliberately language-agnostic) so the claim is checkable rather
than taken on trust: point it at a frozen `_bv_export.json` and it recomputes
each race's `perm` and diffs it against what BetterVoting recorded.

WHY THIS MATTERS — the distinction it makes concrete:
  * RECORDED / reproducible — yes. Re-tally, re-fetch, or re-run this script and
    you get the same order.
  * DERIVABLE FROM THE BALLOTS — no. The only inputs are the ballot COUNT and the
    raceId string. No ranking, score or preference touches the seed. Rewrite every
    ballot (keeping the count, and keeping the race tied) and the same candidate
    still wins the tiebreak.
That is why a case whose WINNER turns on a BV tiebreak is kept LH-only in this
repo: LH's `lot_numbers` is a published input a reader can check, while BV's order
is carried by a database UUID. See
05_Ranked_Robin/concepts/rr_tiebreak_lh_vs_bv.md and the confirmation cases
05_Ranked_Robin/rr_tiebreaks/bv2261_y2fbpc_tiebreak_recorded.md (3 candidates)
and bv2262_*.md (9 candidates).

Usage:
    python3 bv_replay_tiebreak.py <path to *_bv_export.json>
    python3 bv_replay_tiebreak.py <bvid>            # fetches anonymously

Exit code 0 if every race matches, 1 otherwise. Stdlib only.
"""
from __future__ import annotations

import json
import sys
import urllib.request

M32 = 0xFFFFFFFF
API = "https://bettervoting.com/API"


# --- TinyRand v0 (port of tinyrand.ts) -------------------------------------

def _imul(a: int, b: int) -> int:
    """Math.imul — 32-bit signed multiply."""
    r = (a * b) & M32
    return r - 0x100000000 if r >= 0x80000000 else r


def hash_string_to_int(s: str) -> int:
    """hashStringToInt(raceId) from shuffleCandidatesForRandomTiebreak.ts."""
    h = 0
    for ch in s:
        h = (_imul(31, h) + ord(ch)) & M32
        if h >= 0x80000000:          # the trailing `| 0` (signed 32-bit)
            h -= 0x100000000
    return h


class TinyRand0:
    BITS = 32
    NSTATES = 1 << 16

    def __init__(self, seed: int = 0) -> None:
        self.state = [0, 0, 0, 0]
        self.seed(seed)

    def seed(self, seed: int = 0) -> None:
        s = seed & M32
        for i in range(4):
            s = ((s * 121525) + 386076519) & M32
            self.state[i] = s
        for _ in range(6):           # scramble
            self._get()

    def _get(self) -> int:
        x = self.state[0] & M32
        x = (x ^ ((x << 11) & M32)) & M32
        x = (x ^ (x >> 8)) & M32
        self.state[0] = self.state[1]
        self.state[1] = self.state[2]
        self.state[2] = self.state[3]
        w = self.state[3] & M32
        self.state[3] = ((w ^ (w >> 19)) ^ x) & M32
        return self.state[3]

    def shuffle(self, a: list) -> None:
        if len(a) > self.NSTATES:
            raise ValueError(f"List too long: {len(a)}")
        shift, hi = self.BITS - 1, 2
        for j in range(1, len(a)):
            if j == hi:
                hi <<= 1
                shift -= 1
            while True:
                i = self._get() >> shift
                if i <= j:
                    break
            a[i], a[j] = a[j], a[i]


def bv_perm(candidates: list, raw_vote_count: int, race_id: str) -> list:
    """The tiebreak order BV would draw. NOTE: no ballot CONTENT is an input."""
    seed = (raw_vote_count + hash_string_to_int(race_id)) & M32
    order = list(candidates)
    TinyRand0(seed).shuffle(order)
    return order


# --- driver ----------------------------------------------------------------

def _load(arg: str) -> dict:
    if arg.endswith(".json"):
        with open(arg, encoding="utf-8") as fh:
            return json.load(fh)
    # treat as a bvid — assemble what we need from the anonymous endpoints
    def get(path):
        with urllib.request.urlopen(f"{API}/{path}", timeout=30) as r:
            return json.loads(r.read().decode())
    election = get(f"Election/{arg}")["election"]
    ballots = get(f"Election/{arg}/anonymizedBallots")
    results = get(f"ElectionResult/{arg}")
    if isinstance(ballots, dict):
        ballots = ballots.get("ballots", ballots.get("Ballots", []))
    if isinstance(results, dict):
        results = results.get("results", results.get("Results", results))
    return {"Election": election, "Ballots": ballots, "Results": results}


def main(argv: list) -> int:
    if len(argv) != 2:
        print(__doc__.strip().split("Usage:")[1].strip(), file=sys.stderr)
        return 2

    data = _load(argv[1])
    races = data["Election"]["races"]
    results = data["Results"]
    n_raw = len(data["Ballots"])
    names = {c["candidate_id"]: c["candidate_name"]
             for r in races for c in r["candidates"]}

    print(f'election : {data["Election"].get("election_id")} — '
          f'{data["Election"].get("title")}')
    print(f"raw ballot count : {n_raw}")
    print("(the ballots' CONTENT is never an input below — only the count and the raceId)\n")

    ok = True
    for race, res in zip(races, results):
        recorded = res.get("perm")
        tbt = res.get("tieBreakType")
        title = race.get("title", "")
        print(f"race {race['race_id']}")
        print(f"  title        : {title}")
        print(f"  tieBreakType : {tbt}")
        if not recorded:
            print("  no `perm` recorded — nothing to replay (no tiebreak reached)\n")
            continue
        seed = (n_raw + hash_string_to_int(race["race_id"])) & M32
        mine = bv_perm([c["candidate_name"] for c in race["candidates"]],
                       n_raw, race["race_id"])
        theirs = [names.get(cid, cid) for cid in recorded]
        match = mine == theirs
        ok = ok and match
        print(f"  seed         : ({n_raw} + hash(raceId)) >>> 0 = {seed}")
        print(f"  recomputed   : {mine}")
        print(f"  BV recorded  : {theirs}")
        print(f"  MATCH        : {'yes ✓' if match else 'NO ✗'}")
        if res.get("elected"):
            print(f"  BV winner    : {res['elected'][0]['name']}"
                  f"   (= first in perm: {mine[0]})")
        print()

    print("all races reproduced ✓" if ok else "MISMATCH — see above")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
