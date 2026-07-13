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
Then it saves each finished election object as JSON into ../../06_Other/_demo_dropbox/ so
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
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "06_Other/_demo_dropbox")

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
#   BV2135 — Block & Limited voting (as bloc Approval)     -> 3x4vrv   (backs method_comparisons/multi_member_plurality)
#   BV2136 — Village Council by SNTV (multi-winner Plurality) -> y3tvxm  (backs method_comparisons/sntv_village_council)
# Their specs live in git history / the case .yaml files.
#
# MULTI-RACE: a spec may carry a "races": [ {title, method, num_winners,
# max_rankings?, candidates, ballots}, ... ] list INSTEAD of the flat single-race
# fields. One election, several contests; each voter votes in every race, so all
# races must have the SAME number of ballots (aligned by voter index). Score
# ranges per method: Approval/Plurality = 0/1 ; STAR/Bloc/STAR_PR = 0-5 ; ranked
# (RankedRobin/IRV/STV) = ranks 1..max_rankings (0 = unranked).

# --- BV2137 / BV2138 — LeGrand rbvote examples: one ranked electorate, many -----
# tabulations. Both come from Robert LeGrand's ranked-ballot calculator
# (cs.angelo.edu/~rlegrand/rbvote/). Each is ONE election with FOUR races on the
# SAME ranked ballots — the four ranked/score methods BetterVoting supports:
# IRV (Hare), Ranked Robin (Copeland), STV (1 seat), and STAR (ranks mapped to
# 0-5 scores). The other ~11 methods on LeGrand's page (Borda, Bucklin, Coombs,
# Dodgson, Simpson, Schulze, Tideman, Nanson, Baldwin, Raynaud, Small) have no BV
# equivalent and are cross-checked with pref_voting + LeGrand's calculator only.
#
# RANK->SCORE CONVERSION (STAR race), documented once here and in the case .md:
#   score(rank) = round( 1 + 4*(N - rank)/(N - 1) )   # top rank -> 5, bottom -> 1
#   => N=3: 5,3,1   N=5: 5,4,3,2,1   (integer-clean for these two elections)


def _mk_ranked_and_star(blocs, cands):
    """Expand weighted blocs to one row per voter, aligned to `cands` order.
    Returns (ranked_rows, star_rows): ranked = 1..N (1=top) for IRV/RR/STV;
    star = 0-5 via the documented linear top=5/bottom=1 map."""
    N = len(cands)
    def ranks(order):
        pos = {c: i + 1 for i, c in enumerate(order)}      # 1 = top choice
        return [pos[c] for c in cands]
    def star(order):
        pos = {c: i for i, c in enumerate(order)}          # 0-based rank
        sc = {c: round(1 + 4 * (N - 1 - pos[c]) / (N - 1)) for c in cands}
        return [sc[c] for c in cands]
    R, S = [], []
    for cnt, order in blocs:
        R += [ranks(order)] * cnt
        S += [star(order)] * cnt
    return R, S


def _four_races(prefix, blocs, cands):
    """The four BV-supported tabulations of one ranked electorate."""
    R, S = _mk_ranked_and_star(blocs, cands)
    N = len(cands)
    return [
        {"title": f"{prefix} — IRV (Hare)", "method": "IRV",
         "num_winners": 1, "max_rankings": N, "candidates": cands, "ballots": R},
        {"title": f"{prefix} — Ranked Robin (Copeland)", "method": "RankedRobin",
         "num_winners": 1, "max_rankings": N, "candidates": cands, "ballots": R},
        {"title": f"{prefix} — STV, 1 seat (= IRV single-winner)", "method": "STV",
         "num_winners": 1, "max_rankings": N, "candidates": cands, "ballots": R},
        {"title": f"{prefix} — STAR (ranks mapped to 0-5 scores)", "method": "STAR",
         "num_winners": 1, "candidates": cands, "ballots": S},
    ]


# BV2137 — Center squeeze (100 voters, 3 candidates). Anderson is the Condorcet
# winner (beats Reagan 55-45, Carter 65-35) but has the fewest first-choices, so
# IRV/STV eliminate him and elect Carter; Ranked Robin & STAR elect Anderson.
_C1_CANDS = ["Reagan", "Anderson", "Carter"]
_C1_BLOCS = [(45, ["Reagan", "Anderson", "Carter"]),
             (20, ["Anderson", "Carter", "Reagan"]),
             (35, ["Carter", "Anderson", "Reagan"])]

# BV2138 — Five-way (921 voters, 5 candidates), NO Condorcet winner (Smith set =
# Abby/Brad/Dave/Erin). The four BV methods give THREE winners: IRV/STV->Dave,
# Ranked Robin->Abby, STAR->Brad. (Full 15-method set spreads across all five.)
_C2_CANDS = ["Abby", "Brad", "Cora", "Dave", "Erin"]
_C2_BLOCS = [(98,  "Abby Cora Erin Dave Brad"), (64,  "Brad Abby Erin Cora Dave"),
             (12,  "Brad Abby Erin Dave Cora"), (98,  "Brad Erin Abby Cora Dave"),
             (13,  "Brad Erin Abby Dave Cora"), (125, "Brad Erin Dave Abby Cora"),
             (124, "Cora Abby Erin Dave Brad"), (76,  "Cora Erin Abby Dave Brad"),
             (21,  "Dave Abby Brad Erin Cora"), (30,  "Dave Brad Abby Erin Cora"),
             (98,  "Dave Brad Erin Cora Abby"), (139, "Dave Cora Abby Brad Erin"),
             (23,  "Dave Cora Brad Abby Erin")]
_C2_BLOCS = [(cnt, s.split()) for cnt, s in _C2_BLOCS]

# Already created on BetterVoting — kept for reference only. DO NOT re-run these:
# BV elections are PERMANENT and cannot be deleted, so re-running would create
# undeletable duplicates. Only the `ELECTIONS` list at the bottom is executed.
_ALREADY_CREATED = [
    {
        "test_id": "BV2137",
        "title": "Center Squeeze — the centrist Condorcet winner that Instant-Runoff eliminates",
        "description": "A textbook 'center squeeze' (from Robert LeGrand's ranked-ballot calculator). 100 voters, three candidates: Reagan is the polarizing right (45 first-choices), Carter the polarizing left (35), Anderson the broadly-liked centrist (only 20 first-choices but nearly everyone's second). Anderson is the Condorcet winner — he beats Reagan 55-45 and Carter 65-35 head-to-head. Yet Instant-Runoff Voting eliminates Anderson FIRST (fewest first-choices) and elects Carter. This election runs the SAME ranked ballots four ways: IRV and STV (1 seat) elect Carter; Ranked Robin (Copeland / Condorcet) and STAR (ranks mapped to 0-5 scores) elect the centrist Anderson. The tabulation, not the ballot, decides. (13 of the ~15 methods on LeGrand's calculator elect Anderson.)",
        "races": _four_races("Center squeeze", _C1_BLOCS, _C1_CANDS),
        "expected": "IRV & STV -> Carter; Ranked Robin & STAR -> Anderson (the Condorcet winner). Test ID BV2137.",
    },
    {
        "test_id": "BV2138",
        "title": "One Ranked Electorate, Many Tabulations — the winner depends on the method",
        "description": "Robert LeGrand's flagship 'the method decides everything' example: 921 voters, five candidates (Abby, Brad, Cora, Dave, Erin), with NO Condorcet winner (a top cycle; Smith set = Abby, Brad, Dave, Erin). Across the ~15 ranked methods on his rbvote calculator the win splits five ways. This election runs the identical ranked ballots through the four tabulations BetterVoting supports: IRV and STV (1 seat) elect Dave; Ranked Robin (Copeland) elects Abby; STAR (ranks mapped to 0-5 scores) elects Brad — three different winners from one electorate. The remaining methods (Borda, Bucklin, Coombs, Dodgson, Simpson, Schulze, Tideman, Nanson, Baldwin, Raynaud, Small) add Cora and Erin, and are checked with the pref_voting library and LeGrand's calculator.",
        "races": _four_races("Method comparison", _C2_BLOCS, _C2_CANDS),
        "expected": "IRV & STV -> Dave; Ranked Robin -> Abby; STAR -> Brad. Test ID BV2138.",
    },
]


# --- BV2140 — electowiki Ranked Robin worked example (EQUAL-RANK ballots) --------
# electowiki.org/wiki/Ranked_Robin. 35 voters, 5 candidates, ballots that use tied
# ranks (e.g. Ava=Bianca=Cedric). Ava wins the most pairwise matchups (3 of 4) even
# though there is NO Condorcet winner (Ava loses head-to-head to Bianca 15-14). LH
# reproduces the same pairwise matrix + winner (see the case .md).
#
# NOTE: BV ranked ballots put a rank in each candidate's slot (1 = top, 0 = unranked).
# This example needs TIED ranks, so equal-ranked candidates share a rank number
# (dense ranking: 1,1,1,2,3 …). Whether BV's RankedRobin accepts/counts tied
# ranks the same way LH does is UNVERIFIED — if BV rejects or mis-handles ties,
# capture the error / divergence in the case writeup (the create just errors, no
# permanent election is made on a validation failure).
_C3_CANDS = ["Ava", "Bianca", "Cedric", "Deegan", "Eli"]
# Weighted ballots as ordered rank LEVELS (each inner list = candidates tied at that
# level; most-preferred level first).
_C3_LEVELS = [
    (8, [["Ava"], ["Cedric"], ["Deegan"], ["Bianca"], ["Eli"]]),
    (6, [["Ava", "Bianca", "Cedric"], ["Eli"], ["Deegan"]]),
    (6, [["Eli"], ["Ava"], ["Bianca", "Cedric", "Deegan"]]),
    (6, [["Deegan"], ["Bianca", "Cedric"], ["Eli"], ["Ava"]]),
    (4, [["Bianca"], ["Ava"], ["Eli"], ["Deegan"], ["Cedric"]]),
    (3, [["Eli"], ["Deegan"], ["Bianca", "Cedric"], ["Ava"]]),
    (2, [["Deegan", "Eli"], ["Bianca", "Cedric"], ["Ava"]]),
]


def _dense_rank_rows(levels_blocs, cands):
    """Expand weighted rank-LEVEL blocs to one row per voter, dense-ranked
    (level 0 -> rank 1; candidates tied within a level share that rank), aligned
    to `cands` order. 0 = unranked (not used here — every ballot ranks all five)."""
    rows = []
    for cnt, levels in levels_blocs:
        rank = {}
        for i, grp in enumerate(levels):
            for c in grp:
                rank[c] = i + 1
        rows += [[rank.get(c, 0) for c in cands]] * cnt
    return rows


# Already created -> bettervoting.com/48hjkv. Kept for reference; not re-run.
_CREATED_BV2140 = [
    {
        "test_id": "BV2140",
        "title": "Ranked Robin worked example — most pairwise wins, with no Condorcet winner",
        "description": "The electowiki Ranked Robin worked example (electowiki.org/wiki/Ranked_Robin). 35 voters, five candidates (Ava, Bianca, Cedric, Deegan, Eli) on ranked ballots that use EQUAL rankings (e.g. Ava=Bianca=Cedric). Ranked Robin (Copeland) compares every pair head-to-head and elects whoever wins the most matchups: Ava wins 3 of 4 and is elected — even though there is NO Condorcet winner (Ava actually loses head-to-head to Bianca, 15-14). It shows Ranked Robin picking the strongest all-round candidate when nobody beats everyone. The LH tabulation engine reproduces the same pairwise matrix and winner.",
        "method": "RankedRobin",
        "num_winners": 1,
        "max_rankings": len(_C3_CANDS),
        "candidates": _C3_CANDS,
        "ballots": _dense_rank_rows(_C3_LEVELS, _C3_CANDS),
        "expected": "Ranked Robin -> Ava (3 pairwise wins; NO Condorcet winner — Ava loses to Bianca 15-14). Test ID BV2140.",
    },
]


# --- BV2141 — electowiki RR "all 4 tiebreak degrees" example (TIE-DECIDING) ------
# electowiki.org/wiki/Ranked_Robin. 81 voters, 6 candidates, EQUAL ranks + PARTIAL
# ballots (unranked = tied for last). Ava and Bianca TIE for most wins (3 each),
# both +55 margin, both 149 against — the Equal-Vote 4-degree protocol elects
# Bianca via beatpath (14 vs 7). CAUTION: this is a tie-deciding case. Ava vs
# Bianca head-to-head is 29-29 (a tie), so BV's ladder (wins -> 2-way head-to-head
# -> RANDOM) cannot separate them and picks at RANDOM — it does NOT run the higher
# degrees. The BV winner is therefore non-deterministic and NOT freezable; this
# election is a live probe of what BV actually does. Title claims no winner on
# purpose. (Row totals verified == electowiki's 204/204/167/175/169/150; note
# electowiki's printed cell values for Ava/Bianca over Cedric/Deegan/Eli are each
# 4 low and don't sum to its own row totals — a display error, outcome unaffected.)
_C4_CANDS = ["Ava", "Bianca", "Cedric", "Deegan", "Eli", "Fabio"]
_C4_LEVELS = [
    (10, [["Eli"], ["Deegan"], ["Ava", "Cedric"], ["Fabio"]]),
    (9,  [["Bianca", "Deegan"], ["Eli"], ["Cedric"]]),
    (8,  [["Deegan"], ["Eli"], ["Ava", "Bianca", "Cedric"]]),
    (8,  [["Bianca"], ["Ava"], ["Fabio"], ["Cedric"]]),
    (8,  [["Fabio"], ["Cedric"], ["Ava"], ["Deegan"], ["Bianca"]]),
    (7,  [["Ava"], ["Eli"], ["Bianca"], ["Fabio"]]),
    (6,  [["Fabio"], ["Bianca", "Cedric"], ["Ava"]]),
    (6,  [["Cedric"], ["Deegan", "Eli"], ["Ava", "Bianca"], ["Fabio"]]),
    (5,  [["Deegan"], ["Ava", "Bianca"], ["Eli"], ["Cedric"]]),
    (4,  [["Cedric"], ["Bianca"], ["Ava"]]),
    (4,  [["Ava"], ["Bianca", "Fabio"]]),
    (4,  [["Ava", "Bianca"], ["Fabio"]]),
    (2,  [["Bianca", "Fabio"], ["Ava", "Eli"]]),
]

# Already created -> bettervoting.com/3r3yf7. Kept for reference; not re-run.
_CREATED_BV2141 = [
    {
        "test_id": "BV2141",
        "title": "Ranked Robin — a Copeland tie that needs all four Equal-Vote tiebreak degrees",
        "description": "The electowiki Ranked Robin 'all four tie-breaking degrees' example (electowiki.org/wiki/Ranked_Robin). 81 voters, six candidates (Ava, Bianca, Cedric, Deegan, Eli, Fabio) on ranked ballots with equal rankings and partial (truncated) ballots. Ava and Bianca TIE for the most pairwise wins (3 each); they also tie on total win margin (+55) and on votes-against (149). The Equal Vote Coalition's 4-degree tiebreak protocol resolves it to Bianca via a beatpath comparison. But Ava vs Bianca head-to-head is itself a 29-29 tie, so any engine that breaks a 2-way tie by head-to-head alone cannot separate them. This election is a live test of how BetterVoting's Ranked Robin tabulator resolves a genuine tie-of-ties.",
        "method": "RankedRobin",
        "num_winners": 1,
        "max_rankings": len(_C4_CANDS),
        "candidates": _C4_CANDS,
        "ballots": _dense_rank_rows(_C4_LEVELS, _C4_CANDS),
        "expected": "Copeland TIE: Ava & Bianca both 3 wins, +55 margin, 149 against. Equal-Vote 4-degree protocol -> Bianca (beatpath 14 vs 7). Ava vs Bianca head-to-head is 29-29, so a wins->head-to-head->random engine (BV) picks at RANDOM — non-deterministic, not freezable. Test ID BV2141.",
    },
]


# --- BV2142 / BV2143 — electowiki Ranked Robin CLONE INDEPENDENCE (teaming) -----
# electowiki.org/wiki/Ranked_Robin "A note on cloneproofness". A pre/after pair
# in a no-Condorcet-winner cycle. BV divergence is the whole point:
#   * BV2142 (pre): A,B,C tie 3-way at 4 wins (cycle) -> BV RANDOM (this is the
#     LH-only 'coin flip'; LH margin->lot -> A or B).
#   * BV2143 (post, teaming): A-faction runs clones A1,A2. Under a MARGIN tiebreak
#     (LH / Equal Vote) A1 wins (+134) — teaming succeeds. But A1 and C tie at 5
#     wins and C beats A1 head-to-head 21-12, so BV's 2-way head-to-head tiebreak
#     elects C — the teaming attack FAILS on BV. Live probe of that divergence.
# All strict full rankings (no ties). Lesson: 00_start_here/RCV_Ranked_Robin/
# rr_clone_independence.md ; LH-only pair: 05_Ranked_Robin/clone_independence/.
_C5_CANDS = ["A", "B", "C", "D", "E", "F"]
_C5_LEVELS = [
    (12, [["A"], ["B"], ["C"], ["D"], ["E"], ["F"]]),
    (11, [["B"], ["C"], ["A"], ["D"], ["E"], ["F"]]),
    (10, [["C"], ["A"], ["B"], ["D"], ["E"], ["F"]]),
]
_C6_CANDS = ["A1", "A2", "B", "C", "D", "E", "F"]
_C6_LEVELS = [
    (12, [["A1"], ["A2"], ["B"], ["C"], ["D"], ["E"], ["F"]]),
    (11, [["B"], ["C"], ["A1"], ["A2"], ["D"], ["E"], ["F"]]),
    (10, [["C"], ["A1"], ["A2"], ["B"], ["D"], ["E"], ["F"]]),
]

# Already created -> bettervoting.com/4gfwdq (BV2142) / 9pr3wr (BV2143). Reference only.
_CREATED_BV2142_43 = [
    {
        "test_id": "BV2142",
        "title": "Ranked Robin clone independence (1 of 2) — a no-Condorcet-winner cycle before cloning",
        "description": "The electowiki Ranked Robin clone-independence ('cloneproofness') example, part 1 of 2. 33 voters, six candidates. A, B, C form a rock-paper-scissors cycle (A beats B, B beats C, C beats A) so there is NO Condorcet winner; all three tie for the most pairwise wins (4 each). A and B even tie on total win margin (+101), so the winner is effectively a coin flip between them. This election sets up part 2 (BV2143), where the A-faction runs clones to turn that coin flip into a certain win. Note: because A, B, C are a 3-way tie, BetterVoting resolves it at random.",
        "method": "RankedRobin",
        "num_winners": 1,
        "max_rankings": len(_C5_CANDS),
        "candidates": _C5_CANDS,
        "ballots": _dense_rank_rows(_C5_LEVELS, _C5_CANDS),
        "expected": "A,B,C tie 3-way at 4 wins (cycle, no Condorcet winner); A&B tie on margin +101. LH margin->lot -> A. BV: 3-way tie -> RANDOM. Test ID BV2142.",
    },
    {
        "test_id": "BV2143",
        "title": "Ranked Robin clone independence (2 of 2) — a faction runs clones (teaming)",
        "description": "The electowiki Ranked Robin clone-independence example, part 2 of 2. Same election as BV2142, but the A-faction now fields two clones, A1 and A2 (ranked together in A's old slot). Under a margin-based tiebreak (the Equal Vote Coalition's protocol, and the LH engine) this 'teaming' works: A1's win margin rises to +134, B is crowded out of the top tier, and A1 wins deterministically — converting part 1's coin flip into a guaranteed A-faction win. That is a clone-independence failure. BUT A1 and C tie at 5 wins and C beats A1 head-to-head 21-12, so BetterVoting's 2-way head-to-head tiebreak elects C instead — on BV the teaming attack fails. This election is a live test of which tiebreak BV applies.",
        "method": "RankedRobin",
        "num_winners": 1,
        "max_rankings": len(_C6_CANDS),
        "candidates": _C6_CANDS,
        "ballots": _dense_rank_rows(_C6_LEVELS, _C6_CANDS),
        "expected": "Teaming: A1 & C tie at 5 wins. LH margin -> A1 (+134 vs +104), teaming SUCCEEDS. BV 2-way head-to-head: C beats A1 21-12 -> C, teaming FAILS on BV. Test ID BV2143.",
    },
]


# --- BV2144 — Felsenthal (2010) Example 1: plurality's four paradoxes at once ----
# SOURCE: Dan S. Felsenthal, "Review of Paradoxes Afflicting Various Voting
# Procedures Where One Out of m Candidates (m >= 2) Must Be Elected", University
# of Haifa / LSE, revised 26 May 2010 (Leverhulme Trust "Voting Power in
# Practice" workshop, Chateau du Baffy, Normandy, 30 July - 2 August 2010).
# Appendix A1 ("Demonstrating Paradoxes Afflicting the Plurality Procedure"),
# Example 1: 7 voters, candidates a/b/c — 3×(a>b>c), 2×(b>c>a), 2×(c>b>a).
# b is the Condorcet winner; a is the Condorcet loser AND absolute loser
# (a majority ranks a last), yet Plurality elects a; if c drops out, b wins (SCC).
# Cast (named, initials match): Ana=a, Bo=b, Cal=c. Two races, one electorate:
#   Plurality (choose-one): Ana 3, Bo 2, Cal 2 -> Ana.
#   STAR (house rank->score map, N=3: top=5/mid=3/bottom=1): Bo 25, Ana 19,
#   Cal 19 — finalist tie broken head-to-head (Cal beats Ana 4-3); runoff
#   Bo beats Cal 5-2 -> STAR elects the Condorcet winner Bo. (LH-verified.)
_F1_CANDS = ["Ana", "Bo", "Cal"]
_F1_STAR_ROWS = [[5, 3, 1]] * 3 + [[1, 5, 3]] * 2 + [[1, 3, 5]] * 2
_F1_PLUR_ROWS = [[1, 0, 0]] * 3 + [[0, 1, 0]] * 2 + [[0, 0, 1]] * 2

# Already created -> bettervoting.com/mxfmhm. Kept for reference; not re-run.
_CREATED_BV2144 = [
    {
        "test_id": "BV2144",
        "title": "Felsenthal's plurality paradoxes — the absolute loser wins Choose-One; STAR elects the Condorcet winner",
        "description": ("Example 1 from Dan S. Felsenthal, 'Review of Paradoxes "
                        "Afflicting Various Voting Procedures Where One Out of m "
                        "Candidates (m ≥ 2) Must Be Elected' (University of Haifa / "
                        "LSE, revised 26 May 2010; Leverhulme Trust 'Voting Power in "
                        "Practice' workshop, Château du Baffy, Normandy). Appendix A1 "
                        "demonstrates FOUR paradoxes hitting Plurality in one tiny "
                        "election: 7 voters, three candidates — 3 rank Ana>Bo>Cal, "
                        "2 rank Bo>Cal>Ana, 2 rank Cal>Bo>Ana. Bo is the Condorcet "
                        "winner (beats Ana 4-3 and Cal 5-2 head-to-head). Ana is both "
                        "the Condorcet LOSER and the ABSOLUTE loser — a majority (4 of "
                        "7) rank Ana dead last. Yet Choose-One Plurality elects Ana "
                        "(3-2-2 on first choices); and if Cal dropped out, Bo would "
                        "win — the classic spoiler (Felsenthal's SCC). This election "
                        "runs the same 7-voter electorate two ways: a Plurality race "
                        "(Ana wins) and a STAR race with the rankings mapped to 0-5 "
                        "scores (top=5, mid=3, bottom=1: Bo 25, Ana 19, Cal 19; the "
                        "second-finalist tie breaks head-to-head to Cal 4-3, and Bo "
                        "wins the runoff 5-2). STAR elects the Condorcet winner Bo — "
                        "the tabulation, not the ballot, decides."),
        "races": [
            {"title": "Felsenthal Ex.1 — Choose-One (Plurality)", "method": "Plurality",
             "num_winners": 1, "candidates": _F1_CANDS, "ballots": _F1_PLUR_ROWS},
            {"title": "Felsenthal Ex.1 — STAR (ranks mapped to 0-5 scores)", "method": "STAR",
             "num_winners": 1, "candidates": _F1_CANDS, "ballots": _F1_STAR_ROWS},
        ],
        "expected": "Plurality -> Ana (3-2-2; Condorcet & absolute loser). STAR -> Bo "
                    "(25; finalist tie 19-19 broken head-to-head to Cal, runoff 5-2). "
                    "LH-verified both. Test ID BV2144.",
    },
]


# --- BV2145 / BV2146 — Felsenthal (2010) Example 2: runoff-procedure paradoxes ---
# SOURCE: same Felsenthal (2010) paper as BV2144; Appendix A2 ("Demonstrating
# Paradoxes Afflicting the Plurality with Runoff Procedure"), Example 2.
# 17 voters, candidates a/b/c (cast: Ada/Ben/Cleo). a is the Condorcet winner
# (beats b 9-8 and c 9-8; social ordering a>b>c) but has the FEWEST first
# choices (a=5, b=6, c=6), so plurality-with-runoff eliminates a first and b
# beats c 9-8. With THREE candidates IRV is exactly plurality-with-runoff
# (one elimination, then the final pair), so the BV race uses IRV.
#   BV2145 (pre):  IRV -> Ben; Ranked Robin -> Ada; STAR (5/3/1 map: 53/51/49,
#                  runoff 9-8) -> Ada. SCC note: if Cleo withdrew, Ada would win
#                  in the first round outright (9 of 17 = majority).
#   BV2146 (post, non-monotonicity): ceteris paribus, the TWO c>b>a voters
#                  RAISE Ben (-> b>c>a). First choices become a=5, b=8, c=4:
#                  Cleo is eliminated instead of Ada, and Ada beats Ben 9-8 —
#                  Ben LOSES by gaining support. RR & STAR still -> Ada
#                  (monotone here; STAR post scores 55/53/45, runoff Ada 9-8).
# All LH-verified pre-creation (IRV/RR native; STAR via the 5/3/1 map).
_F2_CANDS = ["Ada", "Ben", "Cleo"]
_F2_PRE_BLOCS = [(3, ["Ada", "Ben", "Cleo"]),
                 (2, ["Ada", "Cleo", "Ben"]),
                 (4, ["Ben", "Ada", "Cleo"]),
                 (2, ["Ben", "Cleo", "Ada"]),
                 (4, ["Cleo", "Ada", "Ben"]),
                 (2, ["Cleo", "Ben", "Ada"])]
_F2_POST_BLOCS = [(3, ["Ada", "Ben", "Cleo"]),
                  (2, ["Ada", "Cleo", "Ben"]),
                  (4, ["Ben", "Ada", "Cleo"]),
                  (2, ["Ben", "Cleo", "Ada"]),
                  (4, ["Cleo", "Ada", "Ben"]),
                  (2, ["Ben", "Cleo", "Ada"])]   # <- the two changed voters


def _f2_races(prefix, blocs):
    R, S = _mk_ranked_and_star(blocs, _F2_CANDS)
    N = len(_F2_CANDS)
    return [
        {"title": f"{prefix} — Runoff (IRV; = plurality-with-runoff for 3 candidates)",
         "method": "IRV", "num_winners": 1, "max_rankings": N,
         "candidates": _F2_CANDS, "ballots": R},
        {"title": f"{prefix} — Ranked Robin (Copeland)", "method": "RankedRobin",
         "num_winners": 1, "max_rankings": N, "candidates": _F2_CANDS, "ballots": R},
        {"title": f"{prefix} — STAR (ranks mapped to 0-5 scores)", "method": "STAR",
         "num_winners": 1, "candidates": _F2_CANDS, "ballots": S},
    ]


# Already created -> bettervoting.com/6fj2kg (BV2145) / krk2px (BV2146). Reference.
_CREATED_BV2145_46 = [
    {
        "test_id": "BV2145",
        "title": "Felsenthal's runoff paradoxes (1 of 2) — the runoff eliminates the Condorcet winner",
        "description": ("Example 2 from Dan S. Felsenthal, 'Review of Paradoxes "
                        "Afflicting Various Voting Procedures Where One Out of m "
                        "Candidates (m ≥ 2) Must Be Elected' (University of Haifa / "
                        "LSE, revised 26 May 2010; Leverhulme Trust 'Voting Power in "
                        "Practice' workshop, Château du Baffy, Normandy), Appendix A2: "
                        "the paradoxes afflicting the plurality-with-runoff procedure. "
                        "17 voters, three candidates: 3×(Ada>Ben>Cleo), 2×(Ada>Cleo>Ben), "
                        "4×(Ben>Ada>Cleo), 2×(Ben>Cleo>Ada), 4×(Cleo>Ada>Ben), "
                        "2×(Cleo>Ben>Ada). Ada is the Condorcet winner — she beats Ben "
                        "9-8 and Cleo 9-8; the social ordering is Ada>Ben>Cleo. But Ada "
                        "has the FEWEST first choices (5 vs 6 and 6), so the runoff "
                        "procedure eliminates her first and Ben beats Cleo 9-8. (With "
                        "three candidates, instant-runoff IRV is exactly plurality-with-"
                        "runoff, which is how this race is run here.) The same ranked "
                        "ballots under Ranked Robin (Copeland) elect Ada, and under STAR "
                        "(ranks mapped to 0-5 scores: 53/51/49, runoff 9-8) also Ada. "
                        "Felsenthal also notes the SCC/spoiler: had Cleo withdrawn, Ada "
                        "would have won the first round outright with 9 of 17. Part 2 "
                        "(BV2146) shows this procedure's non-monotonicity."),
        "races": _f2_races("Felsenthal Ex.2", _F2_PRE_BLOCS),
        "expected": "IRV (runoff) -> Ben (Ada eliminated first; Ben beats Cleo 9-8). "
                    "Ranked Robin -> Ada. STAR -> Ada (53/51/49; runoff 9-8). "
                    "LH-verified all three. Test ID BV2145.",
    },
    {
        "test_id": "BV2146",
        "title": "Felsenthal's runoff paradoxes (2 of 2) — more support makes the winner lose (non-monotonicity)",
        "description": ("Example 2 (continued) from Dan S. Felsenthal's 2010 review of "
                        "voting-procedure paradoxes (University of Haifa / LSE; Appendix "
                        "A2). Identical to BV2145 except that, ceteris paribus, the two "
                        "voters whose ordering was Cleo>Ben>Ada RAISE Ben to first: "
                        "Ben>Cleo>Ada — strictly increasing Ben's support and changing "
                        "nothing else. Result: first choices are now Ada 5, Ben 8, Cleo "
                        "4, so the runoff procedure eliminates CLEO instead of Ada, and "
                        "Ada beats Ben head-to-head 9-8. Ben — who WON part 1 — loses "
                        "precisely because two voters moved him UP their ballots. That "
                        "is the lack-of-monotonicity paradox (more-is-less), a "
                        "conditional paradox: one datum changed, everything else held "
                        "constant. Ranked Robin and STAR are unaffected here (both "
                        "elect Ada before and after; STAR post scores 55/53/45 with Ada "
                        "winning the runoff 9-8). Run as IRV, which equals plurality-"
                        "with-runoff for three candidates."),
        "races": _f2_races("Felsenthal Ex.2 after the raise", _F2_POST_BLOCS),
        "expected": "IRV (runoff) -> Ada (Cleo eliminated; Ada beats Ben 9-8) — Ben "
                    "loses by GAINING support vs BV2145. Ranked Robin -> Ada. STAR -> "
                    "Ada (55/53/45; runoff 9-8). LH-verified. Test ID BV2146.",
    },
]


# --- BV2147/48/49 — Felsenthal (2010) Example 3: the Reinforcement paradox ------
# SOURCE: same Felsenthal (2010) paper; Appendix A2, Example 3 (plurality with
# runoff vs the Reinforcement postulate; a.k.a. the multiple-districts /
# inconsistency paradox). THREE elections because the electorates differ:
#   BV2147 District I  (17 voters): 4×(a>b>c), 1×(b>a>c), 5×(b>c>a),
#                      6×(c>a>b), 1×(c>b>a). No first-round majority (4/6/7);
#                      a is deleted and b beats c 10-7. Runoff -> b.
#   BV2148 District II (15 voters): 6×(a>c>b), 8×(b>c>a), 1×(c>a>b). b is
#                      ranked first by a majority (8 of 15) -> elected round 1.
#   BV2149 Combined    (32 voters = I + II amalgamated, ceteris paribus). No
#                      majority (10/14/8); c is deleted and a beats b 17-15.
#                      Runoff -> a — though b won BOTH districts. Reinforcement
#                      paradox, live.
# Cast: Alma=a, Bruno=b, Cora=c. Each election runs TWO races on the same
# ballots: the runoff procedure (IRV — identical for 3 candidates) and STAR
# (5/3/1 map). STAR is consistent HERE (Bruno in I, II, and combined; scores
# 47/51/55 -> runoff b 10-7; 41/47/47 -> b 8-7; 88/98/102 -> b 18-14) — a
# clean contrast, though score+runoff methods are not reinforcement-proof in
# general. NO Ranked Robin race: District I and the combined electorate are
# Condorcet CYCLES (a>b, b>c, c>a), so BV's RR would tie 3-way and resolve at
# RANDOM — not freezable (see the BV2142 caveat). The cycles are discussed in
# the case pages instead. All six races LH-verified pre-creation.
_F3_CANDS = ["Alma", "Bruno", "Cora"]
_F3_D1_BLOCS = [(4, ["Alma", "Bruno", "Cora"]),
                (1, ["Bruno", "Alma", "Cora"]),
                (5, ["Bruno", "Cora", "Alma"]),
                (6, ["Cora", "Alma", "Bruno"]),
                (1, ["Cora", "Bruno", "Alma"])]
_F3_D2_BLOCS = [(6, ["Alma", "Cora", "Bruno"]),
                (8, ["Bruno", "Cora", "Alma"]),
                (1, ["Cora", "Alma", "Bruno"])]
_F3_COMB_BLOCS = [(4, ["Alma", "Bruno", "Cora"]),
                  (6, ["Alma", "Cora", "Bruno"]),
                  (1, ["Bruno", "Alma", "Cora"]),
                  (13, ["Bruno", "Cora", "Alma"]),
                  (7, ["Cora", "Alma", "Bruno"]),
                  (1, ["Cora", "Bruno", "Alma"])]

_F3_SRC = ("Example 3 from Dan S. Felsenthal, 'Review of Paradoxes Afflicting "
           "Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must "
           "Be Elected' (University of Haifa / LSE, revised 26 May 2010; "
           "Leverhulme Trust 'Voting Power in Practice' workshop, Château du "
           "Baffy, Normandy), Appendix A2: the Reinforcement paradox afflicting "
           "the plurality-with-runoff procedure (a.k.a. the multiple-districts / "
           "inconsistency paradox). ")


def _f3_races(prefix, blocs):
    R, S = _mk_ranked_and_star(blocs, _F3_CANDS)
    return [
        {"title": f"{prefix} — Runoff (IRV; = plurality-with-runoff for 3 candidates)",
         "method": "IRV", "num_winners": 1, "max_rankings": len(_F3_CANDS),
         "candidates": _F3_CANDS, "ballots": R},
        {"title": f"{prefix} — STAR (ranks mapped to 0-5 scores)", "method": "STAR",
         "num_winners": 1, "candidates": _F3_CANDS, "ballots": S},
    ]


# Already created -> 9gdrqg (BV2147) / h87k6v (BV2148) / byk9v2 (BV2149). Reference.
_CREATED_BV2147_49 = [
    {
        "test_id": "BV2147",
        "title": "Felsenthal's Reinforcement paradox (I of III) — District I: the runoff elects Bruno",
        "description": (_F3_SRC +
                        "This is DISTRICT I: 17 voters — 4×(Alma>Bruno>Cora), "
                        "1×(Bruno>Alma>Cora), 5×(Bruno>Cora>Alma), 6×(Cora>Alma>Bruno), "
                        "1×(Cora>Bruno>Alma). No candidate has a first-round majority "
                        "(Alma 4, Bruno 6, Cora 7), so Alma is deleted and Bruno beats "
                        "Cora 10-7 in the runoff. Bruno also wins District II (BV2148) "
                        "outright — yet when the two districts are amalgamated (BV2149) "
                        "the SAME procedure elects Alma. A subtlety worth savoring: this "
                        "district's pairwise preferences form a Condorcet CYCLE "
                        "(Alma>Bruno 10-7, Bruno>Cora 10-7, Cora>Alma 12-5), so there is "
                        "no Condorcet winner here at all. The second race runs the same "
                        "ballots as STAR (ranks mapped 5/3/1: 47/51/55; Bruno beats Cora "
                        "10-7 in the automatic runoff) — also Bruno."),
        "races": _f3_races("Felsenthal Ex.3 District I", _F3_D1_BLOCS),
        "expected": "Runoff/IRV -> Bruno (Alma deleted 4/6/7; Bruno beats Cora 10-7). "
                    "STAR -> Bruno (47/51/55; runoff 10-7). District pairwise is a "
                    "CYCLE. LH-verified. Test ID BV2147.",
    },
    {
        "test_id": "BV2148",
        "title": "Felsenthal's Reinforcement paradox (II of III) — District II: Bruno wins outright",
        "description": (_F3_SRC +
                        "This is DISTRICT II: 15 voters — 6×(Alma>Cora>Bruno), "
                        "8×(Bruno>Cora>Alma), 1×(Cora>Alma>Bruno). Bruno is ranked "
                        "first by an absolute majority (8 of 15) and is elected in the "
                        "first round — no runoff needed. Bruno also wins District I "
                        "(BV2147) — yet the amalgamated electorate (BV2149) elects "
                        "Alma under the same procedure. Here Bruno is also the "
                        "Condorcet winner (beats Alma 8-7 and Cora 8-7). The second "
                        "race runs the same ballots as STAR (5/3/1 map: 41/47/47; Bruno "
                        "beats Cora 8-7 in the runoff) — also Bruno."),
        "races": _f3_races("Felsenthal Ex.3 District II", _F3_D2_BLOCS),
        "expected": "Runoff/IRV -> Bruno in round 1 (8 of 15 = majority). STAR -> "
                    "Bruno (41/47/47; runoff 8-7). LH-verified. Test ID BV2148.",
    },
    {
        "test_id": "BV2149",
        "title": "Felsenthal's Reinforcement paradox (III of III) — Combined: Bruno won both districts, Alma wins the whole",
        "description": (_F3_SRC +
                        "This is the AMALGAMATED electorate: the 32 voters of Districts "
                        "I and II together, ceteris paribus — 4×(Alma>Bruno>Cora), "
                        "6×(Alma>Cora>Bruno), 1×(Bruno>Alma>Cora), 13×(Bruno>Cora>Alma), "
                        "7×(Cora>Alma>Bruno), 1×(Cora>Bruno>Alma). No first-round "
                        "majority (Alma 10, Bruno 14, Cora 8), so CORA is deleted — and "
                        "Alma beats Bruno 17-15 in the runoff. Bruno won District I "
                        "(BV2147) AND District II (BV2148); amalgamating two electorates "
                        "that both chose Bruno makes the procedure elect Alma. That "
                        "violates the Reinforcement postulate (a.k.a. the multiple-"
                        "districts / inconsistency paradox). The combined pairwise "
                        "preferences form a Condorcet cycle (Alma>Bruno 17-15, "
                        "Bruno>Cora 18-14, Cora>Alma 21-11), so no Condorcet argument "
                        "rescues the result — the failure is the procedure disagreeing "
                        "with ITSELF. The second race runs the same 32 ballots as STAR "
                        "(5/3/1 map: 88/98/102; Bruno beats Cora 18-14 in the automatic "
                        "runoff) — Bruno, consistent with both districts."),
        "races": _f3_races("Felsenthal Ex.3 Combined", _F3_COMB_BLOCS),
        "expected": "Runoff/IRV -> Alma (Cora deleted 10/14/8; Alma beats Bruno 17-15) "
                    "— though Bruno won BOTH districts. STAR -> Bruno (88/98/102; "
                    "runoff 18-14), consistent. Combined pairwise is a CYCLE. "
                    "LH-verified. Test ID BV2149.",
    },
]


# --- BV2150/51 — Felsenthal (2010) Example 4: the No-Show and Twin paradoxes ----
# SOURCE: same Felsenthal (2010) paper; Appendix A2, Example 4 (plurality with
# runoff vs the No-Show and — weak-form — Twin paradoxes). A pre/after PAIR:
#   BV2150 FULL (11 voters): 4×(a>b>c), 3×(b>c>a), 1×(c>a>b), 3×(c>b>a).
#     No first-round majority (4/3/4); b is deleted and c beats a 7-4 — the
#     WORST outcome for the four a>b>c voters. Note b is the Condorcet winner
#     (beats a 6-5, c 7-4); the runoff elects c, which b beats 7-4.
#   BV2151 NO-SHOW (9 voters): ceteris paribus, TWO of the a>b>c voters stay
#     home. First choices 2/3/4 -> now A is deleted, and b beats c 5-4. The
#     abstainers get b instead of c — a BETTER outcome for them than voting:
#     the No-Show paradox. Read in reverse it is the (weak) TWIN paradox:
#     start from the 9-voter electorate and add two voters IDENTICAL to the
#     a>b>c pair — their twins' arrival elects c, their common worst.
# Cast: Andy=a, Beth=b, Carl=c. THREE races per election this time — b/Beth is
# the Condorcet winner in BOTH electorates, so Ranked Robin is deterministic
# (no cycle, no BV random tiebreak): IRV, RankedRobin, STAR.
#   Expected: BV2150 IRV -> Carl; RR -> Beth; STAR -> Beth (29/37/33, runoff
#   7-4). BV2151 IRV -> Beth; RR -> Beth; STAR -> Beth (19/31/31 — Beth and
#   Carl advance over Andy, no advancement tie — runoff 5-4). RR and STAR
#   elect Beth in both electorates, so for them showing up never hurt the
#   Andy voters HERE (Condorcet methods are not participation-proof in
#   general — Moulin's theorem — but this electorate doesn't trigger it).
# All six races LH-verified pre-creation.
_F4_CANDS = ["Andy", "Beth", "Carl"]
_F4_FULL_BLOCS = [(4, ["Andy", "Beth", "Carl"]),
                  (3, ["Beth", "Carl", "Andy"]),
                  (1, ["Carl", "Andy", "Beth"]),
                  (3, ["Carl", "Beth", "Andy"])]
_F4_NOSHOW_BLOCS = [(2, ["Andy", "Beth", "Carl"]),   # <- two stayed home
                    (3, ["Beth", "Carl", "Andy"]),
                    (1, ["Carl", "Andy", "Beth"]),
                    (3, ["Carl", "Beth", "Andy"])]

_F4_SRC = ("Example 4 from Dan S. Felsenthal, 'Review of Paradoxes Afflicting "
           "Various Voting Procedures Where One Out of m Candidates (m ≥ 2) Must "
           "Be Elected' (University of Haifa / LSE, revised 26 May 2010; "
           "Leverhulme Trust 'Voting Power in Practice' workshop, Château du "
           "Baffy, Normandy), Appendix A2: the No-Show and Twin paradoxes "
           "afflicting the plurality-with-runoff procedure. ")


def _f4_races(prefix, blocs):
    R, S = _mk_ranked_and_star(blocs, _F4_CANDS)
    N = len(_F4_CANDS)
    return [
        {"title": f"{prefix} — Runoff (IRV; = plurality-with-runoff for 3 candidates)",
         "method": "IRV", "num_winners": 1, "max_rankings": N,
         "candidates": _F4_CANDS, "ballots": R},
        {"title": f"{prefix} — Ranked Robin (Copeland)", "method": "RankedRobin",
         "num_winners": 1, "max_rankings": N, "candidates": _F4_CANDS, "ballots": R},
        {"title": f"{prefix} — STAR (ranks mapped to 0-5 scores)", "method": "STAR",
         "num_winners": 1, "candidates": _F4_CANDS, "ballots": S},
    ]


# Already created -> dxg8pb (BV2150) / 97hbpw (BV2151). Reference.
_CREATED_BV2150_51 = [
    {
        "test_id": "BV2150",
        "title": "Felsenthal's No-Show paradox (1 of 2) — everyone votes, and the runoff elects their worst choice",
        "description": (_F4_SRC +
                        "This is the FULL electorate: 11 voters — 4×(Andy>Beth>Carl), "
                        "3×(Beth>Carl>Andy), 1×(Carl>Andy>Beth), 3×(Carl>Beth>Andy). "
                        "No candidate has a first-round majority (Andy 4, Beth 3, Carl "
                        "4), so the runoff procedure — run as IRV, identical for three "
                        "candidates — deletes BETH, and Carl beats Andy 7-4. Carl is "
                        "the WORST outcome for the four Andy>Beth>Carl voters; part 2 "
                        "(BV2151) shows that if two of them had simply stayed home, "
                        "Beth would have won — voting hurt them (the No-Show paradox). "
                        "Beth is in fact this electorate's Condorcet winner (beats "
                        "Andy 6-5 and Carl 7-4): the second race, Ranked Robin "
                        "(Copeland), elects Beth directly, and the third race, STAR "
                        "(ranks mapped 5/3/1: Andy 29, Beth 37, Carl 33), elects Beth "
                        "through the automatic runoff 7-4."),
        "races": _f4_races("Felsenthal Ex.4 full electorate", _F4_FULL_BLOCS),
        "expected": "Runoff/IRV -> Carl (Beth deleted 4/3/4; Carl beats Andy 7-4). "
                    "Ranked Robin -> Beth (Condorcet winner, 2-0). STAR -> Beth "
                    "(29/37/33; runoff 7-4). LH-verified. Test ID BV2150.",
    },
    {
        "test_id": "BV2151",
        "title": "Felsenthal's No-Show paradox (2 of 2) — two supporters stay home, and their side does better",
        "description": (_F4_SRC +
                        "This is the NO-SHOW electorate: ceteris paribus, TWO of the "
                        "four Andy>Beth>Carl voters do not participate — 9 voters: "
                        "2×(Andy>Beth>Carl), 3×(Beth>Carl>Andy), 1×(Carl>Andy>Beth), "
                        "3×(Carl>Beth>Andy). First choices are now Andy 2, Beth 3, "
                        "Carl 4, so the runoff procedure deletes ANDY — and Beth beats "
                        "Carl 5-4. The two abstainers get Beth, their second choice, "
                        "instead of Carl, their last (BV2150): abstaining served them "
                        "better than voting. That is the No-Show paradox. Read in "
                        "reverse it is the weak TWIN paradox: start here and add two "
                        "voters IDENTICAL to the Andy>Beth>Carl pair — the twins' "
                        "arrival (BV2150) elects Carl, their common worst choice. "
                        "Beth remains the Condorcet winner (beats Andy 6-3, Carl 5-4): "
                        "Ranked Robin elects Beth, and STAR (5/3/1 map: Andy 19, Beth "
                        "31, Carl 31; Beth and Carl advance over Andy) elects Beth "
                        "5-4 — both unchanged from BV2150, so under those counts the "
                        "Andy voters were never punished for showing up here."),
        "races": _f4_races("Felsenthal Ex.4 after two no-shows", _F4_NOSHOW_BLOCS),
        "expected": "Runoff/IRV -> Beth (Andy deleted 2/3/4; Beth beats Carl 5-4) — "
                    "the abstaining pair does BETTER than in BV2150. Ranked Robin -> "
                    "Beth. STAR -> Beth (19/31/31; runoff 5-4). LH-verified. "
                    "Test ID BV2151.",
    },
]


# --- BV2152/53/54 — Felsenthal (2010) §A3: paradoxes afflicting APPROVAL --------
# SOURCE: same Felsenthal (2010) paper; Appendix A3 ("Demonstrating the
# Paradoxes Afflicting the Approval Voting Procedure"), Examples 5, 7, 8.
# (Example 6 — the Pareto-dominated paradox — turns on a RANDOM a/b tie, which
# BV can't freeze; it becomes an LH-only case instead.) Each election pairs an
# Approval race (the strategic approval profile from the text, 0/1 ballots)
# with ranked race(s) on the SAME voters' full orderings — all deterministic
# (Condorcet winners exist; no cycles, no BV random tiebreaks).
#   BV2152 (Ex.5; due to Felsenthal & Maoz 1988: 123, Example 2): 47 voters.
#     Rankings 18×(a>b>c), 6×(b>c>a), 8×(b>a>c), 2×(c>a>b), 13×(c>b>a);
#     social ordering b>a>c, b is the Condorcet winner (beats a 27-20, c
#     32-15). Approvals per the text's parentheses: 18×{a}, 6×{b,c}, 8×{b,a},
#     2×{c,a}, 13×{c} -> a 28, b 14, c 21: APPROVAL ELECTS a, not the
#     Condorcet winner. Races: Approval -> Anna; Ranked Robin -> Bert.
#   BV2153 (Ex.7): 100 voters — 51×(a>b>c), 48×(b>c>a), 1×(c>b>a). a is
#     ranked FIRST BY AN ABSOLUTE MAJORITY (51) and is the Condorcet winner.
#     If every voter approves their top two: a 51, b 100, c 49 — APPROVAL
#     ELECTS b: the Absolute Majority paradox. Races: Approval -> Bella;
#     IRV -> Amos (round-1 majority); Ranked Robin -> Amos.
#   BV2154 (Ex.8): 15 voters — 6×(a>b>c), 4×(b>c>a), 1×(c>a>b), 4×(c>b>a).
#     Social ordering b>c>a: a is the Condorcet loser AND absolute loser
#     (ranked last by 8 of 15). If the single c>a>b voter approves the top
#     two and everyone else bullet-votes: a 7, b 4, c 5 — APPROVAL ELECTS a.
#     Bonus: one electorate, THREE winners — Approval -> April, IRV -> Clara
#     (Bruce deleted 6/4/5; Clara beats April 9-6), Ranked Robin -> Bruce.
# Cast: BV2152 Anna/Bert/Carla; BV2153 Amos/Bella/Chad; BV2154 April/Bruce/
# Clara. All eight races LH-verified pre-creation.

_F5_SRC = ("From Dan S. Felsenthal, 'Review of Paradoxes Afflicting Various "
           "Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be "
           "Elected' (University of Haifa / LSE, revised 26 May 2010; Leverhulme "
           "Trust 'Voting Power in Practice' workshop, Château du Baffy, "
           "Normandy), Appendix A3: the paradoxes afflicting the Approval "
           "voting procedure. ")


def _expand(blocs):
    """Weighted (count, row) blocs -> one row per voter."""
    out = []
    for n, row in blocs:
        out += [list(row)] * n
    return out


def _ranks(blocs, cands):
    R, _ = _mk_ranked_and_star(blocs, cands)
    return R


_F6_CANDS = ["Anna", "Bert", "Carla"]
_F6_RANKED = [(18, ["Anna", "Bert", "Carla"]), (6, ["Bert", "Carla", "Anna"]),
              (8, ["Bert", "Anna", "Carla"]), (2, ["Carla", "Anna", "Bert"]),
              (13, ["Carla", "Bert", "Anna"])]
_F6_APPR = [(18, (1, 0, 0)), (6, (0, 1, 1)), (8, (1, 1, 0)),
            (2, (1, 0, 1)), (13, (0, 0, 1))]

_F7_CANDS = ["Amos", "Bella", "Chad"]
_F7_RANKED = [(51, ["Amos", "Bella", "Chad"]), (48, ["Bella", "Chad", "Amos"]),
              (1, ["Chad", "Bella", "Amos"])]
_F7_APPR = [(51, (1, 1, 0)), (48, (0, 1, 1)), (1, (0, 1, 1))]

_F8_CANDS = ["April", "Bruce", "Clara"]
_F8_RANKED = [(6, ["April", "Bruce", "Clara"]), (4, ["Bruce", "Clara", "April"]),
              (1, ["Clara", "April", "Bruce"]), (4, ["Clara", "Bruce", "April"])]
_F8_APPR = [(6, (1, 0, 0)), (4, (0, 1, 0)), (1, (1, 0, 1)), (4, (0, 0, 1))]

# Already created -> r6ctvy (BV2152) / pcttmr (BV2153) / wq6yv7 (BV2154). Reference.
_CREATED_BV2152_54 = [
    {
        "test_id": "BV2152",
        "title": "Felsenthal & Maoz's Approval paradox — the Condorcet winner loses the approval count",
        "description": (_F5_SRC +
                        "Example 5, due to Felsenthal & Maoz (1988: 123, Example 2). "
                        "47 voters, three candidates, rankings 18×(Anna>Bert>Carla), "
                        "6×(Bert>Carla>Anna), 8×(Bert>Anna>Carla), 2×(Carla>Anna>Bert), "
                        "13×(Carla>Bert>Anna). The social preference ordering is "
                        "Bert>Anna>Carla — Bert is the Condorcet winner (beats Anna "
                        "27-20 and Carla 32-15). But when each voter approves the "
                        "candidates the text marks in parentheses — 18×{Anna}, "
                        "6×{Bert,Carla}, 8×{Bert,Anna}, 2×{Carla,Anna}, 13×{Carla} — "
                        "the approval totals are Anna 28, Bert 14, Carla 21, and "
                        "APPROVAL ELECTS ANNA: the Condorcet winner paradox under "
                        "Approval. The second race runs the same voters' full rankings "
                        "as Ranked Robin (Copeland), which elects Bert directly."),
        "races": [
            {"title": "Felsenthal Ex.5 — Approval (the text's approval sets)",
             "method": "Approval", "num_winners": 1, "candidates": _F6_CANDS,
             "ballots": _expand(_F6_APPR)},
            {"title": "Felsenthal Ex.5 — Ranked Robin (the same voters' full rankings)",
             "method": "RankedRobin", "num_winners": 1, "max_rankings": 3,
             "candidates": _F6_CANDS, "ballots": _ranks(_F6_RANKED, _F6_CANDS)},
        ],
        "expected": "Approval -> Anna (28/14/21), NOT the Condorcet winner. "
                    "Ranked Robin -> Bert (beats Anna 27-20, Carla 32-15). "
                    "LH-verified. Test ID BV2152.",
    },
    {
        "test_id": "BV2153",
        "title": "Felsenthal's Absolute Majority paradox — a majority's first choice loses the approval count",
        "description": (_F5_SRC +
                        "Example 7. 100 voters — 51×(Amos>Bella>Chad), "
                        "48×(Bella>Chad>Amos), 1×(Chad>Bella>Amos). Amos is ranked "
                        "FIRST by an absolute majority of the voters (51 of 100) and "
                        "is the Condorcet winner. But if every voter approves their "
                        "top TWO preferences, the approval totals are Amos 51, Bella "
                        "100, Chad 49 — APPROVAL ELECTS BELLA despite Amos's absolute "
                        "majority of first preferences: the Absolute Majority paradox. "
                        "The ranked races on the same orderings show the contrast: "
                        "instant-runoff (IRV) elects Amos immediately (51 is a "
                        "first-round majority), and Ranked Robin (Copeland) elects "
                        "Amos as Condorcet winner (beats Bella 51-49, Chad 51-49)."),
        "races": [
            {"title": "Felsenthal Ex.7 — Approval (everyone approves their top two)",
             "method": "Approval", "num_winners": 1, "candidates": _F7_CANDS,
             "ballots": _expand(_F7_APPR)},
            {"title": "Felsenthal Ex.7 — IRV (majority favorite wins round one)",
             "method": "IRV", "num_winners": 1, "max_rankings": 3,
             "candidates": _F7_CANDS, "ballots": _ranks(_F7_RANKED, _F7_CANDS)},
            {"title": "Felsenthal Ex.7 — Ranked Robin (Copeland)",
             "method": "RankedRobin", "num_winners": 1, "max_rankings": 3,
             "candidates": _F7_CANDS, "ballots": _ranks(_F7_RANKED, _F7_CANDS)},
        ],
        "expected": "Approval -> Bella (51/100/49) despite Amos's absolute majority "
                    "of first preferences. IRV -> Amos (round-1 majority). Ranked "
                    "Robin -> Amos (Condorcet winner). LH-verified. Test ID BV2153.",
    },
    {
        "test_id": "BV2154",
        "title": "Felsenthal's Approval paradox — the absolute loser wins; one electorate, three winners",
        "description": (_F5_SRC +
                        "Example 8. 15 voters — 6×(April>Bruce>Clara), "
                        "4×(Bruce>Clara>April), 1×(Clara>April>Bruce), "
                        "4×(Clara>Bruce>April). The social preference ordering is "
                        "Bruce>Clara>April: April is both the Condorcet LOSER and the "
                        "ABSOLUTE loser — an absolute majority (8 of 15) rank April "
                        "dead last. But if the single Clara>April>Bruce voter approves "
                        "their top two while everyone else votes only their top "
                        "preference, the approval totals are April 7, Bruce 4, Clara 5 "
                        "— APPROVAL ELECTS APRIL: the Condorcet loser and Absolute "
                        "loser paradoxes under Approval. Bonus: this one electorate "
                        "produces THREE different winners — Approval elects April, "
                        "instant-runoff (IRV) elects Clara (Bruce is deleted 6/4/5 and "
                        "Clara beats April 9-6), and Ranked Robin (Copeland) elects "
                        "Bruce, the Condorcet winner (beats April 8-7, Clara 10-5). "
                        "The tabulation, not the ballot, decides."),
        "races": [
            {"title": "Felsenthal Ex.8 — Approval (one strategic voter approves two)",
             "method": "Approval", "num_winners": 1, "candidates": _F8_CANDS,
             "ballots": _expand(_F8_APPR)},
            {"title": "Felsenthal Ex.8 — IRV (Hare)",
             "method": "IRV", "num_winners": 1, "max_rankings": 3,
             "candidates": _F8_CANDS, "ballots": _ranks(_F8_RANKED, _F8_CANDS)},
            {"title": "Felsenthal Ex.8 — Ranked Robin (Copeland)",
             "method": "RankedRobin", "num_winners": 1, "max_rankings": 3,
             "candidates": _F8_CANDS, "ballots": _ranks(_F8_RANKED, _F8_CANDS)},
        ],
        "expected": "Approval -> April (7/4/5; Condorcet & absolute loser). IRV -> "
                    "Clara (Bruce deleted; 9-6). Ranked Robin -> Bruce (Condorcet "
                    "winner). Three winners, one electorate. LH-verified. "
                    "Test ID BV2154.",
    },
]


# --- BV2155–59 — the "Whoops" library promoted to live BV elections -------------
# The five classic method-comparison cases from method_comparisons/
# paradoxes_and_whoops/, each created as a real BV election so the repo pages
# can point at live results (Adam: rename the Whoops files to the bv-case
# naming afterwards). House rule per Adam: STAR IS RACE 1 in every election —
# the lead/reference method the others are compared against. Only
# DETERMINISTIC races are included (the W03 cycle would make BV's Ranked Robin
# tiebreak RANDOM, so that election carries no RR race). All races LH-verified.
_W1_CANDS = ["Memphis", "Nashville", "Chattanooga", "Knoxville"]
_W1_STAR = [(42, (5, 2, 1, 0)), (26, (1, 5, 3, 2)), (15, (0, 3, 5, 4)), (17, (0, 3, 4, 5))]
_W1_PLUR = [(42, (1, 0, 0, 0)), (26, (0, 1, 0, 0)), (15, (0, 0, 1, 0)), (17, (0, 0, 0, 1))]
_W1_RANKS = [(42, (1, 2, 3, 4)), (26, (4, 1, 2, 3)), (15, (4, 3, 1, 2)), (17, (4, 3, 2, 1))]

_W2_CANDS = ["Ada", "Bruno", "Cleo"]
_W2_STAR = [(40, (5, 1, 2)), (35, (1, 5, 2)), (25, (3, 3, 5))]
_W2_RANKS = [(40, (1, 3, 2)), (35, (3, 1, 2)), (25, (2, 2, 1))]   # 25× Cleo first, Ada=Bruno tied 2nd

_W3_CANDS = ["Rock", "Paper", "Scissors"]
_W3_STAR = [(35, (5, 3, 0)), (33, (0, 5, 3)), (32, (3, 0, 5))]
_W3_RANKS = [(35, (1, 2, 3)), (33, (3, 1, 2)), (32, (2, 3, 1))]
_W3_APPR = [(35, (1, 1, 0)), (33, (0, 1, 1)), (32, (1, 0, 1))]    # approve scores >= 3

_W4_CANDS = ["A", "B", "C", "D", "E"]
_W4_BLOCS = [(50, ["A", "B", "C", "D", "E"]), (51, ["B", "A", "C", "D", "E"]),
             (100, ["C", "D", "B", "E", "A"]), (53, ["D", "E", "C", "B", "A"]),
             (49, ["E", "D", "C", "B", "A"])]
_W4_PLUR = [(50, (1, 0, 0, 0, 0)), (51, (0, 1, 0, 0, 0)), (100, (0, 0, 1, 0, 0)),
            (53, (0, 0, 0, 1, 0)), (49, (0, 0, 0, 0, 1))]

_W5_CANDS = ["B", "G", "N", "F"]
_W5_BLOCS = [(7, ["B", "G", "N", "F"]), (6, ["G", "B", "N", "F"]),
             (5, ["N", "G", "B", "F"]), (3, ["F", "N", "G", "B"])]

_W4_R, _W4_S = _mk_ranked_and_star(_W4_BLOCS, _W4_CANDS)   # N=5 map: 5,4,3,2,1
_W5_R, _W5_S = _mk_ranked_and_star(_W5_BLOCS, _W5_CANDS)   # N=4 map: 5,4,2,1

# Already created -> cphxpt/3grpbb/mmcmpy/gr72hd/f4cjpy (BV2155-59). Reference.
_CREATED_BV2155_59 = [
    {
        "test_id": "BV2155",
        "title": "Tennessee capital, four ways — one electorate; Memphis, Knoxville or Nashville depending on the count",
        "description": ("The classic Tennessee state-capital example (a staple of "
                        "voting-methods teaching): 100 voters spread along the state "
                        "vote on where to put the capital, with preferences from simple "
                        "geographic distance — 42 around Memphis (far west), 26 around "
                        "Nashville (central), 15 around Chattanooga and 17 around "
                        "Knoxville (east). One sincere electorate, four counts, three "
                        "winners: STAR (0-5 scores from the distance model) elects "
                        "NASHVILLE, the central compromise that also beats every rival "
                        "head-to-head (the Condorcet winner — confirmed by the Ranked "
                        "Robin race); Choose-One Plurality elects MEMPHIS (biggest "
                        "single bloc, 42, though 58 voters put Memphis dead last); and "
                        "instant-runoff IRV elects KNOXVILLE (Chattanooga's elimination "
                        "feeds east: 15 transfers make Knoxville 32, Nashville is "
                        "deleted next, and Knoxville beats Memphis 58-42). The "
                        "tabulation, not the ballot, decides."),
        "races": [
            {"title": "Tennessee — STAR (distance scores)", "method": "STAR",
             "num_winners": 1, "candidates": _W1_CANDS, "ballots": _expand(_W1_STAR)},
            {"title": "Tennessee — Choose-One (Plurality)", "method": "Plurality",
             "num_winners": 1, "candidates": _W1_CANDS, "ballots": _expand(_W1_PLUR)},
            {"title": "Tennessee — IRV (Hare)", "method": "IRV", "num_winners": 1,
             "max_rankings": 4, "candidates": _W1_CANDS, "ballots": _expand(_W1_RANKS)},
            {"title": "Tennessee — Ranked Robin (Copeland)", "method": "RankedRobin",
             "num_winners": 1, "max_rankings": 4, "candidates": _W1_CANDS,
             "ballots": _expand(_W1_RANKS)},
        ],
        "expected": "STAR -> Nashville; Plurality -> Memphis; IRV -> Knoxville; "
                    "Ranked Robin -> Nashville (Condorcet winner). LH-verified. "
                    "Test ID BV2155.",
    },
    {
        "test_id": "BV2156",
        "title": "STAR's own miss — the Condorcet winner scores third and never reaches the runoff",
        "description": ("STAR is not perfect, and this 100-voter example is its "
                        "signature (and rare) failure, shown honestly. Cleo is the "
                        "CONDORCET WINNER — beats Ada 60-40 and Bruno 65-35 head-to-"
                        "head — but is a low-scored compromise: the two wings score "
                        "Cleo only a 2, so the score totals are Ada 310, Bruno 290, "
                        "Cleo 275 and Cleo finishes THIRD, never reaching the "
                        "automatic runoff. STAR elects ADA (beats Bruno 40-35 with 25 "
                        "Equal Support). Sincere ballots, no strategy — the score-"
                        "method cousin of IRV's center squeeze (STAR is ~98% Condorcet-"
                        "efficient in spatial models, so this is rare but structural). "
                        "The second race counts the same voters' rankings (including "
                        "the 25 ballots ranking Ada and Bruno EQUAL second) by Ranked "
                        "Robin, which elects Cleo directly."),
        "races": [
            {"title": "STAR's miss — STAR (0-5 scores)", "method": "STAR",
             "num_winners": 1, "candidates": _W2_CANDS, "ballots": _expand(_W2_STAR)},
            {"title": "STAR's miss — Ranked Robin (equal ranks allowed)",
             "method": "RankedRobin", "num_winners": 1, "max_rankings": 3,
             "candidates": _W2_CANDS, "ballots": _expand(_W2_RANKS)},
        ],
        "expected": "STAR -> Ada (310/290/275; runoff 40-35). Ranked Robin -> Cleo "
                    "(Condorcet winner 60-40, 65-35). LH-verified. Test ID BV2156.",
    },
    {
        "test_id": "BV2157",
        "title": "Rock, Paper, Scissors — a Condorcet cycle: STAR and IRV pick Rock, Approval picks Paper",
        "description": ("The paradox of voting itself, as a 100-voter election. Rock "
                        "beats Paper 67-33, Paper beats Scissors 68-32, Scissors beats "
                        "Rock 65-35 — a majority CYCLE with NO Condorcet winner, so "
                        "'majority rule' is intransitive on these sincere ballots. "
                        "Methods that don't need a Condorcet winner still finish: STAR "
                        "elects ROCK on a razor-thin scoring round (Rock 271, Paper "
                        "270, Scissors 259; runoff 67-33), IRV also elects ROCK "
                        "(Scissors out first, 32 transfers), and Approval (approving "
                        "scores of 3+) elects PAPER 68-67-65. NOTE: this election "
                        "deliberately carries NO Ranked Robin race — under a perfect "
                        "3-way Copeland tie BetterVoting resolves at RANDOM, which "
                        "cannot be frozen into a repeatable test case."),
        "races": [
            {"title": "Rock-Paper-Scissors — STAR (271 vs 270)", "method": "STAR",
             "num_winners": 1, "candidates": _W3_CANDS, "ballots": _expand(_W3_STAR)},
            {"title": "Rock-Paper-Scissors — IRV (Hare)", "method": "IRV",
             "num_winners": 1, "max_rankings": 3, "candidates": _W3_CANDS,
             "ballots": _expand(_W3_RANKS)},
            {"title": "Rock-Paper-Scissors — Approval (approve 3+)", "method": "Approval",
             "num_winners": 1, "candidates": _W3_CANDS, "ballots": _expand(_W3_APPR)},
        ],
        "expected": "STAR -> Rock (271/270/259; runoff 67-33). IRV -> Rock. "
                    "Approval -> Paper (68/67/65). Cycle: no Condorcet winner; no RR "
                    "race on purpose. LH-verified. Test ID BV2157.",
    },
    {
        "test_id": "BV2158",
        "title": "Ossipoff's buried centrist — the candidate who beats everyone is eliminated by instant runoff",
        "description": ("Mike Ossipoff's one-dimensional 303-voter example (via "
                        "rangevoting.org, §12). Five candidates A-E on a left-right "
                        "line; C is the centrist with 100 first-choice votes — the "
                        "most of any candidate — AND the Condorcet winner (beats every "
                        "rival roughly 2:1). Choose-One Plurality elects C. Ranked "
                        "Robin elects C. STAR (ranks mapped to 0-5 scores, top=5 … "
                        "bottom=1: C 1109, D 1063, B 959) elects C. But instant-runoff "
                        "IRV eliminates C in round three — the wings' transfers pile "
                        "up before the center's do — and elects D. A realistic "
                        "'one-dimensional politics' taper where IRV alone misses the "
                        "consensus candidate that even Plurality finds."),
        "races": [
            {"title": "Ossipoff centrist — STAR (ranks mapped to 0-5)", "method": "STAR",
             "num_winners": 1, "candidates": _W4_CANDS, "ballots": _W4_S},
            {"title": "Ossipoff centrist — Choose-One (Plurality)", "method": "Plurality",
             "num_winners": 1, "candidates": _W4_CANDS, "ballots": _expand(_W4_PLUR)},
            {"title": "Ossipoff centrist — IRV (Hare)", "method": "IRV",
             "num_winners": 1, "max_rankings": 5, "candidates": _W4_CANDS,
             "ballots": _W4_R},
            {"title": "Ossipoff centrist — Ranked Robin (Copeland)", "method": "RankedRobin",
             "num_winners": 1, "max_rankings": 5, "candidates": _W4_CANDS,
             "ballots": _W4_R},
        ],
        "expected": "STAR -> C (1109/1063/959; runoff 201-102). Plurality -> C (100 "
                    "first choices). Ranked Robin -> C (Condorcet winner). IRV -> D "
                    "(C eliminated round 3). LH-verified. Test ID BV2158.",
    },
    {
        "test_id": "BV2159",
        "title": "Brams' 21-voter sampler — IRV elects B while G beats everyone head-to-head",
        "description": ("Steven Brams' famous example (Notices of the AMS, 1982; via "
                        "rangevoting.org §12): 21 voters, four candidates — "
                        "7×(B>G>N>F), 6×(G>B>N>F), 5×(N>G>B>F), 3×(F>N>G>B). G is the "
                        "Condorcet winner (beats B 14-7, N 13-8, F 18-3) — yet "
                        "instant-runoff IRV eliminates G's supporters' chances (N and "
                        "F fall first, transfers make B 11 of 21) and elects B. The "
                        "same 21 ballots also demonstrate a no-show paradox, a "
                        "truncation incentive, favorite betrayal and non-monotonicity "
                        "— several IRV pathologies in one tiny, academically sourced "
                        "election. STAR (ranks mapped to 0-5: G 84, B 72, N 63, F 33; "
                        "runoff G beats B 14-7) and Ranked Robin both elect G."),
        "races": [
            {"title": "Brams sampler — STAR (ranks mapped to 0-5)", "method": "STAR",
             "num_winners": 1, "candidates": _W5_CANDS, "ballots": _W5_S},
            {"title": "Brams sampler — IRV (Hare)", "method": "IRV",
             "num_winners": 1, "max_rankings": 4, "candidates": _W5_CANDS,
             "ballots": _W5_R},
            {"title": "Brams sampler — Ranked Robin (Copeland)", "method": "RankedRobin",
             "num_winners": 1, "max_rankings": 4, "candidates": _W5_CANDS,
             "ballots": _W5_R},
        ],
        "expected": "STAR -> G (84/72/63/33; runoff 14-7). IRV -> B. Ranked Robin -> "
                    "G (Condorcet winner 14-7, 13-8, 18-3). LH-verified. Test ID "
                    "BV2159.",
    },
]


# --- BV2160-63 — Felsenthal (2010) §A5 (Borda) + §A6 (RCV-IRV, a.k.a. "AV") ------
# SOURCE: same Felsenthal (2010) paper; Appendix A5 ("Demonstrating Paradoxes
# Afflicting Borda's procedure", Examples 13-15) and A6 ("...the Alternative
# Vote Procedure" — Felsenthal's British name for instant-runoff; house
# terminology is RCV-IRV, Example 16 due to Nurmi 1999: 63).
# BetterVoting has NO Borda tabulator (and neither does the LH engine — Borda
# is cross-checked via pref_voting), so the Borda counts live as worked
# numbers in the case pages while the BV elections carry the same electorate
# under STAR (race 1, house rule) + the other supported methods that are
# DETERMINISTIC on the profile:
#   Ex.13 (Borda's Absolute-Majority failure, 51/48/1) is the SAME electorate
#     as BV2153 — no new election; the BV2153 case page gains a Borda section
#     (Borda 102/148/50 -> b, missing the 51-vote absolute winner a).
#   BV2160 (Ex.14, adapted from Fishburn 1974: 543): 7 voters, 4 candidates —
#     3×(a>b>c>d), 1×(b>c>a>d), 1×(b>c>d>a), 2×(c>d>a>b). Borda (k..0):
#     19/19/20/12 -> c; if V1-V3 TRUNCATE c: 16/16/14/12 -> a/b tie — the
#     Truncation paradox under Borda (paper only). Pairwise is a CYCLE
#     (a>b 5-2, b>c 5-2, c>a 4-3) -> no RR race (BV random); IRV would hit a
#     RANDOM elimination tie (b/c at 2) -> no IRV race. Live races: STAR
#     (5/4/2/1 map: 22/24/24/14; the b-c tie is for BOTH finalist slots, so
#     both advance and b wins the runoff 5-2) and Plurality (a, 3 of 7).
#   BV2161 (Ex.15): 7 voters — 2×(a>c>b), 2×(b>a>c), 3×(c>b>a). NOTE: the
#     paper PRINTS the third bloc as c>a>b, but its own Borda points 6/7/8
#     (and totals 21) are only consistent with c>b>a — we use the arithmetic-
#     consistent profile. Borda -> c (8); if b (a loser) drops out, Borda ->
#     a 4-3: SCC under Borda (paper only). Pairwise is again a cycle and the
#     IRV first count has an a/b elimination tie -> live races are STAR
#     (19/21/23 -> c beats b 5-2) and Plurality (c, 3 of 7). Note STAR and
#     Plurality agree with Borda here (c) — the paradox is Borda's
#     INSTABILITY when a loser exits, not the initial pick.
#   BV2162/63 (Ex.16, Nurmi 1999: 63) — the Truncation paradox under RCV-IRV,
#     LIVE, as a pre/post pair. 103 voters, 4 candidates:
#     33×(a>b>c>d), 29×(b>a>c>d), 24×(c>b>a>d), 17×(d>c>b>a).
#     b is the Condorcet winner (beats a 70-33, c 62-41, d 86-17).
#     BV2162 (sincere): IRV -> a (d out 17, transfers to c 41; b out 29;
#       a 62) — also a Condorcet-winner failure. STAR (5/4/2/1 map:
#       346/407/312/171) -> b; Ranked Robin -> b.
#     BV2163 (truncated): ceteris paribus the 17 d>c>b>a voters list ONLY d.
#       d is still eliminated first but their ballots exhaust, so C (not b)
#       is eliminated next and B wins — the truncators PREFER b to a:
#       revealing less got them more. STAR -> b (329/373/244/171); RR -> b.
# All ten live races LH-verified pre-creation.

_E14_CANDS = ["A", "B", "C", "D"]
_E14_STAR = [(3, (5, 4, 2, 1)), (1, (2, 5, 4, 1)), (1, (1, 5, 4, 2)), (2, (2, 1, 5, 4))]
_E14_PLUR = [(3, (1, 0, 0, 0)), (2, (0, 1, 0, 0)), (2, (0, 0, 1, 0))]

_E15_CANDS = ["A", "B", "C"]
_E15_STAR = [(2, (5, 1, 3)), (2, (3, 5, 1)), (3, (1, 3, 5))]
_E15_PLUR = [(2, (1, 0, 0)), (2, (0, 1, 0)), (3, (0, 0, 1))]

_E16_CANDS = ["A", "B", "C", "D"]
_E16_BLOCS = [(33, ["A", "B", "C", "D"]), (29, ["B", "A", "C", "D"]),
              (24, ["C", "B", "A", "D"]), (17, ["D", "C", "B", "A"])]
_E16_R, _E16_S = _mk_ranked_and_star(_E16_BLOCS, _E16_CANDS)
# Truncated variant: the 17 d>c>b>a voters list ONLY d (rank 0 = unranked;
# STAR: only d scored).
_E16T_R = ([r for r in _E16_R if r != [4, 3, 2, 1]] + [[0, 0, 0, 1]] * 17)
_E16T_S = ([s for s in _E16_S if s != [1, 2, 4, 5]] + [[0, 0, 0, 5]] * 17)

_F56_SRC = ("From Dan S. Felsenthal, 'Review of Paradoxes Afflicting Various "
            "Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be "
            "Elected' (University of Haifa / LSE, revised 26 May 2010; Leverhulme "
            "Trust 'Voting Power in Practice' workshop, Château du Baffy, "
            "Normandy). ")

# Already created -> r6qc8h/q3h4fk/4htk44/74j6vv (BV2160-63). Reference.
_CREATED_BV2160_63 = [
    {
        "test_id": "BV2160",
        "title": "Fishburn's Borda truncation electorate — STAR and Choose-One disagree; Borda's paradox is on paper",
        "description": (_F56_SRC +
                        "Appendix A5, Example 14, adapted from Fishburn (1974: 543): "
                        "the Truncation paradox under Borda's procedure. 7 voters, "
                        "four candidates — 3×(A>B>C>D), 1×(B>C>A>D), 1×(B>C>D>A), "
                        "2×(C>D>A>B). Under Borda (k points for a top rank … 0 for "
                        "unranked) the counts are A 19, B 19, C 20, D 12 — C is "
                        "elected. But if the three A>B>C>D voters TRUNCATE C from "
                        "their ballots, Borda gives A 16, B 16, C 14, D 12: revealing "
                        "less flips the win away from C, which those voters prefer — "
                        "the Truncation paradox. BetterVoting has no Borda tabulator, "
                        "so the Borda arithmetic lives in this election's case page; "
                        "the live races run the same electorate under STAR (ranks "
                        "mapped 5/4/2/1: A 22, B 24, C 24, D 14 — B and C take both "
                        "finalist seats and B wins the runoff 5-2) and Choose-One "
                        "Plurality (A wins with 3 of 7). The profile's pairwise "
                        "preferences are a CYCLE (A>B 5-2, B>C 5-2, C>A 4-3), so a "
                        "Ranked Robin race would tie 3-ways and resolve at random — "
                        "deliberately omitted, like the IRV race (its first "
                        "elimination is a random B/C tie)."),
        "races": [
            {"title": "Fishburn Ex.14 — STAR (ranks mapped to 0-5)", "method": "STAR",
             "num_winners": 1, "candidates": _E14_CANDS, "ballots": _expand(_E14_STAR)},
            {"title": "Fishburn Ex.14 — Choose-One (Plurality)", "method": "Plurality",
             "num_winners": 1, "candidates": _E14_CANDS, "ballots": _expand(_E14_PLUR)},
        ],
        "expected": "STAR -> B (22/24/24/14; B & C both advance, runoff 5-2). "
                    "Plurality -> A (3 of 7). Borda (paper): C 20; truncation -> "
                    "A/B 16-16 tie. Pairwise cycle. LH-verified. Test ID BV2160.",
    },
    {
        "test_id": "BV2161",
        "title": "Borda's SCC paradox electorate — the winner flips when a loser exits (STAR agrees on the pick)",
        "description": (_F56_SRC +
                        "Appendix A5, Example 15: SCC (the spoiler condition) under "
                        "Borda's procedure. 7 voters, three candidates — 2×(A>C>B), "
                        "2×(B>A>C), 3×(C>B>A). (The paper prints the third bloc as "
                        "C>A>B, but its own Borda totals 6/7/8 are only consistent "
                        "with C>B>A — this election uses the arithmetic-consistent "
                        "profile.) Borda points: A 6, B 7, C 8 — C is elected. Now "
                        "let B, a losing candidate, drop out: Borda on the remaining "
                        "pair gives A 4, C 3 — A wins. A loser's exit flipped the "
                        "winner: SCC violated (paper arithmetic; BetterVoting has no "
                        "Borda tabulator). The live races run the same electorate "
                        "under STAR (5/3/1 map: A 19, B 21, C 23; C beats B 5-2 in "
                        "the runoff) and Choose-One Plurality (C, 3 of 7) — both "
                        "agree with Borda's initial pick, C; the paradox is Borda's "
                        "instability, not the pick. The pairwise preferences are a "
                        "cycle (B>A 5-2, A>C 4-3, C>B 5-2), so Ranked Robin and IRV "
                        "races would hit random ties and are deliberately omitted."),
        "races": [
            {"title": "Borda SCC Ex.15 — STAR (ranks mapped to 0-5)", "method": "STAR",
             "num_winners": 1, "candidates": _E15_CANDS, "ballots": _expand(_E15_STAR)},
            {"title": "Borda SCC Ex.15 — Choose-One (Plurality)", "method": "Plurality",
             "num_winners": 1, "candidates": _E15_CANDS, "ballots": _expand(_E15_PLUR)},
        ],
        "expected": "STAR -> C (19/21/23; runoff 5-2). Plurality -> C. Borda "
                    "(paper): C 8; B exits -> A 4-3 (SCC). Pairwise cycle. "
                    "LH-verified. Test ID BV2161.",
    },
    {
        "test_id": "BV2162",
        "title": "Nurmi's truncation electorate (1 of 2) — everyone ranks fully; IRV misses the Condorcet winner",
        "description": (_F56_SRC +
                        "Appendix A6 ('the Alternative Vote' — Felsenthal's British "
                        "name for instant-runoff, RCV-IRV), Example 16, due to Nurmi "
                        "(1999: 63): the Truncation paradox under IRV, part 1 of 2. "
                        "103 voters, four candidates — 33×(A>B>C>D), 29×(B>A>C>D), "
                        "24×(C>B>A>D), 17×(D>C>B>A), all ranking every candidate. "
                        "B is the Condorcet winner (beats A 70-33, C 62-41, D 86-17). "
                        "IRV: nobody has a first-count majority, D (17) is eliminated "
                        "and transfers to C (41), then B (29) is eliminated — and A "
                        "wins 62. IRV elects A over the Condorcet winner B. STAR "
                        "(ranks mapped 5/4/2/1: A 346, B 407, C 312, D 171) elects B, "
                        "as does Ranked Robin. Part 2 (BV2163): the 17 D-first voters "
                        "truncate to just D — and do BETTER."),
        "races": [
            {"title": "Nurmi Ex.16 sincere — STAR (ranks mapped to 0-5)", "method": "STAR",
             "num_winners": 1, "candidates": _E16_CANDS, "ballots": _E16_S},
            {"title": "Nurmi Ex.16 sincere — IRV (Hare)", "method": "IRV",
             "num_winners": 1, "max_rankings": 4, "candidates": _E16_CANDS,
             "ballots": _E16_R},
            {"title": "Nurmi Ex.16 sincere — Ranked Robin (Copeland)",
             "method": "RankedRobin", "num_winners": 1, "max_rankings": 4,
             "candidates": _E16_CANDS, "ballots": _E16_R},
        ],
        "expected": "STAR -> B (346/407/312/171; runoff 70-33). IRV -> A (D out, "
                    "then B out, A 62). Ranked Robin -> B (Condorcet winner). "
                    "LH-verified. Test ID BV2162.",
    },
    {
        "test_id": "BV2163",
        "title": "Nurmi's truncation electorate (2 of 2) — 17 voters rank ONLY their favorite, and do better",
        "description": (_F56_SRC +
                        "Appendix A6, Example 16 (continued), due to Nurmi (1999: "
                        "63): the Truncation paradox under instant-runoff (RCV-IRV), "
                        "part 2 of 2. Identical to BV2162 except that, ceteris "
                        "paribus, the 17 voters whose ordering is D>C>B>A TRUNCATE "
                        "and list only their top preference, D. IRV: D is eliminated "
                        "first exactly as before, but the truncated ballots exhaust "
                        "instead of transferring to C — so C (24) is eliminated "
                        "instead of B, C's transfers flow to B, and B wins. The "
                        "truncators prefer B to A (their full ordering was D>C>B>A), "
                        "so ranking FEWER candidates got them a BETTER result than "
                        "ranking all — the Truncation paradox, live. (It also happens "
                        "to elect the Condorcet winner B that sincere IRV missed in "
                        "BV2162 — truncation as accidental repair.) STAR (B 373 with "
                        "the truncated ballots scoring only D) and Ranked Robin "
                        "still elect B — both unmoved by the truncation."),
        "races": [
            {"title": "Nurmi Ex.16 truncated — STAR (ranks mapped to 0-5)", "method": "STAR",
             "num_winners": 1, "candidates": _E16_CANDS, "ballots": _E16T_S},
            {"title": "Nurmi Ex.16 truncated — IRV (Hare)", "method": "IRV",
             "num_winners": 1, "max_rankings": 4, "candidates": _E16_CANDS,
             "ballots": _E16T_R},
            {"title": "Nurmi Ex.16 truncated — Ranked Robin (Copeland)",
             "method": "RankedRobin", "num_winners": 1, "max_rankings": 4,
             "candidates": _E16_CANDS, "ballots": _E16T_R},
        ],
        "expected": "STAR -> B (329/373/244/171). IRV -> B (D out, ballots exhaust, "
                    "C out, B wins) — the 17 truncators improve their outcome vs "
                    "BV2162. Ranked Robin -> B. LH-verified. Test ID BV2163.",
    },
]


# --- BV2164-66 — Felsenthal (2010) §A7: Coombs' procedure ------------------------
# SOURCE: same Felsenthal (2010) paper; Appendix A7 ("Demonstrating Paradoxes
# Afflicting Coombs' Procedure", Examples 17-22). Coombs (eliminate whoever is
# ranked LAST by the most voters, unless someone has a first-choice majority)
# has NO tabulator on BetterVoting or in the LH engine (pref_voting can
# cross-check), so — like Borda — the Coombs counts live as worked numbers in
# the case pages while these elections carry the same electorates under the
# supported DETERMINISTIC methods, STAR first (house rule). Per Adam: Ex.17 +
# the Ex.19 pair go live; Ex.18 (a Coombs-only monotonicity flip whose live
# races are unchanged), Ex.20 (reinforcement; NOTE a source typo — District II
# is announced as 6 voters but lists 1+6=7, and the amalgamated table sums to
# 41), Ex.21 (twin; the post-twin Coombs state is a RANDOM a/b tie — not
# freezable) and Ex.22 (SCC) are worked on the coombs teaching page.
#   BV2164 (Ex.17): 33 voters, four candidates — 11×(a>b>c>d), 12×(b>c>d>a),
#     2×(b>a>d>c), 4×(c>a>d>b), 4×(d>a>b>c). Arlo (=a) is the Condorcet
#     winner (beats Bree 19-14, Cole 17-16, Dana 17-16). Coombs (paper):
#     nobody has a first-count majority, and ARLO is ranked last by the most
#     voters (12) — the Condorcet winner is the first one deleted; Bree then
#     has a majority and wins. Live: STAR (5/4/2/1 map: 107/126/96/67 — Bree
#     tops the scores but Arlo wins the runoff 19-14) -> Arlo; Plurality ->
#     Bree (14 of 33); Ranked Robin -> Arlo. No IRV race: its first
#     elimination is a random Cole/Dana tie (4-4). Felsenthal also conjectures
#     4 candidates are MINIMAL for a Coombs Condorcet failure.
#   BV2165 (Ex.19 full, 15 voters): 4×(a>b>c), 4×(b>c>a), 5×(c>a>b),
#     2×(c>b>a). Cast Amy/Boone/Cass. Coombs (paper): Amy is ranked last by
#     the most voters (6) and is deleted; Boone then has a majority — Boone
#     wins. Live: STAR (5/3/1: 41/43/51; Boone beats Cass 8-7 in the runoff)
#     -> Boone; Plurality -> Cass (7 of 15). Pairwise is a cycle (Amy>Boone
#     9-6, Boone>Cass 8-7, Cass>Amy 11-4) -> no RR race; IRV's first
#     elimination is a random Amy/Boone tie -> no IRV race.
#   BV2166 (Ex.19 no-show, 13 voters): ceteris paribus the two c>b>a voters
#     stay home. Coombs (paper): now BOONE is ranked last by the most voters
#     (5) and is deleted; Cass — the abstainers' TOP preference — wins: the
#     No-Show paradox (and, with truncation instead of abstention, the
#     Truncation paradox). LIVE BONUS, shown honestly: STAR flips too —
#     39/37/41, and Cass beats Amy 9-4 in the runoff. The two c>b>a voters
#     get their FAVORITE by staying home where their sincere ballots (which
#     score Boone 3) had helped Boone reach and win the runoff: a genuine
#     STAR participation failure on this profile (STAR's runoff stage is
#     what costs it Moulin-style participation guarantees). Plurality -> Cass
#     in both electorates, unmoved.
# All seven live races LH-verified pre-creation.

_E17_CANDS = ["Arlo", "Bree", "Cole", "Dana"]
_E17_STAR = [(11, (5, 4, 2, 1)), (12, (1, 5, 4, 2)), (2, (4, 5, 1, 2)),
             (4, (4, 1, 5, 2)), (4, (4, 2, 1, 5))]
_E17_PLUR = [(11, (1, 0, 0, 0)), (14, (0, 1, 0, 0)), (4, (0, 0, 1, 0)), (4, (0, 0, 0, 1))]
_E17_RANKS = [(11, (1, 2, 3, 4)), (12, (4, 1, 2, 3)), (2, (2, 1, 4, 3)),
              (4, (2, 4, 1, 3)), (4, (2, 3, 4, 1))]

_E19_CANDS = ["Amy", "Boone", "Cass"]
_E19_STAR = [(4, (5, 3, 1)), (4, (1, 5, 3)), (5, (3, 1, 5)), (2, (1, 3, 5))]
_E19_PLUR = [(4, (1, 0, 0)), (4, (0, 1, 0)), (7, (0, 0, 1))]
_E19N_STAR = [(4, (5, 3, 1)), (4, (1, 5, 3)), (5, (3, 1, 5))]
_E19N_PLUR = [(4, (1, 0, 0)), (4, (0, 1, 0)), (5, (0, 0, 1))]

_F7_SRC = ("From Dan S. Felsenthal, 'Review of Paradoxes Afflicting Various "
           "Voting Procedures Where One Out of m Candidates (m ≥ 2) Must Be "
           "Elected' (University of Haifa / LSE, revised 26 May 2010; Leverhulme "
           "Trust 'Voting Power in Practice' workshop, Château du Baffy, "
           "Normandy), Appendix A7: the paradoxes afflicting Coombs' procedure "
           "(eliminate whoever is ranked LAST by the most voters). ")

# Already created -> xbqq8t/9vxcj7/b7b8dv (BV2164-66). Reference.
_CREATED_BV2164_66 = [
    {
        "test_id": "BV2164",
        "title": "Coombs deletes the Condorcet winner first — STAR and Ranked Robin elect him",
        "description": (_F7_SRC +
                        "Example 17. 33 voters, four candidates — 11×(Arlo>Bree>Cole>"
                        "Dana), 12×(Bree>Cole>Dana>Arlo), 2×(Bree>Arlo>Dana>Cole), "
                        "4×(Cole>Arlo>Dana>Bree), 4×(Dana>Arlo>Bree>Cole). Arlo is "
                        "the Condorcet winner (beats Bree 19-14, Cole 17-16, Dana "
                        "17-16; the social ordering is Arlo>Bree>Cole>Dana). Coombs' "
                        "procedure — worked on this election's case page, since "
                        "BetterVoting has no Coombs tabulator — deletes the candidate "
                        "ranked LAST by the most voters when nobody holds a first-"
                        "count majority: that candidate is ARLO himself (last on 12 "
                        "ballots), and Bree then wins with a majority. The Condorcet "
                        "winner is the first candidate Coombs eliminates (Felsenthal "
                        "conjectures four candidates are the minimum for this). The "
                        "live races: STAR (ranks mapped 5/4/2/1: Arlo 107, Bree 126, "
                        "Cole 96, Dana 67 — Bree tops the scores, but Arlo wins the "
                        "automatic runoff 19-14), Choose-One Plurality (Bree, 14 of "
                        "33), and Ranked Robin (Arlo, directly). No IRV race: its "
                        "first elimination is a random Cole/Dana 4-4 tie."),
        "races": [
            {"title": "Coombs Ex.17 — STAR (ranks mapped to 0-5)", "method": "STAR",
             "num_winners": 1, "candidates": _E17_CANDS, "ballots": _expand(_E17_STAR)},
            {"title": "Coombs Ex.17 — Choose-One (Plurality)", "method": "Plurality",
             "num_winners": 1, "candidates": _E17_CANDS, "ballots": _expand(_E17_PLUR)},
            {"title": "Coombs Ex.17 — Ranked Robin (Copeland)", "method": "RankedRobin",
             "num_winners": 1, "max_rankings": 4, "candidates": _E17_CANDS,
             "ballots": _expand(_E17_RANKS)},
        ],
        "expected": "STAR -> Arlo (107/126/96/67; runoff 19-14). Plurality -> Bree "
                    "(14). Ranked Robin -> Arlo (Condorcet winner). Coombs (paper) "
                    "-> Bree, deleting the Condorcet winner FIRST. LH-verified. "
                    "Test ID BV2164.",
    },
    {
        "test_id": "BV2165",
        "title": "Coombs' No-Show electorate (1 of 2) — everyone votes: STAR picks Boone, Choose-One picks Cass",
        "description": (_F7_SRC +
                        "Example 19, part 1 of 2: the electorate whose Coombs count "
                        "punishes participation. 15 voters, three candidates — "
                        "4×(Amy>Boone>Cass), 4×(Boone>Cass>Amy), 5×(Cass>Amy>Boone), "
                        "2×(Cass>Boone>Amy). Coombs (worked on the case page): "
                        "nobody has a first-count majority; AMY is ranked last by "
                        "the most voters (6) and is deleted, and Boone then holds a "
                        "majority — Boone wins. Part 2 (BV2166): the two "
                        "Cass>Boone>Amy voters stay home, and Coombs elects CASS — "
                        "their top preference: the No-Show paradox (the same flip "
                        "happens if they merely truncate to Cass-only: the "
                        "Truncation paradox). The live races here: STAR (5/3/1 map: "
                        "Amy 41, Boone 43, Cass 51; Boone beats Cass 8-7 in the "
                        "runoff) and Choose-One Plurality (Cass, 7 of 15). The "
                        "pairwise preferences are a cycle (Amy>Boone 9-6, Boone>Cass "
                        "8-7, Cass>Amy 11-4), so no Ranked Robin race; IRV's first "
                        "elimination is a random Amy/Boone tie, so no IRV race."),
        "races": [
            {"title": "Coombs Ex.19 full — STAR (ranks mapped to 0-5)", "method": "STAR",
             "num_winners": 1, "candidates": _E19_CANDS, "ballots": _expand(_E19_STAR)},
            {"title": "Coombs Ex.19 full — Choose-One (Plurality)", "method": "Plurality",
             "num_winners": 1, "candidates": _E19_CANDS, "ballots": _expand(_E19_PLUR)},
        ],
        "expected": "STAR -> Boone (41/43/51; runoff 8-7). Plurality -> Cass (7 of "
                    "15). Coombs (paper) -> Boone. LH-verified. Test ID BV2165.",
    },
    {
        "test_id": "BV2166",
        "title": "Coombs' No-Show electorate (2 of 2) — two voters stay home and their favorite wins (STAR flips too)",
        "description": (_F7_SRC +
                        "Example 19, part 2 of 2: ceteris paribus, the two "
                        "Cass>Boone>Amy voters do NOT participate — 13 voters: "
                        "4×(Amy>Boone>Cass), 4×(Boone>Cass>Amy), 5×(Cass>Amy>Boone). "
                        "Coombs (worked on the case page): now BOONE is ranked last "
                        "by the most voters (5) and is deleted — and Cass, the "
                        "abstainers' TOP preference, wins: the No-Show paradox under "
                        "Coombs (Felsenthal notes the same flip via truncation). "
                        "LIVE BONUS, shown honestly: STAR flips here too. With all "
                        "15 ballots STAR elects Boone (BV2165); on these 13 it "
                        "scores Amy 39, Boone 37, Cass 41 and CASS beats Amy 9-4 in "
                        "the runoff. The two absent voters' sincere ballots (which "
                        "score Boone 3) had helped Boone reach and win the runoff — "
                        "by staying home they get their favorite: a genuine STAR "
                        "participation failure on this profile. (STAR's runoff stage "
                        "is what costs it Moulin-style participation guarantees; "
                        "score-only methods cannot do this.) Choose-One Plurality "
                        "elects Cass in both electorates, unmoved."),
        "races": [
            {"title": "Coombs Ex.19 no-show — STAR (ranks mapped to 0-5)", "method": "STAR",
             "num_winners": 1, "candidates": _E19_CANDS, "ballots": _expand(_E19N_STAR)},
            {"title": "Coombs Ex.19 no-show — Choose-One (Plurality)", "method": "Plurality",
             "num_winners": 1, "candidates": _E19_CANDS, "ballots": _expand(_E19N_PLUR)},
        ],
        "expected": "STAR -> Cass (39/37/41; runoff 9-4) — the two abstainers do "
                    "BETTER than in BV2165 under STAR as well as Coombs. Plurality "
                    "-> Cass. LH-verified. Test ID BV2166.",
    },
]


# --- BV2167 — Felsenthal (2010) §A10 Example 29: Minimax elects the absolute loser
# SOURCE: same Felsenthal (2010) paper; Appendix A10 ("...the Condorcet (aka
# Minimax or Simpson-Kramer) Procedure"), Example 29. Minimax (elect whoever's
# WORST pairwise loss is smallest) has no tabulator on BV or in LH (LH's
# Ranked Robin is Copeland; pref_voting can cross-check), so the Minimax count
# lives on the case page. The election is spectacular on paper: 11 voters,
# four candidates — 2×(d>a>c>b), 3×(d>b>a>c), 3×(c>b>a>d), 1×(b>a>c>d),
# 2×(a>c>b>d). The a/b/c trio is a top cycle (b>a 7-4, a>c 8-3, c>b 7-4) and
# D LOSES EVERY MATCHUP 5-6 — d is the Condorcet loser AND the absolute loser
# (ranked last by 6 of 11, a majority). Yet Minimax elects D: d's worst loss
# margin (6) is smaller than a/b/c's (7, 7, 8). Live races: STAR (5/4/2/1
# map: 34/35/32/31; B beats A 7-4 in the runoff) -> B; Choose-One Plurality
# -> D (5 first choices of 11 — Choose-One AGREES with Minimax on the
# absolute loser). No RR race (the a/b/c Copeland tie -> BV random); no IRV
# race (after B's elimination the A/C transfer tie is random). LH-verified.

_E29_CANDS = ["A", "B", "C", "D"]
_E29_STAR = [(2, (4, 1, 2, 5)), (3, (2, 4, 1, 5)), (3, (2, 4, 5, 1)),
             (1, (4, 5, 2, 1)), (2, (5, 2, 4, 1))]
_E29_PLUR = [(5, (0, 0, 0, 1)), (3, (0, 0, 1, 0)), (1, (0, 1, 0, 0)), (2, (1, 0, 0, 0))]

# ---- BV2168 / BV2169 — FairVote Condorcet-article claim-check pair ---------
# FairVote's "Why the Condorcet Criterion Is Less Important Than It Seems"
# (Slatky, 2010) hypothetical: "a strong liberal who commands between 40% to
# 50% of the vote, a moderate with about 10% to 15%, and a strong conservative
# between 40% and 50%." BV2168 counts exactly that (45/12/43, poles rank the
# Moderate second): Moderate is the Condorcet winner (55-45 v Liberal, 57-43
# v Conservative); STAR -> Moderate (score round Liberal 237 / Moderate 236 /
# Conservative 227; runoff Moderate 55-45); IRV eliminates the Moderate round
# one (12 first choices) and elects Liberal 51-49 — center squeeze in the
# article's own numbers. Both races deterministic (no ties -> freezable).
# BV2169 = same cast, electorate shifted left (56/12/32): the strong LIBERAL
# pole is the Condorcet winner (56-44, 62-38) — refuting "centrist by nature,
# regardless of the preferences of the electorate"; STAR and IRV both ->
# Liberal (IRV: first-choice majority, round one). LH-verified:
# method_comparisons/fairvote_condorcet_claims/ + the claim-check page
# 00_start_here/topics/condorcet/fairvote_condorcet_claim_check.md.

_FV_CANDS = ["Liberal", "Moderate", "Conservative"]
_FV1_STAR = [(45, (5, 2, 0)), (43, (0, 2, 5)), (6, (2, 5, 0)), (6, (0, 5, 2))]
_FV1_IRV = [(45, (1, 2, 3)), (43, (3, 2, 1)), (6, (2, 1, 3)), (6, (3, 1, 2))]
_FV2_STAR = [(56, (5, 2, 0)), (32, (0, 2, 5)), (6, (2, 5, 0)), (6, (0, 5, 2))]
_FV2_IRV = [(56, (1, 2, 3)), (32, (3, 2, 1)), (6, (2, 1, 3)), (6, (3, 1, 2))]

# Already created -> 6w2gq7 (BV2168) / 2jrfpg (BV2169). Reference only — do NOT
# re-run (BV elections are permanent and cannot be deleted; re-running would make
# undeletable duplicates). Only the `ELECTIONS` list at the bottom is executed.
_CREATED_BV2168_69 = [
    {
        "test_id": "BV2168",
        "title": "FairVote's Condorcet hypothetical, counted — the Moderate is the majority's head-to-head choice",
        "description": ("FairVote's article 'Why the Condorcet Criterion Is Less "
                        "Important Than It Seems' (Alec Slatky, 2010) argues from "
                        "a hypothetical: 'a strong liberal who commands between "
                        "40% to 50% of the vote, a moderate with about 10% to "
                        "15%, and a strong conservative between 40% and 50%.' "
                        "This election counts exactly that electorate: 100 "
                        "voters — Liberal 45 first choices, Moderate 12, "
                        "Conservative 43, with each pole ranking the Moderate "
                        "second. The Moderate is the Condorcet winner by real "
                        "majorities (55-45 over Liberal, 57-43 over "
                        "Conservative) — it is majorities, not the 12%, who "
                        "choose the Moderate against either rival. STAR elects "
                        "the Moderate (score round: Liberal 237, Moderate 236, "
                        "Conservative 227; automatic runoff: Moderate 55-45). "
                        "The IRV race on the same voters eliminates the "
                        "Moderate in round one (fewest first choices) and "
                        "elects the Liberal 51-49 — the classic center squeeze, "
                        "in the article's own numbers. Companion election: "
                        "'electorate shifted left' (same candidates, the strong "
                        "Liberal becomes the Condorcet winner)."),
        "races": [
            {"title": "FairVote 45/12/43 — STAR", "method": "STAR",
             "num_winners": 1, "candidates": _FV_CANDS, "ballots": _expand(_FV1_STAR)},
            {"title": "FairVote 45/12/43 — RCV-IRV", "method": "IRV",
             "num_winners": 1, "max_rankings": len(_FV_CANDS),
             "candidates": _FV_CANDS, "ballots": _expand(_FV1_IRV)},
        ],
        "expected": "STAR -> Moderate (237/236/227; runoff 55-45). IRV -> "
                    "Liberal (Moderate eliminated round one 45/43/12; final "
                    "51-49). Condorcet winner = Moderate. Deterministic, no "
                    "ties. LH-verified. Test ID BV2168.",
    },
    {
        "test_id": "BV2169",
        "title": "FairVote's hypothetical, electorate shifted left — the strong Liberal is the Condorcet winner",
        "description": ("The companion to the 'FairVote's Condorcet "
                        "hypothetical, counted' election, refuting the "
                        "article's claim that 'Condorcet winners are centrist "
                        "by nature, regardless of the preferences of the "
                        "electorate' (and that the criterion is 'equivalent to "
                        "saying that moderate candidates should always win'). "
                        "Same three candidates, but the electorate has moved "
                        "left: 100 voters — Liberal 56 first choices, Moderate "
                        "12, Conservative 32. Now the strong LIBERAL — a pole "
                        "candidate, not the moderate — is the Condorcet winner "
                        "(56-44 over Moderate, 62-38 over Conservative): a "
                        "candidate ranked first by an outright majority is "
                        "automatically the Condorcet winner, so the criterion "
                        "follows the electorate rather than pinning the "
                        "center. STAR elects Liberal (scores 292/236/172; "
                        "runoff 56-44) and the IRV race agrees (first-choice "
                        "majority, round one)."),
        "races": [
            {"title": "Shifted-left 56/12/32 — STAR", "method": "STAR",
             "num_winners": 1, "candidates": _FV_CANDS, "ballots": _expand(_FV2_STAR)},
            {"title": "Shifted-left 56/12/32 — RCV-IRV", "method": "IRV",
             "num_winners": 1, "max_rankings": len(_FV_CANDS),
             "candidates": _FV_CANDS, "ballots": _expand(_FV2_IRV)},
        ],
        "expected": "STAR -> Liberal (292/236/172; runoff 56-44). IRV -> "
                    "Liberal (56 first-choice majority, round one). Condorcet "
                    "winner = Liberal. Deterministic, no ties. LH-verified. "
                    "Test ID BV2169.",
    },
]


# ---- BV2170 — the symmetric 47/47/3/3 Condorcet centrist (classroom profile) ----
# The textbook two-poles-plus-a-centrist profile (100 voters, 3 candidates):
#   47 × Avery > Casey > Blake   (left pole ranks the centrist second)
#   47 × Blake > Casey > Avery   (right pole ranks the centrist second)
#    3 × Casey > Avery > Blake   (centrist, leans left)
#    3 × Casey > Blake > Avery   (centrist, leans right)
# Casey is the CONDORCET winner — beats Avery 53-47 and Blake 53-47 head-to-head —
# yet has only 6 first choices. STAR (5/3/1 map: Casey 312 vs Avery/Blake 294) and
# Ranked Robin (Copeland 2-0) elect Casey. IRV eliminates Casey first (6) and the
# two poles DEADLOCK 50-50; Choose-One deadlocks 47-47. The electorate is PERFECTLY
# SYMMETRIC between the two poles, so IRV and Plurality produce an exact Avery/Blake
# tie that BetterVoting breaks at RANDOM (not freezable — like the BV2141/2142
# random-tie probes); the deadlock of the poles once the compromise is squeezed out
# is itself the lesson. STAR is the LEAD race (per request). All four LH-verified.
# Cast: Avery = left pole (A), Blake = right pole (B), Casey = centrist (C) —
# initials aligned to the ballot columns.
_CS_CANDS = ["Avery", "Blake", "Casey"]
_CS_STAR = [(47, (5, 1, 3)), (47, (1, 5, 3)), (3, (3, 1, 5)), (3, (1, 3, 5))]
_CS_RANK = [(47, (1, 3, 2)), (47, (3, 1, 2)), (3, (2, 3, 1)), (3, (3, 2, 1))]
_CS_PLUR = [(47, (1, 0, 0)), (47, (0, 1, 0)), (3, (0, 0, 1)), (3, (0, 0, 1))]

# Already created -> pp2q4q (BV2170). Reference only — do NOT re-run (permanent).
# Superseded for method coverage by BV2172 (same 47/47/3/3 profile, all SEVEN BV
# methods); BV2170 was the original four-method cut. Kept live and cross-linked.
_CREATED_BV2170 = [
    {
        "test_id": "BV2170",
        "title": "The centrist a majority prefers, squeezed out — a symmetric Condorcet electorate, four ways",
        "description": ("The textbook 'two poles and a compromise' electorate: 100 "
                        "voters, three candidates — Avery on the left, Blake on the "
                        "right, and Casey the broadly-liked centrist. 47 voters rank "
                        "Avery > Casey > Blake, 47 rank Blake > Casey > Avery, and 6 "
                        "put Casey first (3 leaning to Avery, 3 to Blake). Casey is "
                        "the Condorcet winner — a majority prefers Casey to Avery "
                        "(53-47) and to Blake (53-47) head-to-head — yet Casey holds "
                        "only 6 first-choice votes. This one electorate is counted "
                        "four ways. STAR elects Casey (score round Casey 312, Avery "
                        "294, Blake 294; the automatic runoff confirms Casey 53-47). "
                        "Ranked Robin (Copeland) elects Casey outright — Casey beats "
                        "everyone head-to-head. But Instant-Runoff eliminates Casey "
                        "in the first round (fewest first choices) and the two poles "
                        "then deadlock 50-50; Choose-One Plurality deadlocks 47-47. "
                        "Because the electorate is perfectly symmetric between the "
                        "two poles, IRV and Choose-One end in an exact Avery-Blake "
                        "tie, which BetterVoting resolves at random — the deadlock of "
                        "the poles, once the candidate a majority actually prefers is "
                        "squeezed out, is the whole point."),
        "races": [
            {"title": "Symmetric centrist — STAR", "method": "STAR",
             "num_winners": 1, "candidates": _CS_CANDS, "ballots": _expand(_CS_STAR)},
            {"title": "Symmetric centrist — RCV-IRV", "method": "IRV",
             "num_winners": 1, "max_rankings": len(_CS_CANDS),
             "candidates": _CS_CANDS, "ballots": _expand(_CS_RANK)},
            {"title": "Symmetric centrist — Ranked Robin (Copeland)", "method": "RankedRobin",
             "num_winners": 1, "max_rankings": len(_CS_CANDS),
             "candidates": _CS_CANDS, "ballots": _expand(_CS_RANK)},
            {"title": "Symmetric centrist — Choose-One (Plurality)", "method": "Plurality",
             "num_winners": 1, "candidates": _CS_CANDS, "ballots": _expand(_CS_PLUR)},
        ],
        "expected": "STAR -> Casey (312/294/294; runoff 53-47). Ranked Robin -> Casey "
                    "(Condorcet winner, 2-0). IRV -> Avery/Blake TIE 50-50 (Casey "
                    "eliminated round one, 6). Plurality -> Avery/Blake TIE 47-47. "
                    "IRV & Plurality ties resolve at RANDOM on BV (not freezable). "
                    "Condorcet winner = Casey. LH-verified. Test ID BV2170.",
    },
]


# ---- BV2171 / BV2172 — the symmetric Condorcet centrist, minimal vs full, ALL 7 ----
# The same two-poles-plus-a-centrist symptom (Casey the Condorcet winner, fewest
# first choices) run through EVERY BetterVoting method, at two sizes:
#   BV2171 = the MINIMAL form, 8 voters (3/3/1/1) — the fewest ballots that still
#            reproduce the whole symptom (Casey Condorcet + strictly fewest first
#            choices + the exact Avery/Blake pole tie under IRV/STV/Plurality).
#   BV2172 = the FULL form, 100 voters (47/47/3/3) — the profile as drawn in the
#            "Should we always elect the Condorcet winner?" video (youtu.be/
#            NlisR8vbpN4?t=53). Same shape, 12.5x the ballots.
# Seven races each (STAR leads): STAR, STAR-PR (1 seat = STAR), Approval (approve
# top two), Ranked Robin, RCV-IRV, STV (1 seat = IRV), Choose-One. The three
# whole-ballot methods (STAR/STAR-PR/Approval), plus Ranked Robin (Condorcet),
# elect Casey; the three first-choice methods (IRV/STV/Plurality) squeeze Casey
# out and, by symmetry, deadlock the two poles in an exact tie (random on BV, not
# freezable). Approval uses an approve-top-two model (everyone's top two include
# Casey, so Casey sweeps approval). Cast: Avery = left pole, Blake = right pole,
# Casey = centrist — same as BV2170. All LH-verified (STAR-PR at 1 seat ≡ STAR in
# LH, which elects Casey).
_SQ_CANDS = ["Avery", "Blake", "Casey"]


def _sq_races(prefix, P, Q):
    """The seven BV tabulations of the symmetric centrist profile: P voters each
    pole (A>C>B / B>C>A), Q voters each centrist lean (C>A>B / C>B>A)."""
    star = [(P, (5, 1, 3)), (P, (1, 5, 3)), (Q, (3, 1, 5)), (Q, (1, 3, 5))]
    appr = [(P, (1, 0, 1)), (P, (0, 1, 1)), (Q, (1, 0, 1)), (Q, (0, 1, 1))]  # top two
    rank = [(P, (1, 3, 2)), (P, (3, 1, 2)), (Q, (2, 3, 1)), (Q, (3, 2, 1))]
    plur = [(P, (1, 0, 0)), (P, (0, 1, 0)), (Q, (0, 0, 1)), (Q, (0, 0, 1))]
    N = len(_SQ_CANDS)
    return [
        {"title": f"{prefix} — STAR", "method": "STAR",
         "num_winners": 1, "candidates": _SQ_CANDS, "ballots": _expand(star)},
        {"title": f"{prefix} — STAR-PR (1 seat)", "method": "STAR_PR",
         "num_winners": 1, "candidates": _SQ_CANDS, "ballots": _expand(star)},
        {"title": f"{prefix} — Approval (approve top two)", "method": "Approval",
         "num_winners": 1, "candidates": _SQ_CANDS, "ballots": _expand(appr)},
        {"title": f"{prefix} — Ranked Robin (Copeland)", "method": "RankedRobin",
         "num_winners": 1, "max_rankings": N, "candidates": _SQ_CANDS, "ballots": _expand(rank)},
        {"title": f"{prefix} — RCV-IRV", "method": "IRV",
         "num_winners": 1, "max_rankings": N, "candidates": _SQ_CANDS, "ballots": _expand(rank)},
        {"title": f"{prefix} — STV (1 seat)", "method": "STV",
         "num_winners": 1, "max_rankings": N, "candidates": _SQ_CANDS, "ballots": _expand(rank)},
        {"title": f"{prefix} — Choose-One (Plurality)", "method": "Plurality",
         "num_winners": 1, "candidates": _SQ_CANDS, "ballots": _expand(plur)},
    ]


_SQ_EXPECTED = ("STAR / STAR-PR / Approval (top two) / Ranked Robin -> Casey (the "
                "Condorcet winner, beats each pole {m}). RCV-IRV / STV / Choose-One "
                "-> exact Avery/Blake pole tie (Casey has the fewest first choices "
                "and is eliminated first), resolved at RANDOM on BV — not freezable. "
                "LH-verified (STAR-PR 1 seat = STAR in LH). ")

_CREATED_BV2171_72 = [
    {
        "test_id": "BV2171",
        "title": "The Condorcet centrist, minimal form (8 voters) — squeezed out by first-choice methods, elected by the rest",
        "description": ("The smallest electorate that still reproduces the whole "
                        "center-squeeze symptom: 8 voters, three candidates — Avery "
                        "(left pole), Blake (right pole), Casey (centrist). 3 rank "
                        "Avery > Casey > Blake, 3 rank Blake > Casey > Avery, 1 ranks "
                        "Casey > Avery > Blake, 1 ranks Casey > Blake > Avery. Casey "
                        "is the Condorcet winner — beats Avery 5-3 and Blake 5-3 "
                        "head-to-head — but has only 2 first-choice votes, the fewest. "
                        "The same 8 voters are counted seven ways, every method "
                        "BetterVoting supports. The whole-ballot methods — STAR, "
                        "STAR-PR, Approval (approve your top two), and Ranked Robin "
                        "(the Condorcet method) — elect Casey. The first-choice "
                        "methods — RCV-IRV, STV, and Choose-One Plurality — eliminate "
                        "Casey first and, because the electorate is perfectly "
                        "symmetric between the two poles, deadlock Avery and Blake in "
                        "an exact tie. This is the minimal companion to the full "
                        "100-voter version (BV2172), the profile from the 'Should we "
                        "always elect the Condorcet winner?' explainer."),
        "races": _sq_races("Condorcet centrist (minimal)", 3, 1),
        "expected": _SQ_EXPECTED.format(m="5-3") + "8 voters (3/3/1/1). Test ID BV2171.",
    },
    {
        "test_id": "BV2172",
        "title": "The Condorcet centrist, full form (100 voters) — squeezed out by first-choice methods, elected by the rest",
        "description": ("The profile as drawn in the 'Should we always elect the "
                        "Condorcet winner?' explainer (youtu.be/NlisR8vbpN4): 100 "
                        "voters, three candidates — Avery (left pole), Blake (right "
                        "pole), Casey (centrist). 47 rank Avery > Casey > Blake, 47 "
                        "rank Blake > Casey > Avery, 3 rank Casey > Avery > Blake, 3 "
                        "rank Casey > Blake > Avery. Casey is the Condorcet winner — "
                        "beats Avery 53-47 and Blake 53-47 head-to-head — yet holds "
                        "only 6 first-choice votes. The same 100 voters are counted "
                        "seven ways, every method BetterVoting supports. The "
                        "whole-ballot methods — STAR, STAR-PR, Approval (approve your "
                        "top two), and Ranked Robin (the Condorcet method) — elect "
                        "Casey. The first-choice methods — RCV-IRV, STV, and "
                        "Choose-One Plurality — eliminate Casey first and, because the "
                        "electorate is perfectly symmetric between the two poles, "
                        "deadlock Avery and Blake in an exact tie. The minimal "
                        "companion (BV2171) shows the identical symptom in just 8 "
                        "voters. (Earlier four-method cut of this profile: BV2170.)"),
        "races": _sq_races("Condorcet centrist (full)", 47, 3),
        "expected": _SQ_EXPECTED.format(m="53-47") + "100 voters (47/47/3/3). Test ID BV2172.",
    },
]

_CREATED_BV2167 = [
    {
        "test_id": "BV2167",
        "title": "Minimax elects the absolute loser — the candidate who loses every matchup has the smallest worst loss",
        "description": ("From Dan S. Felsenthal, 'Review of Paradoxes Afflicting "
                        "Various Voting Procedures Where One Out of m Candidates "
                        "(m ≥ 2) Must Be Elected' (University of Haifa / LSE, revised "
                        "26 May 2010; Leverhulme Trust 'Voting Power in Practice' "
                        "workshop, Château du Baffy, Normandy), Appendix A10: the "
                        "Condorcet (aka Minimax or Simpson-Kramer) procedure — elect "
                        "whoever's WORST pairwise loss is smallest — Example 29. "
                        "11 voters, four candidates: 2×(D>A>C>B), 3×(D>B>A>C), "
                        "3×(C>B>A>D), 1×(B>A>C>D), 2×(A>C>B>D). A, B and C form a "
                        "top cycle (B beats A 7-4, A beats C 8-3, C beats B 7-4) and "
                        "D loses every single matchup 5-6 — D is the Condorcet loser "
                        "AND the absolute loser (a majority, 6 of 11, rank D dead "
                        "last). Yet Minimax elects D, because D's worst loss margin "
                        "(6) is smaller than A's, B's or C's (7, 7, 8): losing to "
                        "everyone NARROWLY beats beating some and losing one badly. "
                        "BetterVoting has no Minimax tabulator, so that count lives "
                        "on this election's case page. The live races: STAR (ranks "
                        "mapped 5/4/2/1: A 34, B 35, C 32, D 31; B beats A 7-4 in "
                        "the automatic runoff) elects B — a top-cycle member, not "
                        "the universal loser — and Choose-One Plurality elects D (5 "
                        "first choices), AGREEING with Minimax on the absolute "
                        "loser. No Ranked Robin race (the A/B/C Copeland tie would "
                        "resolve at random) and no IRV race (a random transfer tie), "
                        "per the freezability rule."),
        "races": [
            {"title": "Minimax Ex.29 — STAR (ranks mapped to 0-5)", "method": "STAR",
             "num_winners": 1, "candidates": _E29_CANDS, "ballots": _expand(_E29_STAR)},
            {"title": "Minimax Ex.29 — Choose-One (Plurality)", "method": "Plurality",
             "num_winners": 1, "candidates": _E29_CANDS, "ballots": _expand(_E29_PLUR)},
        ],
        "expected": "STAR -> B (34/35/32/31; runoff B beats A 7-4). Plurality -> D "
                    "(5 of 11) — agreeing with Minimax's paper pick of the absolute "
                    "loser. Minimax (paper) -> D (worst loss 6 vs 7/7/8). "
                    "LH-verified. Test ID BV2167.",
    },
]

# ---- BV2173 — Edelman's "Myth of the Condorcet Winner" 81-voter profile ----
# SOURCE: Paul H. Edelman, "The Myth of the Condorcet Winner," 22 Supreme
# Court Economic Review 207 (2015), Section III — the Saari / Balinski-Laraki
# "cancellation" profile (per Edelman's fn.24, the example goes back to
# CONDORCET HIMSELF, who used it against Borda): 30 A>B>C, 1 A>C>B, 29 B>A>C,
# 10 B>C>A, 10 C>A>B, 1 C>B>A (81 voters; here A/B/C = Ada/Ben/Cara).
# Ada is the Condorcet winner (41-40 v Ben, 60-21 v Cara). Edelman removes two
# "Condorcet components" (10+10+10 and 1+1+1 — cyclic blocs that pairwise-tie)
# and the remaining 48 voters say Ben 28-20, so he argues Ben is the rightful
# winner; Borda agrees (Ben 109, Ada 101, Cara 33). The live races: STAR ->
# Ada (score round Ben 257 / Ada 233 / Cara 77 — the cancellation-respecting
# count — then runoff Ada 41-40, the majoritarian step); Ranked Robin -> Ada
# (2-0-0); RCV-IRV -> Ada (Cara out 31/39/11... first prefs Ada 31, Ben 39,
# Cara 11 -> Cara eliminated, final Ada 41-40); Choose-One -> Ben (39/31/11,
# agreeing with Borda). All four races deterministic (no ties) -> freezable.
# LH-verified (matrix 41-40 / 60-21 / 69-12).

_EDL_CANDS = ["Ada", "Ben", "Cara"]
_EDL_STAR = [(30, (5, 2, 0)), (1, (5, 0, 2)), (29, (2, 5, 0)),
             (10, (0, 5, 2)), (10, (2, 0, 5)), (1, (0, 2, 5))]
_EDL_RANK = [(30, (1, 2, 3)), (1, (1, 3, 2)), (29, (2, 1, 3)),
             (10, (3, 1, 2)), (10, (2, 3, 1)), (1, (3, 2, 1))]
_EDL_PLUR = [(31, (1, 0, 0)), (39, (0, 1, 0)), (11, (0, 0, 1))]

_CREATED_BV2173 = [
    {
        "test_id": "BV2173",
        "title": "Edelman's 'Myth of the Condorcet Winner' 81 voters — the score count says Ben, the majorities say Ada",
        "description": ("From Paul H. Edelman, 'The Myth of the Condorcet "
                        "Winner,' 22 Supreme Court Economic Review 207 (2015), "
                        "Section III — a 'cancellation' profile that per "
                        "Edelman's own footnote goes back to Condorcet himself "
                        "(who aimed it at Borda), later used by Saari and "
                        "Balinski & Laraki against the Condorcet criterion. "
                        "81 voters: 30 Ada>Ben>Cara, 1 Ada>Cara>Ben, 29 "
                        "Ben>Ada>Cara, 10 Ben>Cara>Ada, 10 Cara>Ada>Ben, 1 "
                        "Cara>Ben>Ada. Ada is the Condorcet winner — 41-40 "
                        "over Ben, 60-21 over Cara. Edelman's argument: two "
                        "cyclic voter blocs (10+10+10 and 1+1+1) are "
                        "'Condorcet components' that pairwise-tie and should "
                        "cancel out; the remaining 48 voters prefer Ben 28-20, "
                        "and Borda agrees (Ben 109, Ada 101, Cara 33). So who "
                        "is right? The races show the split live: Ranked "
                        "Robin and RCV-IRV elect Ada; Choose-One Plurality "
                        "elects Ben (39/31/11); and STAR shows BOTH counts in "
                        "one method — the scoring round (which respects the "
                        "cancellation, like Borda) puts Ben first 257-233, "
                        "then the automatic runoff (the majoritarian step) "
                        "elects Ada 41-40. A 240-year-old argument — "
                        "Condorcet vs Borda — in one election."),
        "races": [
            {"title": "Edelman 81 — STAR (ranks mapped 5/2/0)", "method": "STAR",
             "num_winners": 1, "candidates": _EDL_CANDS, "ballots": _expand(_EDL_STAR)},
            {"title": "Edelman 81 — Ranked Robin", "method": "RankedRobin",
             "num_winners": 1, "max_rankings": len(_EDL_CANDS),
             "candidates": _EDL_CANDS, "ballots": _expand(_EDL_RANK)},
            {"title": "Edelman 81 — RCV-IRV", "method": "IRV",
             "num_winners": 1, "max_rankings": len(_EDL_CANDS),
             "candidates": _EDL_CANDS, "ballots": _expand(_EDL_RANK)},
            {"title": "Edelman 81 — Choose-One (Plurality)", "method": "Plurality",
             "num_winners": 1, "candidates": _EDL_CANDS, "ballots": _expand(_EDL_PLUR)},
        ],
        "expected": "STAR -> Ada (score: Ben 257, Ada 233, Cara 77; runoff Ada "
                    "41-40). RankedRobin -> Ada (2-0-0). IRV -> Ada (Cara "
                    "eliminated 31/39/11; final 41-40). Plurality -> Ben "
                    "(39/31/11). Borda (paper) -> Ben (109/101/33). Condorcet "
                    "winner = Ada. Deterministic, no ties. LH-verified. "
                    "Test ID BV2173.",
    },
]


# ---- BV2174 / BV2175 — the Participation criterion (no-show paradox), live --
# OUR OWN minimal multi-method pair (Participation topic hub). One electorate,
# told twice: BV2174 = 54 voters (8 April fans stay home); BV2175 = the same
# election with those 8 voting sincerely April>Bruno>Celia (62 voters). Effect
# of showing up, per method: Choose-One Celia -> April (helped: last choice ->
# favorite); STAR Bruno -> April (helped: favorite wins; BV2174's STAR count is
# also a Runoff Reversal — Celia tops the scores 136/122/120, Bruno wins the
# runoff 34-20); RCV-IRV Bruno -> Celia (HURT: their 2nd choice replaced by
# their LAST — the no-show paradox; April eliminated first at 16 before, Bruno
# eliminated at 18 after, final Celia 38-24). Both electorates are a Condorcet
# cycle (April > Bruno > Celia > April) — that's WHY the paradox exists — so
# NO RankedRobin race (BV's Copeland tie -> head-to-head -> RANDOM, not
# freezable; LH's margin-based RR resolves deterministically: Celia before,
# April after — told on the case page). LH-verified.

_NS_CANDS = ["April", "Bruno", "Celia"]
_NS1_STAR = [(16, (5, 2, 0)), (18, (0, 5, 2)), (20, (2, 0, 5))]
_NS1_RANK = [(16, (1, 2, 3)), (18, (3, 1, 2)), (20, (2, 3, 1))]
_NS1_PLUR = [(16, (1, 0, 0)), (18, (0, 1, 0)), (20, (0, 0, 1))]
_NS2_STAR = [(24, (5, 2, 0)), (18, (0, 5, 2)), (20, (2, 0, 5))]
_NS2_RANK = [(24, (1, 2, 3)), (18, (3, 1, 2)), (20, (2, 3, 1))]
_NS2_PLUR = [(24, (1, 0, 0)), (18, (0, 1, 0)), (20, (0, 0, 1))]

# Already created -> yyhr66 (BV2174) / 9dhv8y (BV2175). Reference only — do NOT re-run.
_CREATED_BV2174_75 = [
    {
        "test_id": "BV2174",
        "title": "No-show paradox electorate (1 of 2) — 8 April fans stay home",
        "description": ("The Participation criterion, live — election 1 of 2. "
                        "54 voters, three candidates: 16 April > Bruno > Celia, "
                        "18 Bruno > Celia > April, 20 Celia > April > Bruno. "
                        "Eight more April fans (same sincere ranking "
                        "April > Bruno > Celia) exist but STAY HOME here; the "
                        "companion election 2 of 2 adds them. With them absent: "
                        "RCV-IRV eliminates April (16 first choices) and elects "
                        "Bruno 34-20; STAR scores Celia 136, Bruno 122, April "
                        "120, and Bruno wins the automatic runoff 34-20 (a "
                        "Runoff Reversal — the score leader loses the majority "
                        "check); Choose-One elects Celia (20/18/16). The "
                        "pairwise picture is a perfect Condorcet cycle (April "
                        "beats Bruno 36-18, Bruno beats Celia 34-20, Celia "
                        "beats April 38-16) — which is exactly the soil the "
                        "no-show paradox grows in. No Ranked Robin race: with "
                        "a Copeland three-way tie BetterVoting resolves at "
                        "random (not freezable); the LH engine's margin "
                        "tiebreak resolves it deterministically to Celia."),
        "races": [
            {"title": "No-show 1of2 — STAR", "method": "STAR",
             "num_winners": 1, "candidates": _NS_CANDS, "ballots": _expand(_NS1_STAR)},
            {"title": "No-show 1of2 — RCV-IRV", "method": "IRV",
             "num_winners": 1, "max_rankings": len(_NS_CANDS),
             "candidates": _NS_CANDS, "ballots": _expand(_NS1_RANK)},
            {"title": "No-show 1of2 — Choose-One (Plurality)", "method": "Plurality",
             "num_winners": 1, "candidates": _NS_CANDS, "ballots": _expand(_NS1_PLUR)},
        ],
        "expected": "STAR -> Bruno (Celia 136 / Bruno 122 / April 120; runoff "
                    "Bruno 34-20 — Runoff Reversal). IRV -> Bruno (April out "
                    "at 16; final 34-20). Plurality -> Celia (20/18/16). "
                    "Condorcet cycle, no CW. Deterministic, no ties. "
                    "LH-verified. Test ID BV2174.",
    },
    {
        "test_id": "BV2175",
        "title": "No-show paradox electorate (2 of 2) — the 8 April fans vote, and RCV-IRV hands them their last choice",
        "description": ("The Participation criterion, live — election 2 of 2. "
                        "Identical to election 1 of 2 plus the 8 April fans "
                        "casting their sincere ballots April > Bruno > Celia: "
                        "62 voters — 24 April > Bruno > Celia, 18 Bruno > "
                        "Celia > April, 20 Celia > April > Bruno. What their "
                        "showing up buys, by method: Choose-One flips Celia -> "
                        "April (their favorite — helped); STAR flips Bruno -> "
                        "April (scores April 160, Bruno 138, Celia 136; runoff "
                        "April 44-18 — their favorite, helped); RCV-IRV flips "
                        "Bruno -> CELIA (Bruno now eliminated at 18; Celia "
                        "beats April 38-24): the 8 sincere ballots replaced "
                        "the voters' SECOND choice with their LAST choice — "
                        "the no-show paradox. Voting for their favorite, "
                        "honestly, made their outcome worse; had they stayed "
                        "home (election 1 of 2) they would keep Bruno. Same "
                        "Condorcet cycle as the companion (April beats Bruno "
                        "44-18, Bruno beats Celia 42-20, Celia beats April "
                        "38-24); no Ranked Robin race for the same "
                        "freezability reason (LH's margin tiebreak: April)."),
        "races": [
            {"title": "No-show 2of2 — STAR", "method": "STAR",
             "num_winners": 1, "candidates": _NS_CANDS, "ballots": _expand(_NS2_STAR)},
            {"title": "No-show 2of2 — RCV-IRV", "method": "IRV",
             "num_winners": 1, "max_rankings": len(_NS_CANDS),
             "candidates": _NS_CANDS, "ballots": _expand(_NS2_RANK)},
            {"title": "No-show 2of2 — Choose-One (Plurality)", "method": "Plurality",
             "num_winners": 1, "candidates": _NS_CANDS, "ballots": _expand(_NS2_PLUR)},
        ],
        "expected": "STAR -> April (160/138/136; runoff April 44-18). IRV -> "
                    "Celia (Bruno out at 18; final Celia 38-24) — participation "
                    "HURT the 8 added voters (Bruno was their 2nd, Celia their "
                    "last). Plurality -> April (24/20/18). Condorcet cycle, no "
                    "CW. Deterministic, no ties. LH-verified. Test ID BV2175.",
    },
]

# ---- BV2176 — the "How does RCV work? With Post-its!" video, 20 voters -------
# Equal Vote's Post-it demo (https://youtu.be/Vte4nly_Neg): 20 voters, four
# candidates (Purple, Green, Blue, Pink), told three ways on ONE electorate.
# RCV-IRV (the video's walk-through): R1 7/6/4/3 -> Pink out; R2 8/7/4
# (1 exhausted) -> Blue out; final Purple 9 - Green 8 (3 exhausted) -> PURPLE,
# with 9 of the 17 still-active ballots. The video's hypothetical — eliminate
# Green instead of Blue in round 2 — hands BLUE the win 10-9, and indeed Blue
# beats Purple head-to-head 10-9. STAR (the video's own 0-5 scores): Purple 46,
# Blue 44, Pink 44, Green 38 — the 44-44 scoring tie for second breaks
# head-to-head (Blue beats Pink 10-3), and Blue wins the automatic runoff 10-9
# (1 Equal Support) — a Runoff Reversal (score leader Purple loses the
# majority check). Ranked Robin: a genuine Condorcet cycle (Purple > Green >
# Blue > Purple; Pink beats Purple 12-8) leaves Green and Blue tied on record
# 2-1. The tie is FREEZABLE on BV: exactly 2 tied -> BV's ladder goes to their
# head-to-head, Green beats Blue 7-4 -> GREEN, deterministic. LH's ladder
# (total margin) picks BLUE (+5 vs +4) — the documented RankedRobin.ts-vs-LH
# ladder divergence (00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md),
# live for the first time. All LH-verified 2026-07-10.
# Already created -> p8dp28 (BV2176). Reference only — do NOT re-run (permanent).

_PI_CANDS = ["Purple", "Green", "Blue", "Pink"]
_PI_STAR = [(7, (5, 0, 0, 0)), (6, (0, 5, 4, 3)), (2, (0, 0, 5, 4)),
            (1, (0, 4, 5, 3)), (1, (4, 0, 5, 0)), (1, (3, 4, 0, 5)),
            (1, (4, 0, 0, 5)), (1, (0, 0, 0, 5))]
_PI_RANK = [(7, (1, 0, 0, 0)), (6, (0, 1, 2, 3)), (2, (0, 0, 1, 2)),
            (1, (0, 2, 1, 3)), (1, (2, 0, 1, 0)), (1, (3, 2, 0, 1)),
            (1, (2, 0, 0, 1)), (1, (0, 0, 0, 1))]

_CREATED_BV2176 = [
    {
        "test_id": "BV2176",
        "title": "The Post-it RCV example (20 voters) — RCV-IRV elects Purple; STAR and the head-to-head favor Blue",
        "description": ("The 20-voter election from Equal Vote's video 'Updated: "
                        "How does RCV work? — With Post-its!' "
                        "(youtu.be/Vte4nly_Neg), one electorate told three ways. "
                        "RCV-IRV, as walked through on the whiteboard: round 1 "
                        "Purple 7, Green 6, Blue 4, Pink 3 — Pink eliminated "
                        "(1 ballot exhausts); round 2 Purple 8, Green 7, Blue 4 "
                        "— Blue eliminated (2 more exhaust); final Purple 9, "
                        "Green 8 — Purple wins with 9 of the 17 still-active "
                        "ballots. The video then asks: what if round 2 had "
                        "eliminated Green (7 votes) instead of Blue (4)? Blue "
                        "would jump to 10 and WIN 10-9 — and in fact Blue beats "
                        "Purple head-to-head 10-9 on these very ballots. STAR, "
                        "on the video's own 0-5 scores, surfaces that majority "
                        "automatically: scores Purple 46, Blue 44, Pink 44, "
                        "Green 38; the 44-44 tie for second finalist breaks "
                        "head-to-head (Blue beats Pink 10-3); Blue then wins "
                        "the automatic runoff over Purple 10-9 (1 Equal "
                        "Support) — a Runoff Reversal, the score leader losing "
                        "the majority check. Ranked Robin shows WHY no method "
                        "has a clean claim here: the pairwise picture is a "
                        "genuine Condorcet cycle (Purple beats Green 9-8, Green "
                        "beats Blue 7-4, Blue beats Purple 10-9; Pink beats "
                        "Purple 12-8) with Green and Blue tied on record 2-1 — "
                        "BetterVoting's tiebreak ladder (2-way tie -> their "
                        "head-to-head) elects Green deterministically; the LH "
                        "engine's ladder (total margin) picks Blue (+5 vs +4). "
                        "Same ballots, three winners: the tabulation decides."),
        "races": [
            {"title": "Post-its 20 voters — STAR (the video's 0-5 scores)",
             "method": "STAR", "num_winners": 1,
             "candidates": _PI_CANDS, "ballots": _expand(_PI_STAR)},
            {"title": "Post-its 20 voters — RCV-IRV", "method": "IRV",
             "num_winners": 1, "max_rankings": len(_PI_CANDS),
             "candidates": _PI_CANDS, "ballots": _expand(_PI_RANK)},
            {"title": "Post-its 20 voters — Ranked Robin (Copeland)",
             "method": "RankedRobin", "num_winners": 1,
             "max_rankings": len(_PI_CANDS),
             "candidates": _PI_CANDS, "ballots": _expand(_PI_RANK)},
        ],
        "expected": "IRV -> Purple (7/6/4/3 -> 8/7/4 -> 9-8; 3 exhausted). "
                    "STAR -> Blue (46/38/44/44; Blue over Pink head-to-head "
                    "10-3; runoff Blue 10-9 — Runoff Reversal). RankedRobin -> "
                    "Green on BV (2-way Copeland tie at 2-1; head-to-head "
                    "Green 7-4 Blue — deterministic); LH's margin ladder gives "
                    "Blue (+5 vs +4), the documented ladder divergence. No "
                    "Condorcet winner (cycle). LH-verified. Test ID BV2176.",
    },
]

# ---- BV2177 / BV2178 — the Post-it election, seven ways + the switch made real
# Companions to BV2176 (p8dp28). Same source: Equal Vote's "Updated: How does
# RCV work? — With Post-its!" (youtu.be/Vte4nly_Neg), 20 voters.
#
# BV2177 = the SAME electorate as BV2176, run through ALL SEVEN BV methods as
# single-winner races (the BV2172 "all seven" pattern), leading with STAR.
# Winners fan out to ALL FOUR candidates: STAR -> Blue (44-44 scoring tie for
# 2nd finalist breaks head-to-head, runoff Blue 10-9); Ranked Robin -> Green on
# BV (2-way Copeland tie -> head-to-head; LH's margin ladder says Blue — the
# BV2176 ladder divergence, same race); Approval -> Pink 12 (approve = any
# support: the video's scores are only 0/3/4/5, so thresholds 1-3 cast
# identical approvals; at >=4 Blue would win, at =5 Purple — the conversion IS
# the election); IRV -> Purple (7/6/4/3 -> 8/7/4 -> 9-8); Choose-One -> Purple
# (7 first choices); STV 1 seat -> Purple (Droop 11 = IRV, LH round-identical);
# STAR-PR 1 seat -> Purple PREDICTED (Allocated Score's per-seat rule is
# score-only — no runoff — so at 1 seat it's plain Score voting and the Runoff
# Reversal vanishes; LH's allocated refuses seats=1 outright, so this leg is
# BV-only, verify from the live results). All other legs LH-verified 2026-07-10.
#
# BV2178 = the video's round-2 hypothetical MADE REAL: exactly TWO of the six
# Green > Blue > Pink voters flip their top two (-> Blue > Green > Pink).
# RCV-IRV round 1 becomes Purple 7 / Blue 6 / Green 4 / Pink 3; round 2
# Purple 8 / Blue 6 / Green 5 — GREEN is eliminated this time, and the final
# lands the video's exact hypothetical tally: Blue 10, Purple 9. The flip also
# makes Blue the outright Condorcet winner (3-0: beats Purple 10-9, Green 6-5,
# Pink 10-3), so STAR (scores 46/36/46/44; runoff Blue 10-9), Ranked Robin
# (no tie, no ladder needed) and IRV all agree on Blue — while Choose-One
# still says Purple (7 first choices vs 6). Deterministic everywhere
# (the 46-46 scoring tie is between the two finalists themselves, so both
# advance and nothing needs breaking). LH-verified 2026-07-10.
# Already created -> v8r66y (BV2177) / 8kg698 (BV2178). Reference only — do NOT
# re-run (permanent). All 11 live races verified against predictions the same
# day via GET /API/ElectionResult (STAR_PR leg: Purple 46, unique — BV labels
# the round tieBreakType 'random' but the one-candidate 'tied' list shows no
# tie was actually broken).

_PI_APPR = [(7, (1, 0, 0, 0)), (6, (0, 1, 1, 1)), (2, (0, 0, 1, 1)),
            (1, (0, 1, 1, 1)), (1, (1, 0, 1, 0)), (1, (1, 1, 0, 1)),
            (1, (1, 0, 0, 1)), (1, (0, 0, 0, 1))]
_PI_PLUR = [(7, (1, 0, 0, 0)), (6, (0, 1, 0, 0)), (2, (0, 0, 1, 0)),
            (1, (0, 0, 1, 0)), (1, (0, 0, 1, 0)), (1, (0, 0, 0, 1)),
            (1, (0, 0, 0, 1)), (1, (0, 0, 0, 1))]

_SW_STAR = [(7, (5, 0, 0, 0)), (4, (0, 5, 4, 3)), (2, (0, 4, 5, 3)),
            (2, (0, 0, 5, 4)), (1, (0, 4, 5, 3)), (1, (4, 0, 5, 0)),
            (1, (3, 4, 0, 5)), (1, (4, 0, 0, 5)), (1, (0, 0, 0, 5))]
_SW_RANK = [(7, (1, 0, 0, 0)), (4, (0, 1, 2, 3)), (2, (0, 2, 1, 3)),
            (2, (0, 0, 1, 2)), (1, (0, 2, 1, 3)), (1, (2, 0, 1, 0)),
            (1, (3, 2, 0, 1)), (1, (2, 0, 0, 1)), (1, (0, 0, 0, 1))]
_SW_PLUR = [(7, (1, 0, 0, 0)), (4, (0, 1, 0, 0)), (2, (0, 0, 1, 0)),
            (2, (0, 0, 1, 0)), (1, (0, 0, 1, 0)), (1, (0, 0, 1, 0)),
            (1, (0, 0, 0, 1)), (1, (0, 0, 0, 1)), (1, (0, 0, 0, 1))]

_CREATED_BV2177_78 = [
    {
        "test_id": "BV2177",
        "title": "The Post-it election, seven ways — all four candidates win, depending on the method",
        "description": ("The 20-voter election from Equal Vote's video 'Updated: "
                        "How does RCV work? — With Post-its!' "
                        "(youtu.be/Vte4nly_Neg) — the same electorate as BV2176 "
                        "(bettervoting.com/p8dp28) — run through every voting "
                        "method BetterVoting supports, as seven single-winner "
                        "races. The winners fan out to all four candidates. "
                        "STAR: scores Purple 46, Blue 44, Pink 44, Green 38; "
                        "the 44-44 tie for second finalist breaks head-to-head "
                        "(Blue over Pink 10-3) and Blue wins the runoff 10-9. "
                        "Ranked Robin: a genuine Condorcet cycle leaves Green "
                        "and Blue tied 2-1; the head-to-head between the tied "
                        "pair elects Green 7-4. Approval (approve = any "
                        "support; the video's scores use only 0/3/4/5, so any "
                        "threshold from 1 to 3 casts these same approvals): "
                        "Pink 12, Purple 10, Blue 10, Green 8 — Pink wins; had "
                        "voters approved only 4s and 5s Blue would win, and "
                        "only 5s Purple — the rank-to-approval conversion IS "
                        "the election. RCV-IRV: the video's whiteboard count — "
                        "Purple 9, Green 8 after Pink and Blue are eliminated "
                        "(3 ballots exhaust). Choose-One: Purple on 7 first "
                        "choices. STV at 1 seat: identical rounds to IRV — "
                        "Purple. STAR-PR (Allocated Score) at 1 seat: the "
                        "per-seat rule is score-only, no runoff, so it's plain "
                        "Score voting — the score leader Purple, and STAR's "
                        "Runoff Reversal vanishes. One ballot set, seven "
                        "counts, four winners: the tabulation decides."),
        "races": [
            {"title": "Post-its 7 ways — STAR", "method": "STAR",
             "num_winners": 1, "candidates": _PI_CANDS, "ballots": _expand(_PI_STAR)},
            {"title": "Post-its 7 ways — Ranked Robin (Copeland)",
             "method": "RankedRobin", "num_winners": 1,
             "max_rankings": len(_PI_CANDS),
             "candidates": _PI_CANDS, "ballots": _expand(_PI_RANK)},
            {"title": "Post-its 7 ways — Approval (approve = any support)",
             "method": "Approval", "num_winners": 1,
             "candidates": _PI_CANDS, "ballots": _expand(_PI_APPR)},
            {"title": "Post-its 7 ways — RCV-IRV", "method": "IRV",
             "num_winners": 1, "max_rankings": len(_PI_CANDS),
             "candidates": _PI_CANDS, "ballots": _expand(_PI_RANK)},
            {"title": "Post-its 7 ways — Choose-One (Plurality)",
             "method": "Plurality", "num_winners": 1,
             "candidates": _PI_CANDS, "ballots": _expand(_PI_PLUR)},
            {"title": "Post-its 7 ways — STV, 1 seat (= IRV single-winner)",
             "method": "STV", "num_winners": 1,
             "max_rankings": len(_PI_CANDS),
             "candidates": _PI_CANDS, "ballots": _expand(_PI_RANK)},
            {"title": "Post-its 7 ways — STAR-PR (Allocated Score), 1 seat",
             "method": "STAR_PR", "num_winners": 1,
             "candidates": _PI_CANDS, "ballots": _expand(_PI_STAR)},
        ],
        "expected": "STAR -> Blue (runoff 10-9). RankedRobin -> Green (BV "
                    "ladder; LH margin ladder says Blue). Approval -> Pink "
                    "(12/10/10/8). IRV -> Purple (9-8). Plurality -> Purple "
                    "(7). STV -> Purple (= IRV). STAR_PR 1 seat -> Purple "
                    "PREDICTED (score-only rule, 46; LH allocated refuses "
                    "seats=1 — BV-only leg). All four candidates win "
                    "somewhere. Test ID BV2177.",
    },
    {
        "test_id": "BV2178",
        "title": "The Post-it election's round-2 switch, made real — two ballots flip and RCV-IRV elects Blue",
        "description": ("The 'what if?' from Equal Vote's video 'Updated: How "
                        "does RCV work? — With Post-its!' "
                        "(youtu.be/Vte4nly_Neg), made real. The video asks what "
                        "would happen if round 2 had eliminated Green instead "
                        "of Blue, and answers: Blue would win 10-9. This "
                        "election is the companion BV2176/BV2177 electorate "
                        "with exactly TWO of the six Green > Blue > Pink "
                        "voters flipping their top two choices (to Blue > "
                        "Green > Pink; scores 0,4,5,3). That two-ballot switch "
                        "makes the hypothetical the actual count: RCV-IRV "
                        "round 1 is Purple 7, Blue 6, Green 4, Pink 3; round 2 "
                        "Purple 8, Blue 6, Green 5 — Green IS eliminated this "
                        "time, all four Green > Blue > Pink ballots transfer "
                        "to Blue, and the final is the video's exact "
                        "hypothetical tally: Blue 10, Purple 9. The flip also "
                        "makes Blue the outright Condorcet winner (beats "
                        "Purple 10-9, Green 6-5, Pink 10-3), so Ranked Robin "
                        "elects Blue with no tie to break, and STAR elects "
                        "Blue too (scores Blue 46, Purple 46, Pink 44, Green "
                        "36 — both leaders advance, runoff Blue 10-9). Only "
                        "Choose-One still says Purple (7 first choices vs 6). "
                        "Two voters' honesty about their favorite flipped the "
                        "RCV-IRV winner from Purple to Blue; the methods that "
                        "read the whole ballot were already pointing there."),
        "races": [
            {"title": "Post-its switch — STAR", "method": "STAR",
             "num_winners": 1, "candidates": _PI_CANDS, "ballots": _expand(_SW_STAR)},
            {"title": "Post-its switch — Ranked Robin (Copeland)",
             "method": "RankedRobin", "num_winners": 1,
             "max_rankings": len(_PI_CANDS),
             "candidates": _PI_CANDS, "ballots": _expand(_SW_RANK)},
            {"title": "Post-its switch — RCV-IRV", "method": "IRV",
             "num_winners": 1, "max_rankings": len(_PI_CANDS),
             "candidates": _PI_CANDS, "ballots": _expand(_SW_RANK)},
            {"title": "Post-its switch — Choose-One (Plurality)",
             "method": "Plurality", "num_winners": 1,
             "candidates": _PI_CANDS, "ballots": _expand(_SW_PLUR)},
        ],
        "expected": "IRV -> Blue (7/6/4/3 -> 8/6/5, Green out -> Blue 10, "
                    "Purple 9 — the video's hypothetical, real). STAR -> Blue "
                    "(46/36/46/44; runoff 10-9). RankedRobin -> Blue (Condorcet "
                    "winner 3-0, no tiebreak). Plurality -> Purple (7 vs 6). "
                    "Deterministic, LH-verified. Test ID BV2178.",
    },
]

# Add the next election batch here, then run the script.
_ICE_CREAM_LADDER = {
    "test_id": "BV2180",
    "title": "Ice Cream, six flavors — a STAR tie in both rounds, resolved without the lot",
    "description": (
        "The worked example from the STAR tie-breaking documentation (the two-round, "
        "two-ladder tiebreak). Two voters, six ice-cream flavors. Scoring round: "
        "Strawberry leads at 7; Chocolate, Chocolate Chip and Vanilla tie for the "
        "second finalist slot at 5 each. The pairwise rung can't separate the three "
        "(all 2), so the FIVE-STAR rung decides — only Chocolate Chip earned a 5, so "
        "it advances alongside Strawberry. The automatic runoff then ties 1-1 on "
        "head-to-head preference, and the SCORE rung breaks it: Strawberry 7 beats "
        "Chocolate Chip 5. Winner: Strawberry. The point of the case is that STAR "
        "settles ties in BOTH rounds by DETERMINISTIC rungs (five-star, then score) — "
        "the pre-published random lot order is never consulted. LH and BetterVoting "
        "agree; the lot is irrelevant here, so the result is fully reproducible."
    ),
    "method": "STAR",
    "num_winners": 1,
    "candidates": ["Chocolate", "Chocolate Chip", "Fudge Brownie", "Vanilla", "Strawberry", "Mango"],
    "ballots": [
        [4, 5, 4, 1, 2, 0],   # Mango left blank -> counts as 0
        [1, 0, 0, 4, 5, 4],
    ],
    "expected": "Strawberry",
}

_FAQ_RUNOFF = {
    "test_id": "BV2182",
    "title": "Why STAR Has an Automatic Runoff — a Runoff Reversal, with an Equal-Support ballot",
    "description": (
        "STAR FAQ teaching example: why STAR has a second round. 10 voters, three "
        "candidates. Berry is the consensus choice and leads the Scoring Round on total "
        "stars (44), but more voters strictly prefer Almond head-to-head, so Almond wins "
        "the Automatic Runoff 6-3 — a clean 'score leader != runoff winner' Runoff "
        "Reversal. One voter scored both finalists 5 (Equal Support) and is counted in "
        "neither runoff column. Almond is also the Condorcet winner here."
    ),
    "method": "STAR",
    "num_winners": 1,
    "candidates": ["Almond", "Berry", "Cocoa"],
    "ballots": [
        [5, 4, 1], [5, 4, 1], [5, 4, 1], [5, 4, 1],
        [5, 4, 0], [5, 4, 0],
        [0, 5, 2], [0, 5, 2], [0, 5, 2],
        [5, 5, 0],
    ],
    "expected": "Almond",
}

_FORCED_EXHAUSTION = {
    "test_id": "BV2183",
    "title": "Forced Ballot Exhaustion — a 2-rank cap discards more ballots than the winner receives (constructed IRV example)",
    "description": (
        "A deliberately-constructed worst case (clearly not a typical election) showing "
        "the ceiling of RCV-IRV ballot exhaustion under a ranking cap. 50 voters, five "
        "candidates, but the ballot caps you at 2 rankings. Three minor candidates "
        "(Cleo, Dev, Eli) form a rotating bloc; their 21 voters ranked only minor "
        "candidates (all they could fit), so when those are eliminated their ballots "
        "EXHAUST — none reaches the two real contenders. Ada beats Ben 15-14, a margin "
        "of ONE, while 21 ballots (42%) are discarded — more than the winner's own 15 "
        "votes. Ada's 'majority' is 15 of 50 = 30% of the electorate. Lift the 2-rank "
        "cap and the forced exhaustion vanishes. Companion to the repo's forced-vs-"
        "voluntary-exhaustion page; the point is the mechanism's ceiling, not a claim "
        "that real elections look like this (they are much milder — see the real rates)."
    ),
    "method": "IRV",
    "num_winners": 1,
    "max_rankings": 2,
    "candidates": ["Ada", "Ben", "Cleo", "Dev", "Eli"],
    "ballots": (
        [[1, 0, 2, 0, 0]] * 15 +   # Ada > Cleo
        [[0, 1, 0, 2, 0]] * 14 +   # Ben > Dev
        [[0, 0, 1, 0, 2]] * 8 +    # Cleo > Eli
        [[0, 0, 2, 1, 0]] * 7 +    # Dev > Cleo
        [[0, 0, 0, 2, 1]] * 6      # Eli > Dev
    ),
    "expected": "Ada (15 vs Ben 14, margin 1); 21 of 50 ballots forced-exhausted by the 2-rank cap — more than the winner's own total.",
}

_LUNCH_VOTE = {
    "test_id": "BV2184",
    "title": "The Team Lunch Vote — a beginner's STAR example (the compromise everyone likes wins)",
    "description": (
        "The running example from the STAR beginner's on-ramp. Five coworkers pick "
        "lunch: two love Sushi, two love Tacos, and everyone is happy with Pizza. Under "
        "Choose-One each names one favorite, the vote splits (Sushi 2, Tacos 2, Pizza 1), "
        "and Pizza — the option nobody objected to — comes last; a coin flip hands lunch "
        "to Sushi or Tacos and half the team is stuck with something they rated 0. STAR "
        "reads the whole ballot: Pizza tops the Scoring Round (17) and wins the runoff 3-2. "
        "The compromise everyone can live with wins, with no strategic voting. (Choose-One "
        "and RCV-IRV both elect Sushi here; STAR elects Pizza.)"
    ),
    "method": "STAR",
    "num_winners": 1,
    "candidates": ["Sushi", "Tacos", "Pizza"],
    "ballots": [
        [5, 0, 3], [5, 0, 3],   # Sushi-lovers
        [0, 5, 3], [0, 5, 3],   # Taco-lovers
        [3, 1, 5],              # Pizza-fan
    ],
    "expected": "Pizza (Scoring Round 17; runoff 3-2 over Sushi). Choose-One/IRV pick Sushi.",
}

_BEER_VOTE = {
    "test_id": "BV2185",
    "title": "Bond Brothers Beer Picks — STAR Voting NC",
    "description": (
        "A friendly STAR Voting demo from STAR Voting NC: score nine Bond Brothers "
        "Beer Company (Cary, NC) beers 0–5 across the whole spectrum — a crisp Pilsner, "
        "a Blonde Ale, three IPAs, an amber, a brown, and two stouts — and the two "
        "highest-scoring beers meet in an automatic runoff. Everyone has a real favorite "
        "and a real 'hard no', which is exactly what makes STAR interesting. Vote on "
        "paper and/or online and compare. (Taplists rotate; a real event would confirm "
        "what's actually pouring.)"
    ),
    "method": "STAR",
    "num_winners": 1,
    "candidates": ["Cary Parkway Pilsner", "Blonde Roast", "Local", "Lazy Daze Haze",
                   "Long Stride", "Chatham Street Copper", "Bakers", "O'Rascal's",
                   "Breakfast Variant"],
    "ballots": [],   # empty — a live vote; people score fresh at the meetup
    "expected": "live vote (no seed ballots)",
}

ELECTIONS: list = [_BEER_VOTE]

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
