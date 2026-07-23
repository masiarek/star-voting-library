# Counting under encryption — can a STAR election be tallied without opening the ballots?

*Yes — and the reason is worth understanding, because it is a genuine structural advantage of score methods over elimination methods. But STAR has one wrinkle that nobody mentions: **the scoring round is the easy case; the automatic runoff is not.** This page explains why, and how the wrinkle is resolved.*

**Level: 301 → 401.** Companion: [summability](summability/) (the property this rests on) · [voter verifiability and receipt-freeness](../GLOSSARY.md) · [STAR's honest limits](../STAR_Voting/properties_and_limits/STAR_honest_limits.md).

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

**The bonus:** those indicators *are* the full [pairwise preference matrix](pairwise_counting.md). So a verifiable STAR election gets the **Condorcet check** — and [Ranked Robin](../RCV_Ranked_Robin/README.md) itself — for free, on the same encrypted data.

## Why this is an argument for STAR

The asymmetry with elimination methods is structural, and it is the [summability](summability/) property showing up again in cryptography:

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
- **Nobody has built this for STAR.** ElectionGuard, [Helios](https://heliosvoting.org) and [Belenios](https://www.belenios.org) all handle additive tallies; **none handles a STAR runoff.** The pairwise-matrix construction above is a **design direction**, not a deployed system, a published protocol, or a peer-reviewed result. Treat it as a sketch for cryptographers to review and pull apart — the underlying pieces (disjunctive range proofs, threshold ElGamal, homomorphic counting) are all standard, but "assembled from standard parts" is not the same as "proven correct."

## Related

- [Summability](summability/) — the property this whole page rests on
- [Pairwise counting & the preference matrix](pairwise_counting.md) — what the indicator matrix *is*
- [STAR's honest limits](../STAR_Voting/properties_and_limits/STAR_honest_limits.md) — ballot verifiability, and the cast-or-challenge mitigation
- [What makes a voting method good?](what_makes_a_voting_method_good.md) — where auditability sits among the criteria
