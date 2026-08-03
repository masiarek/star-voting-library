# "Traditional" — the choose-one habit, transplanted

*One 5 for your favorite, every other row left blank. The familiar single-choice vote, written on a 5-star ballot.*

← One of thirteen [voting styles](../STAR_ballot_voting_styles.md). Every style is legal and counted; this page is what this one means, when it fits, and what it trades away.

<img src="img/style_traditional.png" width="420" alt="A STAR ballot marked traditional-style: Carmen scored 5; Andre, Blake, David, and Ella left blank, which counts as 0 for each.">

## What this ballot says

**"Carmen. Period."** Carmen gets the full 5; every other row is blank, and a blank simply counts as 0. To the count, this voter loves Carmen and rates everyone else at the very bottom — even candidates they may never have thought about.

## When it fits

- You genuinely support one candidate and genuinely rate everyone else at zero — then this ballot is *exactly* honest, not a shortcut.
- You're new to scored ballots and reach for the familiar one-mark habit. It works: your vote is legal, full-weight, and can't be spoiled.

## The trade-off, honestly

The blanks are real information — *"everyone else: 0"* — whether or not you meant them that deeply. If Carmen makes the [runoff](../the_count/STAR_Automatic_Runoff.md), your full vote backs her there. But if she doesn't, your ballot scores both finalists 0 — [Equal Support](../../../07_Concepts/GLOSSARY.md), no preference — and you sit out the final head-to-head by your own choice. A single mark spends one point of voice out of the twenty-five the ballot offers. Nothing about that is penalized; it's just under-used.

## This exact style in a real election

In the runnable [style-gallery election](../../02_Examples/cases/cases_pages/03c_c6_b8_style-gallery.md) (different names, same eight styles — one ballot per style), the traditional row is `0,5,0,0,0,0`: a lone 5 for Bianca. Bianca reached the runoff, so this ballot's full vote counted for her there — and she won. The happy path. The dedicated two-line demo of the *unhappy* path — your lone pick missing the final — is the bullet-vote case: [reader page](../../02_Examples/cases/cases_pages/03a_c3_b3_style-bullet-vote.md) · [`03a_c3_b3_style-bullet-vote.yaml`](../../02_Examples/cases/03a_c3_b3_style-bullet-vote.yaml).

## What if *everyone* voted this way?

Then the 5-star ballot has nothing left to work with. Here is that election, live on BetterVoting — three voters, the same five candidates, every voter marking exactly one:

**▶ Live on BetterVoting:** [vote](https://bettervoting.com/c8h3tb) · **[results ↗](https://bettervoting.com/c8h3tb/results)** (election `c8h3tb`, Test ID BV2256).

| Voter | Andre | Blake | Carmen | David | Ella |
|---|:--:|:--:|:--:|:--:|:--:|
| 1 — *"Carmen. Period."* | – | – | **5** | – | – |
| 2 — *"Ella. Period."* | – | – | – | – | **5** |
| 3 — *"Ella. Period."* | – | – | – | – | **5** |

```
Scoring Round
   Ella          -- 10 -- First place
   Carmen        --  5 -- Second place
   Andre         --  0
   Blake         --  0
   David         --  0
 Ella and Carmen advance.

Automatic Runoff Round
   Ella          -- 2 -- First place
   Carmen        -- 1
   Equal Support -- 0
 Ella wins.
   Voters with a preference: 3 of 3 (no Equal Support).
   Ella 2 (67%) vs Carmen 1 (33%); majority = 2.
```

The scoring round has become nothing but a first-choice tally, and the runoff has nothing left to add — the two finalists were already the only candidates anyone said anything about. Andre, Blake and David finish on zero having had *nothing* said about them: not "we considered them and rated them last," simply nothing. A ballot carrying one bit per voter gives the method one bit to read, so this count could not have done better than the choose-one ballot it is imitating.

**Said plainly: as an approach and as a strategy, this is a poor use of a STAR ballot** — *unless* one candidate really is your only acceptable choice, period, in which case it is exactly honest and you should vote it. Everything on this page still holds: nothing is penalized, nothing can be spoiled, and a backup score can never hurt your favorite. You are simply choosing not to use the ballot. (Full count: [`bv2256_c8h3tb_traditional_style.md`](../../02_Examples/cases/cases_pages/bv2256_c8h3tb_traditional_style.md).)

## Related

- [Decent Backup](decent_backup.md) — the one-change upgrade: keep your 5, add a 4
- [The Equally Weighted Vote](../properties_and_limits/equally_weighted_vote.md) — why no style, this one included, carries secret extra weight
