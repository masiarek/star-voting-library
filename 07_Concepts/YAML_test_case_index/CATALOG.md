# Test-case catalog — slice the elections & races every way

*Generated — do not edit by hand. Regenerate: `python STARVote_LH_tabulation_engine/tools_adam/scripts/build_catalog.py`.*

Two grains underlie every view here:

- **Election** = the container: one electorate casting into **1..N races**, with a `bvid` (or LH-only). *Single-race* = one contest; *contested* = several.
- **Race** = the atom that gets tabulated: exactly **one method, one seat count, one candidate set, one ballot type, one winner set**. This is the fact table ([`races.csv`](races.csv)).

Each race carries derived facets so you can slice: **ballot type** (score / ranked / approval / choose-one), **seat class** (single- vs multi-winner), and **character** (majoritarian / proportional / Condorcet). BV-only races with no yaml (e.g. Bloc Plurality) are pulled in from the frozen exports.

**Totals:** 506 elections, 685 races. Full drill-down: [`races.csv`](races.csv) · [`elections.csv`](elections.csv). Related: [BV registry](BV_registry.md) · [multi-race index](multirace_elections.md) · [by method](README.md).

## Elections

| Election | Title | Races | Kind | Voters | Methods | Backing |
|---|---|--:|---|--:|---|---|
| [`2jrfpg`](https://bettervoting.com/2jrfpg/results) | BV2169 — FairVote's hypothetical, electorate shifted | 2 | contested (multi-race) | 100 | IRV, STAR | BV |
| [`2p33qq`](https://bettervoting.com/2p33qq/results) | BV2215 — Minority winner — 34% wins Choose-One, but  | 3 | contested (multi-race) | 100 | Plurality, RankedRobin, STAR | BV |
| [`37yf8x`](https://bettervoting.com/37yf8x/results) | BV2280 — Ballot expressiveness — nine candidates, on | 4 | contested (multi-race) | 25 | IRV, RankedRobin, STAR | BV |
| [`38b7fg`](https://bettervoting.com/38b7fg/results) | BV2274 — The cost of districting — the best candidat | 3 | contested (multi-race) | 9 | STAR | BV |
| [`3grpbb`](https://bettervoting.com/3grpbb/results) | BV2156 — STAR's own miss — the Condorcet winner scor | 2 | contested (multi-race) | 100 | RankedRobin, STAR | BV |
| [`3x4vrv`](https://bettervoting.com/3x4vrv/results) | BV2135 — Block & Limited voting, reproduced as bloc  | 2 | contested (multi-race) | 10 | Plurality | BV |
| [`3xgkck`](https://bettervoting.com/3xgkck/results) | BV2227 — Favorite Betrayal — honest ballots (STAR &  | 3 | contested (multi-race) | 34 | IRV, RankedRobin, STAR | BV |
| [`4hfwqd`](https://bettervoting.com/4hfwqd/results) | BV2271 — Satisfaction Approval Voting, Proposition 2 | 3 | contested (multi-race) | 10 | Approval, RankedRobin, STAR | BV |
| [`4htk44`](https://bettervoting.com/4htk44/results) | BV2162 — Nurmi's truncation electorate (1 of 2) — ev | 3 | contested (multi-race) | 103 | IRV, RankedRobin, STAR | BV |
| [`4w96tr`](https://bettervoting.com/4w96tr/results) | BV2253 — Where should the committee meet? — the sinc | 3 | contested (multi-race) | 7 | Plurality, RankedRobin, STAR | BV |
| [`6bry7c`](https://bettervoting.com/6bry7c/results) | BV2192 — The Squeezed Bridge-Builder — everyone's se | 3 | contested (multi-race) | 9 | IRV, RankedRobin, STAR | BV |
| [`6fj2kg`](https://bettervoting.com/6fj2kg/results) | BV2145 — Felsenthal's runoff paradoxes (1 of 2) — th | 3 | contested (multi-race) | 17 | IRV, RankedRobin, STAR | BV |
| [`6mcgkq`](https://bettervoting.com/6mcgkq/results) | BV2275 — One Electorate, Six Ballots — what is your  | 6 | contested (multi-race) | 36 | Approval, RankedRobin, STAR | BV |
| [`6w2gq7`](https://bettervoting.com/6w2gq7/results) | BV2168 — FairVote's Condorcet hypothetical, counted  | 2 | contested (multi-race) | 100 | IRV, STAR | BV |
| [`74j6vv`](https://bettervoting.com/74j6vv/results) | BV2163 — Nurmi's truncation electorate (2 of 2) — 17 | 3 | contested (multi-race) | 103 | IRV, RankedRobin, STAR | BV |
| [`7f4f7q`](https://bettervoting.com/7f4f7q/results) | BV2194 — Bullet Voting Backfires (2 of 2) — the stra | 3 | contested (multi-race) | 9 | IRV, RankedRobin, STAR | BV |
| [`82gg36`](https://bettervoting.com/82gg36/results) | BV2226 — Preference vs Support — the center SUPPORTE | 3 | contested (multi-race) | 36 | IRV, RankedRobin, STAR | BV |
| [`89wwvr`](https://bettervoting.com/89wwvr/results) | BV2199 — Two Seats, One Neighborhood — Bloc STAR swe | 2 | contested (multi-race) | 10 | STAR, STAR_PR | BV |
| [`8cdkkc`](https://bettervoting.com/8cdkkc/results) | BV2278 — Five-Way Race — the moderate who beats both | 4 | contested (multi-race) | 1000 | IRV, Plurality, RankedRobin, STAR | BV |
| [`8kg698`](https://bettervoting.com/8kg698/results) | BV2178 — The Post-it election's round-2 switch, made | 4 | contested (multi-race) | 20 | IRV, Plurality, RankedRobin, STAR | BV |
| [`923q3d`](https://bettervoting.com/923q3d/results) | BV2190 — Two Districts, One Mayor (III of III) — the | 2 | contested (multi-race) | 18 | RankedRobin, STAR | BV |
| [`93gjx6`](https://bettervoting.com/93gjx6/results) | BV2198 — Recruit a Spoiler (2 of 2) — the clone ente | 4 | contested (multi-race) | 9 | IRV, Plurality, RankedRobin, STAR | BV |
| [`97hbpw`](https://bettervoting.com/97hbpw/results) | BV2151 — Felsenthal's No-Show paradox (2 of 2) — two | 3 | contested (multi-race) | 9 | IRV, RankedRobin, STAR | BV |
| [`9gdrqg`](https://bettervoting.com/9gdrqg/results) | BV2147 — Felsenthal's Reinforcement paradox (I of II | 2 | contested (multi-race) | 17 | IRV, STAR | BV |
| [`9kffcv`](https://bettervoting.com/9kffcv/results) | BV2273 — Same ranks, different utilities — two elect | 3 | contested (multi-race) | 3 | RankedRobin, STAR | BV |
| [`9vxcj7`](https://bettervoting.com/9vxcj7/results) | BV2165 — Coombs' No-Show electorate (1 of 2) — every | 2 | contested (multi-race) | 15 | Plurality, STAR | BV |
| `example_tennessee` | Tennessee capital — RCV-IRV engine demo | 2 | contested (multi-race) | 100 | IRV, STAR | LH-only |
| [`b7b8dv`](https://bettervoting.com/b7b8dv/results) | BV2166 — Coombs' No-Show electorate (2 of 2) — two v | 2 | contested (multi-race) | 13 | Plurality, STAR | BV |
| [`bkwfjr`](https://bettervoting.com/bkwfjr/results) | BV2172 — The Condorcet centrist, full form (100 vote | 7 | contested (multi-race) | 100 | Approval, IRV, Plurality, RankedRobin, STAR, STAR_PR, STV | BV |
| [`bvhchj`](https://bettervoting.com/bvhchj/results) | Presidential Board Election | 2 | contested (multi-race) | 102 | Plurality, STAR_PR | BV |
| [`byk9v2`](https://bettervoting.com/byk9v2/results) | BV2149 — Felsenthal's Reinforcement paradox (III of  | 2 | contested (multi-race) | 32 | IRV, STAR | BV |
| [`c73pfw`](https://bettervoting.com/c73pfw/results) | BV2249 — Weak Condorcet loser — when both STAR final | 3 | contested (multi-race) | 5 | Approval, RankedRobin, STAR | BV |
| [`cphxpt`](https://bettervoting.com/cphxpt/results) | BV2155 — Tennessee capital, four ways — one electora | 4 | contested (multi-race) | 100 | IRV, Plurality, RankedRobin, STAR | BV |
| [`cxrf8v`](https://bettervoting.com/cxrf8v/results) | BV2138 — One Ranked Electorate, Many Tabulations — t | 4 | contested (multi-race) | 921 | IRV, RankedRobin, STAR, STV | BV |
| [`d3b9wc`](https://bettervoting.com/d3b9wc/results) | BV2188 — Two Districts, One Mayor (I of III) — West  | 2 | contested (multi-race) | 9 | RankedRobin, STAR | BV |
| [`d4v2dh`](https://bettervoting.com/d4v2dh/results) | BV2258 — Read the ballot, name the method: 35 voters | 2 | contested (multi-race) | 35 | Approval, STAR | BV |
| [`dr6fmg`](https://bettervoting.com/dr6fmg/results) | BV2272 — Satisfaction Approval Voting, Proposition 5 | 3 | contested (multi-race) | 17 | Approval, RankedRobin, STAR | BV |
| [`dxg8pb`](https://bettervoting.com/dxg8pb/results) | BV2150 — Felsenthal's No-Show paradox (1 of 2) — eve | 3 | contested (multi-race) | 11 | IRV, RankedRobin, STAR | BV |
| [`dyh93j`](https://bettervoting.com/dyh93j/results) | BV2223 — STAR vs strategy — 5-1-0 min-max, real mode | 2 | contested (multi-race) | 100 | IRV, STAR | BV |
| [`dyxrbr`](https://bettervoting.com/dyxrbr/results) | BV2133 — Pet poll II: four methods, four winners | 4 | contested (multi-race) | 32 | Approval, IRV, Plurality, STAR | BV |
| [`f3dxq9`](https://bettervoting.com/f3dxq9/results) | BV2167 — Minimax elects the absolute loser — the can | 2 | contested (multi-race) | 11 | Plurality, STAR | BV |
| [`f4cjpy`](https://bettervoting.com/f4cjpy/results) | BV2159 — Brams' 21-voter sampler — IRV elects B whil | 3 | contested (multi-race) | 21 | IRV, RankedRobin, STAR | BV |
| [`fvg8y8`](https://bettervoting.com/fvg8y8/results) | BV2210 — Food-Truck Row — two spots, five counts: vo | 5 | contested (multi-race) | 100 | Plurality, RankedRobin, STAR, STAR_PR, STV | BV |
| [`g6q42v`](https://bettervoting.com/g6q42v/results) | BV2195 — Later-No-Harm (1 of 2) — the reticent ballo | 2 | contested (multi-race) | 9 | IRV, STAR | BV |
| [`ggg7hd`](https://bettervoting.com/ggg7hd/results) | BV2197 — Recruit a Spoiler (1 of 2) — the two-way ba | 2 | contested (multi-race) | 9 | Plurality, STAR | BV |
| [`gr72hd`](https://bettervoting.com/gr72hd/results) | BV2158 — Ossipoff's buried centrist — the candidate  | 4 | contested (multi-race) | 303 | IRV, Plurality, RankedRobin, STAR | BV |
| [`gvdy42`](https://bettervoting.com/gvdy42/results) | 2026 California Governor Election | 2 | contested (multi-race) | 319 | IRV, STAR | BV |
| [`h34pp9`](https://bettervoting.com/h34pp9/results) | BV2218 — Pineapple progression 3/3 — Choose-One elec | 4 | contested (multi-race) | 100 | Approval, Plurality, RankedRobin, STAR | BV |
| [`h87k6v`](https://bettervoting.com/h87k6v/results) | BV2148 — Felsenthal's Reinforcement paradox (II of I | 2 | contested (multi-race) | 15 | IRV, STAR | BV |
| [`h93tm4`](https://bettervoting.com/h93tm4/results) | BV2171 — The Condorcet centrist, minimal form (8 vot | 7 | contested (multi-race) | 8 | Approval, IRV, Plurality, RankedRobin, STAR, STAR_PR, STV | BV |
| [`hf3ckp`](https://bettervoting.com/hf3ckp/results) | BV2282 — Brams's 21 — twenty-one ranked ballots, two | 2 | contested (multi-race) | 21 | IRV, RankedRobin | BV |
| [`ht2c3g`](https://bettervoting.com/ht2c3g/results) | BV2216 — Pineapple progression 1/3 — Choose-One elec | 4 | contested (multi-race) | 99 | Approval, Plurality, RankedRobin, STAR | BV |
| [`jfrk9t`](https://bettervoting.com/jfrk9t/results) | BV655 - “equal opposition” vote - the “Same-Score Ba | 2 | contested (multi-race) | 2 | STAR | BV |
| [`k3fmwv`](https://bettervoting.com/k3fmwv/results) | BV2213 — Alaska 2022 special, scaled model: STAR & R | 4 | contested (multi-race) | 200 | IRV, Plurality, RankedRobin, STAR | BV |
| [`kcf8vf`](https://bettervoting.com/kcf8vf/results) | BV2134 — Pets Governance: six positions, six methods | 6 | contested (multi-race) | 22 | Approval, Plurality, RankedRobin, STAR, STAR_PR, STV | BV |
| [`kdjjkq`](https://bettervoting.com/kdjjkq/results) | BV2251 — Margins matter — one electorate, four diffe | 4 | contested (multi-race) | 12 | IRV, Plurality, RankedRobin, STAR | BV |
| [`khcwm4`](https://bettervoting.com/khcwm4/results) | BV2250 — Condorcet's 1788 rebuttal to Borda — where  | 3 | contested (multi-race) | 11 | IRV, RankedRobin, STAR | BV |
| [`krk2px`](https://bettervoting.com/krk2px/results) | BV2146 — Felsenthal's runoff paradoxes (2 of 2) — mo | 3 | contested (multi-race) | 17 | IRV, RankedRobin, STAR | BV |
| [`m3hb6y`](https://bettervoting.com/m3hb6y/results) | BV2214 — Alaska 2022 GENERAL (reduced model) — IRV g | 4 | contested (multi-race) | 200 | IRV, Plurality, RankedRobin, STAR | BV |
| [`mmcmpy`](https://bettervoting.com/mmcmpy/results) | BV2157 — Rock, Paper, Scissors — a Condorcet cycle:  | 3 | contested (multi-race) | 100 | Approval, IRV, STAR | BV |
| [`mvxbxr`](https://bettervoting.com/mvxbxr/results) | BV2217 — Pineapple progression 2/3 — Choose-One elec | 4 | contested (multi-race) | 100 | Approval, Plurality, RankedRobin, STAR | BV |
| [`mxfmhm`](https://bettervoting.com/mxfmhm/results) | BV2144 — Felsenthal's plurality paradoxes — the abso | 2 | contested (multi-race) | 7 | Plurality, STAR | BV |
| [`p8dp28`](https://bettervoting.com/p8dp28/results) | BV2176 — The Post-it RCV example (20 voters) — RCV-I | 3 | contested (multi-race) | 20 | IRV, RankedRobin, STAR | BV |
| [`pcttmr`](https://bettervoting.com/pcttmr/results) | BV2153 — Felsenthal's Absolute Majority paradox — a  | 3 | contested (multi-race) | 100 | Approval, IRV, RankedRobin | BV |
| [`pp2q4q`](https://bettervoting.com/pp2q4q/results) | BV2170 — The centrist a majority prefers, squeezed o | 4 | contested (multi-race) | 100 | IRV, Plurality, RankedRobin, STAR | BV |
| [`q3h4fk`](https://bettervoting.com/q3h4fk/results) | BV2161 — Borda's SCC paradox electorate — the winner | 2 | contested (multi-race) | 7 | Plurality, STAR | BV |
| [`qdtqf2`](https://bettervoting.com/qdtqf2/results) | BV2200 — Where Do You Draw the Line? — one electorat | 4 | contested (multi-race) | 9 | Approval, STAR | BV |
| [`qycpbx`](https://bettervoting.com/qycpbx/results) | BV2281 — Ossipoff's 303 — the first-round leader who | 2 | contested (multi-race) | 303 | IRV, RankedRobin | BV |
| [`qywq7d`](https://bettervoting.com/qywq7d/results) | BV2279 — Three Brothers, One Fruit — the majoritaria | 3 | contested (multi-race) | 3 | Approval, RankedRobin, STAR | BV |
| [`r6ctvy`](https://bettervoting.com/r6ctvy/results) | BV2152 — Felsenthal & Maoz's Approval paradox — the  | 2 | contested (multi-race) | 47 | Approval, RankedRobin | BV |
| [`r6qc8h`](https://bettervoting.com/r6qc8h/results) | BV2160 — Fishburn's Borda truncation electorate — ST | 2 | contested (multi-race) | 7 | Plurality, STAR | BV |
| [`rfyk46`](https://bettervoting.com/rfyk46/results) | BV2222 — STAR vs strategy — 5-1-0 min-max squeezes t | 2 | contested (multi-race) | 100 | IRV, STAR | BV |
| [`rhbfj7`](https://bettervoting.com/rhbfj7/results) | BV2189 — Two Districts, One Mayor (II of III) — East | 2 | contested (multi-race) | 9 | RankedRobin, STAR | BV |
| [`t4by6x`](https://bettervoting.com/t4by6x/results) | BV2254 — Reinforcement paradox: two towns pick Ada,  | 2 | contested (multi-race) | 9 | RankedRobin, STAR | BV |
| [`tqfdbg`](https://bettervoting.com/tqfdbg/results) | BV2277 — The Mayor's Race — the third-place candidat | 4 | contested (multi-race) | 100 | IRV, Plurality, RankedRobin, STAR | BV |
| [`v8r66y`](https://bettervoting.com/v8r66y/results) | BV2177 — The Post-it election, seven ways — all four | 7 | contested (multi-race) | 20 | Approval, IRV, Plurality, RankedRobin, STAR, STAR_PR, STV | BV |
| [`wq6yv7`](https://bettervoting.com/wq6yv7/results) | BV2154 — Felsenthal's Approval paradox — the absolut | 3 | contested (multi-race) | 15 | Approval, IRV, RankedRobin | BV |
| [`x4dkfd`](https://bettervoting.com/x4dkfd/results) | BV2193 — Bullet Voting Backfires (1 of 2) — the hone | 3 | contested (multi-race) | 9 | IRV, RankedRobin, STAR | BV |
| [`xbqq8t`](https://bettervoting.com/xbqq8t/results) | BV2164 — Coombs deletes the Condorcet winner first — | 3 | contested (multi-race) | 33 | Plurality, RankedRobin, STAR | BV |
| [`y2fbpc`](https://bettervoting.com/y2fbpc/results) | BV2261 — A three-way Ranked Robin tie: the random ti | 2 | contested (multi-race) | 6 | RankedRobin | BV |
| [`ykjjhy`](https://bettervoting.com/ykjjhy/results) | BV2132 — Pet poll: four methods, three winners | 4 | contested (multi-race) | 22 | Approval, IRV, Plurality, STAR | BV |
| [`ywckmg`](https://bettervoting.com/ywckmg/results) | BV2137 — Center Squeeze — the centrist Condorcet win | 4 | contested (multi-race) | 100 | IRV, RankedRobin, STAR, STV | BV |
| [`ywqhq4`](https://bettervoting.com/ywqhq4/results) | BV2191 — One Electorate, Five Verdicts — the snack v | 5 | contested (multi-race) | 9 | Approval, IRV, Plurality, RankedRobin, STAR | BV |
| [`ywx39y`](https://bettervoting.com/ywx39y/results) | BV2225 — Preference vs Support — the center TOLERATE | 3 | contested (multi-race) | 36 | IRV, RankedRobin, STAR | BV |
| [`yyhj9x`](https://bettervoting.com/yyhj9x/results) | BV2196 — Later-No-Harm (2 of 2) — the generous ballo | 2 | contested (multi-race) | 9 | IRV, STAR | BV |
| [`24b623`](https://bettervoting.com/24b623/results) | BV2232 — FairVote-vs-STAR check: Washington 2010 bur | 1 | single-race | 100 | STAR | BV |
| [`26khr3`](https://bettervoting.com/26khr3/results) | NOTA test — None of the Above wins (with a null abst | 1 | single-race | 6 | STAR | BV |
| [`2gvwr9`](https://bettervoting.com/2gvwr9/results) | BV2262 — Nine candidates, a nine-way dead heat: does | 1 | single-race | 9 | RankedRobin | BV |
| [`2hqmrd`](https://bettervoting.com/2hqmrd/results) | BV2230 — FairVote-vs-STAR check: French 2017 coordin | 1 | single-race | 100 | STAR | BV |
| [`2kcwbw`](https://bettervoting.com/2kcwbw/results) | BV2221 — STAR vs strategy — sincere ballots elect th | 1 | single-race | 100 | STAR | BV |
| [`3494cb`](https://bettervoting.com/3494cb/results) | BV132 - verify number of votes vast - bloc STAR voti | 1 | single-race | 4 | STAR | BV |
| [`36f4v2`](https://bettervoting.com/36f4v2/results) | BV2219 — Equally Weighted Vote — base election (STAR | 1 | single-race | 3 | STAR | BV |
| [`39py93`](https://bettervoting.com/39py93/results) | BV2204 — The Transfer Machine, control — an STV fini | 1 | single-race | 13 | STV | BV |
| [`3r3yf7`](https://bettervoting.com/3r3yf7/results) | BV2141 — Ranked Robin — a Copeland tie that needs al | 1 | single-race | 81 | RankedRobin | BV |
| [`3w6v4b`](https://bettervoting.com/3w6v4b/results) | Equal Support vs Abstention — minimal STAR test (A/B | 1 | single-race | 5 | STAR | BV |
| [`3yr2qd`](https://bettervoting.com/3yr2qd/results) | Block STAR | 1 | single-race | 3 | STAR | BV |
| [`484mbm`](https://bettervoting.com/484mbm/results) | BV2263 — Bloc STAR — a three-way tie no rung can bre | 1 | single-race | 3 | STAR | BV |
| [`48hjkv`](https://bettervoting.com/48hjkv/results) | BV2140 — Ranked Robin worked example — most pairwise | 1 | single-race | 35 | RankedRobin | BV |
| [`4gfwdq`](https://bettervoting.com/4gfwdq/results) | BV2142 — Ranked Robin clone independence (1 of 2) —  | 1 | single-race | 33 | RankedRobin | BV |
| [`4h89vj`](https://bettervoting.com/4h89vj/results) | B15 - Basic - 2 candidates - Plurality - Abstain | 1 | single-race | 12 | Plurality | BV |
| [`4jmgrd`](https://bettervoting.com/4jmgrd/results) | BV2234 — The Graders' Divide — a harsh 0-2 camp meet | 1 | single-race | 31 | STAR | BV |
| [`6hv7jf`](https://bettervoting.com/6hv7jf/results) | BV1570 - deactivate selection - plurality voting - C | 1 | single-race | 3 | Plurality | BV |
| [`6m3gxq`](https://bettervoting.com/6m3gxq/results) | BV2268 — Two-seat board by Bloc STAR: a fourth candi | 1 | single-race | 7 | STAR | BV |
| [`6tthfv`](https://bettervoting.com/6tthfv/results) | BV2252 — Goodberry's Frozen Custard, Cary NC — Best  | 1 | single-race | 0 | STAR | BV |
| [`6xhfp8`](https://bettervoting.com/6xhfp8/results) | BV11 - Valid Ballot - Full and Equal Support (2 Cand | 1 | single-race | 3 | STAR | BV |
| [`74pbyg`](https://bettervoting.com/74pbyg/results) | BV2237 — Noise Soup — weak factions, cross-winds, fl | 1 | single-race | 47 | STAR | BV |
| [`7j2bqf`](https://bettervoting.com/7j2bqf/results) | BV2229 — FairVote-vs-STAR check: French 2017 honest  | 1 | single-race | 100 | STAR | BV |
| [`7mckyg`](https://bettervoting.com/7mckyg/results) | BV2206 — Favorite betrayal in STAR, 1 of 2 — honest  | 1 | single-race | 57 | STAR | BV |
| [`7pdq3r`](https://bettervoting.com/7pdq3r/results) | BV95b - Majority Criterion: favorite loses (backs tw | 1 | single-race | 5 | STAR | BV |
| [`7q6by8`](https://bettervoting.com/7q6by8/results) | BV2208 — Burial in Ranked Robin, 1 of 2 — sincere ba | 1 | single-race | 42 | RankedRobin | BV |
| [`8fvd2x`](https://bettervoting.com/8fvd2x/results) | BV126 - “ties every time - every step” - Multiple ti | 1 | single-race | 7 | STAR | BV |
| [`8h3yrx`](https://bettervoting.com/8h3yrx/results) | BV1835 — Committee election, 100 voters, 4 seats: th | 1 | single-race | 100 | STAR | BV |
| [`8h4bvh`](https://bettervoting.com/8h4bvh/results) | BV2270 — Ranked Robin: two candidates tie on pairwis | 1 | single-race | 9 | RankedRobin | BV |
| [`8xwx43`](https://bettervoting.com/8xwx43/results) | BV2205 — The sole-survivor STV finish — six voters,  | 1 | single-race | 6 | STV | BV |
| [`9dhv8y`](https://bettervoting.com/9dhv8y/results) | No-show paradox (2 of 2) — the 8 April fans vote; RC | 1 | single-race | 62 | STAR | BV |
| [`9dx494`](https://bettervoting.com/9dx494/results) | BV2244 — The Herb Garden Council — Bloc STAR, 3 seat | 1 | single-race | 36 | STAR | BV |
| [`9ff9jk`](https://bettervoting.com/9ff9jk/results) | BV130 — 6 candidates / 3 winners, Bloc STAR | 1 | single-race | 4 | STAR | BV |
| [`9m6rxr`](https://bettervoting.com/9m6rxr/results) | BV95a - Majority Criterion: favorite survives (backs | 1 | single-race | 5 | STAR | BV |
| [`9pr3wr`](https://bettervoting.com/9pr3wr/results) | BV2143 — Ranked Robin clone independence (2 of 2) —  | 1 | single-race | 33 | RankedRobin | BV |
| `00_c3_b3_bloc-baseline-2-seats` | Bloc STAR baseline — 3 candidates, 2 seats (clean, n | 1 | single-race | 3 | STAR | LH-only |
| `00_plurality_vs_majority` | Plurality vs Majority — most votes isn't more than h | 1 | single-race | 100 | STAR | LH-only |
| `01_c4_b2_bloc-star-2-seats` | Bloc STAR Voting: 2-Seat Committee Election | 1 | single-race | 2 | STAR | LH-only |
| `01_condorcet_winner` | Condorcet winner exists — Ranked Robin elects it | 1 | single-race | 5 | RankedRobin | LH-only |
| `01_political_left_split` | Spoiler — a split coalition hands the seat to the mi | 1 | single-race | 100 | STAR | LH-only |
| `01a_c2_b1_two-candidates` | The simplest possible STAR Voting example | 1 | single-race | 1 | STAR | LH-only |
| `01a_c3_b3_more-stars-fewer-voters` | More stars, fewer voters — the runoff overturns the  | 1 | single-race | 3 | STAR | LH-only |
| `01b_c2_b2_two-candidates` | Again, very similar - this time second ballot is 5 a | 1 | single-race | 2 | STAR | LH-only |
| `01b_c3_b9_overturn-holds-at-scale` | The same overturn at scale — 67% to 33% | 1 | single-race | 9 | STAR | LH-only |
| `01c_c2_b3_two-candidates` | Equal support example ("I like both flavors") | 1 | single-race | 3 | STAR | LH-only |
| `02_c5_b5_leader-overturned` | Five candidates — the score leader is overturned in  | 1 | single-race | 5 | STAR | LH-only |
| `02_cycle_no_condorcet` | No Condorcet winner (a cycle) — Ranked Robin still e | 1 | single-race | 7 | RankedRobin | LH-only |
| `02_icecream_chocolate_split` | Spoiler — chocolate's majority splits, vanilla steal | 1 | single-race | 100 | STAR | LH-only |
| `02a_c3_b1_three-candidates` | Three candidates, one ballot - single-winner STAR | 1 | single-race | 1 | STAR | LH-only |
| `02a_c5_b63_proportional-allocated-score` | Proportional STAR — Allocated Score Voting | 1 | single-race | 63 | STAR_PR | LH-only |
| `02b_c3_b2_three-candidates` | Three candidates, two ballots - single-winner STAR | 1 | single-race | 2 | STAR | LH-only |
| `02b_c5_b63_proportional-sss` | Proportional STAR — Sequentially Spent Score | 1 | single-race | 63 | STAR_PR | LH-only |
| `02c_c5_b63_proportional-rrv` | Proportional — Reweighted Range Voting | 1 | single-race | 63 | STAR_PR | LH-only |
| `03_c7_b3_ice-cream-live` | Ice Cream — Flavor of the Year (the real recorded ra | 1 | single-race | 3 | STAR | LH-only |
| `03_lunch_veggie_vs_meat` | Spoiler — the veggie majority splits, the burger win | 1 | single-race | 100 | STAR | LH-only |
| `03_real_record0_c6_b5` | No Condorcet winner and Ranked Robin | 1 | single-race | 5 | RankedRobin | LH-only |
| `03a_c3_b3_style-bullet-vote` | Voting styles — a valid STAR bullet vote (3 candidat | 1 | single-race | 3 | STAR | LH-only |
| `03a_stv_3seats` | STV — 3 seats, 7 candidates (proportional RCV) | 1 | single-race | 100 | STV | LH-only |
| `03b_c3_b3_1_style-protest-vote` | Voting styles — low-score ballots | 1 | single-race | 3 | STAR | LH-only |
| `03b_c3_b3_2_expand_style-protest-vote` | Voting styles — low-score ballots (continued) | 1 | single-race | 3 | STAR | LH-only |
| `03b_star_pr_3seats` | Proportional STAR — same 3-seat electorate as the ST | 1 | single-race | 100 | STAR_PR | LH-only |
| `03c_c6_b8_style-gallery` | Voting styles — eight ways to fill out one 5-star ba | 1 | single-race | 8 | STAR | LH-only |
| `03d_c5_b5_style-gallery-five-more` | Voting styles — five more ways to fill out one 5-sta | 1 | single-race | 5 | STAR | LH-only |
| `04_c4_b3_runoff-confirms-leader` | The control case — here the runoff CONFIRMS the scor | 1 | single-race | 3 | STAR | LH-only |
| `04_smith_set_c4_b7` | The Smith set — the smallest club that beats everyon | 1 | single-race | 7 | RankedRobin | LH-only |
| `04_star_wars_vote_split` | The Voting Dilemma — Skywalker & Leia split the Rebe | 1 | single-race | 100 | STAR | LH-only |
| `04b_c4_b3_display-options-all` | All options demo | 1 | single-race | 3 | STAR | LH-only |
| `05_c3_b5_low-scores-bv1265` | Low scores, switched winner — the popover example (B | 1 | single-race | 5 | STAR | LH-only |
| `05a_c5_b3_unanimous-ballots` | Unanimous ballots (five candidates) | 1 | single-race | 3 | STAR | LH-only |
| `05a_residual_split_bullet-voting` | STAR's residual split — a coalition bullet-votes its | 1 | single-race | 100 | STAR | LH-only |
| `05b_residual_split_expressive-fix` | The cure — score your ally, and STAR's split disappe | 1 | single-race | 100 | STAR | LH-only |
| `06_sub_majority_not_spoiled` | A 41% winner that nothing spoiled — sub-majority is  | 1 | single-race | 44 | STAR | LH-only |
| `06a_c9_b3_large-field-equal-support` | Large field (9 candidates) — STAR scales, and Equal  | 1 | single-race | 3 | STAR | LH-only |
| `06b_c9_runoff-overturns-leader` | Large field (9 candidates) — the runoff OVERTURNS th | 1 | single-race | 3 | STAR | LH-only |
| `09_c4_b100_tennessee-capital` | Tennessee Capital — classic STAR example | 1 | single-race | 100 | STAR | LH-only |
| `321_tennessee_blank_encoding_c4_b100` | Tennessee capital by 3-2-1 Voting (blank = Bad) | 1 | single-race | 100 | 3-2-1 | LH-only |
| `BV_Library_approval_single_winner` | BV parity — Approval: most approvals wins (single wi | 1 | single-race | 10 | Approval | LH-only |
| `BV_Library_plurality_single_winner` | BV parity — Plurality (choose-one): most first-marks | 1 | single-race | 14 | Plurality | LH-only |
| `BV_Library_ranked_robin_single_winner` | BV parity — Ranked Robin: Condorcet winner (equal ra | 1 | single-race | 11 | RankedRobin | LH-only |
| `BV_Library_ranked_robin_ties` | BV parity — Ranked Robin: Copeland tie broken by tie | 1 | single-race | 6 | RankedRobin | LH-only |
| `BV_Library_star_condorcet_winner` | BV parity — STAR: highest-scoring Condorcet winner | 1 | single-race | 10 | STAR | LH-only |
| `BV_Library_star_pr_basic_two_seats` | BV parity — STAR_PR (Allocated Score): basic two-sea | 1 | single-race | 10 | STAR_PR | LH-only |
| `BV_Library_star_pr_fractional_surplus` | BV parity — STAR_PR (Allocated Score): fractional su | 1 | single-race | 12 | STAR_PR | LH-only |
| `BV_Library_star_pr_voters_fewer_than_seats` | BV parity — STAR_PR (Allocated Score): fewer voters  | 1 | single-race | 2 | STAR_PR | LH-only |
| `BV_Library_star_runnerup_tie` | BV parity — STAR: runner-up tie, Allison wins | 1 | single-race | 10 | STAR | LH-only |
| `BV_Library_star_runoff` | BV parity — STAR: runoff, lower total wins the runof | 1 | single-race | 2 | STAR | LH-only |
| `BV_Library_star_runoff_score_tie_five_star` | BV parity — STAR: runoff & score tie, five-star tieb | 1 | single-race | 2 | STAR | LH-only |
| `BV_Library_star_runoff_tie_score_resolves` | BV parity — STAR: runoff tie broken by score | 1 | single-race | 2 | STAR | LH-only |
| `Black_Curtain_01_c3_b5_hidden-consensus` | The Black Curtain | 1 | single-race | 5 | STAR | LH-only |
| `Black_Curtain_01a_c3_b5_approval` | The Black Curtain | 1 | single-race | 5 | Approval | LH-only |
| `Black_Curtain_01b_c3_b5_dichotomous` | The Black Curtain | 1 | single-race | 5 | STAR | LH-only |
| `Black_Curtain_02_c3_b5_near-clones` | The Black Curtain | 1 | single-race | 5 | STAR | LH-only |
| `Black_Curtain_03_c3_b5_polarized-on-cal` | The Black Curtain | 1 | single-race | 5 | STAR | LH-only |
| `Black_Curtain_04_c4_b5_four-candidates` | The Black Curtain | 1 | single-race | 5 | STAR | LH-only |
| `Flat_scores_ties_01_baseline_clean` | Flat scores 01 — clean top two (works-fine baseline) | 1 | single-race | 2 | STAR | LH-only |
| `Flat_scores_ties_02_runoff_tie_2cand` | Flat scores 02 — runoff tie, two candidates (everyon | 1 | single-race | 2 | STAR | LH-only |
| `Flat_scores_ties_03_runoff_tie_split` | Flat scores 03 — runoff tie, an even 1-1 split | 1 | single-race | 2 | STAR | LH-only |
| `Flat_scores_ties_04_scoring_tie_2way` | Flat scores 04 — scoring-round tie for the 2nd final | 1 | single-race | 3 | STAR | LH-only |
| `Flat_scores_ties_05_scoring_tie_3way_xmyf7k` | Flat scores 05 — scoring-round 3-way tie (BV555, xmy | 1 | single-race | 2 | STAR | LH-only |
| `Flat_scores_ties_06_scoring_tie_4way` | Flat scores 06 — scoring-round 4-way tie (ties at ev | 1 | single-race | 2 | STAR | LH-only |
| `Flat_scores_ties_07_fully_flat` | Flat scores 07 — fully flat ballots (the maximal tie | 1 | single-race | 2 | STAR | LH-only |
| `Flat_scores_ties_08_all_flat_zero_count` | Flat scores 08 — every ballot flat (BetterVoting cou | 1 | single-race | 5 | STAR | LH-only |
| `RCV_ballot_example` | RCV-IRV — a basic ranked-ballot example (3 candidate | 1 | single-race | 100 | IRV | LH-only |
| `abstention_reconciliation_min_c2_b6` | Abstention vs Equal Support — the minimal reconcilia | 1 | single-race | 6 | STAR | LH-only |
| `abstentions` | Abstentions — blank and abstaining ballots in STAR | 1 | single-race | 6 | STAR | LH-only |
| `alabama_2seats` | The Alabama paradox — 2 seats | 1 | single-race | 5 | STAR_PR | LH-only |
| `alabama_3seats` | The Alabama paradox — 3 seats | 1 | single-race | 5 | STAR_PR | LH-only |
| `alaska_buried_c3_b200` | Alaska 2022 (Begich buried) — a manufactured cycle;  | 1 | single-race | 200 | IRV | LH-only |
| `alaska_sincere_c3_b200` | Alaska 2022 (sincere) — Begich is the Condorcet winn | 1 | single-race | 200 | IRV | LH-only |
| `alaska_upward_after` | Upward monotonicity (Alaska 2022) — AFTER: raise the | 1 | single-race | 200 | IRV | LH-only |
| `alaska_upward_before` | Upward monotonicity (Alaska 2022) — BEFORE: Peltola  | 1 | single-race | 200 | IRV | LH-only |
| `approval_bloc_2seats_c4_b6` | Bloc Approval — 2 seats, majority sweep | 1 | single-race | 6 | Approval | LH-only |
| `approval_bloc_3seats_c6_b5` | Bloc Approval — 3-seat city council at-large | 1 | single-race | 5 | Approval | LH-only |
| `balance_base_irv_c3_b9` | Equal-vote balance — base (IRV elects the Condorcet  | 1 | single-race | 9 | IRV | LH-only |
| `balance_plus_opposite_c3_b15` | Equal-vote balance — plus 3 opposite pairs (IRV flip | 1 | single-race | 15 | IRV | LH-only |
| `ballot_expressiveness_c9_irv_top5` | Nine candidates, 25 voters — ranking only five, coun | 1 | single-race | 25 | IRV | LH-only |
| `batch_all_out_condorcet_c3_b3` | Batch elimination empties the field — with a Condorc | 1 | single-race | 3 | IRV | LH-only |
| `batch_all_out_cycle_c3_b3` | Batch elimination empties the field — the perfect cy | 1 | single-race | 3 | IRV | LH-only |
| `batch_all_out_round2_c4_b6` | The field empties in round two — and Pareto is what  | 1 | single-race | 6 | IRV | LH-only |
| `bloc_lot_path_dependence_a_c3_b5` | Bloc STAR — a seat-1 lot decides who wins seat 2 (lo | 1 | single-race | 5 | STAR | LH-only |
| `bloc_lot_path_dependence_b_c3_b5` | Bloc STAR — a seat-1 lot decides who wins seat 2 (lo | 1 | single-race | 5 | STAR | LH-only |
| `blocs_bloc_c9_b10` | Left, Centre, Right — Bloc STAR fills the council | 1 | single-race | 10 | bloc | LH-only |
| `blocs_pr_c9_b10` | Left, Centre, Right — Proportional STAR fills the co | 1 | single-race | 10 | STAR_PR | LH-only |
| `bpv_bakery_block_plurality_c4_b12` | The same electorate under plurality block voting — t | 1 | single-race | 12 | Plurality | LH-only |
| `bpv_bakery_seat1_c4_b12` | Block preferential voting — seat 1 of 2 (bakery co-o | 1 | single-race | 12 | IRV | LH-only |
| `bpv_bakery_seat2_c3_b12` | Block preferential voting — seat 2 of 2 (bakery co-o | 1 | single-race | 12 | IRV | LH-only |
| `bpv_bakery_stv_c4_b12` | The same ballots under STV — 2 seats, and the minori | 1 | single-race | 12 | STV | LH-only |
| `brams_ex3_two_candidates_c2_b5` | Brams Example 3 — two candidates: two loud fans vs t | 1 | single-race | 5 | STAR | LH-only |
| `brams_ex6_three_winners_c3_b9` | Brams Example 6 — three counts, three winners (STAR  | 1 | single-race | 9 | STAR | LH-only |
| `brams_grading_paradox_c3_b3` | Brams' grading paradox — the grade leader loses the  | 1 | single-race | 3 | STAR | LH-only |
| `burlington_2009_irv` | Burlington 2009 mayor — RCV-IRV: the real center squ | 1 | single-race | 8974 | IRV | LH-only |
| `burlington_2009_raise_kiss_nonmono` | Burlington 2009, the raise — 750 Wright voters rank  | 1 | single-race | 8974 | IRV | LH-only |
| `burlington_2009_ranked_robin` | Burlington 2009 mayor — Ranked Robin: Montroll, a pe | 1 | single-race | 8974 | RankedRobin | LH-only |
| `cav_library_board_blank_is_zero_c3_b12` | Library board on a blank-is-zero score ballot — the  | 1 | single-race | 12 | Range | LH-only |
| `cav_library_board_c3_b12` | Library board by Combined Approval Voting — the newc | 1 | single-race | 12 | CAV | LH-only |
| `center_squeeze_irv` | Center squeeze (RCV-IRV) — minimal 27-voter case (th | 1 | single-race | 27 | IRV | LH-only |
| `center_squeeze_star` | Center squeeze — STAR elects the consensus (Center) | 1 | single-race | 27 | STAR | LH-only |
| `center_squeeze_voteline_1d` | Center squeeze — the voteline 1D spectrum (Red / Gre | 1 | single-race | 998 | STAR | LH-only |
| `chicken_approval` | Chicken / Burr dilemma — Approval, honest: A and B t | 1 | single-race | 100 | Approval | LH-only |
| `chicken_star` | Chicken / Burr dilemma — STAR resolves it (allies A  | 1 | single-race | 100 | STAR | LH-only |
| `clone_teaming_01_pre` | Clone independence (1/2) — before cloning: A, B, C t | 1 | single-race | 33 | RankedRobin | LH-only |
| `clone_teaming_02_post` | Clone independence (2/2) — teaming: A runs clones an | 1 | single-race | 33 | RankedRobin | LH-only |
| `coombs_ex18_monotonicity` | Coombs Ex.18 — Bree is raised on four ballots and lo | 1 | single-race | 33 | IRV | LH-only |
| `coombs_ex20_amalgamated` | Coombs Ex.20 — amalgamated: both districts chose B,  | 1 | single-race | 41 | IRV | LH-only |
| `coombs_ex20_district1` | Coombs Ex.20 — District I: 34 voters, Coombs elects  | 1 | single-race | 34 | IRV | LH-only |
| `coombs_ex20_district2` | Coombs Ex.20 — District II: 7 voters, B wins outrigh | 1 | single-race | 7 | IRV | LH-only |
| `coombs_ex21_twin_after` | Coombs Ex.21 — after: two twins join for B, and B's  | 1 | single-race | 22 | IRV | LH-only |
| `coombs_ex21_twin_before` | Coombs Ex.21 — before: 20 voters, Coombs elects B ou | 1 | single-race | 20 | IRV | LH-only |
| `coombs_ex22_scc` | Coombs Ex.22 — SCC: C drops out and A wins instead o | 1 | single-race | 29 | IRV | LH-only |
| `coop_board_approval` | Co-op board — Yes/No approval ballot (same nine vote | 1 | single-race | 9 | Approval | LH-only |
| `coop_board_scores_allocated` | Co-op board — 0–5 score ballot, allocated | 1 | single-race | 9 | STAR_PR | LH-only |
| `coop_board_scores_sss` | Co-op board — 0–5 score ballot, sss | 1 | single-race | 9 | STAR_PR | LH-only |
| `copeland_half_credit_decides` | Ranked Robin — the half-point for a draw decides the | 1 | single-race | 30 | RankedRobin | LH-only |
| `copeland_vs_clones_c5_b3` | Copeland picks one, composition-consistency demands  | 1 | single-race | 3 | RankedRobin | LH-only |
| `count_simplicity_star_vs_irv` | Same winner, very different counts — STAR adds, IRV  | 1 | single-race | 40 | STAR | LH-only |
| `count_vs_weight_slates_c9_b66` | Three slates, five seats — the count-vs-weight finge | 1 | single-race | 66 | STAR_PR | LH-only |
| `crowded_field_c3_approval` | Crowded field, rung 3 — 3 candidates, 65 voters, cou | 1 | single-race | 65 | Approval | LH-only |
| `crowded_field_c3_irv` | Crowded field, rung 3 — 3 candidates, 65 voters, cou | 1 | single-race | 65 | IRV | LH-only |
| `crowded_field_c3_ranked_robin` | Crowded field, rung 3 — 3 candidates, 65 voters, cou | 1 | single-race | 65 | RankedRobin | LH-only |
| `crowded_field_c3_star` | Crowded field, rung 3 — 3 candidates, 65 voters, cou | 1 | single-race | 65 | STAR | LH-only |
| `crowded_field_c5_approval` | Crowded field, rung 5 — 5 candidates, 65 voters, cou | 1 | single-race | 65 | Approval | LH-only |
| `crowded_field_c5_irv` | Crowded field, rung 5 — 5 candidates, 65 voters, cou | 1 | single-race | 65 | IRV | LH-only |
| `crowded_field_c5_ranked_robin` | Crowded field, rung 5 — 5 candidates, 65 voters, cou | 1 | single-race | 65 | RankedRobin | LH-only |
| `crowded_field_c5_star` | Crowded field, rung 5 — 5 candidates, 65 voters, cou | 1 | single-race | 65 | STAR | LH-only |
| `crowded_field_c7_approval` | Crowded field, rung 7 — 7 candidates, 65 voters, cou | 1 | single-race | 65 | Approval | LH-only |
| `crowded_field_c7_irv` | Crowded field, rung 7 — 7 candidates, 65 voters, cou | 1 | single-race | 65 | IRV | LH-only |
| `crowded_field_c7_ranked_robin` | Crowded field, rung 7 — 7 candidates, 65 voters, cou | 1 | single-race | 65 | RankedRobin | LH-only |
| `crowded_field_c7_star` | Crowded field, rung 7 — 7 candidates, 65 voters, cou | 1 | single-race | 65 | STAR | LH-only |
| `csv_ambiguity_ex1_c4_b8` | The eight ambiguous CSV lines, disambiguated (BV iss | 1 | single-race | 8 | STAR | LH-only |
| `cycle_C03_fewV15_noise_1` | STAR vs RR divergence -- 3 cands, 15 voters, cycle ( | 1 | single-race | 15 | STAR | LH-only |
| `cycle_C03_fewV15_noise_2` | STAR vs RR divergence -- 3 cands, 15 voters, cycle ( | 1 | single-race | 15 | STAR | LH-only |
| `cycle_C03_medV45_noise_1` | STAR vs RR divergence -- 3 cands, 45 voters, cycle ( | 1 | single-race | 45 | STAR | LH-only |
| `cycle_C05_fewV15_noise_2` | STAR vs RR divergence -- 5 cands, 15 voters, cycle ( | 1 | single-race | 15 | STAR | LH-only |
| `cycle_C05_fewV28_bloc_1` | STAR vs RR divergence -- 5 cands, 28 voters, cycle ( | 1 | single-race | 28 | STAR | LH-only |
| `cycle_C05_medV45_noise_1` | STAR vs RR divergence -- 5 cands, 45 voters, cycle ( | 1 | single-race | 45 | STAR | LH-only |
| `cycle_C05_medV45_noise_2` | STAR vs RR divergence -- 5 cands, 45 voters, cycle ( | 1 | single-race | 45 | STAR | LH-only |
| `cycle_C07_fewV15_noise_1` | STAR vs RR divergence -- 7 cands, 15 voters, cycle ( | 1 | single-race | 15 | STAR | LH-only |
| `cycle_C07_largeV598_bloc_1` | STAR vs RR divergence -- 7 cands, 598 voters, cycle  | 1 | single-race | 598 | STAR | LH-only |
| `cycle_C07_medV149_bloc_2` | STAR vs RR divergence -- 7 cands, 149 voters, cycle  | 1 | single-race | 149 | STAR | LH-only |
| `cycle_C10_fewV15_noise_1` | STAR vs RR divergence -- 10 cands, 15 voters, cycle  | 1 | single-race | 15 | STAR | LH-only |
| `cycle_C10_fewV15_noise_2` | STAR vs RR divergence -- 10 cands, 15 voters, cycle  | 1 | single-race | 15 | STAR | LH-only |
| `cycle_C10_fewV28_bloc_1` | STAR vs RR divergence -- 10 cands, 28 voters, cycle  | 1 | single-race | 28 | STAR | LH-only |
| `cycle_C10_fewV29_bloc_2` | STAR vs RR divergence -- 10 cands, 29 voters, cycle  | 1 | single-race | 29 | STAR | LH-only |
| `cycle_C10_medV149_bloc_2` | STAR vs RR divergence -- 10 cands, 149 voters, cycle | 1 | single-race | 149 | STAR | LH-only |
| `cycle_C10_medV45_noise_1` | STAR vs RR divergence -- 10 cands, 45 voters, cycle  | 1 | single-race | 45 | STAR | LH-only |
| `cycle_C10_medV45_noise_2` | STAR vs RR divergence -- 10 cands, 45 voters, cycle  | 1 | single-race | 45 | STAR | LH-only |
| `cycle_copeland_ties_c4_b21` | A cycle Copeland can't break — three trails tie 1-1, | 1 | single-race | 21 | RankedRobin | LH-only |
| `cycle_family_splits_c5_b77` | The whole Condorcet family splits — Minimax & Schulz | 1 | single-race | 77 | RankedRobin | LH-only |
| `cycle_schulze_vs_ranked_pairs_c4_b40` | Same ballots, different Condorcet rule — Schulze say | 1 | single-race | 40 | RankedRobin | LH-only |
| `cycle_vote_on_the_rule_irv_c5_b999` | Best Cycle-Breaking Rule — a society votes on how to | 1 | single-race | 999 | IRV | LH-only |
| `cycle_vote_on_the_rule_rr_c5_b999` | Best Cycle-Breaking Rule — the cycle itself, and who | 1 | single-race | 999 | RankedRobin | LH-only |
| `dark_horse_star` | Dark Horse — STAR elects the honest winner A (Borda  | 1 | single-race | 100 | STAR | LH-only |
| `darkhorse_C03_fewV15_noise_1` | STAR vs RR divergence -- 3 cands, 15 voters, darkhor | 1 | single-race | 15 | STAR | LH-only |
| `darkhorse_C05_largeV599_bloc_1` | STAR vs RR divergence -- 5 cands, 599 voters, darkho | 1 | single-race | 599 | STAR | LH-only |
| `darkhorse_C07_fewV30_bloc_1` | STAR vs RR divergence -- 7 cands, 30 voters, darkhor | 1 | single-race | 30 | STAR | LH-only |
| `darkhorse_C07_largeV597_bloc_1` | STAR vs RR divergence -- 7 cands, 597 voters, darkho | 1 | single-race | 597 | STAR | LH-only |
| `darkhorse_C07_largeV598_bloc_2` | STAR vs RR divergence -- 7 cands, 598 voters, darkho | 1 | single-race | 598 | STAR | LH-only |
| `darkhorse_C07_medV147_bloc_1` | STAR vs RR divergence -- 7 cands, 147 voters, darkho | 1 | single-race | 147 | STAR | LH-only |
| `darkhorse_C07_medV45_noise_1` | STAR vs RR divergence -- 7 cands, 45 voters, darkhor | 1 | single-race | 45 | STAR | LH-only |
| `darkhorse_C10_largeV598_bloc_1` | STAR vs RR divergence -- 10 cands, 598 voters, darkh | 1 | single-race | 598 | STAR | LH-only |
| `darkhorse_C10_largeV599_bloc_2` | STAR vs RR divergence -- 10 cands, 599 voters, darkh | 1 | single-race | 599 | STAR | LH-only |
| `dead_heat_lot_tiebreak` | Ranked Robin — a dead heat that runs the whole tiebr | 1 | single-race | 4 | RankedRobin | LH-only |
| `dead_rung_scoring_dead_cap2` | Dead rung — scoring round, dead five-star rung, cap  | 1 | single-race | 2 | STAR | LH-only |
| `dead_rung_scoring_dead_cap3` | Dead rung — scoring round, dead five-star rung, cap  | 1 | single-race | 2 | STAR | LH-only |
| `dead_rung_scoring_dead_cap4` | Dead rung — scoring round, dead five-star rung, cap  | 1 | single-race | 2 | STAR | LH-only |
| `display_options_demo` | Display options demo | 1 | single-race | 4 | STAR | LH-only |
| `edelman_perfect_component_c3_b30` | A perfect 'Condorcet component' (30 voters) — every  | 1 | single-race | 30 | STAR | LH-only |
| `equal_support_runoff_demo` | Equal Support — counted in both rounds, neutral only | 1 | single-race | 100 | STAR | LH-only |
| `ex02_bella_exits` | Exercise 2 — The tenth ballot: Bella withdraws | 1 | single-race | 9 | STAR | LH-only |
| `ex02_nine_ballots` | Exercise 2 — The tenth ballot: the nine counted ball | 1 | single-race | 9 | STAR | LH-only |
| `ex02_tenth_ballot` | Exercise 2 — The tenth ballot: all ten ballots | 1 | single-race | 10 | STAR | LH-only |
| `ex04_olympics_1994` | Exercise 4 — Lillehammer 1994: nine judges, three sk | 1 | single-race | 9 | STAR | LH-only |
| `ex07_vanishing_votes` | Exercise 7 — The vanishing votes that never vanished | 1 | single-race | 9 | STAR | LH-only |
| `ex08_minimal_reversal_2c` | Exercise 8 — a smallest runoff reversal (sample solu | 1 | single-race | 3 | STAR | LH-only |
| `ex08_minimal_reversal_3c` | Exercise 8 — a small runoff reversal (sample solutio | 1 | single-race | 5 | STAR | LH-only |
| `ex09_game_night_cycle` | Exercise 9 — Game night: nobody is unbeatable (a Ran | 1 | single-race | 10 | RankedRobin | LH-only |
| `felsenthal_ex6_pareto_approval` | Felsenthal Ex.6 — Approval can elect a Pareto-domina | 1 | single-race | 3 | Approval | LH-only |
| `felsenthal_ex6_ranked_robin` | Felsenthal Ex.6 — Ranked Robin: the Pareto-dominant  | 1 | single-race | 3 | RankedRobin | LH-only |
| `five_answers_one_election_c4_b3` | Five defensible answers, one three-ballot election ( | 1 | single-race | 3 | RankedRobin | LH-only |
| `free_ride_arms_race_allocated` | Free riding — both sides ride, nobody gains | 1 | single-race | 20 | STAR_PR | LH-only |
| `free_ride_honest_allocated` | Free riding — honest baseline (Allocated Score) | 1 | single-race | 20 | STAR_PR | LH-only |
| `free_ride_honest_rrv` | Free riding — honest baseline (RRV) | 1 | single-race | 20 | STAR_PR | LH-only |
| `free_ride_honest_sss` | Free riding — honest baseline (SSS) | 1 | single-race | 20 | STAR_PR | LH-only |
| `free_ride_hylland_allocated` | Free riding — the free ride (Allocated Score) | 1 | single-race | 20 | STAR_PR | LH-only |
| `free_ride_hylland_rrv` | Free riding — the free ride fails (RRV) | 1 | single-race | 20 | STAR_PR | LH-only |
| `free_ride_hylland_sss` | Free riding — the free ride (SSS) | 1 | single-race | 20 | STAR_PR | LH-only |
| `hh41_01_approval_as_printed` | Hamlin & Hua §4.1 — the approval count as printed: B | 1 | single-race | 100 | Approval | LH-only |
| `hh41_02_preferences_ranked_robin` | Hamlin & Hua §4.1 — the assumed preferences, counted | 1 | single-race | 100 | RankedRobin | LH-only |
| `hh41_03_marks_read_pairwise` | Hamlin & Hua §4.1 — the same marks read pairwise: 60 | 1 | single-race | 100 | STAR | LH-only |
| `hh41_04_stipulated_utilities_star` | Hamlin & Hua §4.1 — their own utility stipulation, o | 1 | single-race | 100 | STAR | LH-only |
| `hh41_05_majority_bullet_votes` | Hamlin & Hua §4.1 — the majority bullet-votes instea | 1 | single-race | 100 | Approval | LH-only |
| `hillinger_t3_arbitrariness` | Hillinger Table 3 — one approval result, two opposit | 1 | single-race | 7 | Approval | LH-only |
| `hillinger_t4_affine` | Hillinger Table 4, rescaled — what 'cardinal' actual | 1 | single-race | 30 | STAR | LH-only |
| `hillinger_t4_ev3` | Hillinger Table 4 — three methods, three winners (EV | 1 | single-race | 30 | STAR | LH-only |
| `irv_combined` | Summability demo — RCV-IRV combined A+B (B eliminate | 1 | single-race | 26 | IRV | LH-only |
| `irv_district_A` | Summability demo — RCV-IRV district A (B wins) | 1 | single-race | 13 | IRV | LH-only |
| `irv_district_B` | Summability demo — RCV-IRV district B (B wins) | 1 | single-race | 13 | IRV | LH-only |
| `lackner_skowron_shadow_bloc_star_c7_b12` | Shadow STAR (Bloc) — Lackner & Skowron's running exa | 1 | single-race | 12 | STAR | LH-only |
| `lackner_skowron_shadow_star_pr_c7_b12` | Shadow STAR-PR (Allocated Score) — Lackner & Skowron | 1 | single-race | 12 | STAR_PR | LH-only |
| `lackner_skowron_shadow_star_pr_rrv_c7_b12` | Shadow STAR-PR (RRV) — Lackner & Skowron's running e | 1 | single-race | 12 | STAR_PR | LH-only |
| `lot_random_vs_published_jfk7pd_published_order` | Lot-decided tie (BV jfk7pd) — following a determinis | 1 | single-race | 2 | STAR | LH-only |
| `lot_tiebreak_bv_order` | Lot tiebreak — following BetterVoting's drawn order | 1 | single-race | 2 | STAR | LH-only |
| `lot_tiebreak_published_order` | Lot tiebreak — following the new published-lot appro | 1 | single-race | 2 | STAR | LH-only |
| `majority_illusion_c3_b41_score_vs_star` | The majority illusion — Score elects Brian, STAR ele | 1 | single-race | 41 | STAR | LH-only |
| `majority_illusion_c3_b41_two_rivals` | The majority illusion, one score changed — the major | 1 | single-race | 41 | STAR | LH-only |
| `majority_vs_consensus_51_49` | Majority criterion vs. the consensus candidate — the | 1 | single-race | 100 | STAR | LH-only |
| `margins_paper_exact_304` | Margins matter — the textbook profile at its printed | 1 | single-race | 304 | RankedRobin | LH-only |
| `min_bloc_c3_b2` | The smallest divergence — Bloc STAR | 1 | single-race | 2 | bloc | LH-only |
| `min_pr_c3_b2` | The smallest divergence — Proportional STAR (Allocat | 1 | single-race | 2 | STAR_PR | LH-only |
| `minimax_ex30_noshow_after` | Minimax Ex.30 — after: three C>A>B>D voters stay hom | 1 | single-race | 16 | RankedRobin | LH-only |
| `minimax_ex30_noshow_before` | Minimax Ex.30 — before: all 19 vote, Minimax elects  | 1 | single-race | 19 | RankedRobin | LH-only |
| `minimax_ex31_truncation` | Minimax Ex.31 — truncation: the same 19 voters, four | 1 | single-race | 19 | RankedRobin | LH-only |
| `minimax_ex32_amalgamated` | Minimax Ex.32 — amalgamated: both districts elected  | 1 | single-race | 14 | RankedRobin | LH-only |
| `minimax_ex32_district2` | Minimax Ex.32 — District II: three voters, D wins ou | 1 | single-race | 3 | RankedRobin | LH-only |
| `minimax_ex33_scc` | Minimax Ex.33 — SCC: drop a loser and the winner cha | 1 | single-race | 7 | RankedRobin | LH-only |
| `minneapolis_2017_irv` | Minneapolis 2017 Mayor — 105,928 real ballots, and I | 1 | single-race | 104484 | IRV | LH-only |
| `minneapolis_2017_ranked_robin` | Minneapolis 2017 Mayor — the head-to-head check: rig | 1 | single-race | 104484 | RankedRobin | LH-only |
| `misjudged_queue_bury` | Misjudged queue — the free ride backfires | 1 | single-race | 20 | STAR_PR | LH-only |
| `misjudged_queue_honest` | Misjudged queue — honest baseline | 1 | single-race | 20 | STAR_PR | LH-only |
| `misjudged_queue_hylland` | Misjudged queue — the free ride achieves nothing | 1 | single-race | 20 | STAR_PR | LH-only |
| `mmp_block_approval` | Block approval voting — uncap the marks and the swee | 1 | single-race | 9 | Approval | LH-only |
| `mmp_majority_block_runoff` | Majority block voting (round 2) — the runoff hands e | 1 | single-race | 9 | Plurality | LH-only |
| `mmp_majority_ceiling` | Block Voting (3 seats): the majority ceiling — a una | 1 | single-race | 30 | Plurality | LH-only |
| `mmp_minority_sweep` | Plurality block voting — a 44% minority sweeps all t | 1 | single-race | 9 | Plurality | LH-only |
| `mmp_sntv` | Multi-member plurality — SNTV (3 seats): the minorit | 1 | single-race | 10 | Plurality | LH-only |
| `mmp_sweep_floor` | Block voting — the smallest possible minority sweep  | 1 | single-race | 5 | Plurality | LH-only |
| `mono_raise_delete_after` | STAR mono-raise-delete — part 2: raise X, delete Y-b | 1 | single-race | 30 | STAR | LH-only |
| `mono_raise_delete_before` | STAR mono-raise-delete — part 1: baseline, X wins | 1 | single-race | 30 | STAR | LH-only |
| `monotonicity_irv_after` | Non-monotonicity (RCV-IRV) — part 2: raising X makes | 1 | single-race | 34 | IRV | LH-only |
| `monotonicity_irv_before` | Non-monotonicity (RCV-IRV) — part 1: baseline, X win | 1 | single-race | 34 | IRV | LH-only |
| `monotonicity_star_after` | Monotonicity — STAR counterpart (AFTER — X still win | 1 | single-race | 34 | STAR | LH-only |
| `monotonicity_star_before` | Monotonicity — STAR counterpart (BEFORE — X wins) | 1 | single-race | 34 | STAR | LH-only |
| `omr_opposition_decides` | Ordered majority rule — the opposition decides the A | 1 | single-race | 100 | IRV | LH-only |
| `options_examples` | Display-options reference — every reporting toggle ( | 1 | single-race | 100 | STAR | LH-only |
| `p3_manip_compromise_rr` | P3 manipulated — the mild version: three adjacent sw | 1 | single-race | 7 | RankedRobin | LH-only |
| `p3_manip_reversal_rr` | P3 manipulated — Zwicker's complete reversal makes D | 1 | single-race | 7 | RankedRobin | LH-only |
| `p3_manip_star` | P3 manipulated — two voters bury their 4th choice an | 1 | single-race | 7 | STAR | LH-only |
| `put_two_universes_c3_b4` | Parallel universes — one count, two legal answers | 1 | single-race | 4 | IRV | LH-only |
| `quorum_demo_c3_b6` | Quorum — an abstention still counts toward turnout | 1 | single-race | 6 | STAR | LH-only |
| `quorum_fail_demo_c3_b6` | Quorum FAILS — won the count, but not elected | 1 | single-race | 6 | STAR | LH-only |
| `race_nobody_can_lose_two_seat_control` | A race nobody can lose — the two-seat control | 1 | single-race | 7 | STAR | LH-only |
| `range_101_0to9_c3_b5` | Range / Score Voting on its own scale — 0–9, the can | 1 | single-race | 5 | Range | LH-only |
| `range_101_c3_b5` | Range / Score Voting 101 — highest total score wins | 1 | single-race | 5 | Range | LH-only |
| `range_sullivan_score_c4_b10` | Range / Score Voting — Sullivan's Example 5.2 (0–10  | 1 | single-race | 10 | Range | LH-only |
| `ranked_robin_consensus_center` | Ranked Robin (RCV-RR) — the consensus center wins th | 1 | single-race | 13 | RankedRobin | LH-only |
| `ranked_robin_intro_c3_b7` | Ranked Robin (RCV-RR) — the smallest round-robin tha | 1 | single-race | 7 | RankedRobin | LH-only |
| `reinf_combined_ben_c3_b9_rr` | Reinforcement — Combined, Ben branch (9 voters; both | 1 | single-race | 9 | RankedRobin | LH-only |
| `reinf_combined_cara_c3_b9_rr` | Reinforcement — Combined, Cara branch (9 voters; bot | 1 | single-race | 9 | RankedRobin | LH-only |
| `reinf_north_c3_b6_rr` | Reinforcement — North district alone (6 voters, a pe | 1 | single-race | 6 | RankedRobin | LH-only |
| `reinf_south_ben_c3_b3_rr` | Reinforcement — South district, Ben branch (3 voters | 1 | single-race | 3 | RankedRobin | LH-only |
| `reinf_south_c3_b3_rr` | Reinforcement — South district alone (3 voters, Ada  | 1 | single-race | 3 | RankedRobin | LH-only |
| `reinf_south_cara_c3_b3_rr` | Reinforcement — South district, Cara branch (3 voter | 1 | single-race | 3 | RankedRobin | LH-only |
| `reversal_convincing_c3_b100` | Runoff reversal, the convincing case — an intense mi | 1 | single-race | 100 | STAR | LH-only |
| `reversal_irv_original` | Reversal symmetry — RCV-IRV, original: A wins (best) | 1 | single-race | 24 | IRV | LH-only |
| `reversal_irv_reversed` | Reversal symmetry — RCV-IRV, reversed: A wins AGAIN  | 1 | single-race | 24 | IRV | LH-only |
| `reversal_jarring_c3_b100` | Runoff reversal, the jarring case — the near-consens | 1 | single-race | 100 | STAR | LH-only |
| `reversal_star_original` | Reversal symmetry — STAR, original: B (STAR does not | 1 | single-race | 24 | STAR | LH-only |
| `reversal_star_reversed` | Reversal symmetry — STAR, reversed: A (differs from  | 1 | single-race | 24 | STAR | LH-only |
| `rr_blank_is_last_c4_b3` | Ranked Robin — a blank is ranked LAST (and rank numb | 1 | single-race | 3 | RankedRobin | LH-only |
| `rr_combined` | Summability demo — Combined (A+B), counted by Ranked | 1 | single-race | 26 | RankedRobin | LH-only |
| `rr_district_A` | Summability demo — District A, counted by Ranked Rob | 1 | single-race | 13 | RankedRobin | LH-only |
| `rr_district_B` | Summability demo — District B, counted by Ranked Rob | 1 | single-race | 13 | RankedRobin | LH-only |
| `rr_vs_mwsl_cycle_c3_b32` | Ranked Robin vs Consensus Choice — the same cycle, t | 1 | single-race | 32 | RankedRobin | LH-only |
| `rrv_sample_c15_b13_three-parties` | RRV sample as single-winner STAR — three parties (Pu | 1 | single-race | 13 | STAR | LH-only |
| `same_matrix_p1_plurality` | Same matrix, different plurality — electorate P1: Ch | 1 | single-race | 12 | Plurality | LH-only |
| `same_matrix_p1_ranked_robin` | Same matrix, different plurality — electorate P1: Ra | 1 | single-race | 12 | RankedRobin | LH-only |
| `same_matrix_p2_plurality` | Same matrix, different plurality — electorate P2: Ch | 1 | single-race | 12 | Plurality | LH-only |
| `same_matrix_p2_ranked_robin` | Same matrix, different plurality — electorate P2: Ra | 1 | single-race | 12 | RankedRobin | LH-only |
| `same_matrix_p3_plurality` | Same matrix, different plurality — electorate P3: Ch | 1 | single-race | 12 | Plurality | LH-only |
| `same_matrix_p3_ranked_robin` | Same matrix, different plurality — electorate P3: Ra | 1 | single-race | 12 | RankedRobin | LH-only |
| `same_mean_different_spread_c2_b5` | Same mean, different spread — the consensus candidat | 1 | single-race | 5 | STAR | LH-only |
| `same_total_different_shape_c3_b7` | Same-ish total, different shape — the sandwich vote | 1 | single-race | 7 | STAR | LH-only |
| `sf_d7_downward_after` | Downward monotonicity (San Francisco D7 2020) — AFTE | 1 | single-race | 36626 | IRV | LH-only |
| `sf_d7_downward_before` | Downward monotonicity (San Francisco D7 2020) — BEFO | 1 | single-race | 36626 | IRV | LH-only |
| `split_cycle_schulze_spoiler_c5_b40` | A candidate nobody prefers still flips the winner —  | 1 | single-race | 40 | RankedRobin | LH-only |
| `star_ala_approval` | STAR à la Approval — 0/1 & marker ballots are legal  | 1 | single-race | 8 | STAR | LH-only |
| `star_combined` | Summability demo — STAR combined A+B (Oak; precinct  | 1 | single-race | 6 | STAR | LH-only |
| `star_district_A` | Summability demo — STAR district A (Maple wins outri | 1 | single-race | 3 | STAR | LH-only |
| `star_district_B` | Summability demo — STAR district B (Oak wins — a run | 1 | single-race | 3 | STAR | LH-only |
| `star_elects_a_covered_candidate_c4_b5` | STAR elects a covered candidate — five ballots, four | 1 | single-race | 5 | STAR | LH-only |
| `street_trees_five_rounds_c6_b100` | Street trees — five rounds, and the bar keeps droppi | 1 | single-race | 100 | IRV | LH-only |
| `succ_elim_ex10_amalgamated` | Successive elimination Ex.10 — amalgamated: every ro | 1 | single-race | 4 | RankedRobin | LH-only |
| `succ_elim_ex10_district1` | Successive elimination Ex.10 — District I: three vot | 1 | single-race | 3 | RankedRobin | LH-only |
| `succ_elim_ex10_district2` | Successive elimination Ex.10 — District II: a single | 1 | single-race | 1 | RankedRobin | LH-only |
| `succ_elim_ex11_twin_after` | Successive elimination Ex.11 — after: a twin joins a | 1 | single-race | 7 | RankedRobin | LH-only |
| `succ_elim_ex11_twin_before` | Successive elimination Ex.11 — before: six voters, t | 1 | single-race | 6 | RankedRobin | LH-only |
| `succ_elim_ex12_sincere` | Successive elimination Ex.12 — sincere: the A>B>C>D  | 1 | single-race | 6 | RankedRobin | LH-only |
| `succ_elim_ex12_truncated` | Successive elimination Ex.12 — truncated: naming onl | 1 | single-race | 6 | RankedRobin | LH-only |
| `succ_elim_ex9_noshow` | Successive elimination Ex.9 — two D voters stay home | 1 | single-race | 9 | RankedRobin | LH-only |
| `succ_elim_ex9_pareto` | Successive elimination Ex.9 — the agenda elects B, w | 1 | single-race | 11 | RankedRobin | LH-only |
| `tactical_max_c3_b9_hedged` | Tactical maximization in STAR (2 of 2) — four voters | 1 | single-race | 9 | STAR | LH-only |
| `tactical_max_c3_b9_honest` | Tactical maximization in STAR (1 of 2) — honest ball | 1 | single-race | 9 | STAR | LH-only |
| `three_neighbors_allocated` | Three neighbors, two seats — Allocated Score | 1 | single-race | 3 | STAR_PR | LH-only |
| `three_neighbors_rrv` | Three neighbors, two seats — Reweighted Range Voting | 1 | single-race | 3 | STAR_PR | LH-only |
| `three_neighbors_sss` | Three neighbors, two seats — Sequentially Spent Scor | 1 | single-race | 3 | STAR_PR | LH-only |
| `three_way_dead_rung_A` | Three-way dead-rung tie — published order A,B,C elec | 1 | single-race | 3 | STAR | LH-only |
| `three_way_dead_rung_B` | Three-way dead-rung tie — published order B,C,A elec | 1 | single-race | 3 | STAR | LH-only |
| `three_way_dead_rung_C` | Three-way dead-rung tie — published order C,A,B elec | 1 | single-race | 3 | STAR | LH-only |
| `three_winners_cw_score_runoff` | Three notions of "winner" disagree — Condorcet, Scor | 1 | single-race | 5 | STAR | LH-only |
| `tie_break_01_scoring_five_star_breaks` | Tie-break 01 — scoring-round tie, FIVE-STAR breaks i | 1 | single-race | 2 | STAR | LH-only |
| `tie_break_02_scoring_no_fives_to_lot` | Tie-break 02 — scoring-round tie, NO fives, five-sta | 1 | single-race | 2 | STAR | LH-only |
| `tie_break_03_runoff_no_fives_to_lot` | Tie-break 03 — runoff tie, score tied, NO fives → LO | 1 | single-race | 2 | STAR | LH-only |
| `tie_break_04_runoff_five_star_breaks` | Tie-break 04 — runoff tie, score tied, FIVE-STAR bre | 1 | single-race | 2 | STAR | LH-only |
| `tie_break_05_scoring_five_star_vs_adversarial_lot` | Dead rung 01 — scoring tie, five-star rung ALIVE | 1 | single-race | 5 | STAR | LH-only |
| `tie_break_06_scoring_dead_rung_adversarial_lot` | Dead rung 02 — same tie, but nobody scored a 5 | 1 | single-race | 5 | STAR | LH-only |
| `tie_break_07_runoff_five_star_vs_adversarial_lot` | Dead rung 03 — runoff tie broken by five-star | 1 | single-race | 2 | STAR | LH-only |
| `tie_break_08_runoff_dead_rung_adversarial_lot` | Dead rung 04 — runoff tie, nobody scored a 5, lot de | 1 | single-race | 2 | STAR | LH-only |
| `tie_break_09_five_star_tied_nonzero` | Dead rung 05 — five-star rung alive but non-separati | 1 | single-race | 2 | STAR | LH-only |
| `tilted_cycle_c3_b5_irv` | Minimal tilted cycle — 5 voters, margins 3–1–1 (RCV- | 1 | single-race | 5 | IRV | LH-only |
| `tilted_cycle_c3_b5_rr` | Minimal tilted cycle — 5 voters, margins 3–1–1 (Rank | 1 | single-race | 5 | RankedRobin | LH-only |
| `two_bullet_voters_sss` | Two bullet voters, two seats — Sequentially Spent Sc | 1 | single-race | 7 | STAR_PR | LH-only |
| `two_officers_allocated` | Two officers, three candidates — Allocated Score | 1 | single-race | 3 | STAR_PR | LH-only |
| `two_officers_rrv` | Two officers, three candidates — Reweighted Range Vo | 1 | single-race | 3 | STAR_PR | LH-only |
| `two_officers_sss` | Two officers, three candidates — Sequentially Spent  | 1 | single-race | 3 | STAR_PR | LH-only |
| `vcl_c4_b9_score_vs_runoff` | The valuable Condorcet loser — Score elects her, the | 1 | single-race | 9 | STAR | LH-only |
| `vote_splitting` | Vote splitting — two chocolates split the majority | 1 | single-race | 36 | STAR | LH-only |
| `vote_splitting2` | Vote splitting — two chocolates split the majority | 1 | single-race | 360 | STAR | LH-only |
| `vote_splitting3` | Vote splitting — two chocolates split the majority | 1 | single-race | 21 | STAR | LH-only |
| `vote_splitting_scenario1_spoiler` | Vote splitting — scenario 1 of 3 — the spoiler strik | 1 | single-race | 90 | STAR | LH-only |
| `vote_splitting_scenario2_bloc_leads` | Vote splitting — scenario 2 of 3 — no spoiler (bloc  | 1 | single-race | 36 | STAR | LH-only |
| `vote_splitting_scenario3_outsider_wins` | Vote splitting — scenario 3 of 3 — no spoiler (the o | 1 | single-race | 62 | STAR | LH-only |
| [`b4yr3v`](https://bettervoting.com/b4yr3v/results) | BV2231 — FairVote-vs-STAR check: Washington 2010 hon | 1 | single-race | 100 | STAR | BV |
| [`b6xrdr`](https://bettervoting.com/b6xrdr/results) | BV2207 — Favorite betrayal in STAR, 2 of 2 — nine vo | 1 | single-race | 57 | STAR | BV |
| [`bfjqmg`](https://bettervoting.com/bfjqmg/results) | Runoff_04 — the reversal holds at scale (67/33) | 1 | single-race | 9 | STAR | BV |
| [`bgcmxx`](https://bettervoting.com/bgcmxx/results) | BV2228 — Favorite Betrayal — the RCV-IRV betrayal (2 | 1 | single-race | 34 | IRV | BV |
| [`bj8dfc`](https://bettervoting.com/bj8dfc/results) | BV2202 — The Transfer Machine, fully ranked — a book | 1 | single-race | 9 | STV | BV |
| [`btmydt`](https://bettervoting.com/btmydt/results) | BV129 - 3 cand - 2 winners (Bloc STAR) | 1 | single-race | 5 | STAR | BV |
| [`c8h3tb`](https://bettervoting.com/c8h3tb/results) | BV2256 — Traditional voting style: one mark each | 1 | single-race | 3 | STAR | BV |
| [`d664xw`](https://bettervoting.com/d664xw/results) | Runoff_06 - Runoff confirms the leader at scale (con | 1 | single-race | 5 | STAR | BV |
| [`dfw8rj`](https://bettervoting.com/dfw8rj/results) | BV2183 — Forced Ballot Exhaustion — a 2-rank cap dis | 1 | single-race | 50 | IRV | BV |
| [`dkj9dx`](https://bettervoting.com/dkj9dx/results) | BV1525 - Condorcet loser ties for seat 1 (Bloc STAR, | 1 | single-race | 16 | STAR | BV |
| [`dq2dmm`](https://bettervoting.com/dq2dmm/results) | BV Abstentions and flat scores | 1 | single-race | 8 | STAR | BV |
| [`ff6mk3`](https://bettervoting.com/ff6mk3/results) | BV135 - Approval 101 — most approvals wins | 1 | single-race | 5 | Approval | BV |
| [`fk38pk`](https://bettervoting.com/fk38pk/results) | BV1815 - STAR Bloc - 3 candidates - 2 seats (basic / | 1 | single-race | 3 | STAR | BV |
| [`fm8cbv`](https://bettervoting.com/fm8cbv/results) | BV2235 — Cliff City food trucks — everyone scores 0  | 1 | single-race | 40 | STAR | BV |
| [`fp62p2`](https://bettervoting.com/fp62p2/results) | BV2180 — Ice Cream, six flavors — a STAR tie in both | 1 | single-race | 2 | STAR | BV |
| [`fxhw6g`](https://bettervoting.com/fxhw6g/results) | BV2209 — Burial in Ranked Robin, 2 of 2 — fifteen vo | 1 | single-race | 42 | RankedRobin | BV |
| [`fyy886`](https://bettervoting.com/fyy886/results) | BV2184 — The Team Lunch Vote — a beginner's STAR exa | 1 | single-race | 5 | STAR | BV |
| [`g3f7r2`](https://bettervoting.com/g3f7r2/results) | BV2212 — STAR IIA under a Condorcet cycle — a losing | 1 | single-race | 23 | STAR | BV |
| [`gg9qh9`](https://bettervoting.com/gg9qh9/results) | BV2260 — Winning the most head-to-head matchups is n | 1 | single-race | 18 | RankedRobin | BV |
| [`gmfv4c`](https://bettervoting.com/gmfv4c/results) | Edelman's 'Myth of the Condorcet Winner' 81 voters — | 1 | single-race | 81 | STAR | BV |
| [`gvtg2h`](https://bettervoting.com/gvtg2h/results) | BV2203 — The Transfer Machine, flag probe — same STV | 1 | single-race | 9 | STV | BV |
| [`gyv2qt`](https://bettervoting.com/gyv2qt/results) | BV2239 — Narrow Bands — a paint-swatch election scor | 1 | single-race | 24 | STAR | BV |
| [`hb4qvv`](https://bettervoting.com/hb4qvv/results) | BV2283 — Score both candidates 5 (STAR, 2 candidates | 1 | single-race | 5 | STAR | BV |
| [`hckrf7`](https://bettervoting.com/hckrf7/results) | Copy of BV210 - View / report - Distribution of Equa | 1 | single-race | 3 | STAR | BV |
| [`hk27tk`](https://bettervoting.com/hk27tk/results) | BV_Library STAR_PR — fewer voters than seats | 1 | single-race | 2 | STAR_PR | BV |
| [`j3hqvb`](https://bettervoting.com/j3hqvb/results) | BV2264 — Two-seat board by Bloc STAR: the council si | 1 | single-race | 6 | STAR | BV |
| [`jfk7pd`](https://bettervoting.com/jfk7pd/results) | The BV recipe (the "crazy" scenario) | 1 | single-race | 2 | STAR | BV |
| [`jt6r76`](https://bettervoting.com/jt6r76/results) | BV27 - Lackner & Skowron steering committee (Approva | 1 | single-race | 12 | Approval | BV |
| [`k7pfqt`](https://bettervoting.com/k7pfqt/results) | BV2266 — Two-seat board by Bloc STAR: the candidate  | 1 | single-race | 7 | STAR | BV |
| [`kbh3d9`](https://bettervoting.com/kbh3d9/results) | Guido example - bloc STAR | 1 | single-race | 3 | STAR | BV |
| [`kk2gxj`](https://bettervoting.com/kk2gxj/results) | BV_Library STAR_PR — fractional surplus | 1 | single-race | 12 | STAR_PR | BV |
| [`my82v6`](https://bettervoting.com/my82v6/results) | 01a_c2_b2 — two candidates, two ballots (Chocolate/V | 1 | single-race | 2 | STAR | BV |
| [`my9jd9`](https://bettervoting.com/my9jd9/results) | BV2267 — Two-seat board by Bloc STAR: three candidat | 1 | single-race | 7 | STAR | BV |
| [`pet`](https://bettervoting.com/pet/results) | What Makes the Best Pet? | 1 | single-race | 461 | STAR | BV |
| [`pmrq4q`](https://bettervoting.com/pmrq4q/results) | BV2245 — The Herb Garden Council — Allocated Score / | 1 | single-race | 36 | STAR_PR | BV |
| [`q2rkfm`](https://bettervoting.com/q2rkfm/results) | BV2257 — Choose-One lunch vote: five coworkers, one  | 1 | single-race | 5 | Plurality | BV |
| [`q8q9m7`](https://bettervoting.com/q8q9m7/results) | BV2220 — Equally Weighted Vote — add two exact-oppos | 1 | single-race | 5 | STAR | BV |
| [`qdh9qp`](https://bettervoting.com/qdh9qp/results) | BV2246 — Quota Circus — STAR-PR with cliff, slate an | 1 | single-race | 29 | STAR_PR | BV |
| [`qhjyr2`](https://bettervoting.com/qhjyr2/results) | BV2276 — Tied for the second finalist — the runoff p | 1 | single-race | 5 | STAR | BV |
| [`qrw6wb`](https://bettervoting.com/qrw6wb/results) | Ann, Bob, Cal - the canonical leading example (singl | 1 | single-race | 3 | STAR | BV |
| [`r2pvc9`](https://bettervoting.com/r2pvc9/results) | Runoff confirms the leader (control)  | 1 | single-race | 3 | STAR | BV |
| [`r4dqvd`](https://bettervoting.com/r4dqvd/results) | BV2105 - Favorite ice cream (Bloc STAR) - without en | 1 | single-race | 4 | STAR | BV |
| [`rkgtpk`](https://bettervoting.com/rkgtpk/results) | Runoff_03 — the 201-level reversal in a bigger field | 1 | single-race | 5 | STAR | BV |
| [`t488h9`](https://bettervoting.com/t488h9/results) | BV2269 — Three candidates, three seats — a race nobo | 1 | single-race | 7 | STAR | BV |
| [`td7jfy`](https://bettervoting.com/td7jfy/results) | BV2238 — Does the squeeze survive noise? Two poles,  | 1 | single-race | 38 | STAR | BV |
| [`tf73v9`](https://bettervoting.com/tf73v9/results) | Runoff_07 (WIP) — flat ballot exposes the BV abstent | 1 | single-race | 4 | STAR | BV |
| [`tfm64p`](https://bettervoting.com/tfm64p/results) | BV2259 — Read the ballot, name the method: four vote | 1 | single-race | 4 | STAR | BV |
| [`tg4779`](https://bettervoting.com/tg4779/results) | BV2182 — Why STAR Has an Automatic Runoff — a Runoff | 1 | single-race | 10 | STAR | BV |
| [`th3pbp`](https://bettervoting.com/th3pbp/results) | BV2265 — Two-seat board by Bloc STAR: one more hones | 1 | single-race | 7 | STAR | BV |
| [`tk776t`](https://bettervoting.com/tk776t/results) | BV2201 — The Transfer Machine — a book club buys two | 1 | single-race | 9 | STV | BV |
| [`v9rhhr`](https://bettervoting.com/v9rhhr/results) | BV2247 — Replant the Park — Bloc STAR with 7 trees,  | 1 | single-race | 44 | STAR | BV |
| [`vb3xv2`](https://bettervoting.com/vb3xv2/results) | BV830 — No Condorcet winner (top-two tie) — STAR bre | 1 | single-race | 3 | STAR | BV |
| [`vqyqkr`](https://bettervoting.com/vqyqkr/results) | Tennessee capital — Ranked Robin (RR/Condorcet = Nas | 1 | single-race | 100 | RankedRobin | BV |
| [`w3vvff`](https://bettervoting.com/w3vvff/results) | BV2105-r2 — Favorite ice cream (Bloc STAR): the part | 1 | single-race | 4 | STAR | BV |
| [`w9f4vd`](https://bettervoting.com/w9f4vd/results) | BV2236 — Bullet Storm — a bullet-voting electorate a | 1 | single-race | 33 | STAR | BV |
| [`xgkw3w`](https://bettervoting.com/xgkw3w/results) | Runoff_05 - Reversal with Equal Support | 1 | single-race | 5 | STAR | BV |
| [`xw23m9`](https://bettervoting.com/xw23m9/results) | BV2263 — Over 50% — every point on every ballot | 1 | single-race | 3 | STAR | BV |
| [`y3tvxm`](https://bettervoting.com/y3tvxm/results) | BV2136 — Village Council by SNTV — a concentrated mi | 1 | single-race | 9 | Plurality | BV |
| [`yhxy7q`](https://bettervoting.com/yhxy7q/results) | BV130 - original steering committee (Bloc STAR, k=3; | 1 | single-race | 9 | STAR | BV |
| [`yx9447`](https://bettervoting.com/yx9447/results) | Runoff_02 The atom — smallest runoff reversal | 1 | single-race | 3 | STAR | BV |
| [`yyhr66`](https://bettervoting.com/yyhr66/results) | No-show paradox (1 of 2) — 8 April fans stay home; R | 1 | single-race | 54 | STAR | BV |

_A **BV** election id links straight to its live results page on BetterVoting — an independent tabulation of the same ballots. **LH-only** ids are repo-local case stems with no public election behind them._

## Cuts

Counts per facet with example elections; drill into [`races.csv`](races.csv) to filter/sort the full set (GitHub renders CSV with sortable, filterable columns — it's the closest thing to a database view).

### By single vs multi-race

Whether a race sits in a single-contest election or a **contested** (multi-race) one — same electorate, several races.

| single vs multi-race | # races | example elections |
|---|--:|---|
| single-race | 421 | [`24b623`](https://bettervoting.com/24b623/results), [`26khr3`](https://bettervoting.com/26khr3/results), [`2gvwr9`](https://bettervoting.com/2gvwr9/results), [`2hqmrd`](https://bettervoting.com/2hqmrd/results) |
| contested (multi-race) | 264 | [`2jrfpg`](https://bettervoting.com/2jrfpg/results), [`2p33qq`](https://bettervoting.com/2p33qq/results), [`37yf8x`](https://bettervoting.com/37yf8x/results), [`38b7fg`](https://bettervoting.com/38b7fg/results) |

### By seat class

**Single-winner** (num_winners = 1) vs **multi-winner** (a body of seats).

| seat class | # races | example elections |
|---|--:|---|
| single-winner | 581 | [`24b623`](https://bettervoting.com/24b623/results), [`26khr3`](https://bettervoting.com/26khr3/results), [`2gvwr9`](https://bettervoting.com/2gvwr9/results), [`2hqmrd`](https://bettervoting.com/2hqmrd/results) |
| multi-winner | 104 | [`3494cb`](https://bettervoting.com/3494cb/results), [`39py93`](https://bettervoting.com/39py93/results), [`3x4vrv`](https://bettervoting.com/3x4vrv/results), [`3yr2qd`](https://bettervoting.com/3yr2qd/results) |

### By ballot type

What the voter marks: **score** (0–5), **ranked** (A>B>C), **approval** (0/1), or **choose-one**.

| ballot type | # races | example elections |
|---|--:|---|
| score | 357 | [`24b623`](https://bettervoting.com/24b623/results), [`26khr3`](https://bettervoting.com/26khr3/results), [`2hqmrd`](https://bettervoting.com/2hqmrd/results), [`2jrfpg`](https://bettervoting.com/2jrfpg/results) |
| ranked | 236 | [`2gvwr9`](https://bettervoting.com/2gvwr9/results), [`2jrfpg`](https://bettervoting.com/2jrfpg/results), [`2p33qq`](https://bettervoting.com/2p33qq/results), [`37yf8x`](https://bettervoting.com/37yf8x/results) |
| choose-one | 48 | [`2p33qq`](https://bettervoting.com/2p33qq/results), [`3x4vrv`](https://bettervoting.com/3x4vrv/results), [`4h89vj`](https://bettervoting.com/4h89vj/results), [`4w96tr`](https://bettervoting.com/4w96tr/results) |
| approval | 40 | [`4hfwqd`](https://bettervoting.com/4hfwqd/results), [`6mcgkq`](https://bettervoting.com/6mcgkq/results), `BV_Library_approval_single_winner`, `Black_Curtain_01a_c3_b5_approval` |
| ? | 4 | `321_tennessee_blank_encoding_c4_b100`, `blocs_bloc_c9_b10`, `cav_library_board_c3_b12`, `min_bloc_c3_b2` |

### By character

A rough teaching cut: **majoritarian** (a majority can take every seat), **proportional** (seats track factions — STAR-PR, STV), or **Condorcet** (elects the pairwise winner — Ranked Robin).

| character | # races | example elections |
|---|--:|---|
| majoritarian | 498 | [`24b623`](https://bettervoting.com/24b623/results), [`26khr3`](https://bettervoting.com/26khr3/results), [`2hqmrd`](https://bettervoting.com/2hqmrd/results), [`2jrfpg`](https://bettervoting.com/2jrfpg/results) |
| Condorcet | 129 | [`2gvwr9`](https://bettervoting.com/2gvwr9/results), [`2p33qq`](https://bettervoting.com/2p33qq/results), [`37yf8x`](https://bettervoting.com/37yf8x/results), [`3grpbb`](https://bettervoting.com/3grpbb/results) |
| proportional | 58 | [`39py93`](https://bettervoting.com/39py93/results), [`89wwvr`](https://bettervoting.com/89wwvr/results), [`8xwx43`](https://bettervoting.com/8xwx43/results), `02a_c5_b63_proportional-allocated-score` |

### By multi-winner style

*Multi-winner races only.* The distinction that decides whether a minority gets represented: **bloc / at-large** (Bloc STAR, Bloc Approval, Bloc RR, SNTV — no reweighting, so a cohesive majority can sweep **every** seat) vs **proportional** (STAR-PR, STV — seats track factions). This is the one cut the method-family view below hides, since Bloc STAR normalizes to STAR. Note multi-winner Ranked Robin is **Bloc RR** and lands here as bloc, not Condorcet. → [bloc vs proportional, worked](../../01_STAR/05_Practice/ex12_bloc_vs_proportional.md)

| multi-winner style | # races | example elections |
|---|--:|---|
| bloc / at-large | 55 | [`3494cb`](https://bettervoting.com/3494cb/results), [`3x4vrv`](https://bettervoting.com/3x4vrv/results), [`3yr2qd`](https://bettervoting.com/3yr2qd/results), [`484mbm`](https://bettervoting.com/484mbm/results) |
| proportional | 49 | [`39py93`](https://bettervoting.com/39py93/results), [`89wwvr`](https://bettervoting.com/89wwvr/results), `02a_c5_b63_proportional-allocated-score`, `02b_c5_b63_proportional-sss` |

### By method (family)

Canonical method family — e.g. Bloc STAR and STAR both normalize to STAR; allocated/sss/rrv to STAR_PR.

| method (family) | # races | example elections |
|---|--:|---|
| STAR | 309 | [`24b623`](https://bettervoting.com/24b623/results), [`26khr3`](https://bettervoting.com/26khr3/results), [`2hqmrd`](https://bettervoting.com/2hqmrd/results), [`2jrfpg`](https://bettervoting.com/2jrfpg/results) |
| RankedRobin | 129 | [`2gvwr9`](https://bettervoting.com/2gvwr9/results), [`2p33qq`](https://bettervoting.com/2p33qq/results), [`37yf8x`](https://bettervoting.com/37yf8x/results), [`3grpbb`](https://bettervoting.com/3grpbb/results) |
| IRV | 93 | [`2jrfpg`](https://bettervoting.com/2jrfpg/results), [`37yf8x`](https://bettervoting.com/37yf8x/results), [`3xgkck`](https://bettervoting.com/3xgkck/results), [`4htk44`](https://bettervoting.com/4htk44/results) |
| Plurality | 48 | [`2p33qq`](https://bettervoting.com/2p33qq/results), [`3x4vrv`](https://bettervoting.com/3x4vrv/results), [`4h89vj`](https://bettervoting.com/4h89vj/results), [`4w96tr`](https://bettervoting.com/4w96tr/results) |
| STAR_PR | 44 | [`89wwvr`](https://bettervoting.com/89wwvr/results), `02a_c5_b63_proportional-allocated-score`, `02b_c5_b63_proportional-sss`, `02c_c5_b63_proportional-rrv` |
| Approval | 40 | [`4hfwqd`](https://bettervoting.com/4hfwqd/results), [`6mcgkq`](https://bettervoting.com/6mcgkq/results), `BV_Library_approval_single_winner`, `Black_Curtain_01a_c3_b5_approval` |
| STV | 14 | [`39py93`](https://bettervoting.com/39py93/results), [`8xwx43`](https://bettervoting.com/8xwx43/results), `03a_stv_3seats`, `bpv_bakery_stv_c4_b12` |
| Range | 4 | `cav_library_board_blank_is_zero_c3_b12`, `range_101_0to9_c3_b5`, `range_101_c3_b5`, `range_sullivan_score_c4_b10` |
| bloc | 2 | `blocs_bloc_c9_b10`, `min_bloc_c3_b2` |
| CAV | 1 | `cav_library_board_c3_b12` |
| 3-2-1 | 1 | `321_tennessee_blank_encoding_c4_b100` |

### By backing (BV vs LH-only)

**BV** = reproduced on BetterVoting (has a frozen export). **LH-only** = tabulated only by our engine (a migration candidate). **LH-only (exception)** = genuinely can't go to BV (marked `lh_only_reason` in the yaml). Goal: keep plain LH-only near zero — reproduce on BV unless it's a marked exception.

| backing (BV vs LH-only) | # races | example elections |
|---|--:|---|
| LH-only | 326 | `00_c3_b3_bloc-baseline-2-seats`, `00_plurality_vs_majority`, `01_c4_b2_bloc-star-2-seats`, `01_condorcet_winner` |
| BV | 274 | [`24b623`](https://bettervoting.com/24b623/results), [`26khr3`](https://bettervoting.com/26khr3/results), [`2gvwr9`](https://bettervoting.com/2gvwr9/results), [`2hqmrd`](https://bettervoting.com/2hqmrd/results) |
| BV (no yaml) | 83 | [`2jrfpg`](https://bettervoting.com/2jrfpg/results), [`2p33qq`](https://bettervoting.com/2p33qq/results), [`3grpbb`](https://bettervoting.com/3grpbb/results), [`3xgkck`](https://bettervoting.com/3xgkck/results) |
| LH-only (exception) | 2 | `copeland_half_credit_decides`, `dead_heat_lot_tiebreak` |

### Genuine LH-only exceptions

Cases that **cannot** be reproduced on BetterVoting — a real reason (missing BV method / non-deterministic tie-break), not a coverage gap:

| Case | Method | Why it can't go to BV |
|---|---|---|
| Ranked Robin — a dead heat that runs the who | RankedRobin | BetterVoting breaks this exact tie at RANDOM (head-to-head is also tied), so its winner can't be frozen/reproduced. LH resolves it deterministically by margin then lot — the whole point of the case — so it is LH-only by design. |
| Ranked Robin — the half-point for a draw dec | RankedRobin | A pure engine-mechanics illustration of the Copeland half-credit; deterministic and reproducible, but with no BetterVoting election behind it. |

## How this is organized (for adding cases)

- **One yaml = one race.** A single-race election is one yaml; a **contested election is several yamls that share `bv_election_id`** (its bvid). The catalog groups them by that id.
- **Facets are DERIVED, not hand-tagged** — from `voting_method` (→ family + ballot type + character) and `num_winners` (→ seat class). So a case shows up in the right cuts automatically; just set those two fields correctly.
- **BV-only races** (a race that exists on BetterVoting but has no LH yaml, e.g. Bloc Plurality) are read from the frozen `*_bv_export.json` and appear tagged `BV (no yaml)`.
- **Naming:** BV-backed case files carry the bvid (`bv<testid>_<bvid>_<descriptor>`); LH-only files use a descriptive name. A contested election keeps its races in one folder with a lead `.md` and a `README.md`.
- **To add a case:** drop the yaml(s), run the engine (writes the `_tabulated` mirror), then regenerate the indexes (`build_yaml_pages`, `build_bv_registry`, `build_multirace_index`, `build_catalog`). The pre-commit hook refreshes the generated indexes automatically.

