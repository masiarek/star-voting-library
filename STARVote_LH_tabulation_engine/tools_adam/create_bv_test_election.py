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
# environment if you like. BV_USER_ID is just a throwaway self-signed identity.
USER_ID = os.environ.get("BV_USER_ID", "masiarek_mc_demo")
TEMPLATE_ID = os.environ.get("BV_TEMPLATE_ID", "pet")

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
ELECTIONS = [
    {
        "title": "BV27 - Lackner & Skowron steering committee (Approval, k=4)",
        "description": "Multi-Winner Approval (bloc). Example 2.1 from Lackner & "
                       "Skowron, Multi-Winner Voting with Approval Preferences. "
                       "7 candidates, 12 approval ballots, 4 seats. AV seats "
                       "A, B, C then TIES D and F for the 4th seat.",
        "method": "Approval",
        "num_winners": 4,
        "candidates": ["A", "B", "C", "D", "E", "F", "G"],
        "ballots": [
            [1, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0],  # 3× {A,B}
            [1, 0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0],  # 3× {A,C}
            [1, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0],                          # 2× {A,D}
            [0, 1, 1, 0, 0, 1, 0],                                                 # 1× {B,C,F}
            [0, 0, 0, 0, 1, 0, 0],                                                 # 1× {E}
            [0, 0, 0, 0, 0, 1, 0],                                                 # 1× {F}
            [0, 0, 0, 0, 0, 0, 1],                                                 # 1× {G}
        ],
        "expected": "A, B, C, and {D or F} — AV ties for the 4th seat",
    },
]


def _pp(resp):
    """Print a response compactly."""
    body = resp.text
    if len(body) > 600:
        body = body[:600] + " …(truncated)"
    print(f"    -> HTTP {resp.status_code}  {body}")


def build_payload(template, spec):
    """Copy the template election object and rewrite its first race to be our
    3-candidate STAR single-winner poll. Mirrors the doc's 'duplicate pet' recipe."""
    e = json.loads(json.dumps(template))          # deep copy
    elec = e.get("election") or e.get("Election") or e
    elec.pop("election_id", None)                 # let the backend assign a new id
    elec["owner_id"] = USER_ID
    elec["auth_key"] = PUBLIC_PEM                  # PEM RS256 public key (backend requires)
    elec["title"] = spec["title"]
    elec["description"] = spec["description"]
    races = elec.get("races") or []
    if not races:
        sys.exit("Template has no races[] — pick a different BV_TEMPLATE_ID.")
    r = races[0]
    r["title"] = spec["title"]
    r["voting_method"] = spec.get("method", "STAR")
    r["num_winners"] = spec.get("num_winners", 1)
    r["race_id"] = str(uuid.uuid4())               # fresh race id (don't reuse template's)
    # Fresh candidates, each with a UNIQUE id (backend rejects duplicate/empty ids).
    r["candidates"] = [{"candidate_id": str(uuid.uuid4()), "candidate_name": n}
                       for n in spec["candidates"]]
    elec["races"] = [r]
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

    # Re-fetch to learn the assigned race_id + candidate ids.
    g = requests.get(f"{API}/Election/{eid}")
    full = json.loads(g.text)
    felec = full.get("election") or full.get("Election") or full
    race = felec["races"][0]
    race_id = race["race_id"]
    name_to_cid = {c["candidate_name"]: c["candidate_id"] for c in race["candidates"]}

    # Cast the ballots, one temp voter each.
    cands = spec["candidates"]
    for i, row in enumerate(spec["ballots"], start=1):
        scores = [{"candidate_id": name_to_cid[cands[j]], "score": row[j]}
                  for j in range(len(cands))]
        body = {"ballot": {
            "election_id": eid,
            "votes": [{"race_id": race_id, "scores": scores}],
            "date_submitted": int(time.time() * 1000),
            "status": "submitted",
        }}
        v = requests.post(f"{API}/Election/{eid}/vote", json=body,
                          cookies={"temp_id": f"{USER_ID}_voter{i}"})
        print(f"  vote {i} {row}", end="  ")
        _pp(v)

    # Save the finished object for promotion into the repo case.
    final = requests.get(f"{API}/Election/{eid}")
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, f"{spec['title'].split(' -')[0].strip()}-{eid}.json")
    with open(out, "w") as fh:
        fh.write(final.text)
    print(f"  saved -> {out}")
    print(f"  expected: {spec.get('expected', '?')}  |  URL: "
          f"https://bettervoting.com/{eid}")
    return eid


if __name__ == "__main__":
    print(f"BetterVoting API @ {API}")
    print(f"identity BV_USER_ID={USER_ID}  template={TEMPLATE_ID}")
    for spec in ELECTIONS:
        try:
            create(spec)
        except Exception as ex:            # keep going to the second election
            print(f"  !! failed: {ex!r}")
    print("\nDone. If a JSON lacks Results, close the election in the UI once, "
          "then re-run the final GET (or export from the URL above).")
