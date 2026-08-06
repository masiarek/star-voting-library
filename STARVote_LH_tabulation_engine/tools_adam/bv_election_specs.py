"""bv_election_specs.py — election DATA for create_bv_test_election.py.

Split out from the engine so the tool code stays small and the (long) catalogue
of election definitions lives on its own. This module is PURE data plus the small
helpers that expand voter blocs into ballots — no network, no auth, no third-party
imports. The engine imports ELECTIONS from here.

Provenance note: each created election is ALSO recorded on BetterVoting (permanent),
its frozen export in 06_Other/_demo_dropbox/, and BV_registry.md — so this file is
NOT the sole record. Going forward, point ELECTIONS at only what you want to create;
you need not hoard every spec here.
"""

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
#    "enable_write_in": True,   # optional; DEFAULT True so QR/online voters can
#                               # write in a choice. Set False to lock the list.
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
#   BV2187 — Ann, Bob, Cal (canonical STAR mechanics demo)      -> qrw6wb  (backs 01_STAR/02_Examples/bv2187_qrw6wb_ann-bob-cal)
#   BV830 — No Condorcet winner (top-two tie, score breaks it)   -> vb3xv2  (backs 01_STAR/… bv830_vb3xv2_no_condorcet_tie_score; STAR-only, RR unfreezable)
#   BV2212 — STAR IIA under a Condorcet cycle (cycle-spoiler)      -> g3f7r2  (STAR-only, RR unfreezable; a losing candidate flips the winner)
#   BV2213 — Alaska 2022 special (reduced 200-voter model, 4 races) -> k3fmwv  (Plurality/IRV -> Peltola; RR/STAR -> Begich, the Condorcet winner IRV cut)
#   BV2214 — Alaska 2022 GENERAL (reduced model, 4 races) -> m3hb6y  (all four -> Peltola, the Condorcet winner; the "IRV got it right" counterpart to BV2213)
#   BV2215 — Minority winner (canonical; 3 races) -> 2p33qq  (Plurality -> Ada on 34%; RR & STAR -> Cleo, the majority's real choice)
#   BV2216/2217/2218 — Pineapple progression (4 races each) -> ht2c3g / mvxbxr / h34pp9  (Plurality -> Pineapple on 34/25/11%; Approval/RR/STAR -> Cheese)
# Their specs live in git history / the case .yaml files.
#
# MULTI-RACE: a spec may carry a "races": [ {title, method, num_winners,
# max_rankings?, candidates, ballots}, ... ] list INSTEAD of the flat single-race
# fields. One election, several contests; each voter votes in every race, so all
# races must have the SAME number of ballots (aligned by voter index). Score
# ranges per method: Approval/Plurality = 0/1 ; STAR/Bloc/STAR_PR = 0-5 ; ranked
# (RankedRobin/IRV/STV) = ranks 1..max_rankings (0 = unranked).
#
# RACE TITLES: write them WITHOUT the BV<n> prefix — the create script prepends
# the election's test_id to EVERY race title automatically (rule flipped by Adam
# 2026-07-25: BV's /vote page leads with the race title, so each race must be
# self-identifying; the pre-check hard-stops if a race title would go out bare).

# DESCRIPTION BACKLINK — get the URL right the FIRST time; BV descriptions are
# PERMANENT and cannot be edited via the API. Every description must end with
#   "Full lesson & tabulation: https://masiarek.github.io/star-voting-library/<path>.html"
# GOTCHA (found 2026-07-25): when the lesson page is a folder README.md, the site
# serves it as <folder>/index.html — README.html 404s. MkDocs renames a folder
# README to index; use_directory_urls:false only stops the directory-style URL, it
# does NOT keep the README name. So:
#   folder README.md      -> .../method_comparisons/<folder>/index.html   ✓
#   any other page X.md   -> .../<path>/X.html                            ✓
# BV2249's description shipped .../weak_condorcet_loser/README.html, which is a
# permanent 404 (unfixable — no owner-editable path for descriptions). BV2250 uses
# index.html and was verified live BEFORE the mint. VERIFY THE URL WITH curl FIRST:
#   curl -s -o /dev/null -w '%{http_code}' <url>   # must be 200, not 404

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
# All strict full rankings (no ties). Lesson: 05_Ranked_Robin/01_Learn/
# rr_clone_independence.md ; LH-only pair: 05_Ranked_Robin/03_Criteria/clone_independence/.
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
# 07_Concepts/topics/condorcet/fairvote_condorcet_claim_check.md.

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
# ladder divergence (05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md),
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

_ICE_CREAM = {
    "test_id": "BV2186",
    "title": "Best Ice Cream Flavor — STAR Voting NC",
    "description": (
        "A mainstream, politics-free STAR Voting demo built to SHOW vote-splitting. "
        "Three of the eight flavors are chocolate — Dark Chocolate, Chocolate Chip, and "
        "Chocolate Fudge. Under Choose-One, chocolate lovers split their vote three ways, "
        "so a single non-chocolate flavor can win with fewer real fans (the classic "
        "spoiler effect). With STAR you score every flavor 0–5, so you can give all three "
        "chocolates a 5 — the crowd's true favorite isn't punished for having similar "
        "options on the menu. Score them all; the two highest meet in an automatic runoff."
    ),
    "method": "STAR",
    "num_winners": 1,
    "candidates": ["Vanilla", "Strawberry", "Mango", "Dark Chocolate",
                   "Chocolate Chip", "Chocolate Fudge", "Butter Pecan", "Salted Caramel"],
    "ballots": [],   # empty — a live vote
    "expected": "live vote — vote-splitting demo (a 3-flavor chocolate cluster)",
}

_ANN_BOB_CAL = {
    "test_id": "BV2187",
    "title": "Ann, Bob, Cal — the canonical STAR mechanics demo (3 voters, both rounds at work)",
    "description": (
        "The canonical leading example of the STAR education repo (github.com/masiarek/YAML): "
        "the smallest STAR election where both rounds do visible, different work. Three voters "
        "score three candidates: (Ann 5, Bob 4, Cal 0), (3, 5, 2), (0, 3, 5). Scoring Round: "
        "Bob 12, Ann 8, Cal 7 — Bob and Ann advance. Automatic Runoff: voter 1 prefers Ann "
        "(5 > 4), voters 2 and 3 prefer Bob, so Bob wins 2-1. Voter 1's ballot is the runoff "
        "lesson: a friendly 4 for Bob still becomes one full vote for Ann. Deliberately no "
        "twist — the score leader also wins the runoff (and is the Condorcet winner) — so the "
        "procedure itself is the whole lesson. First-choice votes tie 1-1-1: Choose-One can "
        "only shrug here."
    ),
    "method": "STAR",
    "num_winners": 1,
    "candidates": ["Ann", "Bob", "Cal"],
    "ballots": [
        [5, 4, 0],   # voter 1: loves Ann, quite likes Bob
        [3, 5, 2],   # voter 2: a Bob fan who scores honestly
        [0, 3, 5],   # voter 3: loves Cal, Bob is acceptable
    ],
    "enable_write_in": False,   # canonical = frozen: lock the candidate list
    "expected": "Bob (Scoring 12/8/7; runoff 2-1 over Ann; Condorcet winner). Plurality ties 1-1-1.",
}

_BV830_NO_CONDORCET = {
    "test_id": "BV830",
    "title": "No Condorcet winner (top-two tie) — STAR breaks it by score",
    "description": (
        "A STAR Voting edge case: no strict Condorcet winner, resolved by score. Three "
        "voters score three candidates A, B, C — (A0, B0, C1), (A0, B2, C2), (A0, B5, C0). "
        "Scoring Round: B totals 7 and C totals 3, so B and C advance (A gets 0). Automatic "
        "Runoff: the two finalists tie 1-1-1 head-to-head — one voter prefers B, one prefers "
        "C, and one scores them equally — so no candidate beats every rival and there is no "
        "strict Condorcet winner. This is a top-two pairwise tie, not a rock-paper-scissors "
        "cycle. STAR breaks the deadlock with the score total: B (7) outscores C (3), so B "
        "wins. The teaching point: exactly where the head-to-head (Condorcet) standard runs "
        "out of data, STAR's score intensity still identifies the broader-supported winner."
    ),
    "method": "STAR",
    "num_winners": 1,
    "candidates": ["A", "B", "C"],
    "ballots": [
        [0, 0, 1],   # voter 1: only C, a single point
        [0, 2, 2],   # voter 2: B and C equal
        [0, 5, 0],   # voter 3: B to the max
    ],
    "enable_write_in": False,   # frozen reproduction of the BV830 source doc
    "expected": (
        "B — Scoring B7/C3/A0 (B,C advance); Automatic Runoff B vs C ties 1-1-1; "
        "score total breaks the tie for B; no strict Condorcet winner (B and C pairwise tie)."
    ),
}

# --- BV2188/89/90 — "Two Districts, One Mayor": STAR's reinforcement paradox ----
# Already created 2026-07-16 -> d3b9wc (BV2188) / rhbfj7 (BV2189) / 923q3d
# (BV2190); all six races verified live against LH. Reference only — do NOT
# point ELECTIONS back at _TD_TRIO (re-running would create undeletable
# duplicates).
# SOURCE: 01_STAR/05_Practice/ex01_two_districts.md (this repo) — ballots adapted
# from a RangeVoting.org worked example, posed as a districts exercise in
# Brendan W. Sullivan, "An Introduction to the Math of Voting Methods" (2022),
# ch. 5. THREE elections, the STAR-side sibling of the Felsenthal BV2147-49
# trio (where the SAME paradox hits IRV while STAR happens to stay consistent
# on those ballots — this trio is the constructive proof that STAR is not
# reinforcement-proof either):
#   BV2188 West (9):  STAR Avery 35/33/32/25/0; runoff Avery 1-0 (8 Equal Support).
#   BV2189 East (9):  West's mirror (Blake<->Diego): Avery again, vs Diego.
#   BV2190 Combined (18): the runner-ups were LOCAL (Blake West-only, Diego
#                     East-only) while Carmen scored 32 in BOTH: citywide it is
#                     Avery 70 vs Carmen 64, and Carmen wins the runoff 10-8.
#                     Avery swept the districts and lost the city.
# Each election adds a Ranked Robin race on the same opinions (dense EQUAL
# ranks, the encoding proven on BV2140): Elena — the Condorcet winner in every
# electorate — wins 4-0 in all three, deterministic and freezable. All six
# races LH-verified pre-creation (01_STAR/05_Practice/, tested answer keys).
_TD_CANDS = ["Avery", "Blake", "Carmen", "Diego", "Elena"]
_TD_W_STAR = [(5, [3, 3, 4, 0, 5]), (3, [5, 5, 3, 0, 0]), (1, [5, 3, 3, 0, 0])]
_TD_W_RR = [(5, [3, 3, 2, 0, 1]), (3, [1, 1, 2, 0, 0]), (1, [1, 2, 2, 0, 0])]
_TD_E_STAR = [(5, [3, 0, 4, 3, 5]), (3, [5, 0, 3, 5, 0]), (1, [5, 0, 3, 3, 0])]
_TD_E_RR = [(5, [3, 0, 2, 3, 1]), (3, [1, 0, 2, 1, 0]), (1, [1, 0, 2, 2, 0])]


def _td_races(prefix, star_blocs, rr_blocs):
    return [
        {"title": f"{prefix} — STAR (0-5 scores)", "method": "STAR",
         "num_winners": 1, "candidates": _TD_CANDS, "ballots": _expand(star_blocs)},
        {"title": f"{prefix} — Ranked Robin (Copeland; equal ranks allowed)",
         "method": "RankedRobin", "num_winners": 1, "max_rankings": len(_TD_CANDS),
         "candidates": _TD_CANDS, "ballots": _expand(rr_blocs)},
    ]


_TD_SRC = ("The 'Two Districts, One Mayor' consistency exercise from the STAR "
           "education repo (github.com/masiarek/star-voting-library — "
           "01_STAR/05_Practice/ex01_two_districts.md): a live demonstration that "
           "STAR Voting is not reinforcement-proof — a candidate can win every "
           "district separately and still lose the combined election, because "
           "WHO REACHES the automatic runoff is not an additive fact (the "
           "reinforcement / consistency / multiple-districts paradox). Ballots "
           "adapted from a worked example on RangeVoting.org, posed as a "
           "districts exercise in Brendan W. Sullivan, 'An Introduction to the "
           "Math of Voting Methods' (2022), ch. 5; candidates renamed. The "
           "IRV-side counterpart is the Felsenthal Reinforcement trio "
           "(BV2147-BV2149), where plurality-with-runoff commits the same "
           "paradox on different ballots — and STAR happens to stay consistent "
           "there. This trio is the constructive proof that STAR's runoff "
           "forfeits the guarantee too. ")

_TD_TRIO = [
    {
        "test_id": "BV2188",
        "title": "Two Districts, One Mayor (I of III) — West District: STAR elects Avery",
        "description": (_TD_SRC +
                        "This is the WEST DISTRICT: 9 voters — 5×(Avery 3, Blake 3, "
                        "Carmen 4, Diego 0, Elena 5), 3×(Avery 5, Blake 5, Carmen 3, "
                        "Diego 0, Elena 0), 1×(Avery 5, Blake 3, Carmen 3, Diego 0, "
                        "Elena 0). Scoring Round: Avery 35, Blake 33, Carmen 32, Elena "
                        "25, Diego 0 — Avery and Blake advance. Eight of the nine "
                        "ballots score the two finalists identically (Equal Support), "
                        "so the one decided voter settles the Automatic Runoff: Avery "
                        "wins 1-0. East (BV2189) elects Avery too — and the combined "
                        "city (BV2190) elects Carmen. The second race runs the same "
                        "nine opinions as Ranked Robin (Copeland) on ranked ballots "
                        "with EQUAL rankings (e.g. Elena 1st, Carmen 2nd, Avery = "
                        "Blake 3rd): Elena — first choice of 5 of the 9 and this "
                        "district's Condorcet winner — wins every head-to-head 5-4 "
                        "and takes a perfect 4-0 record. LH-verified pre-creation."),
        "races": _td_races("West District", _TD_W_STAR, _TD_W_RR),
        "enable_write_in": False,
        "expected": "STAR -> Avery (35/33/32/25/0; runoff 1-0 over Blake, 8 Equal "
                    "Support). RR -> Elena (Condorcet winner, 4-0). Trio: West Avery, "
                    "East Avery, Combined CARMEN. Test ID BV2188.",
    },
    {
        "test_id": "BV2189",
        "title": "Two Districts, One Mayor (II of III) — East District: STAR elects Avery again",
        "description": (_TD_SRC +
                        "This is the EAST DISTRICT — West's mirror image, with Blake "
                        "and Diego trading places: 9 voters — 5×(Avery 3, Blake 0, "
                        "Carmen 4, Diego 3, Elena 5), 3×(Avery 5, Blake 0, Carmen 3, "
                        "Diego 5, Elena 0), 1×(Avery 5, Blake 0, Carmen 3, Diego 3, "
                        "Elena 0). Scoring Round: Avery 35, Diego 33, Carmen 32, "
                        "Elena 25, Blake 0 — Avery and Diego advance; again eight "
                        "Equal Support ballots, and the one decided voter elects "
                        "Avery 1-0. West (BV2188) chose Avery too — yet the combined "
                        "city (BV2190) chooses Carmen. The second race runs the same "
                        "opinions as Ranked Robin (Copeland, equal ranks): Elena is "
                        "again the Condorcet winner, 4-0. LH-verified pre-creation."),
        "races": _td_races("East District", _TD_E_STAR, _TD_E_RR),
        "enable_write_in": False,
        "expected": "STAR -> Avery (35/33/32/25/0 with Diego as the 33; runoff 1-0 "
                    "over Diego, 8 Equal Support). RR -> Elena (4-0). Test ID BV2189.",
    },
    {
        "test_id": "BV2190",
        "title": "Two Districts, One Mayor (III of III) — the combined city: Carmen wins where Avery swept both districts",
        "description": (_TD_SRC +
                        "This is the COMBINED CITY: all 18 ballots of West (BV2188) "
                        "and East (BV2189) together, ceteris paribus. Citywide "
                        "Scoring Round: Avery 70, Carmen 64, Elena 50, Blake 33, "
                        "Diego 33. Each district's runner-up was LOCAL — Blake's 33 "
                        "points live only in West, Diego's only in East — while "
                        "Carmen scored 32 in BOTH districts, so citywide she replaces "
                        "them as the second finalist. And the Avery-vs-Carmen matchup "
                        "was never Avery's: the two Elena blocs (10 of the 18 voters) "
                        "all score Carmen 4 > Avery 3, so Carmen wins the Automatic "
                        "Runoff 10-8 (56%-44%). Avery won BOTH districts and leads "
                        "the citywide scores 70-64, yet Carmen takes the seat — the "
                        "reinforcement paradox, live. (Plain Score voting is immune: "
                        "totals just add, so Avery leads West, East, and the city "
                        "alike.) The second race runs the same opinions as Ranked "
                        "Robin (Copeland, equal ranks): Elena — first choice of 10 of "
                        "18 and the citywide Condorcet winner (10-8, 10-8, 10-4, "
                        "10-4) — wins 4-0. One engineered electorate, three "
                        "defensible winners: Score says Avery, STAR says Carmen, "
                        "Condorcet logic says Elena. LH-verified pre-creation."),
        "races": _td_races("Combined city", _TD_W_STAR + _TD_E_STAR, _TD_W_RR + _TD_E_RR),
        "enable_write_in": False,
        "expected": "STAR -> CARMEN (Avery 70 / Carmen 64; runoff Carmen 10-8) though "
                    "Avery won both districts (BV2188, BV2189). RR -> Elena (4-0). "
                    "The Score-total leader remains Avery. Test ID BV2190.",
    },
]


# --- BV2191-98 — the exercises set goes live (ex03/05/06/10/11) -----------------
# Already created 2026-07-17 -> ywqhq4 (BV2191) / 6bry7c (BV2192) / x4dkfd
# (BV2193) / 7f4f7q (BV2194) / g6q42v (BV2195) / yyhj9x (BV2196) / ggg7hd
# (BV2197) / 93gjx6 (BV2198); all 22 races verified live against LH. Reference
# only — do NOT point ELECTIONS back at _EX_TRIO_2 (re-running would create
# undeletable duplicates).
# Eight elections backing 01_STAR/05_Practice/ (ex09 stays LH-only on purpose: its
# 3-way Ranked Robin wins tie is BV-random). All races LH-verified pre-creation;
# ranked races use ranks-in-slots (1 = top, 0 = unranked), Approval/Plurality 0/1.
# ex10 carries NO Ranked Robin races: the reticent profile's rank conversion
# yields a Condorcet cycle (3-way tie -> BV random, not freezable), so the pair
# stays symmetric with STAR + IRV only.

_EX_SRC = ("From the exercises set of the STAR education repo "
           "(github.com/masiarek/star-voting-library, 01_STAR/05_Practice/) — "
           "predict-then-peek problems with hidden solutions; this election is "
           "the live, vote-able copy of its exercise. ")

_E3_CANDS = ["Apple", "Banana", "Cherry"]
_E3_STAR = _expand([(4, [5, 0, 3]), (3, [0, 5, 4]), (2, [0, 1, 5])])
_E3_PLUR = _expand([(4, [1, 0, 0]), (3, [0, 1, 0]), (2, [0, 0, 1])])
_E3_APPR = _expand([(4, [1, 0, 1]), (3, [0, 1, 1]), (2, [0, 0, 1])])
_E3_RANK = _expand([(4, [1, 3, 2]), (3, [3, 1, 2]), (2, [3, 2, 1])])

_E5_CANDS = ["Avi", "Brook", "Cole"]
_E5_STAR = _expand([(4, [5, 3, 0]), (3, [0, 3, 5]), (1, [3, 5, 0]), (1, [0, 5, 3])])
_E5_RANK = _expand([(4, [1, 2, 3]), (3, [3, 2, 1]), (1, [2, 1, 3]), (1, [3, 1, 2])])

_E6_CANDS = ["Ari", "Bree", "Cash"]
_E6_STAR_H = _expand([(4, [5, 3, 0]), (4, [0, 2, 5]), (1, [0, 5, 1])])
_E6_RANK_H = _expand([(4, [1, 2, 0]), (4, [0, 2, 1]), (1, [0, 1, 2])])
_E6_STAR_S = _expand([(4, [5, 0, 0]), (4, [0, 2, 5]), (1, [0, 5, 1])])
_E6_RANK_S = _expand([(4, [1, 0, 0]), (4, [0, 2, 1]), (1, [0, 1, 2])])

_E10_CANDS = ["Amir", "Bess", "Cato"]
_E10_STAR_R = _expand([(4, [5, 0, 0]), (2, [2, 5, 0]), (3, [0, 1, 5])])
_E10_RANK_R = _expand([(4, [1, 0, 0]), (2, [2, 1, 0]), (3, [0, 2, 1])])
_E10_STAR_G = _expand([(4, [5, 3, 0]), (2, [2, 5, 0]), (3, [0, 1, 5])])
_E10_RANK_G = _expand([(4, [1, 2, 0]), (2, [2, 1, 0]), (3, [0, 2, 1])])

_E11_CANDS2 = ["Alba", "Brett"]
_E11_PLUR_B = _expand([(5, [1, 0]), (4, [0, 1])])
_E11_STAR_B = _expand([(5, [5, 0]), (4, [0, 5])])
_E11_CANDS3 = ["Alba", "Axl", "Brett"]
_E11_PLUR_S = _expand([(3, [1, 0, 0]), (2, [0, 1, 0]), (4, [0, 0, 1])])
_E11_STAR_S = _expand([(3, [5, 4, 0]), (2, [4, 5, 0]), (4, [0, 0, 5])])
_E11_RANK_S = _expand([(3, [1, 2, 3]), (2, [2, 1, 3]), (4, [0, 0, 1])])

_EX_TRIO_2 = [
    {
        "test_id": "BV2191",
        "title": "One Electorate, Five Verdicts — the snack vote counted five ways",
        "description": (_EX_SRC +
                        "Nine voters pick the office snack (exercise ex03): 4×(Apple 5, "
                        "Cherry 3, Banana 0), 3×(Banana 5, Cherry 4, Apple 0), 2×(Cherry 5, "
                        "Banana 1, Apple 0). FIVE races on the same nine opinions, one per "
                        "counting rule. Choose-One elects Apple (4-3-2 on first choices) — "
                        "who loses head-to-head to BOTH rivals (the Condorcet loser). "
                        "RCV-IRV eliminates Cherry first (2 first choices) and elects "
                        "Banana 5-4. Approval (approve = score 3+) elects Cherry with 9 of "
                        "9 approvals. Score elects Cherry, 34 of 45. STAR advances Cherry "
                        "and Apple and Cherry wins the runoff 5-4. Ranked Robin confirms "
                        "Cherry as the Condorcet winner (beats Apple 5-4, Banana 6-3). One "
                        "electorate, three different winners across five rules — the "
                        "ballot doesn't decide, the method does. LH-verified."),
        "races": [
            {"title": "Snack vote — Choose-One (Plurality)", "method": "Plurality",
             "num_winners": 1, "candidates": _E3_CANDS, "ballots": _E3_PLUR},
            {"title": "Snack vote — RCV-IRV (Instant Runoff)", "method": "IRV",
             "num_winners": 1, "max_rankings": 3, "candidates": _E3_CANDS, "ballots": _E3_RANK},
            {"title": "Snack vote — Approval (approve = 3+)", "method": "Approval",
             "num_winners": 1, "candidates": _E3_CANDS, "ballots": _E3_APPR},
            {"title": "Snack vote — STAR (0-5 scores)", "method": "STAR",
             "num_winners": 1, "candidates": _E3_CANDS, "ballots": _E3_STAR},
            {"title": "Snack vote — Ranked Robin (Copeland)", "method": "RankedRobin",
             "num_winners": 1, "max_rankings": 3, "candidates": _E3_CANDS, "ballots": _E3_RANK},
        ],
        "enable_write_in": False,
        "expected": "Choose-One -> Apple (Condorcet loser); IRV -> Banana; Approval -> "
                    "Cherry (9/9); STAR -> Cherry (34; runoff 5-4); RR -> Cherry "
                    "(Condorcet winner). Test ID BV2191.",
    },
    {
        "test_id": "BV2192",
        "title": "The Squeezed Bridge-Builder — everyone's second choice, IRV's first elimination",
        "description": (_EX_SRC +
                        "The center-squeeze drill (exercise ex05): a club presidency with "
                        "two wings and one bridge-builder. Nine voters — 4×(Avi 5, Brook 3), "
                        "3×(Cole 5, Brook 3), 1×(Brook 5, Avi 3), 1×(Brook 5, Cole 3). "
                        "Every single voter scores Brook 3 or better, and Brook beats each "
                        "rival head-to-head (Avi 5-4, Cole 6-3) — the Condorcet winner. But "
                        "Brook holds only 2 first choices, so RCV-IRV eliminates Brook "
                        "FIRST and elects the wing candidate Avi 5-4. STAR reads the full "
                        "scores: Brook tops the scoring round 31-23-18 and wins the runoff "
                        "5-4; Ranked Robin agrees. The same mechanism as Burlington 2009 "
                        "and Alaska 2022, at whiteboard scale. LH-verified."),
        "races": [
            {"title": "Club presidency — STAR (0-5 scores)", "method": "STAR",
             "num_winners": 1, "candidates": _E5_CANDS, "ballots": _E5_STAR},
            {"title": "Club presidency — RCV-IRV (Instant Runoff)", "method": "IRV",
             "num_winners": 1, "max_rankings": 3, "candidates": _E5_CANDS, "ballots": _E5_RANK},
            {"title": "Club presidency — Ranked Robin (Copeland)", "method": "RankedRobin",
             "num_winners": 1, "max_rankings": 3, "candidates": _E5_CANDS, "ballots": _E5_RANK},
        ],
        "enable_write_in": False,
        "expected": "STAR -> Brook (31/23/18; runoff 5-4). IRV -> Avi (Brook eliminated "
                    "on 2 first choices). RR -> Brook (Condorcet winner). Test ID BV2192.",
    },
    {
        "test_id": "BV2193",
        "title": "Bullet Voting Backfires (1 of 2) — the honest ballots elect the compromise",
        "description": (_EX_SRC +
                        "The strategy pair's base case (exercise ex06): nine voters, three "
                        "speakers — 4×(Ari 5, Bree 3, Cash 0), 4×(Cash 5, Bree 2, Ari 0), "
                        "1×(Bree 5, Cash 1). With Ari's fans voting honestly, the scoring "
                        "round is Bree 25, Cash 21, Ari 20 — and the broad compromise Bree "
                        "beats Cash 5-4 in the runoff. The fans' honest 3s are exactly what "
                        "put their second choice on the podium. Part 2 (BV2194) reruns the "
                        "election after those four fans bullet vote, hoping to lift Ari — "
                        "and elects their nightmare. Side lesson the ranked races add: on "
                        "these same honest opinions RCV-IRV eliminates Bree (1 first "
                        "choice) and elects Cash — the compromise STAR finds, IRV can't "
                        "even see; Ranked Robin agrees with STAR (Bree is the Condorcet "
                        "winner). LH-verified."),
        "races": [
            {"title": "Speaker vote, honest — STAR (0-5 scores)", "method": "STAR",
             "num_winners": 1, "candidates": _E6_CANDS, "ballots": _E6_STAR_H},
            {"title": "Speaker vote, honest — RCV-IRV (Instant Runoff)", "method": "IRV",
             "num_winners": 1, "max_rankings": 3, "candidates": _E6_CANDS, "ballots": _E6_RANK_H},
            {"title": "Speaker vote, honest — Ranked Robin (Copeland)", "method": "RankedRobin",
             "num_winners": 1, "max_rankings": 3, "candidates": _E6_CANDS, "ballots": _E6_RANK_H},
        ],
        "enable_write_in": False,
        "expected": "STAR -> Bree (25/21/20; runoff 5-4 over Cash). IRV -> Cash (Bree "
                    "squeezed). RR -> Bree (Condorcet winner). Test ID BV2193.",
    },
    {
        "test_id": "BV2194",
        "title": "Bullet Voting Backfires (2 of 2) — the strategic ballots elect the nightmare",
        "description": (_EX_SRC +
                        "The strategy pair's payoff (exercise ex06): identical to BV2193 "
                        "except Ari's four fans now BULLET VOTE — Ari 5, Bree 0, Cash 0 — "
                        "hoping to drag Ari past the compromise. It works halfway: Bree "
                        "crashes 25 -> 13 and out of the runoff, and Ari (20) becomes a "
                        "finalist. But the runoff Ari inherits is against Cash (21), and "
                        "zeroing Bree never manufactured a single Ari-over-Cash preference: "
                        "Cash wins 5-4. The fans demoted their sure second choice and "
                        "elected their zero. Under honest ballots (BV2193) they had Bree; "
                        "the gamble bought Cash. The ranked races agree — with Bree's "
                        "support hidden, IRV and Ranked Robin elect Cash too. STAR's "
                        "runoff is exactly the feature that makes bullet voting a risk, "
                        "not a free lift. LH-verified."),
        "races": [
            {"title": "Speaker vote, bullet — STAR (0-5 scores)", "method": "STAR",
             "num_winners": 1, "candidates": _E6_CANDS, "ballots": _E6_STAR_S},
            {"title": "Speaker vote, bullet — RCV-IRV (Instant Runoff)", "method": "IRV",
             "num_winners": 1, "max_rankings": 3, "candidates": _E6_CANDS, "ballots": _E6_RANK_S},
            {"title": "Speaker vote, bullet — Ranked Robin (Copeland)", "method": "RankedRobin",
             "num_winners": 1, "max_rankings": 3, "candidates": _E6_CANDS, "ballots": _E6_RANK_S},
        ],
        "enable_write_in": False,
        "expected": "STAR -> Cash (21/20/13; runoff 5-4 over Ari) — the bullet gamble "
                    "backfires vs BV2193's Bree. IRV -> Cash. RR -> Cash. Test ID BV2194.",
    },
    {
        "test_id": "BV2195",
        "title": "Later-No-Harm (1 of 2) — the reticent ballots protect Amir",
        "description": (_EX_SRC +
                        "The later-no-harm pair, part 1 (exercise ex10): nine voters — "
                        "4×(Amir 5, nothing else), 2×(Bess 5, Amir 2), 3×(Cato 5, Bess 1). "
                        "With Amir's fans scoring nothing below their favorite, the scoring "
                        "round is Amir 24, Cato 15, Bess 13, and Amir wins the runoff 6-3 "
                        "over Cato. RCV-IRV agrees (Bess out first, Amir 6-3). Part 2 "
                        "(BV2196) has the same fans add an honest Bess 3 — and Bess wins "
                        "instead: the later-no-harm failure, live. (No Ranked Robin race "
                        "in this pair: converting the reticent ballots to ranks yields a "
                        "Condorcet cycle whose 3-way tie BetterVoting resolves at random — "
                        "not freezable. The repo's LH tabulation breaks it by margin.) "
                        "LH-verified."),
        "races": [
            {"title": "Reticent ballots — STAR (0-5 scores)", "method": "STAR",
             "num_winners": 1, "candidates": _E10_CANDS, "ballots": _E10_STAR_R},
            {"title": "Reticent ballots — RCV-IRV (Instant Runoff)", "method": "IRV",
             "num_winners": 1, "max_rankings": 3, "candidates": _E10_CANDS, "ballots": _E10_RANK_R},
        ],
        "enable_write_in": False,
        "expected": "STAR -> Amir (24/15/13; runoff 6-3 over Cato). IRV -> Amir. "
                    "Test ID BV2195.",
    },
    {
        "test_id": "BV2196",
        "title": "Later-No-Harm (2 of 2) — the generous ballots reveal Bess",
        "description": (_EX_SRC +
                        "The later-no-harm pair, part 2 (exercise ex10): identical to "
                        "BV2195 except Amir's four fans score honestly — Amir 5, Bess 3 — "
                        "they genuinely like Bess second. Those twelve points lift Bess 13 "
                        "-> 25: scoring round Bess 25, Amir 24, Cato 15, and Bess beats "
                        "Amir 5-4 in the runoff. Scoring a LATER choice harmed the "
                        "EARLIER one: a textbook later-no-harm failure, which STAR accepts "
                        "by design. The counter-reading is on the same ballots: Bess is "
                        "scored 1+ by all nine voters and is the honest Condorcet winner "
                        "(beats Amir 5-4, Cato 6-3) — the reticent zeros of BV2195 were "
                        "not protecting Amir so much as HIDING Bess. And the IRV race "
                        "shows the trade's other side: RCV-IRV still elects Amir here "
                        "(Bess, 2 first choices, is center-squeezed) — IRV keeps "
                        "later-no-harm precisely by never counting the preferences that "
                        "would break it. LH-verified."),
        "races": [
            {"title": "Generous ballots — STAR (0-5 scores)", "method": "STAR",
             "num_winners": 1, "candidates": _E10_CANDS, "ballots": _E10_STAR_G},
            {"title": "Generous ballots — RCV-IRV (Instant Runoff)", "method": "IRV",
             "num_winners": 1, "max_rankings": 3, "candidates": _E10_CANDS, "ballots": _E10_RANK_G},
        ],
        "enable_write_in": False,
        "expected": "STAR -> Bess (25/24/15; runoff 5-4 over Amir) — the LNH failure vs "
                    "BV2195's Amir. IRV -> Amir (keeps LNH by squeezing the Condorcet "
                    "winner Bess). Test ID BV2196.",
    },
    {
        "test_id": "BV2197",
        "title": "Recruit a Spoiler (1 of 2) — the two-way base race",
        "description": (_EX_SRC +
                        "The spoiler pair's base case (exercise ex11): a straight two-way "
                        "race, nine voters — Alba's camp of five (Alba 5, Brett 0), "
                        "Brett's camp of four (Brett 5, Alba 0). Alba wins under "
                        "Choose-One (5-4) and STAR (25-20; runoff 5-4) alike: with two "
                        "names, every reasonable method is majority rule. Part 2 (BV2198) "
                        "adds Axl — a near-clone of Alba recruited by Brett's campaign to "
                        "split her vote — and asks which counting rules fall for it. "
                        "LH-verified."),
        "races": [
            {"title": "Two-way race — Choose-One (Plurality)", "method": "Plurality",
             "num_winners": 1, "candidates": _E11_CANDS2, "ballots": _E11_PLUR_B},
            {"title": "Two-way race — STAR (0-5 scores)", "method": "STAR",
             "num_winners": 1, "candidates": _E11_CANDS2, "ballots": _E11_STAR_B},
        ],
        "enable_write_in": False,
        "expected": "Choose-One -> Alba (5-4). STAR -> Alba (25-20; runoff 5-4). "
                    "Test ID BV2197.",
    },
    {
        "test_id": "BV2198",
        "title": "Recruit a Spoiler (2 of 2) — the clone enters, and only Choose-One falls for it",
        "description": (_EX_SRC +
                        "The spoiler pair's payoff (exercise ex11): the same nine voters "
                        "as BV2197 plus Axl, a near-clone of Alba (recruited, in the "
                        "exercise's story, by Brett's campaign). Alba's five-voter camp "
                        "splits its first choices 3-2 across the clones but scores both "
                        "4-5; Brett's four are unchanged. Choose-One now elects BRETT "
                        "(4 first choices vs 3 and 2) — the attack works. STAR shrugs: "
                        "scoring round Alba 23, Axl 22, Brett 20 — the camp keeps BOTH "
                        "finalist slots and Alba wins the intramural runoff 3-2 (Brett's "
                        "voters score the clones 0-0: Equal Support). RCV-IRV also "
                        "survives: Axl is eliminated first and his ballots come home to "
                        "Alba, 5-4 — pure-clone crowding is the one spoiler variant IRV "
                        "genuinely handles, credit where due. Ranked Robin: Alba 2-0. "
                        "The dirty trick pays only under Choose-One — how much a spoiler "
                        "can extract is a property of the ballot design. LH-verified. "
                        "(Axl shares Alba's initial on purpose: they are clones.)"),
        "races": [
            {"title": "Clone added — Choose-One (Plurality)", "method": "Plurality",
             "num_winners": 1, "candidates": _E11_CANDS3, "ballots": _E11_PLUR_S},
            {"title": "Clone added — RCV-IRV (Instant Runoff)", "method": "IRV",
             "num_winners": 1, "max_rankings": 3, "candidates": _E11_CANDS3, "ballots": _E11_RANK_S},
            {"title": "Clone added — STAR (0-5 scores)", "method": "STAR",
             "num_winners": 1, "candidates": _E11_CANDS3, "ballots": _E11_STAR_S},
            {"title": "Clone added — Ranked Robin (Copeland)", "method": "RankedRobin",
             "num_winners": 1, "max_rankings": 3, "candidates": _E11_CANDS3, "ballots": _E11_RANK_S},
        ],
        "enable_write_in": False,
        "expected": "Choose-One -> Brett (4-3-2) — the spoiler works. IRV -> Alba "
                    "(Axl's transfers come home). STAR -> Alba (23/22/20; clones take "
                    "both finalist slots, runoff 3-2, 4 Equal Support). RR -> Alba (2-0). "
                    "Test ID BV2198.",
    },
]


# --- BV2199-2201 — the exercises' multi-winner wing + threshold dilemma ---------
# Already created 2026-07-17 -> 89wwvr (BV2199) / qdtqf2 (BV2200) / tk776t
# (BV2201); BV2202 probe -> bj8dfc. Reference only — do NOT re-run (permanent
# duplicates). FINDINGS: BV2199 both seat pairs agree (its STAR_PR banner
# says "Tied!" — systemic serializer quirk, elected pair echoed as tied, also
# on jwxr3j); BV2200 all four races agree; BV2201 AND BV2202 crash BV's STV
# tabulator (server errors a5f1af00/b70e18c6/8a75f8f6) while ywckmg/kcf8vf STV
# races compute — reproduction pair documented in ex14_transfer_machine.md.
# ex12 (Bloc vs Allocated), ex13 (approval thresholds), ex14 (STV). Two live
# probes ride along: BV2199's STAR_PR race tests whether BV's surplus handling
# matches LH's `allocated` (expected Asa+Cleo either way is NOT guaranteed —
# capture any divergence in the case page), and BV2201 tests BV's STV transfer
# flavor (seats Austen+Camus are robust to fractional vs whole-vote surplus).

_E12_CANDS = ["Asa", "Bram", "Cleo", "Dane"]
_E12_STAR = _expand([(6, [5, 4, 0, 0]), (4, [0, 0, 5, 4])])

_E13_CANDS = ["Ash", "Beck", "Cora"]
_E13_STAR = _expand([(3, [5, 4, 0]), (2, [0, 5, 3]), (4, [3, 0, 5])])
_E13_A3 = _expand([(3, [1, 1, 0]), (2, [0, 1, 1]), (4, [1, 0, 1])])
_E13_A4 = _expand([(3, [1, 1, 0]), (2, [0, 1, 0]), (4, [0, 0, 1])])
_E13_A5 = _expand([(3, [1, 0, 0]), (2, [0, 1, 0]), (4, [0, 0, 1])])

_E14_CANDS = ["Austen", "Bronte", "Camus", "Dickens"]
_E14_RANK = _expand([(5, [1, 2, 3, 4]), (1, [0, 1, 2, 0]), (3, [0, 0, 1, 2])])

_EX_TRIO_3 = [
    {
        "test_id": "BV2199",
        "title": "Two Seats, One Neighborhood — Bloc STAR sweeps, Allocated Score shares",
        "description": (_EX_SRC +
                        "The multi-winner exercise (ex12): a neighborhood association "
                        "elects a TWO-SEAT board from the same ten honest ballots, "
                        "counted two ways. Ten voters — 6 north-siders (Asa 5, Bram 4), "
                        "4 south-siders (Cleo 5, Dane 4). Race 1, Bloc STAR (STAR once "
                        "per seat): seat 1 Asa (30 points; runoff 6-0 with 4 Equal "
                        "Support), seat 2 Bram (runoff 6-4 over Cleo) — the 60% side "
                        "takes 100% of the board, majoritarian by design. Race 2, "
                        "STAR-PR / Allocated Score: Asa wins seat 1 and his six "
                        "strongest supporters are charged a 5-ballot quota (each keeps "
                        "1/6 weight), so round 2 reads Cleo 20, Dane 16, Bram 4 — Cleo "
                        "takes seat 2 and each side holds one seat, matching the 60/40 "
                        "room. Same ballots, two philosophies: ask what the body is FOR, "
                        "then pick the count. LH-verified (Bloc and allocated); the "
                        "STAR-PR race doubles as a live check that BetterVoting's "
                        "surplus handling agrees."),
        "races": [
            {"title": "Neighborhood board — Bloc STAR (2 seats)", "method": "STAR",
             "num_winners": 2, "candidates": _E12_CANDS, "ballots": _E12_STAR},
            {"title": "Neighborhood board — STAR-PR / Allocated Score (2 seats)", "method": "STAR_PR",
             "num_winners": 2, "candidates": _E12_CANDS, "ballots": _E12_STAR},
        ],
        "enable_write_in": False,
        "expected": "Bloc STAR -> Asa + Bram (the sweep). STAR_PR/Allocated -> Asa + "
                    "Cleo (one seat per side; LH round 2: Cleo 20 / Dane 16 / Bram 4). "
                    "Test ID BV2199.",
    },
    {
        "test_id": "BV2200",
        "title": "Where Do You Draw the Line? — one electorate, three approval thresholds",
        "description": (_EX_SRC +
                        "The approval-threshold exercise (ex13): nine voters' honest "
                        "0-5 opinions — 3×(Ash 5, Beck 4), 2×(Beck 5, Cora 3), "
                        "4×(Cora 5, Ash 3) — converted to Approval ballots under three "
                        "defensible readings, plus the full-resolution STAR count. "
                        "Approve 3+ (generous): Ash wins, 7 of 9. Approve 4+ "
                        "(stricter): Beck wins, 5 — the tolerances vanish and the "
                        "quietly high-graded middle survives. Favorites-only "
                        "(stingiest): Cora wins, 4 — Approval has become Choose-One in "
                        "a costume. STAR on the full scores: Ash 27 and Cora 26 "
                        "advance, Cora wins the runoff 6-3 (plain Score would say "
                        "Ash). One set of honest opinions, five defensible winners "
                        "across five readings — the Approval ballot outsources its "
                        "precision to the voter, and the threshold is a free parameter "
                        "the method never pins down. Pairwise the three candidates "
                        "form a Condorcet cycle, so even the head-to-head standard "
                        "shrugs. LH-verified, all four races."),
        "races": [
            {"title": "Draw the line — STAR (the honest 0-5 opinions)", "method": "STAR",
             "num_winners": 1, "candidates": _E13_CANDS, "ballots": _E13_STAR},
            {"title": "Draw the line — Approval, approve 3 and up", "method": "Approval",
             "num_winners": 1, "candidates": _E13_CANDS, "ballots": _E13_A3},
            {"title": "Draw the line — Approval, approve 4 and up", "method": "Approval",
             "num_winners": 1, "candidates": _E13_CANDS, "ballots": _E13_A4},
            {"title": "Draw the line — Approval, favorites only", "method": "Approval",
             "num_winners": 1, "candidates": _E13_CANDS, "ballots": _E13_A5},
        ],
        "enable_write_in": False,
        "expected": "STAR -> Cora (27/26/22; runoff 6-3). Approve 3+ -> Ash (7/6/5). "
                    "Approve 4+ -> Beck (5/4/3). Favorites only -> Cora (4/3/2 = "
                    "Choose-One). Test ID BV2200.",
    },
    {
        "test_id": "BV2201",
        "title": "The Transfer Machine — a book club buys two novels by STV",
        "description": (_EX_SRC +
                        "The STV drill (ex14): a nine-member book club buys TWO novels "
                        "by ranked ballot — 5×(Austen>Bronte>Camus>Dickens), "
                        "1×(Bronte>Camus), 3×(Camus>Dickens). Droop quota = "
                        "floor(9/3)+1 = 4. Round 1: Austen holds 5 first choices, is "
                        "elected, and her ONE surplus vote transfers to Bronte "
                        "(fractionally, five ballots at 1/5 each). Standings: Bronte "
                        "2, Camus 3, Dickens 0. Nobody reaches quota, so eliminations "
                        "run: Dickens (0), then Bronte (2) — whose pile, including the "
                        "fraction that arrived from Austen's surplus, moves on to "
                        "Camus: 3+2 = 5, elected. Seats: Austen + Camus — one seat per "
                        "~quota of voters, proportional to the room, where a Bloc-style "
                        "count would hand the Austen majority both seats. Follow one "
                        "Austen ballot: 4/5 of it elected Austen, the remaining 1/5 "
                        "rode through Bronte to elect Camus — 0 wasted. LH-verified "
                        "(seats robust to fractional vs whole-vote surplus handling)."),
        "races": [
            {"title": "Two novels — STV (2 seats)", "method": "STV",
             "num_winners": 2, "max_rankings": 4, "candidates": _E14_CANDS, "ballots": _E14_RANK},
        ],
        "enable_write_in": False,
        "expected": "STV -> Austen + Camus (quota 4; Austen round 1 with surplus 1 to "
                    "Bronte; Dickens then Bronte eliminated; Camus reaches 5). "
                    "Test ID BV2201.",
    },
]


# ── WHAT TO CREATE ─────────────────────────────────────────────────────────
# Point ELECTIONS at the spec(s) you want to create THIS run, then run the
# engine. Empty = create nothing (the safe resting state). You need NOT keep
# old specs here — every created election is recorded on BV + its saved export
# in 06_Other/_demo_dropbox/ + BV_registry.md. Example: ELECTIONS = [_ICE_CREAM]
# BV2202 — the fully-ranked variant of BV2201 (tk776t), whose truncated ballots
# crash BV's STV tabulator (ElectionResult returns a server error; the repo's
# fully-ranked STV race on ywckmg computes fine). The trailing rankings added
# here are never reached by any transfer, so quota, rounds, and seats are
# IDENTICAL to the exercise — this election is both the working live copy of
# ex14 and the isolating probe for the truncation bug.
_E14_RANK_FULL = _expand([(5, [1, 2, 3, 4]), (1, [3, 1, 2, 4]), (3, [4, 3, 1, 2])])

_EX14_FULL = [
    {
        "test_id": "BV2202",
        "title": "The Transfer Machine, fully ranked — a book club buys two novels by STV",
        "description": (_EX_SRC +
                        "The STV drill (ex14), fully-ranked variant: the same nine "
                        "voters as BV2201 (tk776t) with every ballot completed to a "
                        "full ranking — 5×(Austen>Bronte>Camus>Dickens), "
                        "1×(Bronte>Camus>Austen>Dickens), 3×(Camus>Dickens>Bronte>"
                        "Austen). The added trailing rankings are never reached by any "
                        "transfer, so the count is identical to the exercise: Droop "
                        "quota 4; Austen elected round 1 with a surplus of 1 that "
                        "transfers to Bronte; Dickens (0) then Bronte (2) eliminated; "
                        "Camus reaches 5 and takes the second seat. Seats: Austen + "
                        "Camus. This variant exists because BetterVoting's STV "
                        "tabulator errors on BV2201's TRUNCATED ballots (legal partial "
                        "rankings) while fully-ranked STV elections compute fine — the "
                        "pair isolates that bug. LH-verified."),
        "races": [
            {"title": "Two novels — STV (2 seats, fully ranked)", "method": "STV",
             "num_winners": 2, "max_rankings": 4, "candidates": _E14_CANDS, "ballots": _E14_RANK_FULL},
        ],
        "enable_write_in": False,
        "expected": "STV -> Austen + Camus (identical rounds to BV2201's design; the "
                    "trailing ranks are never reached). Test ID BV2202.",
    },
]

# BV2203 — the FLAG probe for the BV2201/2202 STV crash. The full config diff
# between the crashing pair (tk776t, bj8dfc) and the working STV races (ywckmg
# 1-seat, kcf8vf 3-seat) is down to ONE key: the crashers' race objects carry
# `enable_write_in: false`; every working STV race LACKS the key entirely
# (created before the script set it). This election is the ex14 ballots
# byte-for-byte with the key OMITTED (enable_write_in: None -> the create
# script now skips the key). One probe, two answers: if it COMPUTES, the flag
# is convicted and the 2-seat/4-candidate/9-voter shape is acquitted in the
# same stroke; if it CRASHES, the flag is acquitted and shape becomes the
# prime suspect (next probe: same flag-less race, different fill).
_EX14_PROBE_NOKEY = [
    {
        "test_id": "BV2203",
        "title": "The Transfer Machine, flag probe — same STV ballots, write-in key omitted",
        "description": (_EX_SRC +
                        "Bisection probe for a live BetterVoting STV bug: elections "
                        "tk776t (BV2201) and bj8dfc (BV2202) crash BV's STV tabulator "
                        "(ElectionResult returns a server error) while older STV races "
                        "(ywckmg, kcf8vf) compute fine. The complete config diff "
                        "between crashers and workers is a single key: the crashing "
                        "races carry enable_write_in: false, the working races lack "
                        "the key. This election repeats BV2201's nine ballots exactly "
                        "— 5x(Austen>Bronte>Camus>Dickens), 1x(Bronte>Camus), "
                        "3x(Camus>Dickens), 2 seats, Droop quota 4, LH-verified seats "
                        "Austen + Camus — with the enable_write_in key omitted from "
                        "the race object. If this computes, the flag is the trigger "
                        "and the 2-seat/4-candidate/9-voter shape is acquitted; if it "
                        "errors, the flag is acquitted."),
        "races": [
            {"title": "Two novels — STV (2 seats, write-in key omitted)", "method": "STV",
             "num_winners": 2, "max_rankings": 4, "candidates": _E14_CANDS, "ballots": _E14_RANK},
        ],
        "enable_write_in": None,
        "expected": "STV -> Austen + Camus IF the tabulator runs (quota 4; surplus 1 "
                    "to Bronte; Dickens then Bronte out; Camus 5). The probe's real "
                    "output is computes-vs-errors. Test ID BV2203.",
    },
]

# BV2203 result (2026-07-17): created -> gvtg2h, key confirmed ABSENT from the
# race object, STILL crashes (error cc9625bb) — enable_write_in ACQUITTED.
# Root cause then found by reading BV's IRV.ts (Equal-Vote/bettervoting,
# packages/backend/src/Tabulators/IRV.ts): when the LAST remaining hopeful
# reaches quota, the elect-branch shifts it out and redistributes its surplus
# via distributeVotes(remainingCandidates=[], ...), whose
# `remainingCandidates.reduce(...)` has NO initial value — [].reduce(f) throws
# TypeError. The under-quota sole survivor is rescued by the fill-remaining-
# seats shortcut (no redistribution); the AT-quota sole survivor crashes.
# BV2204/2205 below are the two confirming probes.

# BV2204 — the CONTROL: byte-level config identical to BV2201 (STV, 2 seats,
# 4 candidates, enable_write_in: false) but the count ends with two hopefuls
# still standing (both seats fill by quota, no candidate is ever eliminated):
# 13 voters, quota floor(13/3+1)=5. R1: Angelou 6 >= 5 elected; surplus 1
# (6 ballots x 1/6) -> Blake 1+1=2. R2: Cummings 5 >= 5 elected (zero surplus,
# redistributed over a NON-empty remainder) — done. Expected: COMPUTES.
_P24_CANDS = ["Angelou", "Blake", "Cummings", "Dickinson"]
_P24_RANK = _expand([(6, [1, 2, 0, 0]), (5, [0, 2, 1, 0]), (1, [0, 1, 0, 0]), (1, [0, 0, 0, 1])])

# BV2205 — the MINIMAL crasher: 1 seat, 3 candidates, 6 voters, every round
# deterministic (3>2>1, then 3>2 — no ties anywhere). Quota floor(6/2+1)=4.
# R1: Ash 3 / Birch 2 / Cedar 1 — nobody at quota, Cedar out (exhausts).
# R2: Ash 3 / Birch 2 — Birch out, both ballots transfer to Ash. R3: Ash 5 is
# the SOLE remaining hopeful at/above quota -> elect-branch -> surplus
# redistribution over an empty candidate list -> [].reduce throws. Expected:
# ERRORS — and proves single-seat STV is affected too, not just multi-seat.
_P25_CANDS = ["Ash", "Birch", "Cedar"]
_P25_RANK = _expand([(3, [1, 0, 0]), (2, [2, 1, 0]), (1, [0, 0, 1])])

_STV_ENDGAME_PROBES = [
    {
        "test_id": "BV2204",
        "title": "The Transfer Machine, control — an STV finish with hopefuls still standing",
        "description": (_EX_SRC +
                        "Control probe for the BetterVoting STV sole-survivor crash "
                        "(see tk776t/BV2201, bj8dfc/BV2202, gvtg2h/BV2203). Config is "
                        "identical to the crashing BV2201 — STV, 2 seats, 4 "
                        "candidates, write-ins off — but these 13 ballots fill both "
                        "seats by quota while two hopefuls still stand, so no "
                        "candidate is ever eliminated: 6x(Angelou>Blake), "
                        "5x(Cummings>Blake), 1x(Blake), 1x(Dickinson); Droop quota 5; "
                        "Angelou elected round 1 (surplus 1 to Blake), Cummings "
                        "elected round 2. If this computes while gvtg2h errors, the "
                        "endgame — electing the LAST remaining hopeful at quota, "
                        "whose surplus then redistributes over an empty candidate "
                        "list ([].reduce with no initial value in IRV.ts "
                        "distributeVotes) — is confirmed as the trigger, and the "
                        "2-seat/4-candidate shape is acquitted. LH-verified seats: "
                        "Angelou + Cummings."),
        "races": [
            {"title": "Poets on the shelf — STV (2 seats, control)", "method": "STV",
             "num_winners": 2, "max_rankings": 4, "candidates": _P24_CANDS, "ballots": _P24_RANK},
        ],
        "enable_write_in": False,
        "expected": "COMPUTES: STV -> Angelou + Cummings (quota 5; no eliminations; "
                    "two hopefuls still standing at the end). Test ID BV2204.",
    },
    {
        "test_id": "BV2205",
        "title": "The sole-survivor STV finish — six voters, one seat, a tabulator edge case",
        "description": (_EX_SRC +
                        "Minimal reproduction of the BetterVoting STV sole-survivor "
                        "crash: 1 seat, 3 candidates, 6 fully deterministic ballots — "
                        "3x(Ash), 2x(Birch>Ash), 1x(Cedar). Droop quota 4. Round 1: "
                        "Ash 3 / Birch 2 / Cedar 1, nobody at quota, Cedar eliminated "
                        "(ballot exhausts). Round 2: Birch eliminated, both ballots "
                        "transfer to Ash. Round 3: Ash, now the ONLY remaining "
                        "candidate, holds 5 >= 4 — the elect-branch removes him and "
                        "redistributes his surplus over an EMPTY candidate list, and "
                        "distributeVotes' remainingCandidates.reduce(...) has no "
                        "initial value, so [].reduce throws (IRV.ts, "
                        "packages/backend/src/Tabulators). Expected here: the results "
                        "page errors until the bug is fixed; any STV engine elects "
                        "Ash. Proves the crash needs neither multi-seat, nor "
                        "truncation-exhaustion mid-transfer, nor the write-in flag — "
                        "only an endgame where eliminations leave one hopeful who "
                        "then reaches quota. LH-verified winner: Ash."),
        "races": [
            {"title": "One seat, three trees — STV (sole-survivor finish)", "method": "STV",
             "num_winners": 1, "max_rankings": 3, "candidates": _P25_CANDS, "ballots": _P25_RANK},
        ],
        "enable_write_in": False,
        "expected": "ERRORS on BV (sole-survivor elect-branch). Any working STV "
                    "engine: Ash (quota 4; Cedar then Birch out; Ash 5). "
                    "Test ID BV2205.",
    },
]

# RESULTS (2026-07-17): BV2204 -> 39py93, COMPUTES (Angelou + Cummings, agrees
# with LH — shape acquitted, endgame convicted). BV2205 -> 8xwx43, ERRORS
# (13617b56) — minimal 1-seat sole-survivor crasher confirmed. Bisection
# CLOSED; case folder: 06_Other/STV/bv_stv_sole_survivor_crash/ (evidence
# table + ready-to-file issue). Do NOT re-run these specs (permanent dupes).

# --- BV2206-2207 — favorite betrayal in STAR, the worked pair -----------------
# The rare construction favorite_betrayal_voting_301.md describes but never
# shows: STAR's FBC leak lives in the runoff (scores pick the FINALISTS), and
# here the leak is real. 57 voters, cast Aster/Bluebell/Clover:
#   9x (Aster 5, Bluebell 5)   the betrayers-to-be: true pref Aster>Bluebell>Clover,
#                              already equal-topping Bluebell — NO room to raise her
#   6x (Aster 5)               Aster-only fans
#  24x (Bluebell 1)            the tepid consensus: broad, feeble Bluebell support
#  18x (Clover 4)              the Clover bloc
# Bluebell is the CONDORCET winner (beats Aster 24-6, Clover 33-18) but scores
# 3rd (75/72/69) — honest runoff Aster-vs-Clover, Clover wins 18-15. If the 9
# demote Aster 5->4 (below Bluebell — the betrayal), Aster falls to 66, the
# runoff becomes Clover-vs-Bluebell, and Bluebell wins it 33-18. Outcome for
# the 9: Clover (their 0) -> Bluebell (their 5). Equal-top could NOT save them
# (Bluebell already at 5); only strict demotion works. Knife-edge: it takes
# >=7 of the 9 coordinating (6 ties Aster with Bluebell at 69; <=5 changes
# nothing) — the fragility the 301 page claims, demonstrated by construction.
_FBC_CANDS = ["Aster", "Bluebell", "Clover"]
_FBC_HONEST = _expand([(9, [5, 5, 0]), (6, [5, 0, 0]), (24, [0, 1, 0]), (18, [0, 0, 4])])
_FBC_BETRAY = _expand([(9, [4, 5, 0]), (6, [5, 0, 0]), (24, [0, 1, 0]), (18, [0, 0, 4])])

_FBC_SRC = ("From the STAR education repo (github.com/masiarek/star-voting-library, "
            "01_STAR/03_Criteria/favorite_betrayal/) — the worked favorite-betrayal pair behind "
            "favorite_betrayal_voting_301.md. ")

_FBC_PAIR = [
    {
        "test_id": "BV2206",
        "title": "Favorite betrayal in STAR, 1 of 2 — honest ballots: the tepid consensus misses the runoff",
        "description": (_FBC_SRC +
                        "Honest ballots. 57 voters: 9x(Aster 5, Bluebell 5), "
                        "6x(Aster 5), 24x(Bluebell 1), 18x(Clover 4). Bluebell is the "
                        "Condorcet winner — beats Aster 24-6 and Clover 33-18 head-to-"
                        "head — but her support is broad and TEPID (twenty-four 1s), "
                        "so the score round reads Aster 75, Clover 72, Bluebell 69 and "
                        "she misses the runoff by three points. Aster-vs-Clover goes to "
                        "Clover 18-15 (24 Equal Support). STAR elects Clover; the "
                        "compromise everyone prefers is standing outside the door. The "
                        "companion election (2 of 2) shows the nine Aster-fans fixing "
                        "this by DEMOTING their favorite — the favorite-betrayal "
                        "construction STAR's runoff makes possible in rare, knife-edge "
                        "electorates. LH-verified."),
        "races": [
            {"title": "Town flower — STAR (honest ballots)", "method": "STAR",
             "num_winners": 1, "candidates": _FBC_CANDS, "ballots": _FBC_HONEST},
        ],
        "enable_write_in": False,
        "expected": "STAR -> Clover (scores 75/72/69; runoff Clover 18 - Aster 15, "
                    "ES 24). Bluebell is the un-elected Condorcet winner. "
                    "Test ID BV2206.",
    },
    {
        "test_id": "BV2207",
        "title": "Favorite betrayal in STAR, 2 of 2 — nine voters demote their favorite and it pays",
        "description": (_FBC_SRC +
                        "The betrayal. Same 57 voters as election 1 of 2, except the "
                        "nine Aster-fans now score Aster 4 instead of 5 — strictly "
                        "below Bluebell on their own ballots. They could NOT fix the "
                        "result by raising Bluebell (she was already at 5 — equal-top "
                        "was free and insufficient); the only move left was demoting "
                        "their true favorite. Scores become Clover 72, Bluebell 69, "
                        "Aster 66: the runoff is now Clover-vs-Bluebell, and the "
                        "Condorcet winner Bluebell takes it 33-18. The nine turned "
                        "their outcome from Clover (their 0) into Bluebell (their 5) "
                        "by betraying Aster — a real STAR favorite-betrayal failure, "
                        "of the fragile kind: it needs at least 7 of the 9 to "
                        "coordinate (6 betrayers tie Aster and Bluebell at 69; 5 or "
                        "fewer changes nothing), near-perfect knowledge of the "
                        "standings, and a 3-point knife-edge. LH-verified."),
        "races": [
            {"title": "Town flower — STAR (nine betray their favorite)", "method": "STAR",
             "num_winners": 1, "candidates": _FBC_CANDS, "ballots": _FBC_BETRAY},
        ],
        "enable_write_in": False,
        "expected": "STAR -> Bluebell (scores 72/69/66; runoff Bluebell 33 - Clover "
                    "18, ES 6). Test ID BV2207.",
    },
]

# RESULTS (2026-07-17): BV2206 -> 7mckyg (Clover), BV2207 -> b6xrdr (Bluebell)
# — BV agrees with LH on both halves, no tiebreaks. Case folder:
# 01_STAR/03_Criteria/favorite_betrayal/. Do NOT re-run (permanent dupes).

# --- BV2208-2209 — burial in Ranked Robin, the worked pair --------------------
# The classic anti-Condorcet strategy nobody in the repo demonstrates yet:
# rank the frontrunner LAST, manufacture a cycle, win on the record. 42
# voters, cast Amber/Beryl/Coral/Diamond:
#   15x Amber>Beryl>Coral>Diamond   (the buriers-to-be; true 2nd = Beryl)
#   12x Beryl>Amber>Diamond>Coral
#    9x Coral>Diamond>Beryl>Amber
#    6x Diamond>Beryl>Coral>Amber
# Sincere: Beryl is the Condorcet winner (27-15 over Amber, 33-9 Coral,
# 27-15 Diamond) — record 3-0, clean. Burial: the 15 switch to
# Amber>Coral>Diamond>Beryl (Beryl LAST). Beryl's slim wins over Coral and
# Diamond flip (24-18 Coral, 30-12 Diamond); her big win over Amber survives.
# Records: Amber 2-1, Coral 2-1, Beryl 1-2, Diamond 1-2 — a cycle with a
# 2-way top tie that AMBER takes on every metric: LH total margin (+12 vs 0),
# BV head-to-head (27-15), pref_voting Copeland-leader set {Amber, Coral}.
# Deterministic on both engines -> freezable despite the LH/BV tiebreak
# difference. Triple-checked (LH native, pref_voting Copeland; BV = this).
_RRB_CANDS = ["Amber", "Beryl", "Coral", "Diamond"]
_RRB_SINCERE = _expand([(15, [1, 2, 3, 4]), (12, [2, 1, 4, 3]), (9, [4, 3, 1, 2]), (6, [4, 2, 3, 1])])
_RRB_BURIED = _expand([(15, [1, 4, 2, 3]), (12, [2, 1, 4, 3]), (9, [4, 3, 1, 2]), (6, [4, 2, 3, 1])])

_RRB_SRC = ("From the STAR education repo (github.com/masiarek/star-voting-library, "
            "05_Ranked_Robin/03_Criteria/burial/) — the worked burial pair: Ranked Robin's "
            "signature strategic wart, shown honestly. ")

_RR_BURIAL_PAIR = [
    {
        "test_id": "BV2208",
        "title": "Burial in Ranked Robin, 1 of 2 — sincere ballots: Beryl beats everyone",
        "description": (_RRB_SRC +
                        "Sincere ballots. A design club of 42 ranks four gemstones. "
                        "Beryl is the Condorcet winner: 27-15 over Amber, 33-9 over "
                        "Coral, 27-15 over Diamond — a clean 3-0 record; Amber runs "
                        "second at 2-1. No cycle, no tie, nothing to break. The "
                        "companion election (2 of 2) shows what happens when the 15 "
                        "Amber-first voters bury Beryl — rank her LAST below "
                        "candidates they honestly like less — and flip the two wins "
                        "she holds by slim margins. LH-verified; pref_voting Copeland "
                        "agrees (unique winner)."),
        "races": [
            {"title": "Gem of the year — Ranked Robin (sincere)", "method": "RankedRobin",
             "num_winners": 1, "max_rankings": 4, "candidates": _RRB_CANDS, "ballots": _RRB_SINCERE},
        ],
        "enable_write_in": False,
        "expected": "RankedRobin -> Beryl (3-0; Condorcet winner). Test ID BV2208.",
    },
    {
        "test_id": "BV2209",
        "title": "Burial in Ranked Robin, 2 of 2 — fifteen voters rank the leader last, and it pays",
        "description": (_RRB_SRC +
                        "The burial. Same 42 voters as election 1 of 2, except the 15 "
                        "Amber-first voters now rank Amber>Coral>Diamond>Beryl — "
                        "burying Beryl, their honest SECOND choice, below two "
                        "candidates they like less. Beryl's slim sincere wins flip "
                        "(Coral now beats her 24-18, Diamond 30-12) while her big win "
                        "over Amber survives (27-15). The round-robin becomes a cycle "
                        "with Amber and Coral tied on top at 2-1 — and Amber takes "
                        "the tiebreak on every metric: total pairwise margin +12 vs "
                        "0 (the LH engine's rule), the direct head-to-head 27-15 "
                        "(BetterVoting's rule), first choices 15 vs 9. The buriers "
                        "turned Beryl's win into Amber's. Burial is Condorcet "
                        "methods' structural wart the way center squeeze is IRV's — "
                        "and this pair is deliberately knife-edged: in election 1 the "
                        "same move would need to flip a 33-9 blowout, which no "
                        "faction can. LH-verified; pref_voting Copeland-leader set "
                        "{Amber, Coral} contains the winner."),
        "races": [
            {"title": "Gem of the year — Ranked Robin (Beryl buried)", "method": "RankedRobin",
             "num_winners": 1, "max_rankings": 4, "candidates": _RRB_CANDS, "ballots": _RRB_BURIED},
        ],
        "enable_write_in": False,
        "expected": "RankedRobin -> Amber (2-1, margin +12; cycle after the burial; "
                    "BV breaks the 2-way tie by head-to-head Amber 27-15 Coral). "
                    "Test ID BV2209.",
    },
]

# RESULTS (2026-07-17): BV2208 -> 7q6by8 (Beryl), BV2209 -> fxhw6g (Amber) —
# unanimous triple-check (LH, pref_voting, BV), tieBreakType none on both.
# Case folder: 05_Ranked_Robin/03_Criteria/burial/. ERRATUM: the live descriptions'
# slim-vs-blowout aside mislabels which wins flip (the buriers sit inside
# Beryl's 33-9 Coral win and 27-15 Diamond win — those flip; her 27-15 Amber
# win holds); the repo yamls/README carry the corrected analysis. Do NOT
# re-run (permanent dupes).

# --- BV2210 — Food-Truck Row: the vote-splitting showcase ---------------------
# One 100-voter electorate, five counts, three different parliaments. Two
# spots on the food-truck row. The SAVORY side is a 57-voter outright
# majority split across three trucks (Arepa 20, Bao 19, Churro 18); the
# SWEET side is a disciplined 43-voter minority on two (Donut 22, Eclair 21).
#   SNTV (choose one, top-2):   Donut + Eclair — the MAJORITY gets ZERO seats
#   Bloc STAR (2 seats):        Arepa + Bao    — the majority SWEEPS both
#   Bloc Ranked Robin (2):      Arepa + Bao    — ranked ballots sweep too
#   STAR-PR / Allocated (2):    Arepa + Donut  — one per side
#   STV (2):                    Arepa + Donut  — one per side
# The LH `blocs:` vote-splitting check fires on the Bloc STAR yaml: "the
# 'Savory' bloc is an outright majority (57 vs Donut's 22) but split across
# 3 candidates, so Donut won Choose-One." All five LH-verified; every rung
# distinct (counts 22/21/20/19/18; no ties anywhere). The STV race ends with
# a hopeful still standing — clear of the BV2201-2205 sole-survivor crash.
_FT_CANDS = ["Arepa", "Bao", "Churro", "Donut", "Eclair"]
_FT_SNTV = _expand([(20, [1, 0, 0, 0, 0]), (19, [0, 1, 0, 0, 0]), (18, [0, 0, 1, 0, 0]),
                    (22, [0, 0, 0, 1, 0]), (21, [0, 0, 0, 0, 1])])
_FT_STAR = _expand([(20, [5, 4, 3, 0, 0]), (19, [4, 5, 3, 0, 0]), (18, [4, 3, 5, 0, 0]),
                    (22, [0, 0, 0, 5, 4]), (21, [0, 0, 0, 4, 5])])
_FT_RANK = _expand([(20, [1, 2, 3, 0, 0]), (19, [2, 1, 3, 0, 0]), (18, [2, 3, 1, 0, 0]),
                    (22, [0, 0, 0, 1, 2]), (21, [0, 0, 0, 2, 1])])

_FOOD_TRUCK = [
    {
        "test_id": "BV2210",
        "title": "Food-Truck Row — two spots, five counts: vote-splitting, sweeps, and shares",
        "description": (
            "From the STAR education repo (github.com/masiarek/star-voting-library, "
            "method_comparisons/food_truck_row/) — the vote-splitting showcase. One "
            "100-voter electorate elects TWO food-truck spots five ways. The savory "
            "side is a 57-voter outright majority split across three trucks (Arepa "
            "20 first choices, Bao 19, Churro 18); the sweet side is a disciplined "
            "43-voter minority on two (Donut 22, Eclair 21). SNTV (choose one, "
            "top-2): Donut + Eclair — the 57% majority gets ZERO seats because it "
            "split its one vote three ways; this is the classic SNTV failure that "
            "punishes running too many candidates. Bloc STAR and Bloc Ranked Robin "
            "(2 seats each): Arepa + Bao — the same majority now SWEEPS both seats; "
            "majoritarian multi-winner counts hand 100% of the seats to 57% of the "
            "room. STAR-PR / Allocated Score and STV (2 seats each): Arepa + Donut "
            "— one seat per side, proportional to the room. Same opinions on every "
            "ballot; only the counting rule changes. Savory ballots score/rank only "
            "savory trucks (5/4/3 by taste), sweet ballots only sweet (5/4) — "
            "cross-side abstentions are Equal Support. LH-verified on all five "
            "counts, every rung distinct (22/21/20/19/18), no tie-breaks anywhere."),
        "races": [
            {"title": "Two spots — SNTV (choose one truck)", "method": "Plurality",
             "num_winners": 2, "candidates": _FT_CANDS, "ballots": _FT_SNTV},
            {"title": "Two spots — Bloc STAR", "method": "STAR",
             "num_winners": 2, "candidates": _FT_CANDS, "ballots": _FT_STAR},
            {"title": "Two spots — Bloc Ranked Robin", "method": "RankedRobin",
             "num_winners": 2, "max_rankings": 5, "candidates": _FT_CANDS, "ballots": _FT_RANK},
            {"title": "Two spots — STAR-PR / Allocated Score", "method": "STAR_PR",
             "num_winners": 2, "candidates": _FT_CANDS, "ballots": _FT_STAR},
            {"title": "Two spots — STV", "method": "STV",
             "num_winners": 2, "max_rankings": 5, "candidates": _FT_CANDS, "ballots": _FT_RANK},
        ],
        "enable_write_in": False,
        "expected": "SNTV -> Donut + Eclair. Bloc STAR -> Arepa + Bao. Bloc RR -> "
                    "Arepa + Bao. STAR_PR -> Arepa + Donut (LH allocated; capture "
                    "any BV divergence). STV -> Arepa + Donut. Test ID BV2210.",
    },
]

# RESULTS (2026-07-17): BV2210 -> fvg8y8 — ALL FIVE races agree with LH
# (SNTV Donut+Eclair / Bloc STAR Arepa+Bao / Bloc RR Arepa+Bao / STAR_PR
# Arepa+Donut / STV Arepa+Donut), no genuine tie anywhere. BONUS: the
# STAR_PR race reports tieBreakType 'random' with no tie — the THIRD
# confirming instance of the STAR_PR 'Tied!' serializer quirk (89wwvr,
# jwxr3j, now fvg8y8). Case folder: method_comparisons/food_truck_row/.
# Do NOT re-run (permanent dupes).

# --- BV2212 — STAR IIA under a Condorcet cycle (cycle-spoiler; STAR single-winner) -
# Backs a STAR honest-limits case: three rotating factions, no Condorcet winner.
# STAR elects Alice; dropping the losing finalist Ben flips the winner to Carla with
# no score changed — an IIA failure in the runoff STAGE (Excellent_Air8235, r/EndFPTP,
# 2026-07). STAR-only on BV: RR here is a Copeland 3-way tie (LH breaks by margin ->
# Alice; BV breaks randomly) so RR is unfreezable, like BV830.
_CYCLE_CANDS = ["Alice", "Ben", "Carla"]
_CYCLE_STAR = _expand([(10, [5, 3, 0]), (6, [0, 5, 3]), (7, [3, 0, 5])])

_STAR_IIA_CYCLE = [
    {
        "test_id": "BV2212",
        "title": "STAR IIA under a Condorcet cycle — a losing candidate flips Alice vs Carla",
        "description": (
            "From the STAR education repo (github.com/masiarek/star-voting-library) — "
            "STAR's sharpest honest limit, made mechanical. 23 voters, three rotating "
            "factions voting sincerely (favorite 5, compromise 3, last 0). Head-to-head "
            "is a Condorcet CYCLE: Alice>Ben, Ben>Carla, Carla>Alice — no Condorcet "
            "winner. Score round: Alice 71, Ben 60, Carla 53, so the finalists are Alice "
            "and Ben, and Alice wins the runoff. But drop Ben — who never wins — and the "
            "finalists become Alice and Carla, whose runoff Carla wins: a losing "
            "candidate decided Alice vs Carla with not one score changed, an "
            "Independence-of-Irrelevant-Alternatives failure in the runoff stage. Bonus "
            "divergence: STAR->Alice, RCV-IRV->Carla, Ranked Robin->Alice (Copeland "
            "3-way tie broken by margin). LH-verified."),
        "method": "STAR",
        "num_winners": 1,
        "candidates": _CYCLE_CANDS,
        "ballots": _CYCLE_STAR,
        "enable_write_in": False,
        "expected": "STAR -> Alice (finalists Alice 71 & Ben 60; runoff Alice beats "
                    "Ben). Drop Ben -> Carla wins (IIA failure). No Condorcet winner "
                    "(cycle). Test ID BV2212.",
    },
]

# RESULTS (2026-07-18): BV2212 -> g3f7r2 — created + 23/23 ballots cast OK.
# STAR -> Alice (expected). Backs a STAR honest-limits cycle-spoiler case; RR
# unfreezable (Copeland 3-way tie). Do NOT re-run (permanent dupes).
# --- BV2213 — Alaska 2022 US House special (reduced 200-voter teaching model) -----
# One real electorate, four counts. A faithful ~943:1 scaling of Table 1 in
# Graham-Squire & McCune, "An Examination of Ranked Choice Voting in the US,
# 2004-2022" (arXiv:2301.12075) — every one of the 9 ballot types matches the
# paper. Plurality & RCV-IRV elect Peltola (Begich has fewest first choices, is
# eliminated, 12 ballots exhaust, Peltola beats Palin 96-92); STAR & Ranked Robin
# elect Begich, the Condorcet winner IRV cut (Begich beats Peltola 93-84 and Palin
# 107-68). RR is deterministic (clear Condorcet winner, no tie) so it is freezable.
_AK_CANDS = ["Peltola", "Begich", "Palin"]
# 9 blocs (count, [Peltola, Begich, Palin]); same voter order across every race.
_AK_STAR = _expand([(25,[5,0,0]),(50,[5,4,0]),(5,[5,0,4]),(12,[0,5,0]),(16,[4,5,0]),
                    (29,[0,5,4]),(23,[0,0,5]),(4,[4,3,5]),(36,[0,4,5])])
_AK_PLUR = _expand([(25,[1,0,0]),(50,[1,0,0]),(5,[1,0,0]),(12,[0,1,0]),(16,[0,1,0]),
                    (29,[0,1,0]),(23,[0,0,1]),(4,[0,0,1]),(36,[0,0,1])])
_AK_RANK = _expand([(25,[1,0,0]),(50,[1,2,3]),(5,[1,3,2]),(12,[0,1,0]),(16,[2,1,3]),
                    (29,[3,1,2]),(23,[0,0,1]),(4,[2,3,1]),(36,[3,2,1])])

_ALASKA = [
    {
        "test_id": "BV2213",
        "title": ("Alaska 2022 special, scaled model: STAR & Ranked Robin elect the "
                  "Condorcet winner IRV cut"),
        "description": (
            "A reduced 200-voter TEACHING MODEL of the August 2022 Alaska US House "
            "special election (Peltola / Begich / Palin) — NOT the real vote data, but "
            "a faithful ~943:1 scaling of the official preference profile (Table 1 of "
            "Graham-Squire & McCune, arXiv:2301.12075); all 9 ballot types match. One "
            "electorate, four counts. First choices: Peltola 80, Palin 63, Begich 57 — "
            "so Choose-One (Plurality) elects Peltola. RCV-IRV eliminates Begich (fewest "
            "first choices), 12 ballots exhaust, and Peltola beats Palin 96-92 — also "
            "Peltola. But Begich is the Condorcet winner (beats Peltola 93-84 and Palin "
            "107-68), so Ranked Robin and STAR both elect Begich — the broadly-preferred "
            "candidate IRV's first-choice elimination threw out (the center squeeze). "
            "Same ballots, four counts, two winners. Companion: Equal Vote's Real RCV "
            "tool (realrcv.equal.vote/alaska22) and the LH education repo "
            "(github.com/masiarek/star-voting-library)."),
        "races": [
            {"title": "Choose-One (Plurality) — first choices only", "method": "Plurality",
             "num_winners": 1, "candidates": _AK_CANDS, "ballots": _AK_PLUR},
            {"title": "RCV-IRV (Hare) — instant runoff by elimination", "method": "IRV",
             "num_winners": 1, "max_rankings": 3, "candidates": _AK_CANDS, "ballots": _AK_RANK},
            {"title": "Ranked Robin (Condorcet) — head-to-head wins", "method": "RankedRobin",
             "num_winners": 1, "max_rankings": 3, "candidates": _AK_CANDS, "ballots": _AK_RANK},
            {"title": "STAR — score then automatic runoff", "method": "STAR",
             "num_winners": 1, "candidates": _AK_CANDS, "ballots": _AK_STAR},
        ],
        "enable_write_in": False,
        "expected": "Plurality -> Peltola (80). RCV-IRV -> Peltola (Begich out, 12 "
                    "exhaust, Peltola 96-92 Palin). Ranked Robin -> Begich (Condorcet). "
                    "STAR -> Begich (finalists Begich 641 & Peltola 480; Begich 93-84). "
                    "Test ID BV2213.",
    },
]

# RESULTS (2026-07-18): BV2212 -> g3f7r2 — created + 23/23 ballots cast OK.
# STAR -> Alice (expected). Backs a STAR honest-limits cycle-spoiler case; RR
# unfreezable (Copeland 3-way tie). Do NOT re-run (permanent dupes).
# RESULTS (2026-07-19): BV2213 -> k3fmwv — created + 200/200 ballots × 4 races OK.
# Backs method_comparisons/alaska_2022 (one electorate, four counts). Plurality &
# IRV -> Peltola; Ranked Robin & STAR -> Begich (Condorcet winner). RR freezable
# (clear CW, no tie). Do NOT re-run (permanent dupes).
# --- BV2214 — Alaska 2022 GENERAL (reduced 200-voter model): IRV got it right ----
# The happy-ending counterpart to BV2213 (the special). Same three candidates,
# November general — a competitive 4-way (Bye eliminated first; here modeled on the
# top 3 as Equal Vote's realrcv does). Reconstructed from realrcv.equal.vote/
# alaska22general's own 200-dot model and cross-checked to its stated results:
# first choices Peltola 98 / Palin 52 / Begich 50; IRV eliminates Begich, Peltola
# wins 104-85 (11 exhaust); Peltola beats BOTH head-to-head (101-82, 104-85) => the
# Condorcet winner. So all four counts elect Peltola — IRV included. RR deterministic
# (clear Condorcet winner) => freezable.
_AKG_CANDS = ["Peltola", "Begich", "Palin"]
_AKG_STAR = _expand([(50,[5,0,0]),(42,[5,4,0]),(6,[5,0,4]),(11,[0,5,0]),(33,[0,5,4]),
                     (6,[4,5,0]),(17,[0,0,5]),(32,[0,4,5]),(3,[4,0,5])])
_AKG_PLUR = _expand([(50,[1,0,0]),(42,[1,0,0]),(6,[1,0,0]),(11,[0,1,0]),(33,[0,1,0]),
                     (6,[0,1,0]),(17,[0,0,1]),(32,[0,0,1]),(3,[0,0,1])])
_AKG_RANK = _expand([(50,[1,0,0]),(42,[1,2,0]),(6,[1,0,2]),(11,[0,1,0]),(33,[0,1,2]),
                     (6,[2,1,0]),(17,[0,0,1]),(32,[0,2,1]),(3,[2,0,1])])

_ALASKA_GENERAL = [
    {
        "test_id": "BV2214",
        "title": ("Alaska 2022 GENERAL (reduced model) — IRV got it right: all four "
                  "counts elect the Condorcet winner, Peltola"),
        "description": (
            "The happy-ending counterpart to the August special (BV2213). A reduced "
            "200-voter TEACHING MODEL of the November 2022 Alaska US House GENERAL "
            "election (same three candidates; the 4th, Bye, was eliminated first and is "
            "dropped, as Equal Vote's realrcv.equal.vote/alaska22general does) — NOT the "
            "real vote data, reconstructed from realrcv's own 200-dot model and matched "
            "to its stated results. First choices: Peltola 98, Palin 52, Begich 50. "
            "RCV-IRV eliminates Begich, 11 ballots exhaust, and Peltola beats Palin "
            "104-85. This time the electorate had shifted and Peltola is the Condorcet "
            "winner (beats Begich 101-82 and Palin 104-85), so ALL FOUR counts elect "
            "her — Plurality, RCV-IRV, Ranked Robin, and STAR. IRV got it right. The "
            "contrast with the special (where IRV cut the Condorcet winner Begich) is "
            "the whole lesson: IRV's center-squeeze failure is real but conditional. "
            "Companion: github.com/masiarek/star-voting-library."),
        "races": [
            {"title": "Choose-One (Plurality) — first choices only", "method": "Plurality",
             "num_winners": 1, "candidates": _AKG_CANDS, "ballots": _AKG_PLUR},
            {"title": "RCV-IRV (Hare) — instant runoff by elimination", "method": "IRV",
             "num_winners": 1, "max_rankings": 3, "candidates": _AKG_CANDS, "ballots": _AKG_RANK},
            {"title": "Ranked Robin (Condorcet) — head-to-head wins", "method": "RankedRobin",
             "num_winners": 1, "max_rankings": 3, "candidates": _AKG_CANDS, "ballots": _AKG_RANK},
            {"title": "STAR — score then automatic runoff", "method": "STAR",
             "num_winners": 1, "candidates": _AKG_CANDS, "ballots": _AKG_STAR},
        ],
        "enable_write_in": False,
        "expected": "All four -> Peltola (the Condorcet winner). Plurality 98; IRV "
                    "Peltola 104-85 (Begich out, 11 exhaust); RR Peltola (beats both); "
                    "STAR Peltola (Begich leads scores 546, Peltola wins runoff "
                    "101-82). Test ID BV2214.",
    },
]

# RESULTS (2026-07-19): BV2213 -> k3fmwv — created + 200/200 ballots × 4 races OK.
# Backs method_comparisons/alaska_2022 (one electorate, four counts). Plurality &
# IRV -> Peltola; Ranked Robin & STAR -> Begich (Condorcet winner). RR freezable
# (clear CW, no tie). Do NOT re-run (permanent dupes).
# RESULTS (2026-07-19): BV2214 -> m3hb6y — created + 200/200 ballots × 4 races OK.
# Backs method_comparisons/alaska_2022_general (the "IRV got it right" counterpart).
# All four counts -> Peltola (Condorcet winner). RR freezable. Do NOT re-run.
# --- BV2215 — Minority winner: 34% wins Choose-One; STAR & RR find the consensus --
# The canonical minority/plurality-winner example. 100 voters, 3 candidates. Ada has
# a devoted third (34 first choices) and wins Choose-One on 34% while 66% rate her
# <=1; Cleo is everyone's warm 4-or-5, the Condorcet winner (beats both head-to-head),
# and STAR + Ranked Robin both elect her. IRV deliberately omitted (Cleo, a minority-
# first-choice centrist, is elimination-tie-fragile here -> not cleanly freezable, and
# the lesson is about Choose-One, not IRV). All three included races deterministic.
_MW_CANDS = ["Ada", "Ben", "Cleo"]
_MW_STAR = _expand([(34,[5,0,4]),(33,[0,5,4]),(33,[2,1,5])])
_MW_PLUR = _expand([(34,[1,0,0]),(33,[0,1,0]),(33,[0,0,1])])
_MW_RANK = _expand([(34,[1,3,2]),(33,[3,1,2]),(33,[2,3,1])])

_MINORITY_WINNER = [
    {
        "test_id": "BV2215",
        "title": ("Minority winner — 34% wins Choose-One, but STAR & Ranked Robin "
                  "elect the candidate a majority prefers"),
        "description": (
            "The canonical minority/plurality-winner example from the STAR education "
            "repo (github.com/masiarek/star-voting-library). 100 voters, three "
            "candidates. Ada has a passionate third of the electorate: 34 rank her "
            "first, so under Choose-One (Plurality) she WINS with 34% — even though 66 "
            "of 100 voters score her 0 or 1. Cleo tells the opposite story: everyone's "
            "warm second choice (most voters rate her 4-5), she is the Condorcet winner "
            "(beats Ada 66-34 and Ben 67-33 head-to-head), leads STAR's scoring round "
            "(433), and wins the automatic runoff 66-34. So STAR and Ranked Robin both "
            "elect Cleo, the candidate a majority is genuinely glad about; only "
            "first-choice-only counting crowns Ada on a third of the vote. Same "
            "opinions, no strategy — the difference is how much of the ballot the "
            "method reads. (RCV-IRV is not shown; the lesson is about Choose-One.)"),
        "races": [
            {"title": "Choose-One (Plurality) — mark your one favorite", "method": "Plurality",
             "num_winners": 1, "candidates": _MW_CANDS, "ballots": _MW_PLUR},
            {"title": "Ranked Robin (Condorcet) — rank; every pair head-to-head", "method": "RankedRobin",
             "num_winners": 1, "max_rankings": 3, "candidates": _MW_CANDS, "ballots": _MW_RANK},
            {"title": "STAR — score 0-5, then an automatic runoff", "method": "STAR",
             "num_winners": 1, "candidates": _MW_CANDS, "ballots": _MW_STAR},
        ],
        "enable_write_in": False,
        "expected": "Plurality -> Ada (34 of 100). Ranked Robin -> Cleo (Condorcet, "
                    "beats both). STAR -> Cleo (scoring round 433; runoff 66-34 over "
                    "Ada). Test ID BV2215.",
    },
]

# RESULTS (2026-07-19): BV2215 -> 2p33qq — created + 100/100 ballots × 3 races OK.
# Canonical minority-winner example; backs method_comparisons/minority_winner.
# Plurality -> Ada (34); RR & STAR -> Cleo (Condorcet). All deterministic. Do NOT re-run.
# --- BV2216-2218 — the Pineapple progression (Choose-One's winner shrinks) --------
# Three rungs of method_comparisons/minority_winner_progression. A shared pizza;
# plain Cheese is nobody's favorite but everybody's easy second. As the menu grows
# 3 -> 4 -> 11 toppings, Choose-One crowns fan-favorite Pineapple on a shrinking
# share (34% -> 25% -> 11%), while STAR, Approval and Ranked Robin all elect Cheese
# (the Condorcet winner) at every rung. Four races each so all methods are clickable.
def _pineapple(niches, blocs, cb):
    cands = niches + ["Cheese"]; N = len(cands); ci = N - 1
    star, plur, appr, rank = [], [], [], []
    for i, cnt in enumerate(blocs):
        s = [0]*N; s[i] = 5; s[ci] = 4; star.append((cnt, s))
        p = [0]*N; p[i] = 1;            plur.append((cnt, p))
        a = [0]*N; a[i] = 1; a[ci] = 1; appr.append((cnt, a))
        r = [0]*N; r[i] = 1; r[ci] = 2; rank.append((cnt, r))
    if cb:
        star.append((cb, [0]*(N-1) + [5])); plur.append((cb, [0]*(N-1) + [1]))
        appr.append((cb, [0]*(N-1) + [1])); rank.append((cb, [0]*(N-1) + [1]))
    return cands, _expand(star), _expand(plur), _expand(appr), _expand(rank)

def _pineapple_election(test_id, part, pct, niches, blocs, cb):
    cands, star, plur, appr, rank = _pineapple(niches, blocs, cb)
    return {
        "test_id": test_id,
        "title": (f"Pineapple progression {part} — Choose-One elects Pineapple on "
                  f"{pct}%, but STAR, Approval & Ranked Robin elect Cheese"),
        "description": (
            f"Rung {part} of the pineapple progression from the STAR education repo "
            "(github.com/masiarek/star-voting-library). A group shares ONE pizza; "
            "plain Cheese is nobody's favorite but everybody's easy second. With "
            f"{len(cands)} toppings on the menu, Choose-One (mark your one favorite) "
            f"crowns the biggest fan club, Pineapple, on just {pct}% — while STAR, "
            "Approval and Ranked Robin all read the whole ballot and elect Cheese, the "
            "Condorcet winner that beats every topping head-to-head. The more crowded "
            "the menu, the smaller Choose-One's winning share; the whole-ballot methods "
            "don't budge. Same lesson as the canonical 34% minority-winner case, one "
            "memorable pizza."),
        "races": [
            {"title": "Choose-One (Plurality) — mark your one favorite topping",
             "method": "Plurality", "num_winners": 1, "candidates": cands, "ballots": plur},
            {"title": "Approval — approve every topping you're fine with",
             "method": "Approval", "num_winners": 1, "candidates": cands, "ballots": appr},
            {"title": "Ranked Robin (Condorcet) — rank; every pair head-to-head",
             "method": "RankedRobin", "num_winners": 1, "max_rankings": 2,
             "candidates": cands, "ballots": rank},
            {"title": "STAR — score 0-5, then an automatic runoff",
             "method": "STAR", "num_winners": 1, "candidates": cands, "ballots": star},
        ],
        "enable_write_in": False,
        "expected": f"Plurality -> Pineapple ({pct}%). Approval / Ranked Robin / STAR "
                    "-> Cheese (Condorcet winner). Test ID " + test_id + ".",
    }

_PINEAPPLE = [
    _pineapple_election("BV2216", "1/3", 34, ["Pineapple", "Anchovy", "Mushroom"],
                        [34, 33, 32], 0),
    _pineapple_election("BV2217", "2/3", 25, ["Pineapple", "Anchovy", "Mushroom", "Olive"],
                        [25, 23, 23, 23], 6),
    _pineapple_election("BV2218", "3/3", 11,
                        ["Pineapple", "Anchovy", "Mushroom", "Olive", "Sausage",
                         "Spinach", "Jalapeno", "Onion", "Pepper", "Basil"],
                        [11, 10, 10, 10, 10, 10, 10, 10, 10, 9], 0),
]

# RESULTS (2026-07-19): pineapple progression created OK, all ballots cast.
#   BV2216 -> ht2c3g (34%, 4 toppings, 99 voters)
#   BV2217 -> mvxbxr (25%, 5 toppings, 100 voters)
#   BV2218 -> h34pp9 (11%, 11 toppings, 100 voters)
# Each: Plurality -> Pineapple; Approval / RankedRobin / STAR -> Cheese. Do NOT re-run.
# BV2219/BV2220 — Equally Weighted Vote (the Equal Vote "Test of Balance").
# Cast Astra…Flux. The 'plus' election adds two voters whose ballots are exact
# opposites (each candidate's two scores sum to 5); every total rises by 5 and
# the runoff cancels 1-1, so STAR elects the same winner (Comet) either way.
# Reproduces 01_STAR/03_Criteria/equal_and_opposite/. Ready to create — see EQO note below.
_EQO_CANDS = ["Astra", "Bolt", "Comet", "Dune", "Echo", "Flux"]
_EQO_BASE = [[3, 2, 5, 1, 4, 0], [2, 4, 5, 0, 3, 1], [4, 1, 4, 2, 5, 0]]
_EQO_MIRROR = [[2, 1, 0, 1, 5, 4], [3, 4, 5, 4, 0, 1]]  # two exact-opposite ballots

EQO_BASE_SPEC = {
    "test_id": "BV2219",
    "title": "Equally Weighted Vote — base election (STAR elects Comet)",
    "description": ("The 'before' half of the Equal Vote Test of Balance. Three "
        "voters, six candidates; STAR elects Comet (score total 14, automatic "
        "runoff 2-1 over Echo). Its twin (BV2220) adds two exact-opposite ballots "
        "and shows the winner never moves — an equally weighted vote."),
    "method": "STAR", "num_winners": 1,
    "candidates": _EQO_CANDS, "ballots": _EQO_BASE,
    "expected": "STAR -> Comet (14; runoff 2-1 over Echo).",
}

EQO_PLUS_SPEC = {
    "test_id": "BV2220",
    "title": "Equally Weighted Vote — add two exact-opposite ballots (Comet still wins)",
    "description": ("The base election (BV2219) plus two voters with exact-opposite "
        "opinions on every candidate (each candidate's two scores sum to 5). Every "
        "score total rises by exactly 5 and the runoff cancels 1-1, so STAR still "
        "elects Comet: an equally weighted vote, demonstrated — any ballot can be "
        "perfectly cancelled by its opposite, which is why STAR has no forced "
        "vote-splitting."),
    "method": "STAR", "num_winners": 1,
    "candidates": _EQO_CANDS, "ballots": _EQO_BASE + _EQO_MIRROR,
    "expected": "STAR -> Comet (19; runoff 3-2 over Echo). Same winner as BV2219.",
}

# BV2221/2222/2223 — rb-j's "5-1-0" strategic challenge (star_5_1_0_challenge/).
# Beth is the Condorcet winner. Same preferences expressed as STAR scores and as
# IRV ranks so the two counts sit side by side on one BV election.
_S510_CANDS = ["Ana", "Beth", "Cole"]
# sincere STAR (poles score the moderate a 3) -> Beth
_S510_SINCERE = [[5, 3, 0]] * 48 + [[0, 3, 5]] * 47 + [[2, 5, 0]] * 5
# strategic 5-1-0, thin moderate base (48/47/5)
_S510_THIN_STAR = [[5, 1, 0]] * 48 + [[0, 1, 5]] * 47 + [[1, 5, 0]] * 5
_S510_THIN_RANK = [[1, 2, 3]] * 48 + [[3, 2, 1]] * 47 + [[2, 1, 3]] * 5
# strategic 5-1-0, real moderate base (40/35/25)
_S510_REAL_STAR = [[5, 1, 0]] * 40 + [[0, 1, 5]] * 35 + [[1, 5, 0]] * 25
_S510_REAL_RANK = [[1, 2, 3]] * 40 + [[3, 2, 1]] * 35 + [[2, 1, 3]] * 25

S510_SINCERE_SPEC = {
    "test_id": "BV2221",
    "title": "STAR vs strategy — sincere ballots elect the Condorcet winner (Beth)",
    "description": ("Center-squeeze electorate; Beth is the Condorcet winner. On "
        "SINCERE STAR ballots the poles score the moderate a genuine 3, so Beth "
        "leads the scoring round and wins the runoff. The strategic-5-1-0 twins "
        "(BV2222/BV2223) show what min-max voting does instead."),
    "method": "STAR", "num_winners": 1,
    "candidates": _S510_CANDS, "ballots": _S510_SINCERE,
    "expected": "STAR -> Beth (the Condorcet winner; scoring 310, runoff 52-48 over Ana).",
}

S510_THIN_SPEC = {
    "test_id": "BV2222",
    "title": "STAR vs strategy — 5-1-0 min-max squeezes the center like IRV (thin moderate)",
    "description": ("rb-j's 5-1-0 challenge, thin moderate base. Every voter min-maxes "
        "(favorite 5, lesser-evil 1, hated 0). Two races on the SAME preferences: "
        "STAR (5-1-0 scores) and RCV-IRV (the same order as ranks). Both elect Ana, "
        "a pole — the moderate Condorcet winner Beth is squeezed out. STAR = IRV here."),
    "races": [
        {"title": "STAR — strategic 5-1-0 scores", "method": "STAR",
         "num_winners": 1, "candidates": _S510_CANDS, "ballots": _S510_THIN_STAR},
        {"title": "RCV-IRV — the same preferences as ranks", "method": "IRV",
         "num_winners": 1, "max_rankings": 3, "candidates": _S510_CANDS,
         "ballots": _S510_THIN_RANK},
    ],
    "expected": "STAR -> Ana (Beth 120, squeezed out of the runoff). IRV -> Ana (Beth "
                "eliminated first, 5 firsts). Same failure — STAR = IRV under 5-1-0 here.",
}

S510_REAL_SPEC = {
    "test_id": "BV2223",
    "title": "STAR vs strategy — 5-1-0 min-max, real moderate: STAR keeps the CW, IRV doesn't",
    "description": ("rb-j's 5-1-0 challenge, but the moderate Beth has a real "
        "first-choice base (25 vs poles 40/35). Same min-max ballots; two races on the "
        "same preferences. STAR: the pooled '1's lift Beth into the runoff and she wins "
        "(the Condorcet winner). IRV: Beth still has the fewest firsts and is eliminated. "
        "So 5-1-0 STAR is IRV-LIKE, not IRV-identical — the '1's carry real weight."),
    "races": [
        {"title": "STAR — strategic 5-1-0 scores", "method": "STAR",
         "num_winners": 1, "candidates": _S510_CANDS, "ballots": _S510_REAL_STAR},
        {"title": "RCV-IRV — the same preferences as ranks", "method": "IRV",
         "num_winners": 1, "max_rankings": 3, "candidates": _S510_CANDS,
         "ballots": _S510_REAL_RANK},
    ],
    "expected": "STAR -> Beth (CW; the 1s lift her, runoff 60-40). IRV -> Ana (Beth "
                "eliminated first). STAR != IRV under the SAME 5-1-0 ballots.",
}

# --- BV2225 / BV2226 — Preference vs Support (center tolerated vs. supported) -----
# The matched pair for 07_Concepts/scores_and_ranks/preference_vs_support.md.
# THREE candidates on a spectrum: Alex (pole), Blair (center), Cole (pole).
# The TWO elections share BYTE-IDENTICAL rankings (Alex>Blair>Cole / Blair>Alex>Cole
# / Cole>Blair>Alex). The ONLY difference is how hard the two wings SCORE Blair as
# their 2nd choice: a grudging 1 ("tolerated") vs. a genuine 4 ("supported").
# Because the orders are identical, IRV and Ranked Robin CANNOT move between the two
# elections — IRV center-squeezes Blair both times (-> Alex); RR finds Blair the
# Condorcet winner both times (-> Blair). Only STAR responds to the support change:
# thin -> Alex (Blair misses the runoff), full -> Blair (real support lifts him in).
# That is the whole preference-vs-support lesson as a live election. NOTE: unlike the
# _four_races demos, the STAR scores are set EXPLICITLY here (not derived from ranks)
# — differing STAR scores over identical ranks is the entire point. LH-verified
# pre-creation (see the case .md). RR is a clean Condorcet win (deterministic/freezable).
_PVS_CANDS = ["Alex", "Blair", "Cole"]
#              (count, ranks[A,B,C],  thin STAR,   full STAR)
_PVS_BLOCS = [(15, [1, 2, 3], [5, 1, 0], [5, 4, 0]),   # Alex > Blair > Cole
              (6,  [2, 1, 3], [1, 5, 0], [1, 5, 0]),   # Blair > Alex > Cole  (base, unchanged)
              (15, [3, 2, 1], [0, 1, 5], [0, 4, 5])]   # Cole > Blair > Alex


def _pvs(which):
    rows = []
    for cnt, rank, thin, full in _PVS_BLOCS:
        rows += [{"rank": rank, "thin": thin, "full": full}[which]] * cnt
    return rows


_PVS_RANK, _PVS_THIN_STAR, _PVS_FULL_STAR = _pvs("rank"), _pvs("thin"), _pvs("full")

PVS_THIN_SPEC = {
    "test_id": "BV2225",
    "title": "Preference vs Support — the center TOLERATED (wings score Blair 1)",
    "description": ("Same rankings as the companion 'center SUPPORTED' election, but the two "
        "wings score the centrist Blair a grudging 1. Three races on these ballots: STAR "
        "(explicit scores), RCV-IRV and Ranked Robin (the identical rankings). STAR -> Alex "
        "(Blair's thin support leaves him out of the runoff); RCV-IRV -> Alex (center squeeze); "
        "Ranked Robin -> Blair (the Condorcet winner). Compare STAR here with the SUPPORTED "
        "election, where only Blair's scores change 1->4 and STAR alone flips to Blair — the "
        "ranked methods can't tell the two electorates apart."),
    "races": [
        {"title": "STAR — Blair merely tolerated (wings score him 1)", "method": "STAR",
         "num_winners": 1, "candidates": _PVS_CANDS, "ballots": _PVS_THIN_STAR},
        {"title": "RCV-IRV — the shared rankings", "method": "IRV",
         "num_winners": 1, "max_rankings": 3, "candidates": _PVS_CANDS, "ballots": _PVS_RANK},
        {"title": "Ranked Robin — the shared rankings", "method": "RankedRobin",
         "num_winners": 1, "max_rankings": 3, "candidates": _PVS_CANDS, "ballots": _PVS_RANK},
    ],
    "expected": "STAR -> Alex (scoring round Alex 81, Cole 75, Blair 60 excluded; runoff Alex 21-15). "
                "IRV -> Alex (Blair fewest firsts, eliminated). Ranked Robin -> Blair (Condorcet, beats both 21-15).",
}

PVS_FULL_SPEC = {
    "test_id": "BV2226",
    "title": "Preference vs Support — the center SUPPORTED (wings score Blair 4)",
    "description": ("Byte-identical rankings to the companion 'center TOLERATED' election — the "
        "ONLY change is the two wings now score the centrist Blair a genuine 4. Three races: STAR "
        "(explicit scores), RCV-IRV and Ranked Robin (the identical rankings). STAR -> Blair (real "
        "support lifts him into the runoff, which he wins); RCV-IRV -> Alex (center squeeze, unchanged); "
        "Ranked Robin -> Blair (Condorcet winner, unchanged). IRV and RR return the SAME winners as the "
        "tolerated election because the orders are identical — only STAR responds to the support change."),
    "races": [
        {"title": "STAR — Blair genuinely supported (wings score him 4)", "method": "STAR",
         "num_winners": 1, "candidates": _PVS_CANDS, "ballots": _PVS_FULL_STAR},
        {"title": "RCV-IRV — the shared rankings", "method": "IRV",
         "num_winners": 1, "max_rankings": 3, "candidates": _PVS_CANDS, "ballots": _PVS_RANK},
        {"title": "Ranked Robin — the shared rankings", "method": "RankedRobin",
         "num_winners": 1, "max_rankings": 3, "candidates": _PVS_CANDS, "ballots": _PVS_RANK},
    ],
    "expected": "STAR -> Blair (scoring round Blair 150, Alex 81; runoff Blair 21-15). IRV -> Alex "
                "(unchanged — center squeeze). Ranked Robin -> Blair (unchanged — Condorcet). Same ranks as "
                "the tolerated election; only STAR moved.",
}

# --- BV2227 / BV2228 — Favorite betrayal, the plain RCV-IRV incentive ------------
# Backs method_comparisons/favorite_betrayal_irv/. Left/Center/Right, 34 voters.
# HONEST election (BV2227), 3 races on the SAME honest ballots: STAR (explicit 5/3/0
# scores) + IRV + Ranked Robin (the ranks those scores imply). STAR & RR elect the
# compromise Center (the Condorcet winner); IRV elects the wing Right (center squeeze).
# BETRAY election (BV2228), IRV only: 2 of the 12 Left voters rank Center FIRST — Left
# is eliminated instead of Center, and Center wins. Same voters, one strategic move,
# opposite result. Explicit STAR scores (bottom = 0, not the rank-map's 1), so this
# does NOT use _mk_ranked_and_star. LH-verified pre-creation; RR is a clean Condorcet win.
_FB_CANDS = ["Left", "Center", "Right"]
#               (count, STAR[L,C,R], rank[L,C,R] 1=top)
_FB_HONEST = [(12, [5, 3, 0], [1, 2, 3]),   # Left > Center > Right
              (4,  [3, 5, 0], [2, 1, 3]),   # Center > Left > Right
              (5,  [0, 5, 3], [3, 1, 2]),   # Center > Right > Left
              (13, [0, 3, 5], [3, 2, 1])]   # Right > Center > Left
_FB_BETRAY = [(10, [1, 2, 3]),   # Left > Center > Right   (10 loyal)
              (6,  [2, 1, 3]),   # Center > Left > Right    (4 + 2 betrayers)
              (5,  [3, 1, 2]),   # Center > Right > Left
              (13, [3, 2, 1])]   # Right > Center > Left


def _fb_expand(which):
    rows = []
    for row in _FB_HONEST:
        cnt = row[0]
        rows += [{"star": row[1], "rank": row[2]}[which]] * cnt
    return rows


_FB_HONEST_STAR = _fb_expand("star")
_FB_HONEST_RANK = _fb_expand("rank")
_FB_BETRAY_RANK = sum(([rk] * cnt for cnt, rk in _FB_BETRAY), [])

FB_HONEST_SPEC = {
    "test_id": "BV2227",
    "title": "Favorite Betrayal — honest ballots (STAR & Ranked Robin elect the compromise; RCV-IRV elects a wing)",
    "description": ("The plain favorite-betrayal question, three ways on the SAME honest ballots. "
        "Left/Center/Right, 34 voters; Center is the compromise everyone ranks second and the "
        "Condorcet winner, but has the fewest first-choices. STAR (honest 5/3/0 scores) and Ranked "
        "Robin elect Center; RCV-IRV squeezes Center out and elects the wing Right. Companion "
        "election shows that under RCV-IRV, 2 Left voters ranking Center FIRST (betraying their "
        "favorite) flips it to Center — a move STAR and RR never require."),
    "races": [
        {"title": "STAR — honest scores (favorite 5, compromise 3, worst 0)", "method": "STAR",
         "num_winners": 1, "candidates": _FB_CANDS, "ballots": _FB_HONEST_STAR},
        {"title": "RCV-IRV — the same honest preferences as ranks", "method": "IRV",
         "num_winners": 1, "max_rankings": 3, "candidates": _FB_CANDS, "ballots": _FB_HONEST_RANK},
        {"title": "Ranked Robin — the same honest preferences as ranks", "method": "RankedRobin",
         "num_winners": 1, "max_rankings": 3, "candidates": _FB_CANDS, "ballots": _FB_HONEST_RANK},
    ],
    "expected": "STAR -> Center (score 120 vs Right 80; runoff 21-13). Ranked Robin -> Center "
                "(Condorcet winner). RCV-IRV -> Right (Center fewest first-choices, squeezed; final 18-16).",
}

FB_BETRAY_SPEC = {
    "test_id": "BV2228",
    "title": "Favorite Betrayal — the RCV-IRV betrayal (2 voters rank the compromise first, and it wins)",
    "description": ("The honest RCV-IRV election (companion BV2227) with ONE change: 2 of the 12 Left "
        "voters betray their favorite and rank Center FIRST. That is enough to eliminate Left instead "
        "of Center; Left's ballots flow to Center, and Center wins 21-13 — the outcome those voters "
        "wanted, obtained only by hiding who they truly preferred. Under RCV-IRV, ranking your favorite "
        "first is safe only when they're very strong or hopeless. STAR & Ranked Robin (BV2227) elect "
        "Center from the honest ballots, no betrayal needed."),
    "races": [
        {"title": "RCV-IRV — 2 Left voters rank Center first (the betrayal)", "method": "IRV",
         "num_winners": 1, "max_rankings": 3, "candidates": _FB_CANDS, "ballots": _FB_BETRAY_RANK},
    ],
    "expected": "RCV-IRV -> Center (Left now fewest first-choices at 10, eliminated; Center wins 21-13). "
                "Contrast BV2227 honest RCV-IRV -> Right.",
}

# --- BV2229-2232 — FairVote white-paper claim-check (French 2017, Washington 2010) ---
# Backs method_comparisons/fairvote_star_whitepaper/. Each is a single STAR race.
# Honest vs. the coordinated burial FairVote's paper describes. LH-verified pre-creation.
def _rows(blocs):
    out = []
    for cnt, scores in blocs:
        out += [scores] * cnt
    return out

_FR_CANDS = ["Macron", "LePen", "Fillon", "Melenchon"]
_WA_CANDS = ["Berkey", "Harper", "Rieger"]

FR_HONEST_SPEC = {
    "test_id": "BV2229",
    "title": "FairVote-vs-STAR check: French 2017 honest — STAR elects the centrist Macron",
    "description": ("FairVote's 2018 white paper says STAR could squeeze a strong centrist. The 2017 "
        "French field (~20% each), scored honestly (favorite 5, the compromise Macron 4). STAR elects "
        "Macron, the Condorcet winner (runoff 51-49). Companion BV2230 shows the coordinated burial. "
        "Simplified 100-voter teaching model. Backs method_comparisons/fairvote_star_whitepaper."),
    "method": "STAR", "num_winners": 1, "candidates": _FR_CANDS,
    "ballots": _rows([(26, [5, 0, 3, 3]), (25, [4, 0, 1, 5]), (24, [4, 2, 5, 0]), (25, [1, 5, 3, 0])]),
    "expected": "STAR -> Macron (351; runoff 51-49 over Fillon). The Condorcet winner, elected sincerely.",
}
FR_STRAT_SPEC = {
    "test_id": "BV2230",
    "title": "FairVote-vs-STAR check: French 2017 coordinated burial — Macron squeezed out",
    "description": ("The burial FairVote's white paper describes: every non-Macron faction scores Macron 0 "
        "and inflates the rival wings to 4 (even ideological enemies) to keep him out of the runoff. Same "
        "honest first choices as BV2229. It works: Macron collapses (130) and STAR elects Melenchon — "
        "FairVote's claim, conceded. But it needs a coordinated conspiracy, honest STAR elects Macron, and "
        "RCV-IRV on these ballots elects Le Pen (worse). Backs method_comparisons/fairvote_star_whitepaper."),
    "method": "STAR", "num_winners": 1, "candidates": _FR_CANDS,
    "ballots": _rows([(26, [5, 0, 3, 3]), (25, [0, 4, 4, 5]), (24, [0, 4, 5, 4]), (25, [0, 5, 4, 4])]),
    "expected": "STAR -> Melenchon (Macron 130, squeezed out of the runoff). Honest STAR -> Macron (BV2229).",
}
WA_HONEST_SPEC = {
    "test_id": "BV2231",
    "title": "FairVote-vs-STAR check: Washington 2010 honest — STAR elects the moderate Berkey",
    "description": ("FairVote's white paper cites the 2010 WA State Senate race (moderate Berkey, progressive "
        "Harper, long-shot conservative Rieger) as a squeeze STAR would make easy. Scored honestly, STAR "
        "elects Berkey, the moderate Condorcet winner (runoff 60-40). Companion BV2232 shows the burial. "
        "Backs method_comparisons/fairvote_star_whitepaper."),
    "method": "STAR", "num_winners": 1, "candidates": _WA_CANDS,
    "ballots": _rows([(35, [5, 3, 1]), (40, [4, 5, 0]), (25, [2, 0, 5])]),
    "expected": "STAR -> Berkey (385; runoff 60-40 over Harper). The moderate Condorcet winner.",
}
WA_STRAT_SPEC = {
    "test_id": "BV2232",
    "title": "FairVote-vs-STAR check: Washington 2010 burial — squeeze works on STAR, IRV resists",
    "description": ("The squeeze FairVote describes: the Harper faction scores Harper 5, conservative Rieger 4, "
        "moderate Berkey 0, to push Berkey out. Same honest first choices as BV2231. It works under STAR "
        "(Berkey 225, squeezed; Harper wins) — conceded. But honest STAR elects Berkey, the burial risks "
        "electing Rieger, and RCV-IRV on these very ballots STILL elects Berkey. A case that cuts fairly. "
        "Backs method_comparisons/fairvote_star_whitepaper."),
    "method": "STAR", "num_winners": 1, "candidates": _WA_CANDS,
    "ballots": _rows([(35, [5, 3, 1]), (40, [0, 5, 4]), (25, [2, 0, 5])]),
    "expected": "STAR -> Harper (Berkey 225, squeezed). Honest STAR -> Berkey (BV2231); RCV-IRV here -> Berkey.",
}


# --- BV2249 — Weak Condorcet loser (3 races) ---------------------------------
# Backs method_comparisons/weak_condorcet_loser/. Five voters, three candidates.
# Pairwise: Ada beats Ben 3-2, Ada beats Cora 3-2, Ben TIES Cora 2-2 — so Ada is
# the Condorcet winner and BOTH Ben and Cora beat nobody (jointly weak Condorcet
# losers; unlike a strict one, a weak one need not be unique).
#   STAR      -> Ben  (Ada eliminated on score; Ben-Cora runoff ties 2-2, score
#                      tiebreaker decides — rung "Runoff 1", identical in LH and BV,
#                      so this is reproducible and does NOT reach BV's random floor)
#   Approval  -> Ben  (5-4-3, no tie)
#   RankedRobin -> Ada (2-0-0; Ben and Cora both 0-1-1, "Beats: —")
# The ranked ballots carry voter 1's Ben=Cora EQUAL RANK (both rank 2) — BV
# preserves equal ranks on creation and counts them like LH (confirmed BV2140
# 48hjkv), which is what keeps the 2-2 pairwise tie intact on the ranked race.
# IRV/Plurality are deliberately NOT included: both elect Ada for reasons
# unrelated to this criterion (she leads first choices 3-2), and an equal rank is
# an overvote under most deployed IRV rules, so a live IRV race would model
# something real IRV does not do.
_WCL_CANDS = ["Ada", "Ben", "Cora"]
_WCL_STAR = [[5, 4, 4], [5, 4, 1], [5, 4, 3], [0, 3, 4], [0, 3, 4]]
_WCL_APPR = [[1, 1, 1], [1, 1, 0], [1, 1, 1], [0, 1, 1], [0, 1, 1]]
_WCL_RANK = [[1, 2, 2], [1, 2, 3], [1, 2, 3], [3, 2, 1], [3, 2, 1]]

WCL_SPEC = {
    "test_id": "BV2249",
    "title": "Weak Condorcet loser \u2014 when both STAR finalists beat nobody",
    "description": (
        "Five voters, three candidates, and a criterion most people have never heard of. "
        "A CONDORCET LOSER loses every head-to-head matchup. A WEAK Condorcet loser is the "
        "ties-allowed version: they lose OR TIE every matchup \u2014 meaning they beat nobody. "
        "Here Ada beats Ben 3-2 and beats Cora 3-2, while Ben and Cora tie each other 2-2, so "
        "Ada is the Condorcet winner and BOTH Ben and Cora beat nobody. Ranked Robin elects "
        "Ada. STAR and Approval both elect Ben, a weak Condorcet loser: Ada is polarizing "
        "(three voters score her 5, two score her 0), so she is eliminated on total score "
        "before the runoff, and the Ben-vs-Cora runoff then ties 2-2 and is settled by STAR's "
        "score tiebreaker. The point is precise: STAR can NEVER elect a STRICT Condorcet "
        "loser, because a strict loser loses the runoff by definition \u2014 but a tie is not a "
        "loss, so the weak version slips through. Read it as a possibility result, not a "
        "warning: it needs an exact pairwise tie between the two finalists, which is "
        "vanishingly rare in any electorate large enough to matter. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/method_comparisons/weak_condorcet_loser/README.html"
    ),
    "enable_write_in": False,
    "races": [
        {"title": "Weak Condorcet loser \u2014 STAR", "method": "STAR",
         "num_winners": 1, "candidates": _WCL_CANDS, "ballots": _WCL_STAR},
        {"title": "Weak Condorcet loser \u2014 Approval", "method": "Approval",
         "num_winners": 1, "candidates": _WCL_CANDS, "ballots": _WCL_APPR},
        {"title": "Weak Condorcet loser \u2014 Ranked Robin (Copeland)", "method": "RankedRobin",
         "num_winners": 1, "max_rankings": 3, "candidates": _WCL_CANDS, "ballots": _WCL_RANK},
    ],
    "expected": ("STAR -> Ben (weak Condorcet loser, via the 2-2 runoff tie + score tiebreak); "
                 "Approval -> Ben 5-4-3; Ranked Robin -> Ada (the Condorcet winner, 2-0-0). "
                 "Test ID BV2249."),
}


# --- BV2250 — Condorcet's 1788 rebuttal to Borda (3 races) -------------------
# Backs method_comparisons/borda_condorcet_1788/. Condorcet's own counterexample
# to the Borda count, in the simplified 11-voter form textbooks use. Candidate
# names are Condorcet's (Peter/Paul/James), kept for fidelity to the source even
# though Peter/Paul share an initial.
#   4 : Peter > Paul  > James        Plurality -> Paul (5 first choices)
#   3 : Paul  > James > Peter        Borda     -> Paul (14 vs Peter 12, James 7)
#   2 : Paul  > Peter > James        but Peter beats Paul 6-5 AND James 6-5,
#   2 : James > Peter > Paul         so PETER is the Condorcet winner.
#   STAR        -> Peter  (scoring round Paul 37 / Peter 32 / James 19 — i.e. it
#                          reproduces Borda's answer — then the runoff reverses
#                          it 6-5. Under a uniform spacing the scoring round IS a
#                          Borda count, so STAR = Borda's step + Condorcet's check.)
#   RankedRobin -> Peter  (2-0-0, the Condorcet winner)
#   IRV         -> Peter  (James eliminated on 2, both ballots transfer, 6-5)
# IRV is included ON PURPOSE: it AGREES here, which keeps the comparison honest —
# this is a Borda/plurality failure, not an IRV one.
# All three races are fully deterministic (no ties at any rung), so the BV result
# is freezable and reproducible against LH.
# Ranks are aligned to the candidate order [Peter, Paul, James]; 1 = top choice.
_C1788_CANDS = ["Peter", "Paul", "James"]
_C1788_STAR = ([[5, 3, 0]] * 4) + ([[0, 5, 3]] * 3) + ([[3, 5, 0]] * 2) + ([[3, 0, 5]] * 2)
_C1788_RANK = ([[1, 2, 3]] * 4) + ([[3, 1, 2]] * 3) + ([[2, 1, 3]] * 2) + ([[2, 3, 1]] * 2)

C1788_SPEC = {
    "test_id": "BV2250",
    "title": "Condorcet's 1788 rebuttal to Borda — where the Condorcet criterion comes from",
    "description": (
        "In 1770 Borda argued his rank-points rule was better than plurality, because the "
        "plurality winner can lose a direct majority contest to somebody else. Condorcet's "
        "reply was that Borda's own rule has the same disease — and this is the election he "
        "used to prove it, in the simplified 11-voter form textbooks still use. The names are "
        "Condorcet's own. Four blocs vote: 4 rank Peter > Paul > James, 3 rank Paul > James > "
        "Peter, 2 rank Paul > Peter > James, and 2 rank James > Peter > Paul. Plurality elects "
        "Paul on 5 first choices. Borda ALSO elects Paul, 14 points to Peter's 12 and James's 7. "
        "Yet Peter beats Paul head-to-head 6-5, and beats James 6-5 as well — Peter beats "
        "everybody one-on-one, which is exactly what we now call the Condorcet winner. Borda "
        "diagnosed plurality's disease correctly and then caught it himself, and that objection "
        "is where the Condorcet criterion comes from. Three races here count the same 11 voters. "
        "Ranked Robin elects Peter, the Condorcet winner. RCV-IRV also elects Peter (James is "
        "eliminated on 2 first choices and both ballots transfer) — included deliberately, "
        "because this is a Borda and plurality failure, NOT an IRV one. STAR elects Peter too, "
        "and how it gets there is the lesson: under an even spacing STAR's scoring round IS a "
        "Borda count, so round one reproduces Borda's answer and puts Paul first on 37 points, "
        "and then the automatic runoff runs precisely the direct majority contest Condorcet "
        "demanded, which Peter wins 6-5. STAR is Borda's scoring step followed by Condorcet's "
        "check, answering a 238-year-old objection on screen. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/method_comparisons/borda_condorcet_1788/index.html"
    ),
    "enable_write_in": False,
    "races": [
        {"title": "Condorcet 1788 — STAR (the runoff overturns Borda's winner)",
         "method": "STAR",
         "num_winners": 1, "candidates": _C1788_CANDS, "ballots": _C1788_STAR},
        {"title": "Condorcet 1788 — Ranked Robin (Copeland)",
         "method": "RankedRobin",
         "num_winners": 1, "max_rankings": 3, "candidates": _C1788_CANDS, "ballots": _C1788_RANK},
        {"title": "Condorcet 1788 — RCV-IRV (agrees here)",
         "method": "IRV",
         "num_winners": 1, "max_rankings": 3, "candidates": _C1788_CANDS, "ballots": _C1788_RANK},
    ],
    "expected": ("STAR -> Peter (scoring round Paul 37 / Peter 32 / James 19; runoff Peter 6-5 "
                 "— a runoff reversal of Borda's winner); Ranked Robin -> Peter (2-0-0, the "
                 "Condorcet winner); RCV-IRV -> Peter (6-5 after James is eliminated). "
                 "For contrast, plurality and Borda both elect Paul. Test ID BV2250."),
}


# --- BV2251 — Margins matter: Copeland vs Borda (4 races) --------------------
# Backs method_comparisons/copeland_vs_borda_margins/. Zwicker's profile P2 from
# "Introduction to the Theory of Voting" (Handbook of Computational Social Choice
# ch. 2), shrunk from its printed 304 ballots to 12 with the symmetric Borda
# scores preserved EXACTLY (0 / +2 / -2) and the Copeland three-way tie intact.
# Flavour initials map onto the book's a/b/c: Almond, Berry, Cocoa.
#   5 : Almond > Berry  > Cocoa      Almond beats Berry  7-5  (margin +2)
#   3 : Berry  > Cocoa  > Almond     Berry  beats Cocoa  8-4  (margin +4)
#   2 : Cocoa  > Almond > Berry      Cocoa  beats Almond 7-5  (margin +2)
#   2 : Cocoa  > Berry  > Almond     -> a cycle; NO Condorcet winner.
# Four races, four different answers from one electorate:
#   Plurality   -> Almond (5 first choices vs Cocoa 4, Berry 3)
#   IRV         -> Cocoa  (Berry eliminated FIRST on 3; all 3 transfer to Cocoa)
#   STAR (5/3/0)-> Almond (scoring round = Borda -> Berry first; runoff 7-5)
#   RankedRobin -> a genuine 3-way Copeland tie (all 1-1-0).
# CAVEAT, deliberate and disclosed in the description: the Ranked Robin race is
# the ONE non-freezable race here. LH breaks the Copeland tie by total margin
# (= the symmetric Borda score) and elects Berry; BetterVoting's ladder only has
# a head-to-head rung for a clean 2-WAY tie, so on a 3-way tie it falls through
# to RANDOM. The pairwise MATRIX is deterministic and is the actual artifact —
# BV's crowned winner in that race is a coin flip and must not be cited as a
# result. See 05_Ranked_Robin/01_Learn/rr_tiebreak_lh_vs_bv.md.
# Ranks are aligned to the candidate order [Almond, Berry, Cocoa]; 1 = top.
_MARG_CANDS = ["Almond", "Berry", "Cocoa"]
_MARG_STAR = ([[5, 3, 0]] * 5) + ([[0, 5, 3]] * 3) + ([[3, 0, 5]] * 2) + ([[0, 3, 5]] * 2)
_MARG_RANK = ([[1, 2, 3]] * 5) + ([[3, 1, 2]] * 3) + ([[2, 3, 1]] * 2) + ([[3, 2, 1]] * 2)
_MARG_PLUR = ([[1, 0, 0]] * 5) + ([[0, 1, 0]] * 3) + ([[0, 0, 1]] * 4)

MARGINS_SPEC = {
    "test_id": "BV2251",
    "title": "Margins matter — one electorate, four different answers",
    "description": (
        "Twelve voters rank three gelato flavours, and the head-to-head results form a loop: "
        "Almond beats Berry 7-5, Berry beats Cocoa 8-4, and Cocoa beats Almond 7-5. Nobody "
        "beats everybody, so there is no Condorcet winner and every voting rule has to fall "
        "back on its own idea of what to do next. What separates them is one question: does "
        "the rule look at the SIZE of each victory, or only at who won? The Copeland rule "
        "counts wins and throws the margins away, so all three flavours go 1-1-0 and it ties "
        "every one of them. The Borda count is that same tournament WEIGHTED by those margins "
        "— add up each flavour's signed margins and you get Almond 0, Berry +2, Cocoa -2 — so "
        "Borda separates them and elects Berry. Four races here count the very same twelve "
        "ballots and produce four different answers. Choose-One elects Almond on 5 first "
        "choices. RCV-IRV eliminates Berry FIRST, because Berry has the fewest first choices "
        "(3) despite winning every margin-weighted measure; all three of those ballots "
        "transfer to Cocoa, which wins 7-5. STAR elects Almond: converting the rankings to "
        "scores on an even 5/3/0 spacing makes the scoring round a Borda count, so Berry leads "
        "round one, and then the automatic runoff holds the direct contest Borda never holds "
        "and Almond takes it 7-5. Ranked Robin is the interesting one — it reports the genuine "
        "three-way Copeland tie, and please read its PAIRWISE TABLE rather than its crowned "
        "winner: BetterVoting resolves a three-way tie at random, so that one name is a coin "
        "flip, not a result. This profile is the twelve-ballot version of a 304-voter textbook "
        "profile, shrunk so you can check every number by hand while the Borda scores stay "
        "identical. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/method_comparisons/copeland_vs_borda_margins/index.html"
    ),
    "enable_write_in": False,
    "races": [
        {"title": "Margins — Choose-One (Plurality): first choices only",
         "method": "Plurality",
         "num_winners": 1, "candidates": _MARG_CANDS, "ballots": _MARG_PLUR},
        {"title": "Margins — STAR (the scoring round is Borda, then a head-to-head)",
         "method": "STAR",
         "num_winners": 1, "candidates": _MARG_CANDS, "ballots": _MARG_STAR},
        {"title": "Margins — RCV-IRV (eliminates the Borda winner first)",
         "method": "IRV",
         "num_winners": 1, "max_rankings": 3, "candidates": _MARG_CANDS, "ballots": _MARG_RANK},
        {"title": "Margins — Ranked Robin (Copeland ties all three; read the table, not the winner)",
         "method": "RankedRobin",
         "num_winners": 1, "max_rankings": 3, "candidates": _MARG_CANDS, "ballots": _MARG_RANK},
    ],
    "expected": ("Plurality -> Almond (5/4/3 first choices); STAR -> Almond (scoring round "
                 "Berry 36 / Almond 31 / Cocoa 29 — a Borda count — then the runoff reverses "
                 "it, Almond 7-5); RCV-IRV -> Cocoa (Berry eliminated first on 3, all three "
                 "ballots transfer, Cocoa 7-5); Ranked Robin -> a genuine 3-way Copeland tie "
                 "(each 1-1-0). LH breaks that tie by total margin (= the symmetric Borda "
                 "score) and elects Berry; BV falls through to RANDOM, so only the pairwise "
                 "matrix is freezable from the BV side. Borda (no BV race, cross-checked in "
                 "pref_voting) -> Berry, 13 to Almond's 12 and Cocoa's 11. Test ID BV2251."),
}


# --- BV2252 — Goodberry's Frozen Custard (Cary, NC): Best Flavor 2026 ---------
# A REAL, live poll — not a constructed teaching case. No seed ballots: the
# election is minted empty and collects actual votes (paper ballots printed from
# the export with bv_ballot_sheet.py, plus the QR/online route). Ten flavors off
# the Cary shop's permanent menu board, spread across its families (custard
# classic, chocolate, nut, coffee, citrus, mix-in, Southern signature); write-ins
# stay ON so a voter whose favorite is Blueberry, Nutella or a calendar special
# (Lavender Limoncello, Piña Colada, Tiramisu…) can still say so.
# Name note: Goodberry's sells FROZEN CUSTARD, not ice cream — the title says so.
_GOODBERRY_CANDS = [
    "Banana Pudding", "Butter Pecan", "Chocolate Malt", "Cookie Dough",
    "Jamocha", "Key Lime", "Mint Chocolate Chip", "Peanut Butter",
    "Salted Caramel", "Sweet Cream",
]

GOODBERRYS_SPEC = {
    "test_id": "BV2252",
    "title": "Goodberry's Frozen Custard, Cary NC — Best Flavor 2026",
    "description": (
        "Which Goodberry's flavor is the best? This is a real poll, counted with STAR Voting "
        "(Score Then Automatic Runoff). Ten flavors from the Cary menu board are on the ballot, "
        "and write-ins are open if your favorite isn't listed. Score EVERY flavor you have an "
        "opinion about from 0 to 5 stars — give your favorite 5, give anything you'd be unhappy "
        "with 0, and use the middle for the ones you'd happily eat but wouldn't pick first. You "
        "are rating, not ranking, so giving two flavors the same score is perfectly fine and is "
        "not a wasted vote. The count then happens in two steps. First the scoring round adds up "
        "every star, and the two highest-scoring flavors become the finalists. Then the automatic "
        "runoff counts every ballot once more, for whichever of those two finalists that ballot "
        "scored higher; the finalist preferred by more voters wins. That second step is what a "
        "plain star-rating poll is missing — it means the winning flavor is the one more people "
        "actually preferred, not merely the one that collected the most generous ratings. It also "
        "means a long menu is safe: adding a tenth flavor similar to the ninth cannot split their "
        "support the way a pick-one poll would, so you never have to vote strategically against a "
        "flavor you like. Paper ballots for this election are printed straight from its own data, "
        "so a table at the shop and the online voters are casting the very same ballot into the "
        "very same count. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/00_start_here/STAR_Voting/hands_on/running_a_paper_ballot_demo.html"
    ),
    "enable_write_in": True,
    "method": "STAR",
    "num_winners": 1,
    "candidates": _GOODBERRY_CANDS,
    "ballots": [],          # minted EMPTY — real voters fill it
    "expected": "no seed ballots; live poll — winner decided by real votes",
}

# --- BV2253 — Manipulability P3: the SINCERE baseline (3 races) --------------
# Backs method_comparisons/manipulability_p3/. Zwicker's profile P3 from
# "Introduction to the Theory of Voting" (HCSC ch. 2), used for Definition 2.3
# (single voter manipulability). 7 voters, 5 candidates, cities A-E.
#   2 : Edinburgh > Cork > Athens > Dublin > Bergen
#   3 : Dublin > Edinburgh > Bergen > Cork > Athens
#   2 : Athens > Bergen > Cork > Dublin > Edinburgh
# ONLY THE SINCERE PROFILE IS MINTED. The teaching page's manipulated variants
# are counterfactual (deliberately insincere ballots) and stay LH-only — casting
# lies as a real public election would misrepresent what the profile is.
#   Plurality   -> Dublin (3 first choices vs Athens 2, Edinburgh 2)
#   STAR        -> Dublin (5/4/3/2/0 conversion: D23 E22 C20 B17 A16;
#                          finalists Dublin & Edinburgh; runoff Dublin 5-2)
#   RankedRobin -> Edinburgh (3-1; symmetric Copeland +2, with Bergen -2 and the
#                          other three 0 — exactly the numbers the chapter prints)
# NO IRV RACE ON PURPOSE: first choices are 3/2/2, so the first elimination is a
# genuine two-way tie between Athens and Edinburgh and the IRV result would be a
# coin flip — not freezable. The repo page reports IRV as INDETERMINATE rather
# than quoting whichever winner a tiebreak produced.
# All three minted races are deterministic: Ranked Robin's Edinburgh wins
# outright on 3 wins (no Copeland tie, so no BV random tiebreak), and the STAR
# and plurality margins are clean.
# NUMBERING NOTE: this case was requested as BV2252, but BV2252 had already been
# consumed by GOODBERRYS_SPEC (election 6tthfv) in a concurrent session, so it
# was minted as BV2253. Test IDs are permanent and must not collide.
# Ranks aligned to [Athens, Bergen, Cork, Dublin, Edinburgh]; 1 = top choice.
_P3_CANDS = ["Athens", "Bergen", "Cork", "Dublin", "Edinburgh"]
_P3_RANK = ([[3, 5, 2, 4, 1]] * 2) + ([[5, 3, 4, 1, 2]] * 3) + ([[1, 2, 3, 4, 5]] * 2)
_P3_STAR = ([[3, 0, 4, 2, 5]] * 2) + ([[0, 3, 2, 5, 4]] * 3) + ([[5, 4, 3, 2, 0]] * 2)
_P3_PLUR = ([[0, 0, 0, 0, 1]] * 2) + ([[0, 0, 0, 1, 0]] * 3) + ([[1, 0, 0, 0, 0]] * 2)

P3_SPEC = {
    "test_id": "BV2253",
    "title": "Where should the committee meet? — the sincere baseline behind a textbook manipulation",
    "description": (
        "Seven committee members rank five cities for a meeting. This is the SINCERE vote — "
        "everyone's honest ranking, nobody playing games — and it is the baseline that a famous "
        "textbook example attacks. Two members rank Edinburgh > Cork > Athens > Dublin > Bergen, "
        "three rank Dublin > Edinburgh > Bergen > Cork > Athens, and two rank Athens > Bergen > "
        "Cork > Dublin > Edinburgh. Three races count those same seven ballots and they do not "
        "all agree. Choose-One elects Dublin, which has the most first choices (3 against 2 and "
        "2). STAR also elects Dublin: converting each ranking to scores puts Dublin first on 23 "
        "points with Edinburgh close behind on 22, and Dublin then wins the automatic runoff 5-2 "
        "because more voters prefer Dublin to Edinburgh than the other way round. Ranked Robin "
        "disagrees and elects Edinburgh, because Edinburgh wins three of its four head-to-head "
        "matchups while Dublin wins only two. Notice that neither of them beats everybody: "
        "Dublin beats Edinburgh 5-2, but Edinburgh beats the other three, so there is no "
        "Condorcet winner in this election. That fragility is exactly why the profile is famous. "
        "In the textbook it is used to define what it means for a voting rule to be MANIPULABLE: "
        "one of the two Athens-first voters, watching their least favourite city Edinburgh about "
        "to win, can submit a dishonest ballot and change the outcome to one they prefer. The "
        "full lesson works that manipulation through — and shows the same thing being done to "
        "STAR, because every voting method can be gamed by somebody. No instant runoff race is "
        "included here, deliberately: the first elimination would be a two-way tie decided by "
        "chance rather than by the ballots, so there is no honest IRV answer to publish. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/method_comparisons/manipulability_p3/index.html"
    ),
    "enable_write_in": False,
    "races": [
        {"title": "Meeting city — Choose-One (Plurality): Dublin on 3 first choices",
         "method": "Plurality",
         "num_winners": 1, "candidates": _P3_CANDS, "ballots": _P3_PLUR},
        {"title": "Meeting city — STAR (Dublin 23, Edinburgh 22, runoff 5-2)",
         "method": "STAR",
         "num_winners": 1, "candidates": _P3_CANDS, "ballots": _P3_STAR},
        {"title": "Meeting city — Ranked Robin (Edinburgh wins 3 of 4 head-to-heads)",
         "method": "RankedRobin",
         "num_winners": 1, "max_rankings": 5, "candidates": _P3_CANDS, "ballots": _P3_RANK},
    ],
    "expected": ("Plurality -> Dublin (3 first choices vs Athens 2, Edinburgh 2); STAR -> Dublin "
                 "(scoring round Dublin 23 / Edinburgh 22 / Cork 20 / Bergen 17 / Athens 16; "
                 "finalists Dublin and Edinburgh; runoff Dublin 5-2); Ranked Robin -> Edinburgh "
                 "(3-1 head-to-head, symmetric Copeland +2, with Bergen -2 and Athens/Cork/Dublin "
                 "all 0 — the exact vector the chapter prints). No Condorcet winner (Dublin beats "
                 "Edinburgh 5-2). All three races deterministic; no IRV race because its first "
                 "elimination is a 2-way tie. Test ID BV2253."),
}


# --- BV2254 — Reinforcement paradox (Brandt, Dong & Peters 2024, Theorem 2) ---
# Backs method_comparisons/reinforcement_paradox/. One election, two races on the
# SAME 9 combined ballots (index-aligned): North (6) + South (3) merged. Ada wins
# both districts, but the union elects Cara. STAR (scoring round -> Ada, runoff ->
# Cara) and Ranked Robin (Cara, the combined Condorcet winner) both land on Cara.
# LH-verified pre-creation; both races deterministic/freezable (no tiebreak).
_REINF_CANDS = ["Ada", "Ben", "Cara"]
#                Ada>Ben>Cara Ada>Ben>Cara Ben>Cara>Ada Ben>Cara>Ada Cara>Ada>Ben Cara>Ada>Ben Cara>Ada>Ben Ada>Cara>Ben Ada>Cara>Ben
_REINF_STAR = [[5,3,0], [5,3,0], [0,5,3], [0,5,3], [3,0,5], [3,0,5], [3,0,5], [5,0,3], [5,0,3]]
_REINF_RANK = [[1,2,3], [1,2,3], [3,1,2], [3,1,2], [2,3,1], [2,3,1], [2,3,1], [1,3,2], [1,3,2]]
REINFORCEMENT_SPEC = {
    "test_id": "BV2254",
    "title": "Reinforcement paradox: two towns pick Ada, together pick Cara",
    "description": (
        "Two towns each elect Ada, but merged they elect Cara — the reinforcement paradox "
        "(Brandt, Dong & Peters, 2024): every Condorcet method must show it once there are 8 or "
        "more voters. STAR's scoring round keeps Ada, but its automatic runoff flips to Cara. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/method_comparisons/reinforcement_paradox/index.html"),
    "races": [
        {"title": "STAR — scoring round leads Ada, the runoff flips to Cara",
         "method": "STAR", "num_winners": 1, "candidates": _REINF_CANDS, "ballots": _REINF_STAR},
        {"title": "Ranked Robin — Cara is the combined Condorcet winner",
         "method": "RankedRobin", "num_winners": 1, "max_rankings": 3,
         "candidates": _REINF_CANDS, "ballots": _REINF_RANK},
    ],
    "expected": "STAR -> Cara (score round Ada 29 vs Cara 27; runoff Cara 5-4). "
                "Ranked Robin -> Cara (beats Ada 5-4 and Ben 5-4). Ada won both districts.",
}

# --- BV2255 — The "traditional" style, all the way down (four ballots, one bit) ---
# Backs 01_STAR/01_Learn/voting_styles/traditional.md — the choose-one habit
# transplanted onto a 5-star ballot. Here EVERY voter votes that way: 3 voters, 5
# candidates, one mark each (Carmen 1, Ella 2). The same single mark is then encoded on
# all three ballot formats — choose-one, 0-5 score, ranked — and counted four ways. All
# four elect Ella, and that is the point: a ballot carrying one bit per voter gives every
# method the same thing to read, so the methods cannot disagree. Andre, Blake and David
# get literally zero information expressed about them. LH-verified pre-creation; every
# race deterministic (Ella is the Condorcet winner and has a round-1 IRV majority; only
# the three winless also-rans tie, which cannot touch the winner).
_TRAD_CANDS = ["Andre", "Blake", "Carmen", "David", "Ella"]
#                        Carmen        Ella          Ella
_TRAD_STAR = [[0, 0, 5, 0, 0], [0, 0, 0, 0, 5], [0, 0, 0, 0, 5]]
_TRAD_ONE = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1]]   # choose-one: 0/1
_TRAD_RANK = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1]]  # rank 1 only; 0 = unranked
TRADITIONAL_SPEC = {
    "test_id": "BV2255",
    "title": "One mark each: the traditional choose-one ballot, counted four ways",
    "description": (
        "Three voters, five candidates, and every voter uses the 'traditional' style — one "
        "mark for a favorite, nothing for anyone else (Carmen 1, Ella 2). The same single "
        "mark is then written on all three ballot formats: choose-one, a 0-5 STAR ballot "
        "(a lone 5, four blanks), and a ranked ballot (one first choice, four blanks). Four "
        "counts, one answer — Ella wins every race. That is the lesson, and it is not a "
        "point in STAR's favour: when every ballot carries a single bit, every method has "
        "the same one bit to read, so no method can do better than choose-one. Andre, Blake "
        "and David finish on zero with nothing ever said about them, and STAR's automatic "
        "runoff has nothing left to add. A bullet vote is legal, full-weight and unspoilable "
        "— it just hands back the expressiveness the ballot was offering. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/00_start_here/STAR_Voting/voting_styles/traditional.html"),
    "races": [
        {"title": "Choose-One (Plurality) — the traditional ballot itself",
         "method": "Plurality", "num_winners": 1,
         "candidates": _TRAD_CANDS, "ballots": _TRAD_ONE},
        {"title": "STAR — the same single mark on a 0-5 score ballot",
         "method": "STAR", "num_winners": 1,
         "candidates": _TRAD_CANDS, "ballots": _TRAD_STAR},
        {"title": "RCV-IRV — the same single mark on a ranked ballot",
         "method": "IRV", "num_winners": 1, "max_rankings": 5,
         "candidates": _TRAD_CANDS, "ballots": _TRAD_RANK},
        {"title": "Ranked Robin — the same ranked ballot, every pair head-to-head",
         "method": "RankedRobin", "num_winners": 1, "max_rankings": 5,
         "candidates": _TRAD_CANDS, "ballots": _TRAD_RANK},
    ],
    "enable_write_in": False,
    "expected": "All four races -> Ella. Choose-One: Ella 2 of 3. STAR: scoring round "
                "Ella 10, Carmen 5, everyone else 0; runoff Ella 2-1 (no Equal Support). "
                "RCV-IRV: Ella has a round-1 majority (2 of 3). Ranked Robin: Ella beats "
                "all four head-to-head (the Condorcet winner); Andre, Blake and David are "
                "jointly winless.",
}

# RESULTS (2026-07-26): BV2255 -> 2jpcxd — created + 3/3 ballots × 4 races OK; all four
# races elected Ella. But the ELECTION IS ORPHANED: Adam wanted a plain single-race STAR
# illustration of the traditional voting style, not a four-method comparison. The ballots
# are right, the framing is over-built. Superseded by BV2256 (single STAR race, same
# ballots). Logged in tabulation_engines/BV/bv_api_election_creation_notes.md. Do NOT re-run.
# (Lesson: when the ask is "an example OF a ballot style," one race is the deliverable —
# a method line-up is a different lesson, and BV titles are permanent.)


# --- BV2256 — Traditional voting style: one mark each (the BV2255 redo) -----------
# The plain version: ONE STAR race, the same three bullet ballots. Backs the "What if
# everyone voted this way?" example on 01_STAR/01_Learn/voting_styles/
# traditional.md — every voter fills the 5-star ballot the old choose-one way (one 5, four
# blanks), so the scoring round is just a first-choice count and the runoff has nothing
# left to add. LH-verified: Ella 10, Carmen 5, everyone else 0; runoff Ella 2-1.
TRADITIONAL_STAR_SPEC = {
    "test_id": "BV2256",
    "title": "Traditional voting style: one mark each",
    "description": (
        "Three voters, five candidates, and every voter fills out the 5-star STAR ballot the "
        "old familiar way — one 5 for a favorite, the other four rows left blank (a blank "
        "counts as 0). One marks Carmen, two mark Ella. This is the 'traditional' voting "
        "style, and this election is deliberately an example of it done to the hilt. "
        "PLAINLY: as an approach and as a strategy this is a POOR use of a STAR ballot — "
        "unless one candidate really is your only acceptable choice, period, in which case "
        "it is exactly honest and you should vote it. Otherwise you spend 5 of the 25 points "
        "the ballot offers, say nothing about the rest of the field, and if your one pick "
        "misses the runoff your ballot has no voice in the final head-to-head. Nothing is "
        "penalized — a bullet vote is legal, full-weight and impossible to spoil, and a "
        "backup score can never hurt your favorite — you are simply choosing not to use the "
        "ballot. Watch what it costs the count: STAR's scoring round becomes nothing but a "
        "first-choice tally (Ella 10, Carmen 5, and Andre, Blake and David on 0 with nothing "
        "ever said about them), and the automatic runoff has nothing left to add — Ella "
        "beats Carmen 2-1, with nobody at Equal Support. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/00_start_here/STAR_Voting/voting_styles/traditional.html"),
    "method": "STAR",
    "num_winners": 1,
    "candidates": _TRAD_CANDS,
    "ballots": _TRAD_STAR,
    "enable_write_in": False,
    "expected": "STAR -> Ella. Scoring round Ella 10, Carmen 5, Andre/Blake/David 0; "
                "runoff Ella 2 - Carmen 1, no Equal Support (majority = 2).",
}

# RESULTS (2026-07-26): BV2256 -> c8h3tb — created + 3/3 ballots OK, STAR -> Ella.
# The plain single-race redo of BV2255. Do NOT re-run.


# --- BV2257 — Choose-One lunch vote: the simplest count, and a dead tie ----------
# Backs 06_Other/Plurality/README.md. Five coworkers, three lunches, ONE box each —
# the canonical team-lunch electorate handed the old ballot. Sushi 2 · Tacos 2 ·
# Pizza 1, and the ballots have nothing left to say. CAVEAT, deliberate: the result
# is a TIE, so unlike every other case here the winner is NOT deterministic — LH uses
# the case's pre-published lot order (-> Sushi); BV breaks a Plurality tie at RANDOM,
# so the live BV winner may be Sushi or Tacos and cannot be frozen. That divergence is
# the lesson, not a defect: with one bit per voter there is nothing to break a tie with.
_LUNCH1_CANDS = ["Sushi", "Tacos", "Pizza"]
_LUNCH1_ONE = [[1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1]]
LUNCH_CHOOSE_ONE_SPEC = {
    "test_id": "BV2257",
    "title": "Choose-One lunch vote: five coworkers, one box each, and a 2-2 tie",
    "description": (
        "The simplest voting method there is, doing its best. Five coworkers pick lunch "
        "from three options on the ballot everyone already knows: mark ONE box. Two mark "
        "Sushi, two mark Tacos, one marks Pizza. Count the marks — Sushi 2, Tacos 2, "
        "Pizza 1 — and that is the entire count. It is a dead tie, and the ballots have "
        "nothing left to say: there is no second preference to look at and no head-to-head "
        "to check, because a choose-one ballot never collected any. So a coin, or a "
        "pre-published lot order, picks lunch for five people. Note the Pizza voter: "
        "theirs is the ONE ballot that could break this tie, since they are the only person "
        "in the room with no stake in Sushi-vs-Tacos — and the ballot gave them no way to "
        "say so. Hand these same five people a 5-star ballot and they settle it themselves, "
        "with no lot at all: four of them quietly rate Pizza a 3, and STAR elects Pizza, the "
        "lunch nobody objects to (see BV2184, election fyy886). Same voters, same opinions, "
        "no strategy — the whole difference is how much the ballot let them say. This is not "
        "a knock on Choose-One: it counted its ballots perfectly, it just wasn't given much "
        "to count. Heads up: because this race is a genuine tie, BetterVoting breaks it at "
        "RANDOM, so the winner shown here may differ from the repo's copy, which uses the "
        "pre-published lot order Sushi > Tacos > Pizza. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/06_Other/Plurality/index.html"),
    "method": "Plurality",
    "num_winners": 1,
    "candidates": _LUNCH1_CANDS,
    "ballots": _LUNCH1_ONE,
    "enable_write_in": False,
    "expected": "Sushi 2 · Tacos 2 · Pizza 1 — a 2-2 tie. NOT deterministic: BV breaks "
                "the tie at random (Sushi or Tacos); LH's copy uses the published lot "
                "order and elects Sushi.",
}

# --- BV2258 / BV2259 — Exercise 15, "Read the ballot, name the method" ---
# Backs 01_STAR/05_Practice/ex15_read_the_ballot.md. Two SEPARATE elections because
# the two profiles have different electorates (35 voters vs 4) — they cannot be
# races of one election, since every BV voter votes every race.
# BV2258 = profile (a): 35 voters, Yes/No, two races on the SAME index-aligned
# ballots (Approval, then the identical marks as 5/0 scores so the head-to-head
# view prints). BV2259 = profile (b): 4 voters, 0-5 scores.
# No Ranked Robin race on either: both profiles carry ties that a ranked ballot
# cannot express without inventing preferences the voters never gave.
_EX15A_CANDS = ["Ada", "Blair", "Cosmo"]
_EX15A_APPROVE = ([[0, 1, 1]] * 15) + ([[1, 1, 0]] * 8) + ([[1, 0, 1]] * 7) + ([[0, 1, 0]] * 5)
_EX15A_STAR = ([[0, 5, 5]] * 15) + ([[5, 5, 0]] * 8) + ([[5, 0, 5]] * 7) + ([[0, 5, 0]] * 5)
EX15A_SPEC = {
    "test_id": "BV2258",
    "title": "Read the ballot, name the method: 35 voters say only Yes or No",
    "description": (
        "A puzzle before it is an election. You are handed a filled-in ballot and no method "
        "name: 35 voters, three candidates, and every voter has marked each candidate Yes or "
        "No. Which voting method is this? Two features settle it. Each candidate is marked "
        "independently with only two states, so there are no rankings and no degrees of "
        "support — that rules out every ranked and every scored method. And voters mark "
        "DIFFERENT NUMBERS of candidates: 30 of them approve two, five approve just one — "
        "which rules out choose-one and vote-for-exactly-k. Independent, binary, unlimited "
        "marks is the definition of an APPROVAL ballot. Count the Yeses and Blair wins with "
        "28 of 35, ahead of Cosmo 22 and Ada 15. Read those percentages carefully: 80 percent "
        "approve Blair and 63 percent approve Cosmo, which sums past 100 and is perfectly "
        "correct, because an approval share is a share of BALLOTS, not a slice of one pie. "
        "The second race re-reads the very same 35 ballots with each Yes written as five "
        "stars and each No as zero — nothing about any voter changes — so the head-to-head "
        "view prints. Blair beats Cosmo 13 to 7, with 15 voters expressing no preference "
        "because they approved both, and Blair beats Ada 20 to 7. The head-to-head order, "
        "Blair then Cosmo then Ada, is exactly the order of the approval totals, and that is "
        "guaranteed rather than lucky: on a ballot with only two levels, 'more voters prefer "
        "x to y' just means 'more voters approve x than y', so a Condorcet winner always "
        "exists and approval agrees with every head-to-head method. The catch worth carrying "
        "away: that guarantee is about the BALLOTS, not about the voters. Real approval "
        "ballots are compressed from richer opinions, and the compression can move the "
        "answer. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/01_STAR/exercises/ex15_read_the_ballot.html"
    ),
    "enable_write_in": False,
    "races": [
        {"title": "Which method is this? — the Yes/No count (Approval): Blair 28 of 35",
         "method": "Approval",
         "num_winners": 1, "candidates": _EX15A_CANDS, "ballots": _EX15A_APPROVE},
        {"title": "The same 35 ballots head-to-head — Blair beats Cosmo 13-7, 15 no preference",
         "method": "STAR",
         "num_winners": 1, "candidates": _EX15A_CANDS, "ballots": _EX15A_STAR},
    ],
    "expected": ("Approval -> Blair 28 (80%), Cosmo 22 (63%), Ada 15 (43%). STAR on the same "
                 "marks as 5/0 -> Blair (scoring round Blair 140 / Cosmo 110 / Ada 75; runoff "
                 "Blair 13, Cosmo 7, Equal Support 15). Blair is the Condorcet winner of the "
                 "dichotomous profile (20-7 over Ada, 13-7 over Cosmo); Cosmo beats Ada 15-8. "
                 "Both races deterministic. Test ID BV2258."),
}

_EX15B_CANDS = ["Alice", "Bruno", "Clara", "Diego"]
_EX15B_STAR = [[0, 2, 5, 4], [3, 5, 5, 3], [0, 1, 5, 4], [4, 3, 4, 2]]
EX15B_SPEC = {
    "test_id": "BV2259",
    "title": "Read the ballot, name the method: four voters score four candidates 0 to 5",
    "description": (
        "The companion puzzle to BV2258, and a deliberately uneventful election. Four voters "
        "rate four candidates on a 0 to 5 scale. Which method is this? Adding the columns and "
        "electing the highest total is SCORE voting, also called Range — and it is called a "
        "CARDINAL method because each candidate is judged against the scale rather than "
        "against the other candidates. That is what lets voter 2 rate Bruno and Clara both a "
        "five, a statement no ranking can make: a ranked ballot can only say which came "
        "first, never that two are equal or that one is far better than another. Totals: "
        "Clara 19, Diego 13, Bruno 11, Alice 7. Clara wins. This race is run as STAR because "
        "the scoring round of a STAR count IS the score-voting tally — the numbers you see "
        "in the first round are the Score result — and here the automatic runoff changes "
        "nothing at all: Clara wins it 4 to 0, and she is also the candidate who beats every "
        "rival head-to-head. Choose-one, instant runoff, approval, score and STAR all elect "
        "her, because all four voters score her top or joint-top. Nothing diverges, and that "
        "is why it is published: a library that only ever shows elections where the methods "
        "disagree would be telling you half the truth. One thing the table cannot tell you, "
        "though — who is each voter's FAVOURITE? For voters 1 and 3 it is clearly Clara, but "
        "voter 2 ties Bruno with Clara and voter 4 ties Alice with Clara, and the ballot "
        "offers no tiebreaker. You cannot rebuild a choose-one count from these ballots "
        "without inventing information the voters never gave. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/01_STAR/exercises/ex15_read_the_ballot.html"
    ),
    "method": "STAR",
    "num_winners": 1,
    "candidates": _EX15B_CANDS,
    "ballots": _EX15B_STAR,
    "enable_write_in": False,
    "expected": ("STAR -> Clara. Scoring round Clara 19 / Diego 13 / Bruno 11 / Alice 7 (that "
                 "round is the Score-voting result); runoff Clara 4, Diego 0, no Equal "
                 "Support. Clara is also the Condorcet winner and Alice the Condorcet loser. "
                 "No method diverges. Deterministic. Test ID BV2259."),
}


# --- BV2260 — Most matchups won is NOT the Condorcet winner ------------------------
# The counterexample to "if you beat more candidates head-to-head than anyone else, you
# must be the Condorcet winner." Cora wins 3 of 4 matchups — strictly the most, not tied
# — and is elected, yet Amy beats Cora 12-6. No Condorcet winner exists at all (the Smith
# set is all five). Built with NO drawn matchups on purpose, so raw wins and the Copeland
# score coincide exactly and the claim fails on its own terms rather than on tie-credit.
#
# SINGLE RankedRobin race on purpose. First choices split 6-6-6-0-0 (Cora and Erin are
# nobody's favourite), so Choose-One and RCV-IRV both deadlock three ways — their results
# here are not reproducible and there would be nothing honest to freeze. The RR race IS
# deterministic: Cora is the unique Copeland leader at 3 against 2/2/2/1, so no tiebreak
# rung is reached and LH and BetterVoting cannot diverge.
# LH-verified pre-creation; pref_voting cross-check AGREE.
_MWC_CANDS = ["Amy", "Blake", "Cora", "Diego", "Erin"]
#                    Blake>Erin>Amy>Cora>Diego / Amy>Cora>Erin>Diego>Blake / Diego>Cora>Blake>Erin>Amy
_MWC_RANK = ([[3, 1, 4, 5, 2]] * 6) + ([[1, 5, 2, 4, 3]] * 6) + ([[5, 3, 2, 1, 4]] * 6)
MOST_WINS_NOT_CONDORCET_SPEC = {
    "test_id": "BV2260",
    "title": "Winning the most head-to-head matchups is not the same as being the Condorcet winner",
    "description": (
        "Eighteen voters, five candidates, three equal blocs — a counterexample to a claim "
        "that circulates in voting-reform discussion: 'if you win head-to-head against more "
        "candidates than anyone else, you must be the Condorcet winner.' Cora wins three of "
        "four matchups, strictly more than anyone else and not tied, and is elected. And Amy "
        "beats Cora 12-6, so Cora is not the Condorcet winner — in fact nobody is, the whole "
        "field is one cycle. What IS true is only the one-way version: a Condorcet winner "
        "always has the uniquely highest Copeland score; the converse does not follow. "
        "Note there is not a single drawn matchup here, so raw wins and the Copeland score "
        "agree exactly — the claim fails on its own terms, not on a technicality about how "
        "ties are credited. A second lesson comes free: Cora has ZERO first-choice votes "
        "(they split 6-6-6-0-0) and wins anyway, because a round robin never asks who your "
        "favourite is, only which of two you prefer. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/05_Ranked_Robin/most_wins_vs_condorcet/index.html"),
    "races": [
        {"title": "Student council president — every pair head-to-head",
         "method": "RankedRobin", "num_winners": 1, "max_rankings": 5,
         "candidates": _MWC_CANDS, "ballots": _MWC_RANK},
    ],
    "enable_write_in": False,
    "expected": ("Ranked Robin -> Cora, 3-1-0, Copeland 3 (unique leader; Amy, Blake and Erin "
                 "on 2, Diego on 1). Cora beats Blake, Erin and Diego 12-6 each and LOSES to "
                 "Amy 6-12. No Condorcet winner; Smith set is all five. Every matchup is 12-6, "
                 "so every margin is identical and Minimax / Ranked Pairs / Schulze / Split "
                 "Cycle all return a five-way tie — only Copeland decides. Deterministic, no "
                 "tiebreak rung reached. Test ID BV2260."),
}


# --- BV2261 — the random tiebreak is RECORDED, not lost ---------------------------
# Purpose: a formal confirmation instrument. Both races are engineered so every
# DETERMINISTIC rung of the Ranked Robin ladder ties, forcing each engine onto its
# rung of last resort (BV: "random"; LH: pre-published lot). The question under test
# is what the BV results export preserves — and the answer is: the whole order.
# `shuffleCandidatesForRandomTiebreak.ts` seeds TinyRand with
# (rawVoteCount + hash(raceId)) >>> 0, shuffles once, and writes each candidate's
# index back as `tieBreakOrder`; the shuffled id order ships as `perm`. So the draw
# is reproducible on re-tally AND fully published — winner and runners-up.
#
# TWO races on purpose, reaching the same dead end by different routes:
#   race 1 — every pair DRAWS (all six rankings appear once: a perfectly balanced
#            electorate). W-L-T 0-0-2, Copeland 1, margin 0 for all three.
#   race 2 — every pair has a WINNER but they cycle (Anika>Beto>Cleo>Anika, all
#            4-2). W-L-T 1-1-0, Copeland 1, margin 0 for all three.
# The per-race offset in the seed should give the two races DIFFERENT perms — that
# is itself part of what this election confirms.
# LH-verified pre-creation: both races tie at Copeland 1 with margin +0 and fall to
# the lot rung. LH labels them correctly and distinctly ("a dead heat (they draw
# head-to-head, not a cycle)" vs "a Condorcet cycle").
_RTB_CANDS = ["Anika", "Beto", "Cleo"]
#  all six permutations, one voter each -> every matchup 3-3
_RTB_BALANCED = [[1, 2, 3], [3, 2, 1], [3, 1, 2], [1, 3, 2], [2, 3, 1], [2, 1, 3]]
#  2 x (Anika>Beto>Cleo), 2 x (Beto>Cleo>Anika), 2 x (Cleo>Anika>Beto) -> a cycle
_RTB_CYCLE = ([[1, 2, 3]] * 2) + ([[3, 1, 2]] * 2) + ([[2, 3, 1]] * 2)
RANDOM_TIEBREAK_RECORDED_SPEC = {
    "test_id": "BV2261",
    "title": "A three-way Ranked Robin tie: the random tiebreak is recorded, not lost",
    "description": (
        "Six voters, three candidates, two races — both built so that every "
        "deterministic step of the Ranked Robin count ties and the result has to fall "
        "through to a tiebreak of last resort. Race 1 is a perfectly balanced "
        "electorate: all six possible rankings appear exactly once, so every "
        "head-to-head draws 3-3 and all three candidates finish on a Copeland score "
        "of 1. Race 2 is a Condorcet cycle: Anika beats Beto, Beto beats Cleo and "
        "Cleo beats Anika, every one of them 4-2 — so again all three finish on 1, "
        "with identical margins. Two different routes to the same dead end. "
        "What this election is really testing is what the results export preserves. "
        "BetterVoting's random tiebreak is deterministic by design: the candidate "
        "order is shuffled once from a seed built out of the ballot count plus a "
        "per-race offset, and that shuffled order is published in the results as "
        "'perm', with each candidate's place in it stored as 'tieBreakOrder'. So the "
        "export does not merely name a winner — it records the entire tiebreak "
        "sequence, runners-up included, and re-running the count returns the same "
        "answer. The two races use different offsets, so their orders should differ. "
        "The library's own tabulation replays each recorded order as a pre-published "
        "lot and reproduces BetterVoting's winner, and its full ordering, exactly. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/05_Ranked_Robin/rr_tiebreaks/index.html"),
    "races": [
        {"title": "Mural commission — a perfectly balanced electorate (every pair draws)",
         "method": "RankedRobin", "num_winners": 1, "max_rankings": 3,
         "candidates": _RTB_CANDS, "ballots": _RTB_BALANCED},
        {"title": "Mural commission — a Condorcet cycle (every pair has a winner)",
         "method": "RankedRobin", "num_winners": 1, "max_rankings": 3,
         "candidates": _RTB_CANDS, "ballots": _RTB_CYCLE},
    ],
    "enable_write_in": False,
    "expected": ("BOTH races: a three-way tie at Copeland 1 with margin +0 for Anika, "
                 "Beto and Cleo, so no deterministic rung separates them. Race 1 is "
                 "0-0-2 each (all pairs draw 3-3); race 2 is 1-1-0 each (Anika>Beto, "
                 "Beto>Cleo, Cleo>Anika, all 4-2). BV must report tieBreakType "
                 "'random' on both and publish `perm` + `tieBreakOrder`; the two "
                 "races should get DIFFERENT perms (per-race seed offset). Winner is "
                 "whichever candidate BV's perm puts first — not predictable from the "
                 "ballots, but recorded and stable on re-tally. LH reproduces each "
                 "race exactly when lot_numbers is pinned to that race's perm. "
                 "Test ID BV2261."),
}


# --- BV2262 — the same confirmation at NINE candidates ----------------------------
# BV2261 proved the tiebreak order is recorded and replayable on 3 candidates. This
# is the scale check Adam asked for: nine candidates, a nine-way dead end, does the
# export still pin the winner?
#
# The profile is a round table. Nine club members are the nine candidates, and each
# one ranks themselves first and then continues clockwise around the table — a single
# cyclic rotation per voter. That construction makes the dead heat exact rather than
# fiddled: for candidates X and Y at cyclic distance d, exactly 9-d voters prefer X,
# so X beats the four members that follow them and loses to the four that precede
# them. Every candidate finishes 4-4-0 (Copeland 4), and each one's margins are
# +7,+5,+3,+1 against -7,-5,-3,-1 — a net of +0 for all nine. So Copeland ties, the
# margin rung ties, and BV's head-to-head rung cannot apply (it is 2-way only, and
# nine are tied). Both engines must reach their rung of last resort.
# LH-verified pre-creation: 9-way tie at Copeland 4, margin +0 for all, falls to lot.
_RT9_CANDS = ["Alice", "Boris", "Carmen", "Dmitri", "Elena",
              "Felix", "Greta", "Hugo", "Ivan"]
#  voter i ranks candidate i first, then clockwise: rank of candidate j is
#  ((j - i) mod 9) + 1
_RT9_RANKS = [[((j - i) % 9) + 1 for j in range(9)] for i in range(9)]
RANDOM_TIEBREAK_NINE_SPEC = {
    "test_id": "BV2262",
    "title": "Nine candidates, a nine-way dead heat: does the recorded tiebreak still pin the winner?",
    "description": (
        "Nine club members sit around a table, and all nine are candidates for chair. "
        "Each member ranks themselves first and then continues clockwise, so the nine "
        "ballots are nine rotations of the same order. That makes the deadlock exact: "
        "every member beats the four who follow them and loses to the four who "
        "precede them, so all nine finish 4-4-0 on a Copeland score of 4, and every "
        "single one has a net margin of exactly zero (+7, +5, +3, +1 against -7, -5, "
        "-3, -1). Nothing in the ballots separates them, and no pairwise result is "
        "even close to a draw — this is a nine-way Condorcet cycle, not a set of "
        "tied matchups. "
        "It is a scale test for a claim confirmed earlier at three candidates: that "
        "BetterVoting's tiebreak of last resort, labelled 'random', is a seeded "
        "shuffle whose result is published in the export as 'perm', with each "
        "candidate's place stored as 'tieBreakOrder'. The export should therefore "
        "record the full nine-deep order rather than just a winner, return the same "
        "answer on a re-tally, and let an independent tabulation reproduce the "
        "winner exactly by replaying that order as a pre-published lot. "
        "Worth saying plainly: who wins here is decided by the shuffle, not by the "
        "voters, and no argument about how people voted can rest on it. The point of "
        "the election is what gets recorded, not who gets elected. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/05_Ranked_Robin/rr_tiebreaks/index.html"),
    "races": [
        {"title": "Club chair — nine members, nine candidates, one round table",
         "method": "RankedRobin", "num_winners": 1, "max_rankings": 9,
         "candidates": _RT9_CANDS, "ballots": _RT9_RANKS},
    ],
    "enable_write_in": False,
    "expected": ("A nine-way tie: every candidate 4-4-0, Copeland 4, net margin +0, so "
                 "no deterministic rung separates anyone and BV's 2-way head-to-head "
                 "rung cannot apply. BV must report tieBreakType 'random' and publish a "
                 "nine-deep `perm` with matching `tieBreakOrder` values 0..8; `other[]` "
                 "should list the eight losers in that same order. Winner = whoever "
                 "`perm` puts first — recorded and stable on re-tally, but not "
                 "derivable from the ballots. LH must reproduce that winner exactly "
                 "when lot_numbers is pinned to `perm`, and bv_replay_tiebreak.py must "
                 "recompute `perm` from (9 ballots + raceId) alone. Test ID BV2262."),
}


# --- BV1835 — 100 voters, 4 seats: the score leader wins nothing ------------------
# Sass's Bloc STAR example, the first case in 02_STAR_Bloc at a realistic electorate
# (every other case there is 2-16 ballots). Two camps of 49 mirror each other, and a
# 2-ballot swing bloc decides all four seats.
#
# Ava is scored 3 by 98 of the 100 voters and leads the score round in EVERY round
# (294, sixty-three clear of the runner-up) — and takes NO seat, losing all four
# automatic runoffs 51-49. Each camp of 49 prefers Ava to the other camp's people, so
# the 2 swing ballots (who score Ava 0) are what turns 49-49 into 51-49, four times.
# The lesson is the runoff step: Bloc STAR fills seats by who is PREFERRED, and a
# broadly-liked compromise who is nobody's first choice can be shut out completely.
# LH-verified pre-creation: winners Bianca, Cedric, Deegan, Eli; all four runoffs 51-49.
_SASS_CANDS = ["Ava", "Bianca", "Cedric", "Deegan", "Eli"]
_SASS_BLOCS = [(25, [3, 5, 4, 0, 0]), (24, [3, 4, 5, 0, 0]),
               (25, [3, 0, 0, 5, 4]), (24, [3, 0, 0, 4, 5]),
               (2,  [0, 5, 4, 3, 2])]
BLOC_SASS_100_SPEC = {
    "test_id": "BV1835",
    "title": "Committee election, 100 voters, 4 seats: the highest-scoring candidate wins no seat",
    "description": (
        "A hundred voters fill four committee seats by Bloc STAR — the same 0-5 STAR "
        "ballot, counted once per seat, removing each winner before the next round. "
        "The electorate splits into two even camps of 49 who share no candidates, plus "
        "two voters who break every tie. "
        "Ava is the compromise: 98 of the 100 voters give her a 3, and she leads the "
        "score round of all four rounds by a wide margin (294 against 231, 228, 227, "
        "224). She wins nothing. In each round she reaches the automatic runoff and "
        "loses it 51-49, because 'scored well by nearly everyone' is not the same as "
        "'preferred head to head' — each camp of 49 ranks its own two candidates above "
        "her, and the two swing voters score her 0. "
        "The point is what the runoff step does: Bloc STAR awards a seat to whoever is "
        "PREFERRED by more voters, not to whoever accumulates the most points, so a "
        "broadly acceptable candidate who is nobody's favourite can be shut out of a "
        "four-seat body entirely. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/02_STAR_Bloc/index.html"),
    "method": "STAR",
    "num_winners": 4,
    "candidates": _SASS_CANDS,
    "ballots": _rows(_SASS_BLOCS),
    "enable_write_in": False,
    "expected": (
        "Winners Bianca, Cedric, Deegan, Eli — in that seat order. Scores: Ava 294, "
        "Bianca 231, Cedric 228, Deegan 227, Eli 224. Ava is the score leader in all "
        "four scoring rounds and loses all four automatic runoffs 51-49 (100 of 100 "
        "voters express a preference each time; no Equal Support). No ties, no lot — "
        "the whole result is deterministic. BV stores this as voting_method 'STAR' "
        "with num_winners 4, i.e. 'Bloc STAR' appears nowhere in the export (#1086). "
        "Cross-check: Stevan Leonard ran the same 100 ballots through EPRv3 in Sep 2023 "
        "and got the same four winners in the order B, D, C, E. Test ID BV1835."),
}


# BV2263 — the ceiling case, and the single-seat twin of BV1815 (fk38pk). One
# candidate holds every point on every ballot, so score share, ballot share and
# decided-voter share all read 100% — the one election where "over 50%" means the
# same thing on every denominator, which is what makes it the control for reading
# any other result. Backs 01_STAR/02_Examples/cases/over_50_percent_star_c3_b3.yaml
# (LH-only until now; the file keeps its descriptive name, since its page URL is
# already published in bettervoting#1471 and a rename would 404 it).
OVER_50_PERCENT_SPEC = {
    "test_id": "BV2263",
    "title": "Over 50% — every point on every ballot",
    "description": (
        "Three voters, three candidates, and one candidate who takes everything on offer: "
        "A is scored 5 by all three voters, one voter gives B a single point, and nobody "
        "scores C at all. Scoring round: A 15 of a possible 15, B 1, C 0, so A and B "
        "advance. Automatic runoff: all three ballots prefer A, 3-0, with nobody at Equal "
        "Support. "
        "The election exists to be the CONTROL, not a surprise. A STAR result can be read "
        "against three different denominators — share of the maximum possible score, share "
        "of all ballots in the runoff, and share of the voters who expressed a preference "
        "between the two finalists — and this is the one case where all three give the same "
        "answer: 100%. Anywhere else they come apart, and the moment a ballot rates the two "
        "finalists equally they must. "
        "Note also what did NOT happen: the count did not stop early. A held every point on "
        "every ballot and was still put through the automatic runoff, because the scoring "
        "round only ever picks the two finalists — it never elects anyone. "
        "The multi-seat twin is BV1815 (bettervoting.com/fk38pk/results), where a candidate "
        "with 12 of 15 points wins the first of two seats and the second goes to a candidate "
        "on 2 points, after a runoff that ends in a tie. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/01_STAR/02_Examples/cases/cases_pages/over_50_percent_star_c3_b3.html"),
    "method": "STAR",
    "num_winners": 1,
    "candidates": ["A", "B", "C"],
    "ballots": [[5, 0, 0], [5, 1, 0], [5, 0, 0]],
    "enable_write_in": False,
    "expected": (
        "STAR -> A. Scoring round A 15 (average 5.0), B 1, C 0; automatic runoff A 3 - B 0 "
        "with 0 Equal Support (3 of 3 voters express a preference; majority = 2). All three "
        "denominators read 100%. No tie, no rung of the ladder consulted. Test ID BV2263."),
}


# ---------------------------------------------------------------------------
# BV2105-r2 — the ice cream abstention re-check.
#
# A deliberate RE-RUN of BV2105 (r4dqvd, minted 2025-10-31) on the SAME four
# ballots. That election reported nTallyVotes 2 / nAbstentions 2: it filed the
# partial ballot "Vanilla 1, rest blank" as an abstention alongside the genuinely
# blank one, and Vanilla's score came out as an average over 2 ballots instead of
# 3. That counting defect is filed as bettervoting#1478 (2026-08-04). (It is
# NOT #1056 —
# the library mis-cited it for a year; #1056 is a demo-election 401 on ballot
# download, closed via #1058. They share only the BV2105 test-doc name.)
#
# Why a new election rather than a re-fetch: re-fetching r4dqvd today still
# returns nTallyVotes 2 / nAbstentions 2, but that election is `closed` and its
# stored ElectionResult may simply be the tally computed back in 2025 — a
# re-fetch cannot distinguish "the bug is still live" from "we are reading a
# 2025 result." Only ballots cast through TODAY's tabulator can.
#
# Why the repo's other exports cannot answer it either: the discriminating shape
# is a ballot whose non-blank marks are ALL EQUAL (here a single "1"), because
# that is what #884's all-equal rule mistakes for an abstention. The only other
# 2026-minted export with a partial ballot is BV215 (26khr3), whose partial is
# "Ada 5, Bruno 1, blank" — two DISTINCT marks, so it counts under the buggy
# rule and a fixed one alike. It settles nothing.
#
# Reads as a real election on its own terms (a 3-flavour ice cream vote, 2 seats),
# so the permanent public title stands up without needing the bug context.
# ---------------------------------------------------------------------------
ICE_CREAM_ABSTENTION_RECHECK_SPEC = {
    "test_id": "BV2105-r2",
    "title": "Favorite ice cream (Bloc STAR): the partial ballot re-check",
    "description": (
        "Three flavours, two seats, four voters, scored 0-5. This is a deliberate re-run of "
        "an earlier election (bettervoting.com/r4dqvd/results) on exactly the same four "
        "ballots, cast again so they are counted by today's tabulator. "
        "The ballots are chosen so that each one is a different KIND of ballot. One voter "
        "scores everything 5. One leaves the whole ballot blank — a true abstention, nobody "
        "scored. One scores Vanilla 1 and leaves the other two blank — a real vote, cast by "
        "a voter who rated exactly one flavour. One fills the ballot out normally: Vanilla 2, "
        "Chocolate 5, Strawberry 4. "
        "The winners are not in question and do not depend on any of this: Chocolate takes "
        "the first seat, and the second seat is a Vanilla/Strawberry runoff tie broken by "
        "score, 9 to 8, for Strawberry. "
        "What the election actually measures is the COUNT rather than the winner — whether "
        "that third ballot is recorded as a vote or as an abstention. It is the smallest "
        "ballot that can tell the difference, because its only mark is a single 1: a rule "
        "that treats an all-equal ballot as an abstention cannot tell that ballot apart from "
        "an empty one, while a voter plainly did rate a flavour. Read it off the tallied-ballot "
        "and abstention counts on the results page: 3 and 1 if the partial ballot is counted, "
        "2 and 2 if it is not. Vanilla's reported average is the corroborating figure — it is "
        "taken over three ballots (5, 1 and 2) once the single point is added, and over only "
        "two (5 and 2) if that ballot is dropped. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/02_STAR_Bloc/02_Examples/index.html"),
    "method": "STAR",          # BV has no separate "Bloc STAR" string: STAR + num_winners > 1
    "num_winners": 2,
    "candidates": ["Vanilla", "Chocolate", "Strawberry"],
    # `None` serialises to JSON null — a blank score slot, NOT a zero. That
    # distinction is the entire experiment; do not "clean up" these to 0.
    "ballots": [
        [5, 5, 5],              # loves everything
        [None, None, None],     # fully blank — a TRUE abstention
        [1, None, None],        # Vanilla=1, rest blank — a REAL partial vote (the probe)
        [2, 5, 4],              # an ordinary full ballot
    ],
    "enable_write_in": False,   # a write-in would add a fourth column to the probe ballot
    "expected": (
        "Winners Chocolate, Strawberry either way — seat 1 to Chocolate, seat 2 by score "
        "tiebreak, Strawberry 9 > Vanilla 8. The count is the probe. FIXED looks like "
        "nTallyVotes 3 / nAbstentions 1, Vanilla averaged over 3 ballots (8/3). STILL BROKEN "
        "looks like nTallyVotes 2 / nAbstentions 2, Vanilla over 2 ballots (7/2) — the exact "
        "shape BV2105 recorded in 2025, where BV displayed that as `score: 3` (it floors the "
        "average: Strawberry's 9/2 displayed as 4). LH counts 4 ballots, 1 abstention, "
        "Vanilla total 8. "
        "Test ID BV2105-r2; re-run of BV2105 (r4dqvd); evidence for bettervoting#1478."),
}


# --- BV2270 — the head-to-head rung, and where the two tied candidates SIT --------
# Purpose: a display-layer probe, not a tabulation probe. The WINNER here is fully
# determined by the ballots — no lot, no shuffle — because the Copeland tie at the
# top is exactly two candidates with a decisive match between them, which is BV's
# rung 2 (head-to-head). What is NOT determined by the ballots is the ORDER the two
# tied candidates appear in on the results page: `getSummaryData` sorts by
# copelandScore then `tieBreakOrder`, and `tieBreakOrder` is the seeded shuffle
# (rawVoteCount + hash(raceId)), which knows nothing about who beat whom.
#
# BetterVoting's results page stars/gold-highlights by ROW POSITION, so when the
# shuffle puts the head-to-head LOSER first, the heading names one candidate and the
# star sits on the other. That is the defect this election is minted to exhibit;
# see bettervoting-qa issues/rr-winner-highlight-positional-vs-elected.md and #1166.
#
# Three voters, four candidates. Pairwise: Alder>Birch 2-1, Alder>Cedar 2-1,
# Dogwood>Alder 2-1, Birch>Cedar 3-0, Birch>Dogwood 2-1, Cedar>Dogwood 2-1.
# Copeland: Alder 2, Birch 2, Cedar 1, Dogwood 1 -> tie {Alder, Birch}, Alder wins
# the runoff. NOTE: the shuffle re-rolls on every ballot cast ("the tiebreak priority
# is reset after every vote"), so a MIRROR PAIR of ballots (one ranking + its exact
# reverse) re-rolls the display order while leaving every pairwise winner and every
# Copeland score untouched — that is the intended way to re-roll this election if the
# first draw happens to agree with the head-to-head result.
_HHT_CANDS = ["Alder", "Birch", "Cedar", "Dogwood"]
#  ranks per candidate slot, 1 = top:  Alder>Birch>Cedar>Dogwood, etc.
_HHT_BALLOTS = [[1, 2, 3, 4],   # Alder  > Birch  > Cedar   > Dogwood
                [4, 1, 2, 3],   # Birch  > Cedar  > Dogwood > Alder
                [2, 3, 4, 1]]   # Dogwood > Alder > Birch   > Cedar
HEAD_TO_HEAD_ROW_ORDER_SPEC = {
    "test_id": "BV2270",
    "title": "Ranked Robin: two candidates tie on pairwise wins, and the head-to-head settles it",
    "description": (
        "Three voters rank four trees for a street-planting commission, and the count "
        "lands on the middle rung of Ranked Robin's tiebreak ladder — the one that is "
        "usually skipped past. Alder and Birch finish level on pairwise wins: Alder "
        "beats Birch and Cedar but loses to Dogwood; Birch beats Cedar and Dogwood but "
        "loses to Alder. Two wins each. Cedar and Dogwood have one each. "
        "A three-way tie would fall through to a random draw, but a tie of exactly two "
        "does not have to: Alder and Birch played each other, and Alder won that match "
        "2-1, so BetterVoting settles it head-to-head and elects Alder. Nothing here "
        "rests on chance — the winner follows from the ballots alone, and any reader "
        "can check it by hand from the six matchups. "
        "What does NOT follow from the ballots is the ORDER the two tied candidates "
        "appear in on the results page. Candidates are sorted by pairwise wins and "
        "then by BetterVoting's tiebreak order, which is a shuffle seeded from the "
        "ballot count and the race id — deterministic, published in the results export, "
        "and carrying no information at all about who beat whom. So the head-to-head "
        "winner may be listed second. This election exists to make that visible. "
        "Display-layer analysis and follow-up: "
        "https://github.com/masiarek/bettervoting-qa/blob/master/issues/rr-winner-highlight-positional-vs-elected.md "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/05_Ranked_Robin/03_Criteria/rr_tiebreaks/index.html"),
    "method": "RankedRobin",
    "num_winners": 1,
    "max_rankings": 4,
    "enable_write_in": False,  # a write-in would add a fifth candidate and break the tie by 3
    "candidates": _HHT_CANDS,
    "ballots": _HHT_BALLOTS,
    "expected": (
        "Copeland: Alder 2, Birch 2, Cedar 1, Dogwood 1. Exactly two tied at the top "
        "with a decisive match between them, so tieBreakType stays 'none' and the log "
        "should read 'Alder preferred over Birch in runoff.' Winner: ALDER, derivable "
        "from the ballots. The open variable is `tieBreakOrder`: if Birch draws the "
        "lower value, Birch is row 0 and the results page will star and gold-highlight "
        "BIRCH while the heading says Alder wins — the defect under test. If Alder "
        "draws it, the page looks correct and the election needs a mirror pair of "
        "ballots to re-roll the seed. Test ID BV2270."),
}


# --- BV2271 / BV2272 — Satisfaction Approval Voting (Brams & Kilgour 2010) -----
# SOURCE: Brams, S. J. & Kilgour, D. M., "Satisfaction Approval Voting", MPRA
# Paper 22709 (Apr 2010), sections 2 and its Propositions 2 and 5. SAV gives each
# voter ONE vote, split evenly among the candidates they approved (approve n, each
# gets 1/n); the top k satisfaction scores win.
#
# BetterVoting does NOT implement SAV — these two elections carry the three
# BV methods that DO read this ballot (Approval, STAR, Ranked Robin, all bloc at
# 2 seats), so the lesson page can answer "do the real methods agree?" (they do,
# within each election) against the SAV committee computed off-platform with
# Lackner's abcvoting. Every race below is tie-free in its WINNER SET.
#
# Score encodings per race, aligned by voter index across all three races:
#   Approval = 0/1 ; STAR = 0-5 ; RankedRobin = ranks 1..max_rankings (0 = unranked)
# The STAR/ranked races REFINE the approval ballot (they add a within-slate
# preference the approval ballot cannot express); the approval sets are exactly
# the paper's. That refinement is stated on the lesson page.

_SAV_P2_CANDS = ["Ada", "Ben", "Cleo", "Dev"]
# 4 voters approve the Ada+Ben slate (3 prefer Ada, 1 prefers Ben), 3 bullet Cleo,
# 3 bullet Dev.  AV -> Ada,Ben (4,4 vs 3,3).  SAV -> Cleo,Dev (2,2 vs 3,3).
_SAV_P2_APPROVAL = ([[1, 1, 0, 0]] * 4 + [[0, 0, 1, 0]] * 3 + [[0, 0, 0, 1]] * 3)
_SAV_P2_STAR = ([[5, 4, 0, 0]] * 3 + [[4, 5, 0, 0]] * 1
                + [[0, 0, 5, 0]] * 3 + [[0, 0, 0, 5]] * 3)
_SAV_P2_RANK = ([[1, 2, 0, 0]] * 3 + [[2, 1, 0, 0]] * 1
                + [[0, 0, 1, 0]] * 3 + [[0, 0, 0, 1]] * 3)

SAV_DISJOINT_SPEC = {
    "test_id": "BV2271",
    "title": ("Satisfaction Approval Voting, Proposition 2 — the committee with "
              "nothing in common"),
    "description": (
        "Brams & Kilgour's own worked example (Satisfaction Approval Voting, MPRA "
        "22709, 2010, section 2), the proof of their Proposition 2: AV and SAV can "
        "elect DISJOINT committees from identical ballots. Ten voters, four "
        "candidates, TWO seats. Four voters approve the Ada+Ben slate; three bullet-"
        "vote Cleo; three bullet-vote Dev. Bloc Approval gives every mark a whole "
        "vote — Ada 4, Ben 4, Cleo 3, Dev 3 — and seats Ada and Ben. SAV gives each "
        "BALLOT one vote split among its marks, so the slate voters contribute a half "
        "each: Ada 2, Ben 2, Cleo 3, Dev 3 — and it seats Cleo and Dev. Not one "
        "candidate in common. BetterVoting has no SAV tabulator, so the three races "
        "here are the methods that DO read this electorate: Approval, STAR and Ranked "
        "Robin, all bloc at 2 seats. The question the lesson asks is whether they "
        "agree with each other — they do, all three seating Ada and Ben, which makes "
        "SAV the lone dissenter rather than AV the outlier. The STAR and ranked "
        "ballots add a within-slate preference (3 of the 4 slate voters prefer Ada) "
        "that the approval ballot cannot express; the approval sets are exactly the "
        "paper's. Full lesson & tabulation: https://masiarek.github.io/star-voting-"
        "library/04_Approval/01_Learn/Multiwinner_Approval/satisfaction_approval_voting.html"),
    "races": [
        {"title": "Brams & Kilgour Prop. 2 — Approval (bloc, 2 seats)",
         "method": "Approval", "num_winners": 2,
         "candidates": _SAV_P2_CANDS, "ballots": _SAV_P2_APPROVAL},
        {"title": "Brams & Kilgour Prop. 2 — STAR (bloc, 2 seats)",
         "method": "STAR", "num_winners": 2,
         "candidates": _SAV_P2_CANDS, "ballots": _SAV_P2_STAR},
        {"title": "Brams & Kilgour Prop. 2 — Ranked Robin (bloc, 2 seats)",
         "method": "RankedRobin", "num_winners": 2,
         "max_rankings": len(_SAV_P2_CANDS),
         "candidates": _SAV_P2_CANDS, "ballots": _SAV_P2_RANK},
    ],
    "expected": (
        "All three races -> Ada, Ben. Approval 4/4/3/3. Bloc STAR: seat 1 scoring "
        "Ada 19, Ben 17, Cleo 15, Dev 15, runoff Ada 3 - Ben 1 (6 Equal Support); "
        "seat 2 has a Cleo/Dev finalist tie at 15 that Ben beats either way (4-3), so "
        "the WINNER is tiebreak-independent. Bloc RR: Ada 3-0-0, Ben 2-1-0, then a "
        "Cleo/Dev tie for third that does not touch the seats. SAV (abcvoting, "
        "off-platform) -> Cleo, Dev. PAV ties {Ada,Cleo}/{Ada,Dev}/{Ben,Cleo}/"
        "{Ben,Dev}. LH-verified on all three. Test ID BV2271."),
}

_SAV_P5_CANDS = ["Ash", "Bree", "Cole"]
# 5 approve Ash+Bree, 5 approve Ash+Cole, 4 bullet Bree, 3 bullet Cole.
# AV -> Ash,Bree (10,9,8).  SAV -> Bree,Cole (5, 6 1/2, 5 1/2) — represents all 17.
_SAV_P5_APPROVAL = ([[1, 1, 0]] * 5 + [[1, 0, 1]] * 5
                    + [[0, 1, 0]] * 4 + [[0, 0, 1]] * 3)
_SAV_P5_STAR = ([[5, 4, 0]] * 5 + [[5, 0, 4]] * 5
                + [[0, 5, 0]] * 4 + [[0, 0, 5]] * 3)
_SAV_P5_RANK = ([[1, 2, 0]] * 5 + [[1, 0, 2]] * 5
                + [[0, 1, 0]] * 4 + [[0, 0, 1]] * 3)

SAV_COVERAGE_SPEC = {
    "test_id": "BV2272",
    "title": ("Satisfaction Approval Voting, Proposition 5 — the most-approved "
              "candidate nobody needs to seat"),
    "description": (
        "Brams & Kilgour, Satisfaction Approval Voting (MPRA 22709, 2010), "
        "Proposition 5: SAV can find a minimal representative set where bloc Approval "
        "cannot. Seventeen voters, three candidates, TWO seats. Five voters approve "
        "Ash and Bree, five approve Ash and Cole, four bullet-vote Bree, three bullet-"
        "vote Cole. Bloc Approval counts Ash 10, Bree 9, Cole 8 and seats Ash and "
        "Bree — leaving the three Cole-only voters with no representative at all. SAV "
        "splits each ballot's single vote among its marks, so Ash (approved by the ten "
        "slate voters and nobody else) collects only 5, while Bree gets 6 1/2 and Cole "
        "5 1/2 by combining half-votes with the WHOLE votes of bullet voters: SAV "
        "seats Bree and Cole, the smallest pair that represents all seventeen voters. "
        "The most-approved candidate in the field wins no seat, because every one of "
        "Ash's supporters already has a second choice seated. BetterVoting has no SAV "
        "tabulator; the three races here are Approval, STAR and Ranked Robin (all bloc "
        "at 2 seats), so the lesson can show that the methods people actually use all "
        "land on Ash and Bree. The STAR and ranked ballots add the within-slate "
        "preference the approval ballot cannot express; the approval sets are exactly "
        "the paper's. Full lesson & tabulation: https://masiarek.github.io/star-voting-"
        "library/04_Approval/01_Learn/Multiwinner_Approval/satisfaction_approval_voting.html"),
    "races": [
        {"title": "Brams & Kilgour Prop. 5 — Approval (bloc, 2 seats)",
         "method": "Approval", "num_winners": 2,
         "candidates": _SAV_P5_CANDS, "ballots": _SAV_P5_APPROVAL},
        {"title": "Brams & Kilgour Prop. 5 — STAR (bloc, 2 seats)",
         "method": "STAR", "num_winners": 2,
         "candidates": _SAV_P5_CANDS, "ballots": _SAV_P5_STAR},
        {"title": "Brams & Kilgour Prop. 5 — Ranked Robin (bloc, 2 seats)",
         "method": "RankedRobin", "num_winners": 2,
         "max_rankings": len(_SAV_P5_CANDS),
         "candidates": _SAV_P5_CANDS, "ballots": _SAV_P5_RANK},
    ],
    "expected": (
        "All three races -> Ash, Bree. Approval 10/9/8. Bloc STAR: seat 1 scoring Ash "
        "50, Bree 40, Cole 35, runoff Ash 10 - Bree 4; seat 2 runoff Bree 9 - Cole 8. "
        "Bloc RR: Ash 2-0-0 (beats Bree 10-4, Cole 10-3), Bree 1-1-0 (beats Cole 9-8), "
        "Cole 0-2-0 — no ties anywhere. SAV (abcvoting, off-platform) -> Bree, Cole, "
        "representing all 17; PAV agrees with SAV here. LH-verified on all three. "
        "Test ID BV2272."),
}


# --- The founding distortion impossibility: two electorates, one ranked ballot ---
# Procaccia & Rosenschein, "The Distortion of Cardinal Preferences in Voting"
# (CIA 2006), Proposition 1: EVERY social choice function has distortion > 1 at
# 3 voters and 2 candidates. The proof is a matched pair of utility profiles that
# induce the SAME rankings and have OPPOSITE welfare-maximizing winners.
#
# Why this is one election with three races rather than two elections: the paper's
# construction is the same three voters twice, and BV's multirace shape aligns
# ballots by voter index — which is exactly the claim. Races 1 and 2 are the two
# score profiles; race 3 is the ranking they share, and there is only ONE of it
# because the rankings are identical. That asymmetry (two score races, one ranked
# race) IS Proposition 1 rendered as a ballot.
#
# Every voter spends exactly 5 points in both score races — the paper's unit-sum
# normalization, which on a 0-5 ballot reads as "everyone gets the same ink."
# Nothing here rests on a tie-break: every race is decided 2-1.
SAME_RANKS_DISTORTION_SPEC = {
    "test_id": "BV2273",
    "title": "Same ranks, different utilities — two elections a ranked ballot cannot tell apart",
    "description": (
        "Three voters, two candidates, and the smallest impossibility result in voting theory. "
        "This election reproduces Proposition 1 of Procaccia & Rosenschein, 'The Distortion of "
        "Cardinal Preferences in Voting' (2006) — the paper that defined 'distortion' — which "
        "proves that NO voting rule reading only rankings can always elect the candidate who "
        "maximizes total voter satisfaction, and needs only 3 voters and 2 candidates to prove it. "
        "Races 1 and 2 are two different electorates. In race 1 the two A-voters are lukewarm "
        "(A 3, B 2) and the B-voter is devoted (A 0, B 5); in race 2 nobody is lukewarm (A 5, B 0 "
        "and A 0, B 5). Every voter spends exactly 5 points in both, so no voter has more "
        "influence than another. Now read the rankings: both races are A>B, B>A, A>B — identical, "
        "mark for mark. That is why race 3, the Ranked Robin race, appears only ONCE: a ranked "
        "ballot cannot tell these two elections apart, so there is only one ranked contest to run. "
        "The totals, however, point opposite ways. In race 1 candidate B carries 9 points to A's 6, "
        "so B is the candidate who maximizes total satisfaction; in race 2 candidate A carries 10 "
        "to B's 5. Any method that reads only order must return the same winner in both, and no "
        "single answer is right in both. "
        "DO NOT read this election for who won — all three races elect A, and that is the point "
        "rather than the result. Watch the SCORING ROUNDS instead: race 1 shows B ahead 9 to 6 and "
        "then the automatic runoff elects A anyway, because with only two candidates STAR's runoff "
        "is plain majority rule and two of the three voters prefer A. STAR measures the intensity "
        "and declines to elect on it — the majority guarantee is what it buys with that. Pure Score "
        "voting, which elects the point leader outright, would split these two races (B, then A) "
        "and match the utility optimum in both. "
        "The lesson is not that one method failed. It is that two genuinely different electorates "
        "produced the same three ranked ballots, so the loss lives in the ballot rather than in "
        "the count — which is also why this result sits comfortably beside May's theorem, whose "
        "conditions are stated over ranked input. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/method_comparisons/same_ranks_different_utilities/index.html"
    ),
    "enable_write_in": False,   # a third candidate would void the 2-candidate construction
    "races": [
        {
            "title": "Profile 1 — the lukewarm majority (scores 0-5)",
            "method": "STAR",
            "num_winners": 1,
            "candidates": ["A", "B"],
            "ballots": [
                [3, 2],   # voter 1 — mildly prefers A
                [0, 5],   # voter 2 — devoted to B
                [3, 2],   # voter 3 — mildly prefers A
            ],
        },
        {
            "title": "Profile 2 — the polarized electorate (scores 0-5)",
            "method": "STAR",
            "num_winners": 1,
            "candidates": ["A", "B"],
            "ballots": [
                [5, 0],   # voter 1 — all-in for A
                [0, 5],   # voter 2 — devoted to B
                [5, 0],   # voter 3 — all-in for A
            ],
        },
        {
            "title": "The ranking BOTH profiles share (Ranked Robin)",
            "method": "RankedRobin",
            "num_winners": 1,
            "max_rankings": 2,
            "candidates": ["A", "B"],
            "ballots": [
                [1, 2],   # voter 1 — A first, B second
                [2, 1],   # voter 2 — B first, A second
                [1, 2],   # voter 3 — A first, B second
            ],
        },
    ],
    "expected": (
        "All three races elect A, decisively and with no tie-break anywhere. Race 1: scoring "
        "round B 9, A 6 (B leads), automatic runoff A 2 - B 1 -> A, a Runoff Reversal on three "
        "ballots. Race 2: scoring round A 10, B 5, runoff A 2 - B 1 -> A, no reversal. Race 3: "
        "A beats B 2-1 head-to-head -> A. The teaching content is the CONTRAST between the two "
        "scoring rounds against the single shared ranking, not the winner. LH agrees on all "
        "three (STAR path for races 1-2, Ranked Robin for race 3). Test ID BV2273."),
}


ELECTIONS: list = []   # resting state — point this at a spec only for the run that mints it
# Previously: [SAME_RANKS_DISTORTION_SPEC]   # BV2273 -> 9kffcv
#   Created as designed, 3 ballots × 3 races. BV agrees with LH on all three races
#   (all elect A) and reports tieBreakType 'none' everywhere — nothing in this
#   election rests on a tie-break, which matters because the lesson is the contrast
#   between the two scoring rounds, not the winner. BV's own results page renders it
#   perfectly: race 1's Scoring Round shows B 9 / A 6 and the Automatic Runoff still
#   elects A, and BV volunteers its "Why is the top scoring candidate different from
#   the winner?" explainer unprompted.
# Previously: [SAV_DISJOINT_SPEC, SAV_COVERAGE_SPEC]   # BV2271 -> 4hfwqd, BV2272 -> dr6fmg
#   Both created as designed. BV agrees with LH on all six races: BV2271 all three ->
#   Ada, Ben (the STAR race reports tieBreakType 'random' for the Cleo/Dev FINALIST tie
#   at 15, but Ben beats either finalist 4-3, so the winner set is tiebreak-independent);
#   BV2272 all three -> Ash, Bree with tieBreakType 'none' everywhere. SAV — which BV does
#   not implement — elects Cleo,Dev and Bree,Cole respectively (abcvoting, off-platform).
# Previously: [HEAD_TO_HEAD_ROW_ORDER_SPEC]   # BV2270 — head-to-head rung vs row order
#   (created -> 8h4bvh). Result as designed: Copeland Alder 2, Birch 2, Cedar 1, Dogwood 1;
#   tieBreakType 'none'; log "Alder preferred over Birch in runoff."; winner ALDER.
#   The first draw put Alder in row 0, so the page looked correct — THREE MIRROR PAIRS were
#   then cast (a ranking plus its exact reverse: they cancel on every pairwise, so Copeland
#   and the winner are untouched) to re-roll the seed, which resets on every vote. The third
#   landed on a disagreeing order: 9 ballots, row 0 = Birch, winner still Alder. The results
#   page then reads "Alder wins!" with the star AND the gold table row on Birch — filed as
#   bettervoting#1480. (The sibling defect, the hard-coded single winner, is #1166 / PR #1479.)
# Previously: [ICE_CREAM_ABSTENTION_RECHECK_SPEC]   # BV2105-r2 — ice cream partial-ballot
#   re-check (created -> w3vvff). Result: the miscount STILL REPRODUCES on today's
#   tabulator — nTallyVotes 2 / nAbstentions 2, identical to BV2105 (r4dqvd) in 2025.
# Previously: [TIE_EVERY_RUNG_BLOC_SPEC]   # tie at every rung (created -> 484mbm). NOTE: minted
#   concurrently with OVER_50_PERCENT_SPEC below and both went out titled BV2263 — see that
#   spec's note. 484mbm is filed by bvid, with no bv_test_id.
# Previously: [OVER_50_PERCENT_SPEC]   # BV2263 — the over-50% ceiling case (created -> xw23m9)
# Previously: [BLOC_SASS_100_SPEC]   # BV1835 — 100 voters, 4 seats, score leader shut out
# Previously: [RANDOM_TIEBREAK_NINE_SPEC]   # BV2262 — nine-way dead heat, scale check
# Previously: [RANDOM_TIEBREAK_RECORDED_SPEC]   # BV2261 — random tiebreak is recorded (created -> y2fbpc)
# Previously: [MOST_WINS_NOT_CONDORCET_SPEC]   # BV2260 — most wins ≠ Condorcet winner (created -> gg9qh9)
# Previously: [EX15A_SPEC, EX15B_SPEC]   # BV2258/BV2259 — exercise 15, read the ballot
# Previously: [LUNCH_CHOOSE_ONE_SPEC]   # BV2257 — choose-one lunch, dead tie (created -> q2rkfm)
# Previously: [TRADITIONAL_STAR_SPEC]  # BV2256 — traditional style, one STAR race (created)
# Previously: [TRADITIONAL_SPEC]  # BV2255 — traditional style, four races (created; ORPHANED)
# Previously: [REINFORCEMENT_SPEC]  # BV2254 — reinforcement paradox (created -> t4by6x)
# Previously: [P3_SPEC]  # BV2253 — Manipulability P3, sincere baseline (created)
# Previously: [GOODBERRYS_SPEC]  # BV2252 — Goodberry's Best Flavor 2026 (created, live poll)
# Previously: [MARGINS_SPEC]  # BV2251 — Margins matter: Copeland vs Borda (created)
# Previously: [C1788_SPEC]  # BV2250 — Condorcet's 1788 rebuttal to Borda (created)
# Previously: [WCL_SPEC]  # BV2249 — weak Condorcet loser (created)
# Previously: [FR_HONEST_SPEC, FR_STRAT_SPEC, WA_HONEST_SPEC, WA_STRAT_SPEC]  # BV2229-2232 (created)


def spec_names(module=None):
    """Every election spec defined in this module, as {NAME: spec}.

    `ELECTIONS` is normally EMPTY (its resting state — you point it at a spec only
    for the run that creates it), so both tools need a way to find a spec by name:
    `create_bv_test_election.py --dry-run NAME` and `bv_ballot_sheet.py --spec NAME`.
    A spec is a module-level dict with a title and either candidates or races."""
    import sys as _sys
    mod = module or _sys.modules[__name__]
    out = {}
    for name, val in vars(mod).items():
        if name.startswith("_") or not isinstance(val, dict):
            continue
        if val.get("title") and (val.get("candidates") or val.get("races")):
            out[name] = val
    return out


# --- Tie at every rung — Bloc STAR, 3 candidates / 2 seats (created -> 484mbm) ---
# Backs 02_STAR_Bloc/02_Examples/b484mbm_tie_every_rung.md and the .starvote
# input-format page. Three rotating ballots (rock-paper-scissors): every candidate
# totals 12, collects 3 pairwise ballot-preferences, and holds exactly one score-5
# vote, so the scoring round, the pairwise rung and the five-star rung ALL tie and
# the two seats are filled purely by tie-break policy.
#
# ⚠ NUMBERING COLLISION — DO NOT "FIX" THE TITLE. This election was minted in a
# session whose collision gate could only see committed YAMLs (the _demo_dropbox
# ledger was on an unmounted volume), concurrently with OVER_50_PERCENT_SPEC. Both
# went out titled "BV2263 — …" and BV titles are permanent, so BV2263 names two
# elections: xw23m9 (over-50% control) and 484mbm (this one). The repo resolves it
# by giving BV2263 to xw23m9 and filing this case under its bvid with NO
# bv_test_id — the bvid is unique by construction. Nothing here is re-runnable:
# the spec is kept as the record of what was sent.
TIE_EVERY_RUNG_BLOC_SPEC = {
    "test_id": "BV2263",       # as sent — permanently on the election title; see the note above
    "title": "Bloc STAR — a three-way tie no rung can break (3 candidates, 2 seats)",
    "description": (
        "Three voters, three candidates, two seats, scored 0-5. The ballots rotate: "
        "one voter scores Arden 3 / Blythe 4 / Corin 5, the next Arden 5 / Blythe 3 / Corin 4, "
        "the last Arden 4 / Blythe 5 / Corin 3. Every candidate therefore totals 12 stars, is "
        "preferred on 3 ballots across the head-to-head matchups, and holds exactly one "
        "score-5 vote — so the scoring round, the pairwise rung and the five-star rung all "
        "come back tied. Nothing in the ballots distinguishes the three, and the two seats can "
        "only be filled by whatever tie-breaking policy was published before the count. Run "
        "through Larry Hastings' starvote engine with the tiebreaker switched off, it declines "
        "to pick a winner at all. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/07_Concepts/tabulation_engines/"
        "LH_starvote/starvote_file_format.html"
    ),
    "method": "STAR",          # BV has no separate "Bloc STAR" string: STAR + num_winners > 1
    "num_winners": 2,
    "enable_write_in": False,  # a write-in would destroy the tie this election exists to show
    "candidates": ["Arden", "Blythe", "Corin"],
    "ballots": [
        [3, 4, 5],
        [5, 3, 4],
        [4, 5, 3],
    ],
    "expected": ("a perfect three-way tie; LH with tiebreaker=none refuses to decide, "
                 "hashed_ballots gives Arden+Corin, the wrapper's lot order gives Blythe+Arden"),
}


# --- Degenerate seat count — 3 candidates for 3 seats (§2.4 of the Bloc scenario list) ---
# A behaviour PROBE, not a lesson: the LH engine refuses this election outright
# ("cannot fill 3 seats from 3 candidate(s)", exit 1), and the only way to learn
# whether BetterVoting refuses it too is to create one. Adam authorised the mint
# on 2026-08-04 after it was held back on 2026-08-04 as his call to make.
#
# The ballots are deliberately decisive on their own terms — totals 28/23/16, and
# each runoff won 5-2 — so nothing here rests on a tie-break and the SEAT ORDER
# stays reproducible even though the membership is a foregone conclusion.
# Write-ins MUST stay off: one write-in supplies the fourth candidate the whole
# premise excludes.
DEGENERATE_SEATS_SPEC = {
    "test_id": "BV2269",
    "title": "Three candidates, three seats — a race nobody can lose",
    "description": (
        "Three candidates for three seats, scored 0-5 by seven voters. There are exactly as "
        "many seats as candidates, so every candidate is seated no matter how anyone votes — "
        "the membership of this board is settled before a single ballot is cast. "
        "The election exists to ask a question about tabulators rather than to teach a result. "
        "Larry Hastings' starvote engine refuses an election of this shape outright: it stops "
        "with 'cannot fill 3 seats from 3 candidate(s) — num_winners must be smaller than the "
        "number of candidates' and counts nothing. BetterVoting's bloc tabulator takes a seat "
        "count and runs rounds until the candidates are used up, so the question is whether it "
        "accepts the race, seats all three, and prints a scoring round and an automatic runoff "
        "for a contest that cannot decide anything. Whatever it does is recorded on the lesson "
        "page linked below. "
        "The ballots are ordinary and fully decisive on their own terms — Abby totals 28 stars, "
        "Bruno 23, Celia 16, and each automatic runoff is won 5-2 with no voter at Equal "
        "Support — so the SEAT ORDER carries real information even though the membership does "
        "not, and no part of the result rests on a tie-break. Write-ins are off, because a "
        "single write-in would supply the fourth candidate the premise excludes. "
        "This shape is not exotic: an organisation creates it by accident every time "
        "nominations exactly fill the board. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/02_STAR_Bloc/02_Examples/index.html"
    ),
    "method": "STAR",          # BV has no separate "Bloc STAR" string: STAR + num_winners > 1
    "num_winners": 3,
    "enable_write_in": False,  # a write-in would give the race a loser and void the probe
    "candidates": ["Abby", "Bruno", "Celia"],
    "ballots": [
        [5, 3, 1],
        [5, 4, 0],
        [4, 3, 2],
        [5, 2, 3],
        [3, 5, 1],
        [2, 5, 4],
        [4, 1, 5],
    ],
    "expected": (
        "LH refuses the file (exit 1, no tally). BetterVoting: unknown before the mint — that "
        "is the probe. If it accepts, expect all three seated in score order Abby, Bruno, "
        "Celia, with round 1 Abby 5 - Bruno 2, round 2 Bruno 5 - Celia 2, and a third round "
        "with a single candidate and nothing to run against. Test ID BV2269."),
}


# --------------------------------------------------------------------------
# Districting cost — the best candidate wins no district at all.
# Runnable companion to 07_Concepts/topics/distributed_voting_distortion.md and
# the case set method_comparisons/districting_cost/.
#
# ONE election, THREE races. Districts hold DIFFERENT voters, but BV races are
# aligned by voter index and must all carry the same ballot count — so each
# chapter race carries all nine papers and the other chapter's members leave it
# blank. Blank scores 0, which adds nothing to any total and lands in Equal
# Support in the runoff, so every scoring total and every winner is identical to
# the 5- and 4-ballot LH yamls. That is the only difference between the frozen
# export and the case files, and it is by construction.
#
# Nothing here rests on a tie-break: no scoring round ties (23/19/0, 19/14/0,
# 33/23/19) and every runoff is decisive.
DISTRICTING_COST_SPEC = {
    "test_id": "BV2274",   # from the create script's printed next-free line
    "title": "The cost of districting — the best candidate wins no district at all",
    "description": (
        "Two chapters of one club elect a single national delegate, and the same nine "
        "members are counted three ways. Ana is adored in Northside and unknown in "
        "Southside; Beto is the exact mirror image; Cleo is everybody's solid second "
        "choice. Race 1 counts Northside's five members and elects Ana. Race 2 counts "
        "Southside's four and elects Beto. Race 3 counts all nine together and elects "
        "CLEO — who won neither chapter. "
        "Nothing about anyone's ballot changed between the races. Only the map did. "
        "Ana's 23 points are concentrated in one chapter and Beto's 19 in the other, "
        "while Cleo's 33 are spread evenly across both, so a chapter-by-chapter count "
        "reads concentration and a combined count reads the total. Cleo also beats both "
        "rivals head-to-head, so she is the Condorcet winner as well as the points "
        "leader: both notions of 'best' agree, and the district map overrides both. "
        "This is the distortion of DISTRIBUTED voting, made countable. Computational "
        "social choice proves that splitting an electorate into k districts and then "
        "choosing among the district winners multiplies the worst-case welfare loss by "
        "k — and that the loss survives even when every district counts perfect "
        "utilities. Here at k=2 you can check it by hand: every chapter ran a full 0-5 "
        "score count and still discarded the best candidate, so no ballot reform "
        "touches this. What costs the club is the requirement that the delegate be "
        "somebody's chapter winner. Picking Ana costs 30% of the available "
        "satisfaction; picking Beto costs 42%. "
        "In the two chapter races every member of the OTHER chapter leaves the contest "
        "blank, which is how a real districted election works — you get one ballot "
        "paper and vote only your own district's contest. A blank adds zero to every "
        "total, so the counts match the 5- and 4-member tallies exactly. "
        "Read it fairly: this is a constructed example showing the mechanism, not a "
        "claim about how often real district maps do this. Published experiments on "
        "real-world data find the effect far milder than the worst-case bound, because "
        "real electorates are homogeneous. The library's other districting case "
        "(Exercise 1, two districts and one mayor) is the honest twin, where districting "
        "costs nothing at all and the combined count is the one that gives ground. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/07_Concepts/topics/distributed_voting_distortion.html"
    ),
    "enable_write_in": False,   # a write-in would break the three-candidate construction
    "races": [
        {
            "title": "Northside chapter (5 members)",
            "method": "STAR", "num_winners": 1,
            "candidates": ["Ana", "Beto", "Cleo"],
            "ballots": [
                [5, 0, 3], [5, 0, 3], [5, 0, 3],   # Northside: Ana loyalists
                [4, 0, 5], [4, 0, 5],              # Northside: Cleo-leaning
                [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],   # Southside: not their contest
            ],
        },
        {
            "title": "Southside chapter (4 members)",
            "method": "STAR", "num_winners": 1,
            "candidates": ["Ana", "Beto", "Cleo"],
            "ballots": [
                [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],   # Northside: not their contest
                [0, 5, 3], [0, 5, 3], [0, 5, 3],   # Southside: Beto loyalists
                [0, 4, 5],                          # Southside: Cleo-leaning
            ],
        },
        {
            "title": "Both chapters together (9 members)",
            "method": "STAR", "num_winners": 1,
            "candidates": ["Ana", "Beto", "Cleo"],
            "ballots": [
                [5, 0, 3], [5, 0, 3], [5, 0, 3], [4, 0, 5], [4, 0, 5],
                [0, 5, 3], [0, 5, 3], [0, 5, 3], [0, 4, 5],
            ],
        },
    ],
    "expected": (
        "Race 1 -> Ana (23 to Cleo's 19; runoff 3-2). "
        "Race 2 -> Beto (19 to Cleo's 14; runoff 3-1). "
        "Race 3 -> Cleo (33 to Ana's 23; runoff 6-3). "
        "Cleo wins the combined race having won neither chapter, and is the "
        "welfare optimum (33 vs 23 vs 19) and the Condorcet winner."
    ),
}

# --- BV2275 — Kim / Myerson (A,B)-scoring: one electorate, six ballots ---------
# Backs method_comparisons/kim_ordinal_vs_cardinal/ and the concept page
# 07_Concepts/topics/ordinal_vs_cardinal_mechanism_design.md.
#
# 36 voters with FIXED rankings vote six times. Only what a voter's SECOND choice
# is worth changes — Myerson's (A,B) dial, the subject of Semin Kim's "Ordinal
# versus cardinal voting rules" (GEB 104, 2017). Races 1-3 set the dial for
# everybody and produce THREE different winners; races 4-5 hand it to the voters
# as Approval ballots and produce two more from the same rankings; race 6 is the
# invariant reference. Every result is deterministic — LH-verified pre-creation,
# no tie anywhere, so nothing in this election rests on a tie-break.
_KIM_CANDS = ["Almond", "Berry", "Cocoa"]

# (count, ranking, approves-two-when-LUKEWARM, approves-two-when-INTENSE)
_KIM_BLOCS = [
    (12, ["Almond", "Berry", "Cocoa"], False, True),
    (8,  ["Berry", "Almond", "Cocoa"], False, False),
    (7,  ["Cocoa", "Almond", "Berry"], True,  False),
    (9,  ["Cocoa", "Berry", "Almond"], False, True),
]


def _kim_rows(build):
    """Expand the blocs into one ballot row per voter, aligned across races."""
    rows = []
    for cnt, order, lukewarm, intense in _KIM_BLOCS:
        rows += [build(order, lukewarm, intense)] * cnt
    return rows


def _kim_scores(middle):
    """(1, A, 0) written x4 on the 0-5 scale: top 4, middle `middle`, bottom 0."""
    def build(order, _lukewarm, _intense):
        by_rank = [4, middle, 0]
        sc = {c: by_rank[order.index(c)] for c in _KIM_CANDS}
        return [sc[c] for c in _KIM_CANDS]
    return build


def _kim_approval(which):
    """Approve your favorite; approve your second too only if it is a close one."""
    def build(order, lukewarm, intense):
        two = lukewarm if which == "lukewarm" else intense
        approved = set(order[:2] if two else order[:1])
        return [1 if c in approved else 0 for c in _KIM_CANDS]
    return build


def _kim_ranks(order, _lukewarm, _intense):
    return [order.index(c) + 1 for c in _KIM_CANDS]


KIM_AB_SCORING_SPEC = {
    "test_id": "BV2275",
    "title": "One Electorate, Six Ballots — what is your second choice worth?",
    "description": (
        "Thirty-six voters with FIXED rankings vote six times, and the only thing "
        "that changes between the races is what a voter's SECOND choice is worth. "
        "That one number is the dial Roger Myerson (2002) called A in the "
        "(A,B)-scoring rules, and it is the subject of Semin Kim's 'Ordinal versus "
        "cardinal voting rules: A mechanism design approach' (Games and Economic "
        "Behavior 104, 2017). The electorate: 12 voters rank Almond > Berry > "
        "Cocoa, 8 rank Berry > Almond > Cocoa, 7 rank Cocoa > Almond > Berry, and "
        "9 rank Cocoa > Berry > Almond. Nobody changes their mind in any race. "
        "RACES 1-3 set the dial for everybody. Worth nothing (a Choose-One shaped "
        "ballot) elects COCOA. Worth half - the Borda count, which Kim proves is "
        "the best an ordinal ballot can do in this setting - elects ALMOND. Worth "
        "as much as your first choice (negative voting, where a ballot says only "
        "who you left out) elects BERRY. Three winners, one electorate, and not "
        "one change of heart: a designer turned a dial. "
        "RACES 4-5 hand the dial to the VOTERS, as Approval ballots. Approval is "
        "the corner of the same family where each voter decides for themselves "
        "whether their second choice counts, and it is the one corner a ranking "
        "cannot fill in. The same 36 rankings elect ALMOND when second choices are "
        "lukewarm and BERRY when they are intense - decided by information that no "
        "ranked ballot records. "
        "RACE 6 is the reference: Ranked Robin reads the rankings alone and elects "
        "Almond, the Condorcet winner, whatever the dial is doing. "
        "Full lesson & tabulation: https://masiarek.github.io/star-voting-library/"
        "method_comparisons/kim_ordinal_vs_cardinal/index.html"
    ),
    "races": [
        {"title": "A=0 — second choice worth nothing (Choose-One shaped)",
         "method": "STAR", "num_winners": 1, "candidates": _KIM_CANDS,
         "ballots": _kim_rows(_kim_scores(0))},
        {"title": "A=1/2 — second choice worth half (Borda)",
         "method": "STAR", "num_winners": 1, "candidates": _KIM_CANDS,
         "ballots": _kim_rows(_kim_scores(2))},
        {"title": "A=1 — second choice worth everything (Negative voting)",
         "method": "STAR", "num_winners": 1, "candidates": _KIM_CANDS,
         "ballots": _kim_rows(_kim_scores(4))},
        {"title": "Approval — lukewarm second choices",
         "method": "Approval", "num_winners": 1, "candidates": _KIM_CANDS,
         "ballots": _kim_rows(_kim_approval("lukewarm"))},
        {"title": "Approval — intense second choices",
         "method": "Approval", "num_winners": 1, "candidates": _KIM_CANDS,
         "ballots": _kim_rows(_kim_approval("intense"))},
        {"title": "Ranked Robin — the ranking alone",
         "method": "RankedRobin", "num_winners": 1, "max_rankings": 3,
         "candidates": _KIM_CANDS, "ballots": _kim_rows(_kim_ranks)},
    ],
    "expected": (
        "Race 1 (A=0) -> Cocoa (scores Cocoa 64 / Almond 48 / Berry 32; runoff "
        "Cocoa 16 - Almond 12, 8 Equal Support). "
        "Race 2 (A=1/2) -> Almond (78 / Berry 74 / Cocoa 64; runoff 19-17, no "
        "Equal Support). "
        "Race 3 (A=1) -> Berry (116 / Almond 108 / Cocoa 64; runoff Berry 9 - "
        "Almond 7, 20 Equal Support). "
        "Race 4 (Approval, lukewarm) -> Almond 19 / Cocoa 16 / Berry 8. "
        "Race 5 (Approval, intense) -> Berry 29 / Cocoa 16 / Almond 12. "
        "Race 6 (Ranked Robin) -> Almond, the Condorcet winner (beats Berry 19-17, "
        "beats Cocoa 20-16). "
        "No race turns on a tiebreak. Test ID BV2275."
    ),
}

SECOND_FINALIST_TIE_SPEC = {
    "test_id": "BV2276",
    "title": "Tied for the second finalist — the runoff pair settled without a coin toss",
    "description": (
        "Five voters score four candidates 0-5. Ana leads the scoring round with 15 stars, "
        "but Ben and Cora BOTH finish on 14, so the scoring round names only one finalist "
        "outright and the second seat in the runoff has to be settled some other way. "
        "STAR's tiebreak ladder settles it on its first deterministic rung, the head-to-head: "
        "Cora is preferred to Ben on three of the five ballots to Ben's two, so CORA advances "
        "and the runoff is Ana vs Cora. No coin toss, no lot, no random rung — re-run the "
        "count and you get the same pair every time, which is the point worth teaching here. "
        "A tie for a finalist slot sounds alarming and usually is not; it has an ordinary "
        "answer, and the answer does not depend on candidate order or on who happened to be "
        "listed second. "
        "In the runoff Ana beats Cora 2 to 1 with 2 of the 5 voters rating the two finalists "
        "equally — one voter gives both 3 stars, one gives both 5 — so Equal Support is the "
        "largest single group on the chart even though Ana wins. "
        "The election is deliberately tiny so every number can be checked by hand, and it "
        "doubles as a fixture for BetterVoting reporting issue #1484, which asks whether every "
        "panel on the results page names the same second finalist once a tiebreak has moved "
        "it. Write-ins are off, because one extra ballot line would break the exact 14-14 tie "
        "the whole election is built around. "
        "Full lesson & tabulation: "
        "https://masiarek.github.io/star-voting-library/01_STAR/03_Criteria/tie_break_ladder/index.html"
    ),
    "method": "STAR",
    "num_winners": 1,
    "enable_write_in": False,  # a write-in could disturb the exact 14-14 scoring tie
    "candidates": ["Ana", "Ben", "Cora", "Dev"],
    "ballots": [
        [5, 3, 5, 0],
        [3, 1, 3, 0],
        [5, 4, 2, 1],
        [1, 4, 0, 5],
        [1, 2, 4, 5],
    ],
    "expected": (
        "Scoring round Ana 15, Ben 14, Cora 14, Dev 11. Ben and Cora tie for the second "
        "finalist slot; the head-to-head rung advances Cora (preferred on 3 ballots to Ben's "
        "2), so the finalists are Ana and Cora and tieBreakType should be head_to_head, not "
        "random. Automatic runoff Ana 2 - Cora 1 with 2 voters at Equal Support (one pair at "
        "3 stars, one at 5), so Distribution of Equal Support is 3* 50% / 5* 50%. Ana wins. "
        "LH agrees on every number and also advances Cora at its head-to-head rung. "
        "Confirmed in the BV sandbox before minting: runoff chart reads Ana 40% / Cora 20% / "
        "Equal Support 40%. "
        "REGRESSION CHECK for issue #1484: the Scores Table highlight and the Runoff Table "
        "must name CORA, not Ben. Naming Ben (with Equal Support collapsing to 0, since Ana "
        "vs Ben is 3-2 with nobody equal) is the bug. Test ID BV2276."
    ),
}

ELECTIONS: list = []   # resting state — point this at a spec only for the run that mints it
# Previously: [SECOND_FINALIST_TIE_SPEC]   # BV2276 -> qhjyr2
#   Created as designed, 5 ballots × 1 race. BV agrees with LH on every number:
#   scores Ana 15 / Ben 14 / Cora 14 / Dev 11, the Ben-Cora tie resolved on the
#   HEAD-TO-HEAD rung (Cora 3 - Ben 2, tieBreakType 'head_to_head' — no five-star,
#   no random), runoff Ana 2 - Cora 1 with 2 voters at Equal Support. Ana wins.
#   Minted as the regression fixture for BetterVoting issue #1484: the live results
#   page's Race Details tables name BEN (the second-highest scorer) instead of Cora
#   (the candidate the tiebreak advanced), and Equal Support collapses from 2 to 0,
#   while the charts and Tabulation Steps on the same page correctly say Cora. The
#   bug reproduces on this brand-new election, which rules out a stale stored
#   payload. Case: 01_STAR/03_Criteria/tie_break_ladder/bv2276_qhjyr2_second_finalist_tie.md
# Previously: [KIM_AB_SCORING_SPEC]   # BV2275 -> 6mcgkq
#   Created as designed, 36 ballots × 6 races.
# Previously: [DISTRICTING_COST_SPEC]   # BV2274 -> 38b7fg
#   Created as designed, 9 ballots x 3 races. BV agrees with LH on all three
#   (Ana / Beto / Cleo) and reports tieBreakType 'none' everywhere — nothing in
#   this election rests on a tie-break, which matters because the lesson is that
#   the combined winner won neither district.
