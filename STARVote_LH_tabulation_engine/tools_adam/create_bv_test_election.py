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


ELECTIONS = [
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
