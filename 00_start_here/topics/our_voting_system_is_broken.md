# Our Voting System Is Broken — The Problem with Plurality
### Voting 101 · foundational

The **diagnosis** — the "why fix anything at all?" that comes *before* the spoiler-effect mechanism and the STAR pitch. Four honest questions decide whether Choose-One Plurality is worth replacing: is it **prone to failure**, have the failures been **frequent**, were they **serious**, and are they getting **worse**? This page answers all four, then shows why STAR settles on a single ballot the one question Plurality can't.

*Prefer it spoken? The narrated pitch is [What's so good about STAR](../STAR_Voting/whats_so_good_about_STAR_Voting.md); the slide version is the [Why STAR Voting deck](Why_STAR_Voting.md).*

---

## Is the system actually broken?

The fundamental problem with Choose-One Plurality isn't really in dispute: the rules let a candidate who is the *least* preferred choice of a majority be declared the winner. A majority can be against you and you can still take office — just by leading a divided field. That plainly violates majority rule, and nobody seriously argues it's democratic. The only open question is whether it's worth doing something about — so take the honest version of the skeptic's four questions in turn.

## "But usually the front-runner really is the favorite, right?"

Usually — yes, and it's worth conceding plainly. When you have richer ballots to check against, the plurality front-runner *usually* turns out to be the broader choice too: in Australia's ranked elections the first-preference leader goes on to win about **90%** of the time. But flip that around — roughly **one race in ten** is decided differently once you look past first choices. And here's the catch: a Choose-One ballot gives you **no way to tell which kind of race you're in.** From the marks on the ballot you can't know whether your plurality winner is the majority's real choice or an accident of vote-splitting. The ballot itself hides the answer — and that hidden answer is exactly what STAR puts back on the table.

## How often, and how serious? — the two-party mask

If it's only one in ten, why has nobody noticed? Because for decades two dominant parties *masked* it. Squeeze almost every race into two big tents and you rarely see a third candidate split the vote — the flaw was real but invisible. That has been changing. The moment serious independents show up — Perot-style or otherwise — we snap right back to plurality winners instead of majority winners. In **1992**, with Perot in the race, Bill Clinton won an outright *majority* of the popular vote in exactly **one state — his home state of Arkansas** (plus the District of Columbia). Every other state was carried with a plurality, not a majority: a president elected while 49 states out of 50 never gave *any* candidate more than half their vote.

That's not a fluke of one strange year — it's structural. The instant voters have more than two real choices (which is exactly what most people *say* they want), Choose-One starts handing out minority winners and punishing the voters who dared back a third option. That's vote-splitting and the [spoiler effect](spoiler_effect.md), and as the two-party grip loosens it's getting *more* common, not less.

So: **prone to failure, yes; serious when it happens, yes; and trending worse.** Three yeses — which is why it's worth fixing.

**Worked demo.** [`01_political_left_split`](../../method_comparisons/split_voting/_main/_main_pages/01_political_left_split.md) ([`.yaml`](../../method_comparisons/split_voting/_main/01_political_left_split.yaml)) — a 60–66% coalition splits and Choose-One hands the seat to a candidate the majority ranked last; the engine's `[Vote-splitting check]` block says it in numbers.

## How STAR fixes it

STAR removes the two things that break Plurality. **First, you're never punished for honesty:** you score every candidate 0–5, so backing your favorite *and* a compromise can't split your own side. **Second — and this answers the skeptic's real question — STAR doesn't just *hope* the winner has majority support, it *checks*.** The automatic runoff is a head-to-head majority test between the top two, and the preference matrix shows exactly who beats whom. The very thing Choose-One hides — "is this winner actually the majority's choice?" — STAR prints right on the result, from one single ballot.

Under Choose-One you *can't know*. Under STAR you *read it off the result.* That's the whole difference between hoping for majority rule and measuring it.

**Worked demo.** [`04_star_wars_vote_split`](../../method_comparisons/split_voting/_main/_main_pages/04_star_wars_vote_split.md) ([`.yaml`](../../method_comparisons/split_voting/_main/04_star_wars_vote_split.yaml)) — Choose-One elects Vader (40%, the candidate 60% ranked last); STAR elects Leia, the majority's real choice, and the `[Divergence from STAR]` line shows **Choose-One (Plurality)** disagreeing with STAR while STAR matches the head-to-head ([Condorcet](condorcet/)) winner.

## The one-liner

> **"Choose-One can crown the candidate a majority likes *least*, and the ballot itself won't tell you when that's happened. STAR refuses to split your vote, then *proves* the winner has majority support — on one ballot, in plain sight."**

---

## Where this fits in the overall teaching

- **Level:** Voting 101 — **foundational**. This is the *diagnosis*; read it before the spoiler-effect mechanism and the STAR pitch.
- **Pairs with:** the [spoiler effect](spoiler_effect.md) and the [`split_voting/`](../../method_comparisons/split_voting/) demos — this page argues *that* the system is broken; those show *how*. Then [What's so good about STAR](../STAR_Voting/whats_so_good_about_STAR_Voting.md) delivers the fix.
- **Terminology:** keep it `Choose-One` / `Plurality` for a public audience; the point is method-accurate for Plurality specifically. (Reworked from a classic pro-reform passage that originally leaned on IRV; here the resolution is STAR's majority runoff + preference matrix, which answer "is the plurality winner the real winner?" directly, on one ballot.)

Cross-references:
- [GLOSSARY](../GLOSSARY.md) — "Choose-One / Plurality / First-Past-The-Post," "Plurality / minority winner," "Vote splitting," "Spoiler effect," "Majority finish."
- [Why STAR Voting](Why_STAR_Voting.md) — Part 1 problem bullets.
- [What's so good about STAR](../STAR_Voting/whats_so_good_about_STAR_Voting.md) — Segment 1 (the spoiler).
- [LINKS.md](../LINKS.md) → **Full Deck 2025** ("PROBLEM: VOTE-SPLITTING," "THE VOTING DILEMMA"), **Torrance LWV (Arend)** ("SPOILER EFFECT").

<!-- Sourced facts: Clinton 1992 won an absolute majority of the popular vote only
in Arkansas (53.2%) and DC (every other state a plurality). In Australian IRV
elections the first-preference leader wins ~90% of seats (≈1 in 10 differ from
first-past-the-post). -->
