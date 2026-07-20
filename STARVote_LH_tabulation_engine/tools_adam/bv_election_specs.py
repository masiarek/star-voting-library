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
#   BV2187 — Ann, Bob, Cal (canonical STAR mechanics demo)      -> qrw6wb  (backs 01_STAR/_main/bv2187_qrw6wb_ann-bob-cal)
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
# SOURCE: 01_STAR/exercises/ex01_two_districts.md (this repo) — ballots adapted
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
# races LH-verified pre-creation (01_STAR/exercises/, tested answer keys).
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
           "01_STAR/exercises/ex01_two_districts.md): a live demonstration that "
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
# Eight elections backing 01_STAR/exercises/ (ex09 stays LH-only on purpose: its
# 3-way Ranked Robin wins tie is BV-random). All races LH-verified pre-creation;
# ranked races use ranks-in-slots (1 = top, 0 = unranked), Approval/Plurality 0/1.
# ex10 carries NO Ranked Robin races: the reticent profile's rank conversion
# yields a Condorcet cycle (3-way tie -> BV random, not freezable), so the pair
# stays symmetric with STAR + IRV only.

_EX_SRC = ("From the exercises set of the STAR education repo "
           "(github.com/masiarek/star-voting-library, 01_STAR/exercises/) — "
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
            "01_STAR/favorite_betrayal/) — the worked favorite-betrayal pair behind "
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
# 01_STAR/favorite_betrayal/. Do NOT re-run (permanent dupes).

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
            "05_Ranked_Robin/burial/) — the worked burial pair: Ranked Robin's "
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
# Case folder: 05_Ranked_Robin/burial/. ERRATUM: the live descriptions'
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
# Reproduces 01_STAR/equal_and_opposite/. Ready to create — see EQO note below.
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

ELECTIONS: list = []   # reset (BV2221->2kcwbw, BV2222->rfyk46, BV2223->dyh93j done 2026-07-20)
