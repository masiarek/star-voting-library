#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyjwt", "requests", "cryptography"]
# ///
"""
create_bv_test_election.py — create BetterVoting test elections via the REST API
================================================================================

Creates the BV95a / BV95b "Majority Criterion" demo elections on bettervoting.com
and casts their ballots, using the API recipe from the Discord-bot integration
doc (POST /API/Elections, POST /API/Election/{id}/vote, GET /API/Election/{id}).
Then it saves each finished election object as JSON into ../../_demo_dropbox/ so
it can be promoted into the BV95a/BV95b cases.

WHY A SCRIPT (and not the UI, or Claude): the BetterVoting builder UI is fiddly to
automate, and Claude's sandbox can't make external HTTP calls or hold your
credentials. You run this locally with your own identity; nothing secret is stored
in this file.

--------------------------------------------------------------------------------
SETUP  (uv-native — dependencies are declared inline above, PEP 723)
--------------------------------------------------------------------------------
    # Just run it with uv; it installs pyjwt/requests/cryptography automatically
    # into an ephemeral env — no pip, no .venv pollution:
    uv run STARVote_LH_tabulation_engine/tools_adam/create_bv_test_election.py

    # (Optional) override the defaults below via environment variables.

    # A throwaway identity. The doc's trick: sign the JWT with a secret that
    # equals the user id ("for now we'll just have it match"). This creates a
    # self-consistent custom_id_token the backend accepts — no real account
    # password/secret is used or stored.
    export BV_USER_ID="masiarek_mc_demo"          # any stable string you choose

    # A TEMPLATE election to copy the object shape from (safest per the doc,
    # which duplicates an existing election rather than hand-building the payload).
    # Use ANY simple STAR / single-winner election id you can GET publicly.
    # If copying breaks, try a different template id.
    export BV_TEMPLATE_ID="pet"

    python3 create_bv_test_election.py

--------------------------------------------------------------------------------
NOTES / CAVEATS (read these)
--------------------------------------------------------------------------------
* This was written from the API doc WITHOUT being able to test it — treat it as a
  strong first draft. It prints every response so you can see exactly where any
  step fails and adjust. The three endpoints and the vote payload come straight
  from the doc.
* Casting multiple ballots: each ballot uses a distinct `temp_id` cookie, so the
  backend doesn't reject them as "already voted."
* Results: STAR results are computed when the election is finalized/closed. These
  two elections have NO ties, so the outcome is deterministic (Ada / Bruno). If
  the saved JSON lacks a Results block, open the election in the UI once and close
  it, then re-run just the final GET (or use the printed URL to export normally).
* If POST /API/Elections rejects the copied payload, the most likely fix is the
  `settings`/voter-access fields — pick a template election that is already an
  unrestricted / unlimited-voting poll so those fields copy over correctly.
"""

import json
import os
import sys
import time
import uuid
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import jwt          # PyJWT
    import requests
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
except ImportError:
    sys.exit("Missing deps. Run this script with:  uv run <this file>  "
             "(deps are declared inline via PEP 723).")

API = "https://bettervoting.com/API"
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "_demo_dropbox")

# Defaults so it runs from PyCharm's green button with NO env setup. Override via
# environment if you like. BV_USER_ID becomes the election's owner_id — set it to
# your REAL BetterVoting account id so script-made elections show up in /manage
# (the manage list is filtered by owner_id). Adam's account (Admin1) is the id
# below; it's not a secret (it's the owner_id in the frozen _bv_export.json files).
USER_ID = os.environ.get("BV_USER_ID", "ea09e7c7-b00d-427a-bef8-32ade437d49d")
TEMPLATE_ID = os.environ.get("BV_TEMPLATE_ID", "pet")

# Ballots are cast CONCURRENTLY (each is an independent voter, so order doesn't
# matter). A bounded pool keeps us fast without hammering the live server — the
# serial version waited ~1s per POST (100 ballots ≈ 2-4 min); at 8-wide that's
# ~15-30s. Bump BV_CONCURRENCY if you're impatient and the server tolerates it,
# but keep it modest — this is a shared public service.
CONCURRENCY = max(1, int(os.environ.get("BV_CONCURRENCY", "8")))

# The election title is MEANINGFUL and PUBLIC — these elections are listed on
# BetterVoting and their name shows on the results page, so it must read like a
# real election. NO "trash/delete/test" junk. We prepend only the BV Test ID
# (test_id, e.g. "BV2132") for traceability; the descriptive title carries the
# rest. Default prefix is empty; set BV_TITLE_PREFIX only if you deliberately want
# an extra tag. (API-created elections can't be deleted from the UI anyway, so a
# "delete me" tag was never actionable — and it looked terrible in public.)
TITLE_PREFIX = os.environ.get("BV_TITLE_PREFIX", "")

# The backend now requires ASYMMETRIC auth: the election's `auth_key` must be a
# PEM RS256 *public* key, and the identity token is signed with the matching
# *private* key. We mint a fresh keypair per run (self-consistent: the create
# request carries the public key AND a token the backend verifies against it).
_KEY = rsa.generate_private_key(public_exponent=65537, key_size=2048)
PRIVATE_PEM = _KEY.private_bytes(
    serialization.Encoding.PEM,
    serialization.PrivateFormat.PKCS8,
    serialization.NoEncryption()).decode()
PUBLIC_PEM = _KEY.public_key().public_bytes(
    serialization.Encoding.PEM,
    serialization.PublicFormat.SubjectPublicKeyInfo).decode()

ID_TOKEN = jwt.encode({"email": f"{USER_ID}@example.com", "sub": USER_ID},
                      PRIVATE_PEM, algorithm="RS256")
CREATE_COOKIES = {"custom_id_token": ID_TOKEN}

# --------------------------------------------------------------------------
# Elections to create. Each entry is SELF-CONTAINED:
#   title, description, method (BV voting_method), num_winners,
#   candidates (names, fixed order), ballots (one row per voter, scores aligned
#   to `candidates`), expected (free text). Score range depends on the method:
#   Approval = 0/1 ; STAR / STAR_PR / Bloc STAR = 0-5.
# (Older runs used STAR single-winner; the BV95a/BV95b elections already exist —
#  don't recreate them. Add new elections here and re-run.)
# --------------------------------------------------------------------------
# Add the election(s) to create here, then run the script. Entry shape:
#   {"title": ..., "description": ..., "method": "STAR"|"Approval"|...,
#    "num_winners": 1, "candidates": [...], "ballots": [[...], ...],
#    "expected": "free text"}
# (Score range: Approval = 0/1 ; STAR / Bloc / STAR_PR = 0-5.)
# Already created (do NOT re-run — would duplicate):
#   BV_Library STAR_PR — basic two-seat allocation   -> jwxr3j
#   BV_Library STAR_PR — fewer voters than seats      -> hk27tk
#   BV_Library STAR_PR — fractional surplus           -> kk2gxj
#   NOTA test — None of the Above wins               -> 26khr3
#   01a_c2_b2 — two candidates, two ballots            -> my82v6
#   Tennessee capital — Ranked Robin (single race)     -> vqyqkr   (backs case bv2131_…_vqyqkr; RR-only)
#   BV2132 — Pet poll (4 methods, THREE winners)        -> ykjjhy   (multi-race; backs method_comparisons/pet_poll_four_methods)
#   BV2133 — Pet poll II (4 methods, FOUR winners)       -> dyxrbr   (multi-race; backs method_comparisons/pet_poll_four_winners)
#   BV2134 — Pets Governance (6 methods, 6 positions)     -> kcf8vf   (multi-race; backs method_comparisons/pets_governance)
# Their specs live in git history / the case .yaml files.
#
# MULTI-RACE: a spec may carry a "races": [ {title, method, num_winners,
# max_rankings?, candidates, ballots}, ... ] list INSTEAD of the flat single-race
# fields. One election, several contests; each voter votes in every race, so all
# races must have the SAME number of ballots (aligned by voter index). Score
# ranges per method: Approval/Plurality = 0/1 ; STAR/Bloc/STAR_PR = 0-5 ; ranked
# (RankedRobin/IRV/STV) = ranks 1..max_rankings (0 = unranked).

# --- BV2135 — Block & Limited voting reproduced as bloc Approval ---------------
# Proves the equivalence: the multi-member plurality family (Block / Limited /
# SNTV) is just "mark k candidates, top N win", which is exactly BV's multi-winner
# Approval. Same 60/40 electorate as method_comparisons/multi_member_plurality
# (6-voter Home majority: Ada, Ben, Cal; 4-voter Away minority: Uma, Val, Wren; 3
# seats). Both races are Approval + num_winners:3; only the number of marks differs:
#   Block   (approve full slate of 3) -> Ada, Ben, Cal   (majority sweeps 3-0)
#   Limited (approve up to 2; Away bullets Uma) -> Ada, Ben, Uma  (2-1)
# BV should elect exactly what LH's Plurality-family cases do — that's the point.
_MMP_CANDS = ["Ada", "Ben", "Cal", "Uma", "Val", "Wren"]
_MMP_BLOCS = [
    # count, block (approve 3),      limited (approve <=2)
    (6, [1, 1, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0]),   # Home majority
    (4, [0, 0, 0, 1, 1, 1], [0, 0, 0, 1, 0, 0]),   # Away minority (bullets Uma under Limited)
]
def _mmp(k):
    return [rows[k] for n, *rows in _MMP_BLOCS for _ in range(n)]
_MMP_BLOCK, _MMP_LIMITED = _mmp(0), _mmp(1)

ELECTIONS = [
    {
        "test_id": "BV2135",
        "title": "Block & Limited voting, reproduced as bloc Approval",
        "description": "Demonstrates that Block Voting and Limited Voting (the multi-member plurality family) are just multi-winner Approval with a different number of marks per voter. One 60/40 electorate, 3 seats, 6 candidates (Home: Ada, Ben, Cal; Away: Uma, Val, Wren). Block = each voter approves a full 3-candidate slate -> the majority sweeps (Ada, Ben, Cal). Limited = each voter approves up to 2, with the minority concentrating on Uma -> a 2-1 split (Ada, Ben, Uma). Same ballots and winners as the LH Plurality-family cases in method_comparisons/multi_member_plurality, tabulated by BV as Approval.",
        "races": [
            {"title": "Block Voting (as bloc Approval, 3 seats)", "method": "Approval",
             "num_winners": 3, "candidates": _MMP_CANDS, "ballots": _MMP_BLOCK},
            {"title": "Limited Voting (as bloc Approval, 3 seats)", "method": "Approval",
             "num_winners": 3, "candidates": _MMP_CANDS, "ballots": _MMP_LIMITED},
        ],
        "expected": "Block: Ada,Ben,Cal (majority sweep) ; Limited: Ada,Ben,Uma (2-1).  Test ID BV2135.",
    },
]


def _race_specs(spec):
    """Normalize a spec to a LIST of race specs. Accepts either the multi-race
    `races: [...]` form or the flat single-race form (method/candidates/ballots)."""
    if spec.get("races"):
        return spec["races"]
    r = {"title": spec["title"], "method": spec.get("method", "STAR"),
         "num_winners": spec.get("num_winners", 1),
         "candidates": spec["candidates"], "ballots": spec["ballots"]}
    if "max_rankings" in spec:
        r["max_rankings"] = spec["max_rankings"]
    return [r]


def _pp(resp):
    """Print a response compactly."""
    body = resp.text
    if len(body) > 600:
        body = body[:600] + " …(truncated)"
    print(f"    -> HTTP {resp.status_code}  {body}")


def _verify_ballot_count(eid, expected):
    """Post-cast sanity check: GET the election's ballots and compare the count the
    server actually holds against how many we tried to cast. Non-fatal — if the
    endpoint 404s or returns an unexpected shape, we say so and move on (you can
    still confirm nTallyVotes from the UI export)."""
    url = f"{API}/Election/{eid}/ballots"
    try:
        g = requests.get(url, cookies=CREATE_COOKIES, timeout=30)
    except Exception as ex:
        print(f"  ballot-count check: GET {url} failed ({ex!r}) — skipped.")
        return
    if g.status_code != 200:
        print(f"  ballot-count check: HTTP {g.status_code} from /ballots — skipped "
              "(confirm via the UI export's nTallyVotes).")
        return
    try:
        data = g.json()
    except Exception:
        print("  ballot-count check: non-JSON response — skipped.")
        return
    got = None
    if isinstance(data, list):
        got = len(data)
    elif isinstance(data, dict):
        for k in ("ballots", "Ballots", "data"):
            if isinstance(data.get(k), list):
                got = len(data[k])
                break
        if got is None:
            got = data.get("count") or data.get("total")
    if got is None:
        print(f"  ballot-count check: unrecognized /ballots shape "
              f"({type(data).__name__}) — skipped.")
    elif got == expected:
        print(f"  ballot-count check: server holds {got}/{expected} ballots ✓")
    else:
        print(f"  ⚠ ballot-count check: server holds {got}, expected {expected} "
              "— investigate before freezing the export.")


def _cid(name):
    """Fresh unique candidate id. SPECIAL CASE: 'None of the Above' must use the
    fixed id 'c-nota' (NOTA_ID in star-vote-shared/utils/makeID) — the frontend
    recognizes NOTA by id, not name."""
    return 'c-nota' if name.strip().lower() == 'none of the above' else str(uuid.uuid4())


def build_payload(template, spec):
    """Copy the template election and rewrite its race(s) from the spec. Supports
    one race (flat spec) or several (spec['races']). Mirrors the doc's 'duplicate
    pet' recipe, cloning the template's race object once per requested race."""
    e = json.loads(json.dumps(template))          # deep copy
    elec = e.get("election") or e.get("Election") or e
    elec.pop("election_id", None)                 # let the backend assign a new id
    elec["owner_id"] = USER_ID
    elec["auth_key"] = PUBLIC_PEM                  # PEM RS256 public key (backend requires)
    # Title = "trash delete test — BV<nnn> — <title>". The BV<nnn> Test ID is put
    # INTO the title so it's actually stored on BV (visible in /manage and the
    # export), not just in our local `expected` note.
    tid = spec.get("test_id")
    title = TITLE_PREFIX + (f"{tid} — " if tid else "") + spec["title"]
    elec["title"] = title
    elec["description"] = spec["description"]
    tmpl_races = elec.get("races") or []
    if not tmpl_races:
        sys.exit("Template has no races[] — pick a different BV_TEMPLATE_ID.")
    base = tmpl_races[0]

    races_out = []
    for rs in _race_specs(spec):
        r = json.loads(json.dumps(base))           # a fresh clone of the template race
        r["title"] = rs.get("title", title)
        r["voting_method"] = rs.get("method", "STAR")
        r["num_winners"] = rs.get("num_winners", 1)
        # Ranked methods (IRV / STV / RankedRobin) validate ballots as 0..max_rankings
        # (rank, not score: 1 = top choice, 0 = unranked). Set the cap when given so
        # the copied STAR template doesn't reject rank values on submit.
        if "max_rankings" in rs:
            r["max_rankings"] = rs["max_rankings"]
        r["race_id"] = str(uuid.uuid4())           # fresh race id (don't reuse template's)
        # Fresh candidates, each with a UNIQUE id (backend rejects duplicate/empty ids).
        r["candidates"] = [{"candidate_id": _cid(n), "candidate_name": n}
                           for n in rs["candidates"]]
        races_out.append(r)
    elec["races"] = races_out
    # NOTE: owner_id makes the election appear in /manage, but it does NOT grant
    # UI admin access — BV's /admin page authorizes off a server-side role binding
    # that only the authenticated (Keycloak) create flow writes, not off the
    # election's owner_id/admin_ids. Setting admin_ids here was tested and IGNORED
    # (xb8r6v had admin_ids=[owner] and was still denied; the working manual
    # election had admin_ids=null). So API-created elections are public, listable,
    # and exportable, but not UI-administrable from your real login. Don't bother
    # setting admin_ids — it has no effect. (See the BV issue draft in git log.)
    return {"Election": elec}                      # API expects capital "Election"


def create(spec):
    print(f"\n=== {spec['title']} ===")
    print(f"  GET template /Election/{TEMPLATE_ID}")
    t = requests.get(f"{API}/Election/{TEMPLATE_ID}")
    _pp(t)
    template = json.loads(t.text)

    payload = build_payload(template, spec)
    print("  POST /Elections (create)")
    c = requests.post(f"{API}/Elections", json=payload, cookies=CREATE_COOKIES)
    _pp(c)
    created = json.loads(c.text)
    elec = created.get("election") or created.get("Election") or created
    if not isinstance(elec, dict) or "election_id" not in elec:
        raise RuntimeError(f"create failed (HTTP {c.status_code}): {c.text[:300]}")
    eid = elec["election_id"]
    print(f"  created election_id = {eid}   ({'https://bettervoting.com/' + eid})")

    # Re-fetch to learn the assigned race_ids + candidate ids (per race).
    g = requests.get(f"{API}/Election/{eid}")
    full = json.loads(g.text)
    felec = full.get("election") or full.get("Election") or full
    rspecs = _race_specs(spec)
    races_fetched = felec.get("races", [])
    if len(races_fetched) != len(rspecs):
        raise RuntimeError(f"expected {len(rspecs)} race(s), server returned "
                           f"{len(races_fetched)}")
    # Align by order; one voter votes EVERY race, so ballot counts must match.
    race_info = []                   # (race_id, cand_names, name->cid, ballots)
    for rs, rf in zip(rspecs, races_fetched):
        n2c = {c["candidate_name"]: c["candidate_id"] for c in rf["candidates"]}
        race_info.append((rf["race_id"], rs["candidates"], n2c, rs["ballots"]))
    nb = len(race_info[0][3])
    if any(len(ri[3]) != nb for ri in race_info):
        raise RuntimeError("all races must have the same number of ballots "
                           "(one per voter): " + ", ".join(str(len(ri[3])) for ri in race_info))

    # Cast the ballots. Each is an independent voter (distinct temp_id cookie so
    # the backend doesn't reject as "already voted"), so we fire them CONCURRENTLY
    # through a bounded pool and report a compact per-bloc summary. A voter's
    # ballot carries one `votes` entry PER race.
    def _sig(idx):                   # per-voter signature across races (for bloc grouping)
        return tuple(tuple(ri[3][idx - 1]) for ri in race_info)

    def _cast_one(idx):
        votes = []
        for race_id, cnames, n2c, rballots in race_info:
            row = rballots[idx - 1]
            votes.append({"race_id": race_id,
                          "scores": [{"candidate_id": n2c[cnames[j]], "score": row[j]}
                                     for j in range(len(cnames))]})
        body = {"ballot": {
            "election_id": eid,
            "votes": votes,
            "date_submitted": int(time.time() * 1000),
            "status": "submitted",
        }}
        try:
            v = requests.post(f"{API}/Election/{eid}/vote", json=body,
                              cookies={"temp_id": f"{USER_ID}_voter{idx}"}, timeout=30)
            return (idx, v.status_code, v.status_code == 200, v.text[:200])
        except Exception as ex:
            return (idx, None, False, repr(ex))

    def _cast_all(idxs):
        results = []
        with ThreadPoolExecutor(max_workers=CONCURRENCY) as pool:
            futs = [pool.submit(_cast_one, i) for i in idxs]
            for fut in as_completed(futs):
                results.append(fut.result())
        return results

    voters = list(range(1, nb + 1))
    print(f"  casting {nb} ballots × {len(race_info)} race(s) ({CONCURRENCY}-wide)…")
    results = _cast_all(voters)

    # One retry (gentle) for any that failed.
    failed = [i for i, _sc, ok, _b in results if not ok]
    if failed:
        print(f"  retrying {len(failed)} failed ballot(s) once…")
        results += _cast_all(failed)

    # A voter that failed then succeeded on retry counts as OK.
    ok_idx = {i for i, _sc, ok, _b in results if ok}
    last = {}
    for i, sc, ok, b in results:
        if i not in ok_idx or ok:
            last[i] = (sc, b)

    # Per-bloc summary keyed by the voter's cross-race signature.
    want_by_sig = Counter(_sig(i) for i in voters)
    ok_by_sig = Counter(_sig(i) for i in voters if i in ok_idx)
    for sig in sorted(want_by_sig, key=lambda s: [-x for row in s for x in row]):
        label = " | ".join("[" + ",".join(map(str, row)) + "]" for row in sig)
        mark = "✓" if ok_by_sig[sig] == want_by_sig[sig] else "⚠"
        print(f"    {ok_by_sig[sig]:>3}/{want_by_sig[sig]} × {label}  {mark}")
    print(f"  cast {len(ok_idx)}/{nb} ballots OK.")
    still_bad = [i for i in voters if i not in ok_idx]
    if still_bad:
        print(f"  ⚠ {len(still_bad)} ballot(s) still failing after retry:")
        for i in still_bad[:10]:
            sc, b = last.get(i, (None, ""))
            print(f"      voter{i}  HTTP {sc}  {b}")

    # Server-side confirmation: does BV actually hold the ballots we think it does?
    _verify_ballot_count(eid, nb)

    # Save the finished object for promotion into the repo case.
    final = requests.get(f"{API}/Election/{eid}")
    os.makedirs(OUT_DIR, exist_ok=True)
    # Sanitize the title for use as a filename (titles may contain '/', ':' etc.,
    # e.g. "Chocolate/Vanilla" — an unsanitized '/' makes the write fail).
    safe_title = "".join(c if c not in '/\\:*?"<>|' else "-" for c in spec["title"]).strip()[:60]
    out = os.path.join(OUT_DIR, f"{safe_title}-{eid}.json")
    with open(out, "w") as fh:
        fh.write(final.text)
    print(f"  saved -> {out}")
    print(f"  expected: {spec.get('expected', '?')}  |  URL: "
          f"https://bettervoting.com/{eid}")
    return eid


def _effective_title(spec):
    """The exact title BV will store (what the pre-check must judge)."""
    tid = spec.get("test_id")
    return TITLE_PREFIX + (f"{tid} — " if tid else "") + spec.get("title", "")


def _preflight_test_ids(elections):
    """PRE-CHECK (before any network call). Elections created via the API are
    PUBLIC and CANNOT be renamed, closed, or deleted afterward (only a BV admin
    with DB access can purge them), so the title has to be right the FIRST time.
    This gate:
      • requires a BV Test ID (`test_id`, e.g. 'BV2132') — embedded in the title
        for traceability; missing/malformed/duplicate IDs are flagged;
      • blocks JUNK/placeholder titles ('trash', 'delete', 'test', 'tbd', 'xxx',
        'asdf', 'todo', 'zzz', 'foo/bar') — that's how 'trash delete test —' went
        public on bwbc6d/mw9kpp and can't be undone.
    Any problem requires an explicit y/N confirmation. Skip non-interactively with
    BV_ALLOW_NO_TESTID=1 (missing id) / BV_ALLOW_JUNK_TITLE=1 (junk title)."""
    import re
    print("  reminder: BV titles are PERMANENT and PUBLIC — API elections can't be "
          "renamed or deleted. Make each title real.")

    # Junk/placeholder title guard (the thing that actually burned us). Whole-word
    # match so real titles aren't caught ("test" won't trip "contest"/"latest").
    JUNK = ("trash", "delete", "test", "tests", "junk", "tbd", "xxx", "asdf",
            "todo", "zzz", "foobar", "foo", "bar", "dummy", "placeholder")
    def _junk_hits(title):
        low = title.lower()
        return [w for w in JUNK if re.search(rf"\b{re.escape(w)}\b", low)]
    bad_titles = [(_effective_title(s), _junk_hits(_effective_title(s)))
                  for s in elections if _junk_hits(_effective_title(s))]
    if bad_titles:
        print("\n⚠ PRE-CHECK — these titles look like throwaway/junk names "
              "(they will be PUBLIC and permanent):")
        for t, hits in bad_titles:
            print(f"    • “{t}”   ← {', '.join(hits)}")
        if os.environ.get("BV_ALLOW_JUNK_TITLE") != "1":
            try:
                ans = input("  Publish these titles anyway, on purpose? [y/N] ").strip().lower()
            except EOFError:
                ans = ""
            if ans not in ("y", "yes"):
                sys.exit("Aborted. Give each election a real, meaningful title "
                         "(set BV_ALLOW_JUNK_TITLE=1 only if you truly mean it).")
        print("  Proceeding with those titles.\n")

    missing = [s.get("title", "<untitled>") for s in elections if not s.get("test_id")]
    odd = [(s.get("test_id"), s.get("title", "<untitled>"))
           for s in elections
           if s.get("test_id") and not re.match(r"^BV\w+$", str(s["test_id"]))]
    dupes = [t for t, c in Counter(s.get("test_id") for s in elections
                                   if s.get("test_id")).items() if c > 1]
    for tid, ttl in odd:
        print(f"  note: test_id {tid!r} on “{ttl}” doesn’t look like 'BV<n>'.")
    if dupes:
        print(f"  ⚠ duplicate test_id(s) across this run: {', '.join(map(str, dupes))}")
    if not missing:
        return
    print("\n⚠ PRE-CHECK — these election(s) have NO BV Test ID (test_id, e.g. 'BV2132'):")
    for t in missing:
        print(f"    • {t}")
    print("  The Test ID is embedded in the BV title for traceability in /manage.")
    if os.environ.get("BV_ALLOW_NO_TESTID") == "1":
        print("  BV_ALLOW_NO_TESTID=1 set — proceeding un-numbered ON PURPOSE.\n")
        return
    try:
        ans = input("  Create these WITHOUT a BV number, on purpose? [y/N] ").strip().lower()
    except EOFError:
        ans = ""
    if ans not in ("y", "yes"):
        sys.exit("Aborted. Add a `test_id` (e.g. \"BV2132\") to each election above, "
                 "or set BV_ALLOW_NO_TESTID=1 to proceed intentionally.")
    print("  Confirmed — proceeding without a BV number.\n")


if __name__ == "__main__":
    print(f"BetterVoting API @ {API}")
    print(f"identity BV_USER_ID={USER_ID}  template={TEMPLATE_ID}")
    print(f"Creating {len(ELECTIONS)} election(s)...\n")

    _preflight_test_ids(ELECTIONS)          # gate: confirm any missing BV Test IDs

    summary = []  # (title, eid_or_None, expected)
    for spec in ELECTIONS:
        try:
            eid = create(spec)
            summary.append((spec["title"], eid, spec.get("expected", "?")))
        except Exception as ex:            # keep going to the next election
            print(f"  !! failed: {ex!r}")
            summary.append((spec["title"], None, spec.get("expected", "?")))

    created = [s for s in summary if s[1]]
    print("\n" + "=" * 72)
    print(f"SUMMARY — {len(created)} of {len(ELECTIONS)} election(s) created")
    print("=" * 72)
    for title, eid, expected in summary:
        if eid:
            print(f"  [OK]   {title}")
            print(f"           vote:     https://bettervoting.com/{eid}")
            print(f"           results:  https://bettervoting.com/{eid}/results")
            print(f"           expected: {expected}")
        else:
            print(f"  [FAIL] {title}")
    print("=" * 72)
    print("\nDone. If a JSON lacks Results, close the election in the UI once, "
          "then re-run the final GET (or export from the URL above).")
