# The Problem with Choose-One Plurality

*"Our voting system is broken" is a big claim, so this page tests it the way a fair skeptic would: is the problem real? Is it frequent? Is it serious when it happens? Is it getting worse? The answers are honest — including the concessions reform advocates should make — and they end at the part that actually stings: a Choose-One ballot cannot even tell you whether its winner was the majority's choice.*

→ Companions: [What is a voting method? (ballot + count)](voting_method_ballot_and_count.md) — the foundation this builds on · [the spoiler effect](spoiler_effect.md) and the [vote-splitting worked set](../method_comparisons/split_voting/README.md) — the mechanism in numbers · [What's so good about STAR Voting?](STAR_Voting/whats_so_good_about_STAR_Voting.md) — the fix · Glossary: [Choose-One / Plurality, minority winner, vote splitting, lesser-evil voting](GLOSSARY.md)

---

## Is the problem real? Yes — it's in the rules, not in anyone's opinion

The core defect of Choose-One Plurality is not in dispute: the rules allow a candidate who is the *least* preferred choice of a majority of voters to be declared the winner. A majority can be against you and you can still win — just by leading a divided field. Nobody seriously argues that outcome is democratic; it plainly violates majority rule. The genuinely open questions are the practical ones — how often it happens, how much it costs, and which way it's trending — and those deserve honest answers, not slogans.

## The honest concession: usually the front-runner really is the favorite

Most of the time, the candidate with the most votes really is the one most people wanted, and there is no point pretending otherwise. Where richer ballots exist to check against, the plurality front-runner usually turns out to be the broader choice too: in Australia's ranked elections, the first-preference leader goes on to win about **90%** of the time.

Flip that around, though, and the concession has teeth: roughly **one race in ten** is decided differently once you look past first choices. And here is the catch — a Choose-One ballot gives you **no way to tell which kind of race you're in.** One mark per voter is all the data that exists. You cannot know, from the marks on the ballot, whether your plurality winner is the majority's real choice or an accident of a divided field. The ballot itself hides the answer.

## What Choose-One cannot see

A Choose-One ballot records a single fact per voter — one name — and discards everything else the voter thinks. Two failure modes live in that blind spot:

- **Vote-splitting.** Similar candidates divide their shared supporters, and a candidate most voters oppose slips past the divided majority. The ballot never collected the information ("I'd take either of those two over *that* one") that would have exposed it. The mechanism, in runnable numbers: the [vote-splitting worked set](../method_comparisons/split_voting/README.md) and [the spoiler effect](spoiler_effect.md).
- **The lesser-evil incentive.** Voters can see the trap, so they defend themselves the only way one mark allows: abandon the favorite and back a tolerable front-runner instead. The system doesn't just miscount honest preferences — it teaches voters to stop expressing them. That's [lesser-evil voting](GLOSSARY.md), and it means even the marks Choose-One *does* collect are distorted by the method itself.

## Watch it happen: the team lunch

The smallest version of the trap is the canonical [team lunch vote](../01_STAR/_main/_main_pages/bv2184_fyy886_lunch_vote.md) ([live BetterVoting results ↗](https://bettervoting.com/fyy886/results)). Five coworkers pick lunch: two love Sushi, two love Tacos, and everyone is perfectly happy with Pizza. Under Choose-One each person names exactly one favorite, so the vote splits **Sushi 2, Tacos 2, Pizza 1** — and Pizza, the option nobody objected to, comes *last*. A coin flip hands lunch to Sushi or Tacos, and half the team is stuck with something they rated a 0.

Give the same five voters a ballot that can carry their full opinion — 0–5 scores — and the hidden information surfaces:

```text
--- STAR Voting Method (single winner) ---
 Tabulating 5 ballots.
Count × Sushi,Tacos,Pizza
    2 ×     5,    0,    3
    2 ×     0,    5,    3
    1 ×     3,    1,    5

Scoring Round
 The two highest-scoring candidates advance to the next round.
   Pizza         -- 17 -- First place
   Sushi         -- 13 -- Second place
   Tacos         -- 11
 Pizza and Sushi advance.

Automatic Runoff Round
 The candidate preferred in the most head-to-head matchups wins.
   Pizza         -- 3 -- First place
   Sushi         -- 2
   Equal Support -- 0
 Pizza wins.
   Voters with a preference: 5 of 5 (no Equal Support).
   Pizza 3 (60%) vs Sushi 2 (40%); majority = 3.
```

Same voters, same preferences — the only thing that changed is how much of each voter's opinion the ballot was allowed to carry. The engine's method comparison states the diagnosis directly:

```text
[Divergence from STAR]
  STAR                   = Pizza
  Choose-One (Plurality) = Sushi   (differs from STAR)
  RCV-IRV                = Sushi   (differs from STAR)
  Note: no ballots had tied scores, so RCV-IRV vs STAR here is a genuine
        method difference, not a tie-breaking artifact.
  Note: Ranked Robin (RCV-RR) agrees with STAR, so RCV-IRV is the lone
        outlier — the classic center-squeeze signature.
```

Choose-One elects Sushi, the choice a majority scored at 0. And note the RCV-IRV line: it elects Sushi here too — eliminating candidates by first-choice counts inherits a version of the same blindness ([center squeeze](topics/center_squeeze/README.md)). The full case page, with the preference matrix and every method's round-by-round report, is [the team lunch vote](../01_STAR/_main/_main_pages/bv2184_fyy886_lunch_vote.md) (source: [`bv2184_fyy886_lunch_vote.yaml`](../01_STAR/_main/bv2184_fyy886_lunch_vote.yaml)).

## How often, and how serious? The two-party mask

If one race in ten can come out wrong, why did nobody notice for so long? Because for decades two dominant parties *masked* it. Squeeze almost every race into two big tents and you rarely see a third candidate split the vote — the flaw was real but invisible. That's the second honest concession: in a strictly two-candidate world, Choose-One works fine, because with two candidates "most votes" and "majority" are the same thing.

The mask slips the moment serious independents show up. In 1992, with Ross Perot in the race, Bill Clinton won an outright *majority* of the popular vote in exactly **one state — his home state of Arkansas** (plus the District of Columbia). Every other state was carried with a plurality, not a majority: a president elected while 49 states out of 50 never gave *any* candidate more than half their vote. Not a fluke of one strange year — structural. The instant voters have more than two real choices, which is exactly what most people say they want, Choose-One starts producing minority winners and punishing the voters who dared back a third option.

**Is it getting worse?** Yes, by construction: the failure rate scales with the number of serious candidates, and the two-party grip that suppressed third candidacies is loosening. So the skeptic's scorecard reads: prone to failure — yes, by rule; serious when it happens — yes, it can seat the majority's least-preferred choice; trending worse — yes, as fields grow. Three yeses is why it's worth fixing.

## What a fix has to do — and how STAR does it

A real fix has to close both halves of the blind spot, not just exhort people to "vote smarter":

1. **Stop punishing honesty.** In [STAR Voting](STAR_Voting/STAR_start_here.md) you score every candidate 0–5, so supporting your favorite *and* a compromise can't split your own side. The lesser-evil dilemma isn't managed — it's removed, because one mark per voter was the thing creating it.
2. **Check majority support instead of hoping for it.** STAR's Automatic Runoff is a head-to-head majority test between the two strongest candidates, and the preference matrix shows exactly who beats whom ([Condorcet / head-to-head](topics/condorcet/README.md)). The very question Choose-One cannot answer — "is this winner actually the majority's choice?" — STAR prints right on the result, from one single ballot.

Under Choose-One, "is the plurality winner the real winner?" is unknowable from the ballots. Under STAR, you read it off the result. That's the whole difference between hoping for majority rule and measuring it. The full pitch is its own page: [What's so good about STAR Voting?](STAR_Voting/whats_so_good_about_STAR_Voting.md)

## The takeaway

Choose-One can crown the candidate a majority likes *least*, and the ballot itself won't tell you when that's happened. It usually gets the winner right — and gives you no way to know when it didn't. STAR refuses to split your vote, then *proves* the winner has majority support — on one ballot, in plain sight.

---

## Where this fits in the teaching

This is Voting 101, **foundational** — the *diagnosis* that comes before the mechanism and the fix. Reading order: [What is a voting method?](voting_method_ballot_and_count.md) (ballot vs count) → this page (why the Choose-One count fails) → [the spoiler effect](spoiler_effect.md) and the [vote-splitting demos](../method_comparisons/split_voting/README.md) (the mechanism, case by case) → [What's so good about STAR Voting?](STAR_Voting/whats_so_good_about_STAR_Voting.md) (the fix). Keep the words "Choose-One" / "Plurality" for a public audience; the argument here is method-accurate for Plurality specifically. (Reworked from a classic pro-reform passage that originally leaned on IRV; here the resolution is STAR's majority runoff + preference matrix, which answer "is the plurality winner the real winner?" directly, on one ballot.)

**Presenters:** the recorded-episode cues for this material — **[SLIDE]** Full Deck 2025: "PROBLEM: VOTE-SPLITTING," "THE VOTING DILEMMA"; Torrance LWV (Arend): "SPOILER EFFECT" · **[DEMO]** [the team lunch](../01_STAR/_main/_main_pages/bv2184_fyy886_lunch_vote.md), [01_political_left_split](../method_comparisons/split_voting/_main/_main_pages/01_political_left_split.md), [04_star_wars_vote_split](../method_comparisons/split_voting/_main/_main_pages/04_star_wars_vote_split.md). Slide short names resolve in [LINKS.md](LINKS.md); the episode roadmap (episode 1.5) lives in [conversation scripts](conversation_scripts.md).

<!-- Sourced facts: Clinton 1992 won an absolute majority of the popular vote only
in Arkansas (53.2%) and DC (every other state a plurality). In Australian IRV
elections the first-preference leader wins ~90% of seats (≈1 in 10 differ from
first-past-the-post). -->

# file: our_voting_system_is_broken.md
