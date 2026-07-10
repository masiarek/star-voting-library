# The Post-it election, seven ways — all four candidates win, depending on the method

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/v8r66y) · **[results ↗](https://bettervoting.com/v8r66y/results)** (election `v8r66y`, Test ID **BV2177**).

The same 20 voters as [the Post-it RCV example (BV2176)](bv2176_p8dp28_postit_rcv_example.md) — the electorate from Equal Vote's video ["Updated: How does RCV work? — With Post-its!"](https://youtu.be/Vte4nly_Neg) — run through **every voting method BetterVoting supports**, as seven single-winner races, leading with STAR. The headline: **all four candidates win, depending only on how the same preferences are counted.**

## One electorate, seven counts, four winners

| # | Race (BV) | Method | BV winner | How |
|--:|---|---|:--:|:--|
| 1 | STAR | STAR | **Blue** | scores 46/38/44/44; 44–44 second-finalist tie → head-to-head Blue 10–3 Pink; runoff **Blue 10–9 Purple** (a Runoff Reversal) |
| 2 | Ranked Robin | RankedRobin (Copeland) | **Green** | cycle; Green and Blue tie 2–1; BV's head-to-head rung → Green 7–4 (LH's margin rung says **Blue** — [the ladder divergence](../../00_start_here/RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md)) |
| 3 | Approval (approve = any support) | Approval | **Pink** | approvals 12/10/10/8 — the six Green fans' 3-for-their-last-choice carries Pink |
| 4 | RCV-IRV | IRV | **Purple** | the video's whiteboard count: 7/6/4/3 → 8/7/4 → 9–8, 3 exhausted |
| 5 | Choose-One | Plurality | **Purple** | 7 first choices (35%) |
| 6 | STV, 1 seat | STV | **Purple** | Droop quota ⌊20/2⌋+1 = 11 — identical rounds to IRV |
| 7 | STAR-PR, 1 seat | STAR_PR (Allocated Score) | **Purple** | the per-seat rule is **score-only** (no runoff) — the score leader (46) wins and the Runoff Reversal vanishes |

Blue wins the method that holds the head-to-head runoff; Green wins BetterVoting's Condorcet-family count; Pink wins when mild support counts the same as strong support; Purple wins every method that only reads first choices (and the score-only STAR-PR round). **The tabulation, not the ballot, decides.**

## Three conversions, three lessons

The seven races use three ballot forms derived from one set of preferences — and each derivation quietly makes a choice:

- **Ranks → the video's 0–5 scores** (races 1, 7): verified strictly order-consistent, ballot by ballot, with the video's rankings — but the *gap sizes* are editorial, and they matter. With the video's generous 5/4/3 down-ballot scores, Blue reaches the runoff and wins; re-score the same rankings stingily (5/2/1) and the scoring round is Purple 40, Green 34, Blue 32, Pink 26 — **STAR elects Purple**, agreeing with IRV. Preference *strength* is real information that ranks don't carry. Full analysis: [is the video fair and balanced?](postit_video_fair_and_balanced.md)
- **Scores → approvals** (race 3): the video's scores use only 0/3/4/5, so "approve = any support" is unambiguous up to threshold 3 — and elects **Pink** (12). But approve only 4s and 5s and **Blue** wins (10/9/8/5); only 5s and **Purple** wins (7/6/4/3). Three defensible thresholds, three winners: *the conversion is the election.*
- **Ranks as ranks** (races 2, 4, 6): even with no conversion at all, the ranked-ballot family splits — IRV/STV elect Purple, Ranked Robin elects Green (BV) or Blue (LH). "RCV" names the ballot; the tabulation still decides.

## STAR-PR at one seat is Score voting, not STAR

A subtle catch worth its own paragraph: **Allocated Score (STAR-PR) elects each seat by score alone** — the automatic-runoff step exists only in single-winner STAR. At 1 seat that means plain Score voting: Purple's 46 wins and Blue's 10–9 runoff majority never gets consulted; the Runoff Reversal that defines the STAR race simply vanishes. (The LH engine refuses `allocated` with `seats=1` outright and tells you to use STAR — so this leg is BV-only; the live result confirms Purple, score 46, no tie. BV labels the round's `tieBreakType` "random", but the one-candidate tie list in the raw result shows nothing was actually drawn — 46 is unique.)

## Files

| Race | YAML | `_tabulated` mirror |
|---|---|---|
| STAR / RCV-IRV / Ranked Robin / STV | identical ballots to BV2176 — [star](bv2176_p8dp28_star.yaml) · [irv](bv2176_p8dp28_irv.yaml) · [ranked_robin](bv2176_p8dp28_ranked_robin.yaml) | [see BV2176's mirrors](postit_rcv_example_tabulated/) |
| Approval | [bv2177_v8r66y_approval.yaml](bv2177_v8r66y_approval.yaml) | [txt](postit_rcv_example_tabulated/bv2177_v8r66y_approval_tabulated.txt) |
| Choose-One | [bv2177_v8r66y_plurality.yaml](bv2177_v8r66y_plurality.yaml) | [txt](postit_rcv_example_tabulated/bv2177_v8r66y_plurality_tabulated.txt) |
| STAR-PR (1 seat) | BV-only (LH's allocated requires ≥ 2 seats); scoring round = the STAR yaml's | — |

Frozen BetterVoting export (Election + Ballots + Results): `bv2177_v8r66y_bv_export.json` — *pending; export from the BV UI and drop it here.*

Related: [the BV2176 case page](bv2176_p8dp28_postit_rcv_example.md) · [the switch, made real (BV2178)](bv2178_8kg698_switch_made_real.md) · [is the video fair and balanced?](postit_video_fair_and_balanced.md) · up: [method_comparisons](../)

# file: bv2177_v8r66y_seven_methods.md
