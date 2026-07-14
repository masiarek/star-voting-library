# RCV or IRV — What's the Right Word?

*Your friends say "Ranked Choice." Advocates say RCV. Critics say IRV. This repo writes RCV-IRV. Which is right? They aren't synonyms — they name different things, and one distinction untangles all of it. This page teaches that one idea and the usage rule that follows from it. The full family tree, alias table, and house style live in the canonical references — deliberately not restated here.*

→ Canonical references: [Tips — Terminology: RCV vs IRV vs RCV-IRV](../TIPS_terminology.md) · [GLOSSARY.md](../GLOSSARY.md) · deeper history: [the naming problem](RCV-IRV-confusing-name.md) · foundation: [a ballot **and** a count](../voting_method_ballot_and_count.md)

---

## RCV names a ballot; IRV names one count of it

A voting method is [two parts](../voting_method_ballot_and_count.md): the **ballot** is what you mark; the **tabulation** is how it's counted. The two words live on opposite sides of that split.

**RCV — Ranked-Choice Voting — names the ballot.** It says the voter ranks the candidates: 1st, 2nd, 3rd. That's all it says. It does not tell you how the ranks get counted.

**IRV — Instant-Runoff Voting — names one tabulation** of that ballot: eliminate the last-place candidate, transfer their votes, repeat. It's the count almost everyone *means* when they say "RCV" — but it isn't the only one. The same ranked ballot can instead be counted by [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) (a Condorcet "consensus" count — most head-to-head wins) or by [STV](../proportional_representation/stv/proportional_stv_vs_star.md) (the proportional, multi-winner count). Same marks, different math — and sometimes a different winner.

So saying "RCV won't elect extremists" or "RCV has problems" is like saying "the paper ballot won": it names the ballot when the claim is really about a count. In the US the two got fused — FairVote branded IRV as "Ranked Choice Voting" and the label stuck (the full story is on [the naming problem](RCV-IRV-confusing-name.md) and [origins & spread](RCV_IRV_history.md)). The family tree and the what-you'll-hear alias table are canon in [TIPS_terminology.md](../TIPS_terminology.md).

## Why the precision isn't pedantry

Several of the sharpest criticisms in this whole debate — [center squeeze](RCV_IRV_center_squeeze.md), [exhausted ballots](RCV_IRV_exhausted_ballots.md), [non-monotonicity](RCV_IRV_non_monotonicity.md) — are failures of **IRV's elimination count**, not of ranked ballots in general. Ranked Robin reads the exact same ranked ballot and doesn't suffer center squeeze.

That asymmetry is a trap for the imprecise. Say *"RCV has center squeeze"* and a well-informed opponent can correctly answer *"Ranked Robin is RCV and it doesn't."* Say *"**IRV** has center squeeze"* and you are precisely, unarguably right. Precision is armor — which is why the [false-claims index](rcv_irv_false_claims.md) aims every rebuttal at IRV, not at ranked ballots.

The same discipline points back at STAR: "STAR" is one tabulation (Score Then Automatic Runoff) of a **score** ballot that could also be counted as Approval, pure Score, or Proportional STAR. Ballot, then tabulation — every time, for every method. (The mirror-image write-up is in [TIPS_terminology.md](../TIPS_terminology.md).)

## What to say, where

This repo's rule of thumb — the full when-to-use table is in [TIPS_terminology.md](../TIPS_terminology.md):

- **Technical, comparative, or critical writing → "RCV-IRV"** (or bare **"IRV"** once it's established you mean the elimination count). Unambiguous, and it keeps IRV-specific criticisms pinned to IRV.
- **Public-facing copy (slides, an intro talk) → plain "RCV" is fine** — it's the only word a general US audience knows, and "RCV-IRV" looks odd outside method-wonk circles. Just clarify once at first mention — *"RCV — ranked ballots counted by instant runoff (IRV)"* — then use the familiar word.
- **Bare "RCV" otherwise means the ranked-ballot family**, and say so when you use it that way.
- **Ranked Robin and STV get their own names, always** — never folded into "RCV" meaning IRV.

## Correct once, move on

When someone else says "RCV" loosely, don't derail the conversation to police it. Keep their word, add the clarification once — "right, and to be precise, that's IRV, one way of counting ranked ballots" — and get back to the substance. The precision matters most in *your own* claims, where a loose word hands your opponent a free rebuttal. Being the purist who fights every gust of wind costs more credibility than it buys.

## The takeaway

**RCV is a ballot; IRV is a count.** In the US they were mashed into one word, so this repo writes **RCV-IRV** when it means the method everyone calls RCV — and says **Ranked Robin** or **STV** when it means the other ways to count the very same ranked ballot.

---

## Where this fits in the teaching

This sits right after the [ballot-and-count foundation](../voting_method_ballot_and_count.md): every later comparison — spoiler, favorite betrayal, exhausted ballots — is cleaner once the audience won't conflate "RCV" with "IRV." Presenters: the matching slides are indexed by short name in [LINKS.md](../LINKS.md) (Full Deck 2025 — "About Ranked Choice"; the **Beyond RCV zine**), and the episode roadmap lives in [conversation scripts](../conversation_scripts.md).
