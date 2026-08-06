# Ranked Robin (RCV-RR) — Honest Limits

**One line:** Ranked Robin (RCV-RR) is a strong Condorcet method — it reads every rank, allows equal ranks, passes the Equal Vote, and has **no center squeeze** — but it inherits the two structural limits of ranked, Condorcet counting: it can hit a **cycle** with no clear winner, and it sees only **order, not strength**, so it can crown a bland compromise.

→ Companion critical pages (parity across methods): [STAR's limits](../../01_STAR/01_Learn/properties_and_limits/STAR_honest_limits.md) · [Approval's limits](../../04_Approval/01_Learn/approval_honest_limits.md) · [RCV-IRV fails the Equal Vote](../../06_Other/RCV_IRV/concepts/RCV_IRV_equal_vote.md). What RCV-RR *is*: [Ranked Robin](ranked_robin.md). Curriculum: [301.4](../../07_Concepts/CURRICULUM.md).

**Also called — and why it matters here.** These limits belong to the *method*, not to the brand, so they follow it under every name it travels under. The algorithm is **Copeland's method** (**Copeland//Borda** once the margins tiebreak is attached), and after the man who described it in 1299 it is also the **Llull method** — Wikipedia's article opens "The Copeland or Llull method." The family it sits in answers to **Condorcet methods**, **round-robin voting**, **paired comparison**, and **tournament voting**. Two campaigns brand it further: **Consensus Choice** (Better Choices for Democracy — a genuinely different cycle rule, so not a straight synonym) and **Instant Round-Robin Voting (IRRV)**, the banner of the Condorcet Canada Initiative, though that term is used loosely enough — sometimes for the whole family, sometimes for Schulze — to be worth pinning down before you rely on it. If you arrived here from any of those words, §1–§5 are still about your method. Which word means what: [the naming decoder](condorcet_naming_decoder.md) · which one we should lead with: [what to call this method](what_to_call_this_method.md).

---

## 1. Condorcet cycles (no clear winner)

Sometimes there is **no Condorcet winner**: A beats B, B beats C, C beats A — a rock-paper-scissors "cycle." Then RCV-RR must fall back to a **resolution rule** (Copeland / margins), and any such rule is harder to explain and can feel arbitrary to a voter ("why did we break it *that* way?"). **How much it matters:** cycles are rare with real electorates, but they are the honest soft spot of every Condorcet method. See [cycle resolution](cycle_resolution.md).

## 2. No preference strength — the "milquetoast" winner

A ranked ballot captures *order only*, not *how much*. RCV-RR elects the candidate who wins the most head-to-head matchups — which can be a **broadly-acceptable compromise everyone ranks second and nobody is excited about**, over a candidate a majority passionately prefers. That's sometimes the right, consensus-seeking answer; but the method literally cannot see intensity, so it can't tell "warm second choice" from "grudging tolerance." (This is the mirror image of STAR's design, which *does* read strength via the 0–5 score.)

## 3. Fails Later-No-Harm; open to burial

Like STAR and Approval, RCV-RR fails Later-No-Harm — ranking a later choice can help them. More specifically it is open to **[burial](../../07_Concepts/topics/burial/README.md)**: insincerely ranking a strong rival *last* can flip a pairwise matchup in your favorite's favor. Honest ranking is usually best, but the incentive exists (Gibbard again: no method is strategy-proof).

Two things the topic hub adds, both worth knowing before conceding the point in a debate: **no Condorcet method can avoid this** — later-no-harm and Condorcet compliance are incompatible, so this is a family property, not a Copeland quirk — and **it isn't ours alone**: Borda is worse, STAR fails the same criterion, and only IRV largely escapes, by not reading your lower ranks at all. Worked on four methods side by side: [Burial](../../07_Concepts/topics/burial/README.md). This method's own worked pair: [burial](../03_Criteria/burial/README.md).

## 4. The count is harder to explain

"Add the stars" (STAR/Score) or "most approvals" (Approval) is a one-sentence tally. A **pairwise matrix** — every candidate against every other — plus cycle-handling is more to show a general audience, even though it's fully **summable and auditable**. Simplicity of *explanation* is a real adoption cost.

## 5. Clone independence — teaming (a narrow, tiebreak-specific failure)

RR **passes** vote-splitting (crowding) clone independence — because it counts head-to-head wins, cloning a candidate can't make that candidate lose. But it can fail **teaming** (running clones of *yourself*) in the one situation where there's **no Condorcet winner** and the winner turns on a **margin** tiebreak: a faction can field clones to reshape the margins and crowd a rival out of the top tier. Worth knowing, easy to overstate — and note it's implementation-dependent: an engine that breaks a 2-way tie by head-to-head (BetterVoting) resists the same attack that a margin tiebreak (LH / the Equal Vote protocol) succumbs to. Worked example: [Clone independence — crowding, teaming, and the tiebreak](rr_clone_independence.md).

## Keep it in perspective

RCV-RR's strengths are exactly why it's worth taking seriously: it passes the **Equal Vote**, reads **every** rank (nothing exhausts), allows equal ranks, and avoids RCV-IRV's center squeeze and non-monotonicity. Its limits — cycles and blindness to intensity — are the genuine cost of a ranked, consensus-first count. Every method trades something away (Arrow, Gibbard); the fair question is which tradeoffs you want, laid out for all four methods on the companion pages above.
