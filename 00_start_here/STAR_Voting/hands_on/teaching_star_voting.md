# Teaching STAR Voting — a guide for presenters, teachers & organizers

*Explaining STAR to a class, a club, a city council, or a skeptical uncle? This page collects what actually works — the order to teach it in, the terms to cover (and how to phrase them), which examples to reach for, the misconceptions to head off, and how to run a live demo. It's the presenter's companion to the learner-facing [STAR — start here](../STAR_start_here.md).*

**Level: reference (a teaching aid).**

## The one rule that matters most: problem before mechanics

The single biggest mistake is opening with the ballot ("so you score everyone 0 to 5…"). People don't care *how* until they feel *why*. **Lead with the failure of the way we vote now**, let them feel it, *then* introduce STAR as the fix. The proven arc (it's exactly how [STAR — start here](../STAR_start_here.md) is built — use it as your script):

1. **A problem they already know** — vote-splitting. The [team-lunch story](../STAR_start_here.md#first-a-problem-you-already-know-the-team-lunch): everyone's happy with Pizza, but "pick one" splits the vote and buries it. *Now* they want a fix.
2. **STAR in one breath** — score 0–5 (like Yelp), then the top two have an automatic runoff.
3. **Watch it fix the same problem** — re-run the lunch; the compromise wins.
4. **The ballot** — show a real one; "there's no wrong way to fill it out."
5. **Why two rounds** — the one idea worth pausing on (scores find the contenders; the runoff picks the winner).

Everything else (criteria, comparisons, theory) is optional depth for the audience that wants it.

## Terms to make sure you cover (and how to say them)

| Term | Say it like this |
|---|---|
| **Score 0–5** | "Rate each candidate like a Yelp review — 5 for a favorite, 0 for a hard no, anything in between." |
| **[Scoring Round](../the_count/STAR_Scoring_Round.md)** | "Add up everyone's stars. The two highest-scoring candidates become the **finalists**." |
| **[Finalists](../the_count/STAR_Scoring_Round.md)** | "The top two — the only ones left in the final step." |
| **[Automatic Runoff](../the_count/STAR_Automatic_Runoff.md)** | "A built-in final round — *no second trip to the polls*. Each ballot counts as one vote for whichever finalist it scored higher." |
| **[Equal Support](../reference/are_equal_score_votes_discounted.md)** | "If you rated the two finalists the same, you're saying 'either is fine' — your ballot still counted in the scoring round." |
| **Vote-splitting / [spoiler](../../topics/spoiler_effect.md)** | "The problem STAR solves — where similar candidates split support and the wrong one wins." |

*Reach for these only with an audience that wants depth:* [Condorcet winner](../../topics/condorcet/), [monotonicity](../properties_and_limits/STAR_monotonicity.md), [summability](../properties_and_limits/STAR_summability.md), the [honest limits](../properties_and_limits/STAR_honest_limits.md). **Skip them for a first-timer** — they're 201/301, not the on-ramp.

## Which example, and when

| Use… | For… |
|---|---|
| **[The team lunch](../../../01_STAR/_main/cases/cases_pages/bv2184_fyy886_lunch_vote.md)** | your go-to intro — 5 voters, politics-free, relatable, and the compromise wins. |
| **[Tennessee capital](../../../01_STAR/_main/cases/cases_pages/09_c4_b100_tennessee-capital.md)** | the classic textbook case — same shape as the lunch, at scale. |
| **[Runoff reversal](../../../01_STAR/runoff_overturns_leader/)** | the "aha" — the top scorer can *lose* the runoff. The most important single lesson; use it *after* the basics land. |
| **[Ways to vote](../STAR_ballot_voting_styles.md)** | reassuring voters there's no wrong ballot (bullet, equal scores, "anyone but…"). |
| **[Count by hand](count_star_by_hand.md)** | a hands-on demystifier — tally a tiny election live. |
| **[Center squeeze](../../RCV_IRV/RCV_IRV_center_squeeze.md)** | only when the room asks "why not RCV/IRV?" |

## Tips & tricks

- **Keep examples tiny.** 3–5 voters. A big electorate hides the point; a 5-voter example you can hold in your head wins.
- **Use ONE running cast the whole talk.** Don't switch from Sushi/Tacos/Pizza to Alice/Bob/Carol mid-session — it forces the audience to re-load. (New scenario? New memorable cast; *within* a scenario, keep it.)
- **Stay politics-free for mixed rooms.** Lunch, ice cream, movies. The moment you use real parties, half the room stops listening and starts defending. Make the *method* the hero, not a candidate.
- **Do a live count.** Either hand-tally a 3-voter election on the board, or run a real poll of the room on [bettervoting.com](https://bettervoting.com) and reveal the result. Participation beats slides.
- **Preempt the five misconceptions** *before* they derail you:
  - *"Isn't it just averaging?"* — No; the **runoff** is what makes it a majority method, not a mean.
  - *"Do I have to rate everyone?"* — No; blanks count as 0, bullet-voting is fine.
  - *"Isn't giving a 0 wasting my vote?"* — No; a 0 is a real score, and you never [split your own vote](../../topics/wasted_votes.md).
  - *"Is the runoff a second election?"* — No; it's **automatic**, computed from the same ballots.
  - *"Won't everyone just give all 5s and 0s?"* — The runoff removes the payoff for that, so honest scoring is also the smart move.

  (Hand your audience the full set: [Common misunderstandings about STAR](../getting_started/common_misunderstandings.md).)
- **Concede a limit — on purpose.** "No method is perfect ([that's a theorem](../../topics/gibbard_satterthwaite_theorem.md))" and naming one honest [limit](../properties_and_limits/STAR_honest_limits.md) *builds* trust; overselling loses the skeptics.
- **Match depth to the audience** (see [curriculum pacing](../../CURRICULUM.md#suggested-pacing-by-audience)): a 15-min public talk = the arc above and stop; officials = add [summability & audits](../properties_and_limits/STAR_summability.md); skeptics/debaters = [honest limits](../properties_and_limits/STAR_honest_limits.md) + [the criteria](../../topics/criteria_at_a_glance.md).
- **End with a call to action** — have them cast a real STAR ballot or run their own poll before they leave.

## Print your own paper ballots (the hands-on loop)

The repo has a tool that **turns a BetterVoting election into print-ready paper ballots** — [`bv_ballot_sheet.py`](../../../STARVote_LH_tabulation_engine/tools_adam/bv_ballot_sheet.py). **One route:** create the election on BetterVoting, export its JSON, and print from that export — so the ballot's QR and results link are always real:

```bash
python3 STARVote_LH_tabulation_engine/tools_adam/bv_ballot_sheet.py \
    --bv-export "06_Other/_demo_dropbox/<election>-<id>.json" \
    --serials --write-ins 1 --copies 25 --verify-bv --out pets.pdf
```

The ballot is styled after the **official Equal Vote STAR ballot** (STAR VOTING header, bulleted instructions, Worst/Best labels, star column headers, zebra stripes, finalist footer), so it's instantly familiar. The output is a **print-ready PDF** (`--out ballots.pdf`), one ballot per page. The fun parts:

- **two QR codes** → *scan to vote* and *scan for results*, so a class can vote **on paper *and* online** and compare;
- optional **serial "receipts"** (`--serials`) — a lovely way to teach *verifiability* and the secret-ballot tension (publish the counted serials; discuss why a name→number list would be bad);
- optional **write-in rows** (`--write-ins N`), a **`--logo`** for the real STAR / chapter logo, and `--promo` / `--chapter` for a footer, and **`--verify-bv`** so no one scans a dead link.

The full walkthrough — the create → export → print → vote → count loop, the print checklist, the three ways to count the result, and the ready-made [pet](https://bettervoting.com/pet) / [meta_pets](https://bettervoting.com/meta_pets) / [beer](https://bettervoting.com/yt3232) / [ice cream](https://bettervoting.com/2wfth7) elections — is [**Run a paper-ballot STAR demo**](running_a_paper_ballot_demo.md).

## Running a real hand-count (for organizers)

For an actual election, STAR is genuinely hand-countable. The Equal Vote Coalition's official procedure is worth following: [**BetterVoting — Hand Counting STAR**](https://docs.bettervoting.com/help/hand_count.html). The gist:

- **Scoring round:** a *caller* reads each ballot aloud, a *verifier* confirms, and **one tallier per star-level** (five talliers) marks tally sheets; multiply each tally by its star value and sum. An *observer* watches for errors.
- **Runoff:** sort every ballot into **three piles** — *prefers finalist A*, *prefers finalist B*, or *no preference (Equal Support)* — and count the piles. (This pile-sort is also the fastest way to demo the runoff live.)
- **Practical tips from the guide:** train on test ballots (fake names / colored paper) first; record the total ballot count before you start; use a big-display calculator; a straight-edge keeps tally rows aligned; a stencil covering the non-finalists speeds the runoff sort.

The conceptual walkthrough is [Count a STAR election by hand](count_star_by_hand.md); why it scales (precinct-summable, unlike IRV) is [summability](../properties_and_limits/STAR_summability.md).

## Ready-made materials

- **Scripts:** [What's so good about STAR](../reference/whats_so_good_about_STAR_Voting.md) · [Why do you love STAR](../reference/why_do_you_love_STAR_Voting.md) (conversation-style walkthroughs) · [the Automatic Runoff, as slides](../the_count/STAR_Automatic_Runoff_slides.md)
- **The ballot image, the lunch diagram, and worked pages** in [STAR — start here](../STAR_start_here.md); the [FAQ](../getting_started/STAR_FAQ.md) and [second-round FAQ](../the_count/STAR_second_round_FAQ.md) for the questions that come up
- **Videos & official guides:** [STAR resources](../reference/STAR_resources.md)
- **Print paper ballots & run a hands-on demo:** [Run a paper-ballot STAR demo](running_a_paper_ballot_demo.md) (QR, serial receipts, write-ins) + [Count a STAR election by hand](count_star_by_hand.md)
- **Teaching runoff reversal specifically:** [the step-by-step guide](../../../01_STAR/runoff_overturns_leader/) with a devil's-advocate Q&A

## Audience quick-adaptations

- **Classroom / kids** → the lunch, a live hand-count, colored-paper "candidates." Pure mechanics, no theory.
- **Voters / general public** → the arc + [ways to vote](../STAR_ballot_voting_styles.md) ("no wrong ballot") + a live poll.
- **Officials / administrators** → [summability](../properties_and_limits/STAR_summability.md), [hand-count](count_star_by_hand.md), audits; skip the criteria theory.
- **Skeptics / debaters / RCV advocates** → [honest limits](../properties_and_limits/STAR_honest_limits.md), [criteria at a glance](../../topics/criteria_at_a_glance.md), [STAR vs RCV-IRV](../../topics/rcv_irv_vs_star.md). Concede limits first — it's disarming.
