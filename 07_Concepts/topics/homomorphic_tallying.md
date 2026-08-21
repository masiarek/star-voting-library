---
tags:
  - criteria
---

# Counting under encryption — can a STAR election be tallied without opening the ballots?

*Yes — and the reason is worth understanding, because it is a genuine structural advantage of score methods over elimination methods. But STAR has one wrinkle that nobody mentions: **the scoring round is the easy case; the automatic runoff is not.** This page explains why, and the two routes that resolve it.*

**Level: 301 → 401 · deep dive** Companion: [summability](summability/README.md) (the property this rests on) · [voter verifiability and receipt-freeness](../GLOSSARY.md) · [STAR's honest limits](../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md).

---

## The idea in one picture

**Additively homomorphic encryption** lets you *add encrypted numbers without decrypting them*. Encrypt every ballot, multiply the ciphertexts together, and you hold an encrypted **total** — which you decrypt *once*, at the end. No individual ballot is ever opened, yet:

- each voter can confirm **their** ballot is among those counted, and
- **anyone** can verify the published total really is the sum of the published encrypted ballots.

That is [end-to-end verifiability](https://en.wikipedia.org/wiki/End-to-end_auditable_voting_systems), and it works for one reason: **a tally is addition.** [Microsoft's ElectionGuard](https://github.com/Election-Tech-Initiative/electionguard) (open source, homomorphic ElGamal, designed by Josh Benaloh) is the reference implementation for 0/1 ballots.

Note the scope: you need only **partial** homomorphic encryption — addition, not multiplication. That's decades-old, well-understood mathematics. **Fully homomorphic encryption (FHE) is not required** and would be the wrong tool: orders of magnitude slower, solving a problem elections don't have.

## The easy case — STAR's Scoring Round

STAR's first round is a **sum of scores per candidate**. That is exactly ElectionGuard's construction with a wider range: scores 0–5 instead of 0/1. Two standard pieces are needed:

- **A range (validity) proof** — proof that each encrypted score really is a value in {0,…,5}, without revealing which. Otherwise a malicious client encrypts "1000" for its favourite. This is a **disjunctive zero-knowledge proof** (prove the ciphertext is one of six values); ElectionGuard already does it for {0,1}, and widening it to six is routine engineering, not research.
- **Threshold decryption** — the decryption key is split across several trustees, so no single party can open anything; *k* of *n* must cooperate to decrypt the final totals.

So the **entire Scoring Round is verifiable with partial homomorphic encryption**, using components that already exist.

## The hard case — the Automatic Runoff

Here is the part that gets glossed over. The runoff asks, of each ballot: **"did you score A above B?"** That breaks the model twice:

1. **It's a comparison, not a sum.** Additive encryption adds. It cannot compare two encrypted numbers.
2. **The pair isn't known in advance.** The two finalists only emerge *after* the scoring round is decrypted — so the voter's device, which is long gone by then, cannot have precomputed the answer for the right pair.

Naively, you'd have to decrypt the individual ballots to run the runoff — which throws away the property the whole exercise was protecting.

## The fix — carry the pairwise matrix

Have each ballot carry, **in addition** to its encrypted scores, an encrypted **1/0 indicator for every ordered pair** of candidates: *"I scored i above j."*

Now the runoff for **any** pair is a **sum** of those indicators again. Decrypt two totals, done — in one shot, with no second round of decryption, and no ballot ever opened.

| Candidates | Extra encrypted values per ballot — n(n−1) |
|---|--:|
| 3 | 6 |
| 5 | 20 |
| 10 | 90 |

Trivial sizes for an organizational election.

**The real work** is proving the matrix is **consistent with the scores** — otherwise a malicious client submits scores saying one thing and comparisons saying another. That's another disjunctive proof, over the possible score pairs. This is the genuine engineering task, and it is tractable.

**The bonus:** those indicators *are* the full [pairwise preference matrix](pairwise_counting.md). So a verifiable STAR election gets the **Condorcet check** — and [Ranked Robin](../../05_Ranked_Robin/01_Learn/README.md) itself — for free, on the same encrypted data.

## The other route — hide the tally instead of decrypting it

The construction above has a cost this page owed you earlier: **it decrypts more than the winner.** Score totals *and* the whole pairwise matrix become public. For a public election that is not a leak at all — voters expect the numbers, and the matrix is the Condorcet check people keep asking for. For a seven-person board or a jury, it is a great deal of information about a very small number of people.

There is a published line of work that attacks the comparison problem head-on rather than routing around it: **tally-hiding** e-voting, where the count runs under [secure multi-party computation](https://en.wikipedia.org/wiki/Secure_multi-party_computation) and only the *result* is ever revealed.

- **[Ordinos](https://eprint.iacr.org/2020/405)** (Küsters, Liedtke, Müller, Rausch, Vogt — IEEE EuroS&P 2020) publishes only the winner or the ranking, never the per-candidate counts, using *an MPC protocol for greater-than tests*. That is exactly the operation additive encryption cannot perform, and exactly the operation STAR's runoff needs.
- **[A toolbox for verifiable tally-hiding e-voting systems](https://eprint.iacr.org/2021/491)** (Cortier, Gaudry, Yang — ESORICS 2022) builds MPC-plus-verifiable-mixnet schemes for D'Hondt, Condorcet, STV and Majority Judgment. The Condorcet instantiation is the nearest published relative of what a STAR runoff needs.
- **[Kryvos](https://eprint.iacr.org/2022/1132)** (Huber, Küsters, Krips, Liedtke, Müller, Rausch, Reisert, Vogt — ACM CCS 2022) is the efficiency-minded relaxation, and the distinction is worth keeping straight: *publicly* tally-hiding means the authorities **do** learn the full tally internally and publish only the result. A weaker guarantee than Ordinos's, and cheaper to run.

The two routes trade off like this:

| | Carry the pairwise matrix | Tally-hiding MPC |
|---|---|---|
| **The runoff comparison costs** | **nothing** — the voter's own device does it in plaintext | an MPC greater-than test, under encryption |
| **What gets published** | score totals **and** the whole pairwise matrix | the winner (or the ranking), and nothing else |
| **Crypto needed** | partial HE + zero-knowledge proofs | MPC, sometimes mixnets as well |
| **Built for STAR?** | no — the sketch above | no — but the machinery is published and instantiated for other methods |
| **Suits** | public elections, where the totals are wanted anyway | small high-privacy electorates — boards, juries, committees |

Neither route has been worked out for STAR. The point of naming them together is that **"the runoff is a comparison" is a known problem with known answers** — not an exotic obstacle peculiar to this method.

## Careful — "STAR-Vote" is a different thing entirely

[STAR-Vote](https://arxiv.org/abs/1211.1904) (Benaloh, Byrne, Kortum, McBurnett, Pereira, Stark, Wallach, 2012) stands for **Secure, Transparent, Auditable, and Reliable**. It is a *polling-place architecture* — a DRE-style interface, a paper trail, end-to-end verifiability, ballot-level risk-limiting audits — and it has nothing whatever to do with Score Then Automatic Runoff. It does use homomorphic tallying, which makes the collision maximally confusing.

Two practical consequences. A literature search for "homomorphic STAR voting" fills up with STAR-Vote hits, so **the apparent absence of prior work on the method is partly an artefact of the name** — search *score voting*, *range voting* and *tally-hiding* instead before concluding anything about a gap. And when writing to cryptographers, spell out **Score Then Automatic Runoff** on first mention rather than trusting the acronym to land.

## Why this is an argument for STAR

The asymmetry with elimination methods is structural, and it is the [summability](summability/README.md) property showing up again in cryptography:

| | What the tally needs | Crypto required |
|---|---|---|
| **STAR / Score / Approval** | a **fixed set of sums**, all decidable at once | **partial** HE — add, prove range, decrypt totals |
| **RCV-IRV / STV** | **sequential, adaptive** rounds — round 3 depends on decrypting rounds 1–2 | **mixnets** — shuffle and decrypt *individual ballots*, with proofs the shuffle was honest |

STAR stays inside partial homomorphic encryption **end to end**. IRV cannot, because there is no fixed sum to compute — which is why verifiable IRV implementations open individual ballots. Same structural property as the [central tabulation](central_tabulation.md) cost, in a different domain.

## The honest bounds

Read these before repeating any of the above as a selling point:

- **This protects the *count*, not the *client*.** Malware on the voting device sees your choices **before** encryption. Homomorphic tallying does nothing about that, and it is the hardest unsolved problem in remote voting.
- **It is not an argument for internet voting.** Both the [US Vote Foundation's E2E-V study](https://www.usvotefoundation.org/E2E-VIV) (2015) and the National Academies' *Securing the Vote* (2018) concluded internet voting is not ready for public elections **even with** end-to-end verifiability. The technology suits in-person paper systems and lower-stakes organizational elections.
- **Trustees are a trust assumption**, not its absence: *k* of *n* colluding can decrypt.
- **Verifiability fights receipt-freeness.** A voter must be able to check their ballot counted *without* being able to **prove to anyone else** what it said — or you have rebuilt the vote-buying market the [secret ballot](../GLOSSARY.md) abolished. Systems square this by proving *inclusion* without revealing *content*.
- **Nobody has built this for STAR.** ElectionGuard, [Helios](https://vote.heliosvoting.org) and [Belenios](https://www.belenios.org) all handle additive tallies; **none handles a STAR runoff.** The pairwise-matrix construction above is a **design direction**, not a deployed system, a published protocol, or a peer-reviewed result. Treat it as a sketch for cryptographers to review and pull apart — the underlying pieces (disjunctive range proofs, threshold ElGamal, homomorphic counting) are all standard, but "assembled from standard parts" is not the same as "proven correct." Note carefully what the tally-hiding route above does *not* change: the machinery for counting a comparison under encryption is peer-reviewed and instantiated — just never for this method. **The gap is STAR-shaped, not machinery-shaped.**

## Related

- [Summability](summability/README.md) — the property this whole page rests on
- [Pairwise counting & the preference matrix](pairwise_counting.md) — what the indicator matrix *is*
- [STAR's honest limits](../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) — ballot verifiability, and the cast-or-challenge mitigation
- [What makes a voting method good?](what_makes_a_voting_method_good.md) — where auditability sits among the criteria
