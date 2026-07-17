# 06_Other/ballot_style_lab — random-but-human electorates (the style lab)

*What happens when you fill a whole election with the ballot styles real people actually use — bullet votes, partisan slates, harsh graders who top out at 2, gentle souls who never score below 3, cliff voters who jump straight from 0 to "one of mine"? This folder is a seeded generator plus six frozen elections it found: random enough to surprise, human enough to mean something, deterministic enough to be test cases.*

→ The style taxonomy these voters follow: [Filling Out the 5-Star Ballot — Voting Styles](../../00_start_here/STAR_Voting/STAR_ballot_voting_styles.md) · the methodology this generator obeys: [Simulate utilities, not ballots](../../00_start_here/topics/simulate_utilities_not_ballots.md) · one voter's opinion across ballot *formats*: [Alternate ballot styles](../../00_start_here/topics/ballot_styles.md)

---

## The idea — opinion first, expression second

Pure-uniform random ballots correspond to no electorate on Earth, and the methodology page explains why they rig method comparisons. So this generator injects randomness in two human-shaped layers:

1. **Opinion (layer 1):** each voter's underlying 0–1 *utilities* are sampled from a **faction model** — slanted camps with a shared lean, personal noise on top, plus a few genuinely noisy voters.
2. **Expression (layer 2):** those utilities are then *rendered* through the voter's **ballot style** — the legal styles from the [style gallery](../../00_start_here/STAR_Voting/STAR_ballot_voting_styles.md) (bullet, backups, slate, ranked-style, nuanced, anyone-but, protest) plus deliberately compressed scale habits (0–2 harsh, 3–5 gentle, 0-or-3–5 cliff, 3–4 sliver, flat lines, pure noise).

Same opinion, different rendering — the [same-opinion line-up idea](../../00_start_here/topics/ballot_styles.md), scaled up to a whole electorate. Per the methodology page, this sits in the honest **"stress-test the tabulator"** job (not a method-welfare comparison): the ballots exist to exercise the count, and the human shaping makes the exercises look like elections instead of dice.

**Full disclosure — the seeds are hunted.** The generator tabulates hundreds of seeds with the real LH engine and keeps the *interesting* draws: runoff reversals, Condorcet cycles, tie rungs, photo finishes, Equal-Support blowouts. A typical random seed is boring; these six are champions selected across 250 seeds each, then frozen. That selection bias is the point of a test fixture — and it's disclosed here and inside every file.

## The six frozen elections

Every file records its scenario + seed and regenerates byte-identically (`--emit <scenario>`); `expected_winners` is embedded and the whole folder runs in the repo's positive test suite. All six are single-winner STAR, 24–47 individual ballots, fresh casts per the naming rules.

| # | Case | The electorate | What the frozen seed produced | Source |
|---|---|---|---|---|
| 1 | [The Graders' Divide](ballot_style_lab_pages/01_c3_b31_graders-divide.md) | 15 harsh graders (0–2) vs 16 gentle souls (3–5) — two grading cultures, zero overlap | Totals bunch at **80–80–78**; the top two tie dead even and Clara wins the runoff 13–11. **No Condorcet winner**; Plurality & RCV-IRV say Bruno, Approval-thinking says Abby — four counting philosophies, three different "winners" from 31 ballots | [`yaml`](01_c3_b31_graders-divide.yaml) · [`report`](ballot_style_lab_tabulated/01_c3_b31_graders-divide_tabulated.txt) |
| 2 | [Cliff City](ballot_style_lab_pages/02_c4_b40_cliff-city.md) | 40 food-truck voters, all cliff/slate ballots — the 1–2 middle of the scale is a ghost town | Scoring 100–99; Churro beats Bao 15–14 in the runoff (11 Equal Support) and is the **Condorcet winner**; Plurality and RCV-IRV both pick Bao — the engine flags the center-squeeze signature | [`yaml`](02_c4_b40_cliff-city.yaml) · [`report`](ballot_style_lab_tabulated/02_c4_b40_cliff-city_tabulated.txt) |
| 3 | [Bullet Storm](ballot_style_lab_pages/03_c4_b33_bullet-storm.md) | Three bullet-voting brigades (many leave blanks, as real bulleters do) + a thoughtful few who spread scores | The runoff **ties 13–13** (7 Equal Support — a whole brigade went silent) and is broken by STAR's official next tiebreaker: higher scoring total → Carla. Plurality & RCV-IRV say Astrid | [`yaml`](03_c4_b33_bullet-storm.yaml) · [`report`](ballot_style_lab_tabulated/03_c4_b33_bullet-storm_tabulated.txt) |
| 4 | [Noise Soup](ballot_style_lab_pages/04_c4_b47_noise-soup.md) | 47 messy ballots: weak leans, cross-winds, flat-liners, pure noise, a race abstention `~`, a spoiled `?`, stray blanks | A genuine **Condorcet cycle out of noise**; scoring leader Beth *loses* the runoff to Caleb 18–16 (13 Equal Support); Plurality says Aaron, RCV-IRV says Beth. Markers all tabulate as 0 and are reported honestly | [`yaml`](04_c4_b47_noise-soup.yaml) · [`report`](ballot_style_lab_tabulated/04_c4_b47_noise-soup_tabulated.txt) |
| 5 | [Does the squeeze survive noise?](ballot_style_lab_pages/05_c3_b38_squeeze-survives.md) | The center-squeeze profile rebuilt from noisy utilities + mixed styles (nuanced, ranked-style, backups, harsh, slate, gentle) | **Yes.** Consensus-Ben trails the scoring round, wins the runoff 19–18, and is the Condorcet winner; RCV-IRV eliminates him and elects Cora — the tidy classroom demos aren't cherry-picked, the squeeze survives real-world mess | [`yaml`](05_c3_b38_squeeze-survives.yaml) · [`report`](ballot_style_lab_tabulated/05_c3_b38_squeeze-survives_tabulated.txt) |
| 6 | [Narrow Bands](ballot_style_lab_pages/06_c4_b24_narrow-bands.md) | 24 paint-swatch voters and *nobody* uses the whole ballot: 0–2 camp, 3–5 camp, cliff & sliver voters, flat-liners, one protest | Compressed totals produce a **three-way scoring tie 61–61–61**; the official head-to-head tiebreaker picks the finalists, the runoff lands 9–8, and there's no Condorcet winner. Plurality, RCV-IRV and Approval-thinking all say Azure; STAR says Beige, Ranked Robin says Coral | [`yaml`](06_c4_b24_narrow-bands.yaml) · [`report`](ballot_style_lab_tabulated/06_c4_b24_narrow-bands_tabulated.txt) |

Voter counts here (24–47) deliberately sit *above* the repo's keep-it-small default ([choosing voter counts](../../00_start_here/tips/TIPS_choosing_voter_counts.md)): statistical style patterns need a crowd, and 20–50 is still small enough to eyeball every row.

## A taste — the Graders' Divide on screen

Two camps that never touch each other's half of the scale. Look at the Score Distribution: Abby's column is *nothing but* 2s and 3s (all 31 voters!), Bruno's is *nothing but* 5s and 0s — and the totals land 80–80–78:

```
[Score Distribution] (how many ballots gave each star rating)
                   Score
Candidate   5   4   3   2   1   0  | Total   Avg
Abby        0   0  16  15   0   0  |    78   2.5
Bruno      16   0   0   0   0  15  |    80   2.6
Clara       5   8   3   1  12   2  |    80   2.6

Scoring Round
 The two highest-scoring candidates advance to the next round.
   Bruno         -- 80 -- First place
   Clara         -- 80 -- Second place
   Abby          -- 78
 Bruno and Clara advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Clara         -- 13 -- First place
   Bruno         -- 11
   Equal Support --  7
 Clara wins.
   Voters with a preference: 24 of 31 (7 Equal Support).
   Clara 13 (54%) vs Bruno 11 (46%); majority = 13.
```

The Scoring Round can't tell a harsh 2 from a gentle enthusiasm — but the Automatic Runoff only asks *which finalist each ballot scored higher*, and on that question the grading cultures cancel out. Full detail (matrix, divergence block, the Condorcet wobble): [the `_tabulated` report](ballot_style_lab_tabulated/01_c3_b31_graders-divide_tabulated.txt).

## The style menu

Renderings implemented by the generator (utilities → 0–5 scores). Gallery styles carry the [style-gallery](../../00_start_here/STAR_Voting/STAR_ballot_voting_styles.md) names; band styles are the lab's additions.

| Style | Renders as | From |
|---|---|---|
| `nuanced` | honest min-max onto the full 0–5, ties kept | gallery |
| `bullet` | favorite 5, everyone else 0/blank | gallery (Traditional) |
| `strong_backup` / `weak_backup` | 5 plus a 4 (or a grudging 1) for the runner-up | gallery |
| `slate` | equal 5s for the in-group, 0 outside | gallery (Partisan slate) |
| `ranked_style` | each score used once, 5 downward, like a ranking | gallery |
| `anyone_but` | 5 for everyone except the villain (0) | gallery |
| `protest` | all zeros plus a lone least-bad 1 | gallery |
| `harsh` | everything squeezed into 0–2 | band |
| `gentle` | everything squeezed into 3–5, zeros never | band |
| `cliff35` / `cliff34` | 0 or 3–5 (or 3–4) — nothing in between | band |
| `flat` | the same score for everyone (legal no-preference ballot) | band |
| `chaos` | uniform noise — the fuzzing voter the methodology page blesses | band |

Realism garnishes: bullet/backup/slate voters flip a coin between writing `0`s and leaving real-world *blanks* (`-`); Noise Soup adds a race abstention row (`~`), a spoiled row (`?`), and stray blank cells — all tabulate as 0 and are reported honestly.

## Running the lab

```
python generate_ballot_styles.py --list                 # scenario menu + frozen seeds
python generate_ballot_styles.py --emit all             # regenerate the six files byte-identically
python generate_ballot_styles.py --hunt cliff_city --seeds 250   # go gem-hunting yourself
```

The hunter tabulates every seed with the real LH engine and scores it for: runoff reversals, no-Condorcet/cycles, RCV-IRV divergence (and the engine's center-squeeze note), Equal-Support share, runoff margins and tie rungs, finalist-line photo finishes, and lot-decided anything. Champions must also satisfy the scenario's target predicate and resolve **deterministically** (a lot-decided result can't be a frozen test case). To add a scenario: give it factions, a style mix, a fresh cast ([naming rules](../../CLAUDE.md)), hunt, freeze the seed, `--emit`.

Stdlib-only; runs with the repo `.venv` (or any Python 3) and calls `starvote_larry_hastings.py` for every tabulation — the engine is the oracle, the generator never reimplements the count.

## Related

- [Filling Out the 5-Star Ballot — Voting Styles](../../00_start_here/STAR_Voting/STAR_ballot_voting_styles.md) — the human taxonomy these voters follow
- [Simulate utilities, not ballots](../../00_start_here/topics/simulate_utilities_not_ballots.md) — why layer 1 exists at all
- [Election simulation models](../../00_start_here/topics/election_simulation_models.md) — the menu of utility models beyond this lab's faction-Gaussian
- [`06_Other/simulations/`](../simulations/README.md) — the brute-force method-comparison sims (utility-first, like this lab)
- [Divergence review index](../../method_comparisons/divergence_review/INDEX.md) — where these cases' method disagreements are ledgered

# file: README.md
