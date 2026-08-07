# Topic: The four kinds of insincere vote

**Level: 201 → 301 · for debaters**

**Topic hub — a cross-method view.** The [Equal Vote Coalition](https://www.equal.vote)'s taxonomy names four distinct ways to vote insincerely on a rated or ranked ballot. The names matter because people argue past each other by confusing them: "STAR is vulnerable to strategy" and "IRV is vulnerable to strategy" can be true of the same word and mean opposite things about the ballot, the risk, and the cure.

> **The one idea to take away:** two of the four **invert** your order — they state a preference you don't have. Two **erase** it — they state an *indifference* you don't have. Inversion is only available where the count reads order; erasure is only available where the count reads degree. That single split explains which strategies each method is exposed to, and it is why [choose-one](../plurality.md) is the worst of both worlds: it forces you to erase every distinction below your one mark, *and* it rewards inverting the top.

| Type | Also called | What the voter does | Which ballots it's possible on | Full page |
|---|---|---|---|---|
| **Strong insincerity** | **Favorite betrayal**, *compromising*, *decapitation* | Gives someone a **higher** score/rank than their true favorite — inverts the **top** | any ballot with more than one level | [Favorite betrayal — Voting 301](../../../01_STAR/01_Learn/properties_and_limits/favorite_betrayal_voting_301.md) · [the worked pair](../../../01_STAR/03_Criteria/favorite_betrayal/README.md) |
| **Weak insincerity** | **Burial**, *skipping* | Keeps the favorite on top, but puts a *less*-preferred candidate **below** an even-less-preferred one — inverts **below the top** | ranked, and rated | [Burial (topic hub)](../burial/README.md) |
| **Restrictive sincerity** | **Tactical minimization**, *bullet voting*, *truncation* (down-voting) | **Lowers** support for non-favorites — erases your preferences **downward** | rated, approval, truncatable ranked | [Restrictive sincerity](restrictive_sincerity.md) |
| **Expansive sincerity** | **Tactical maximization** (up-voting) | **Raises** support for non-favorites — erases your preferences **upward** | rated, approval | [Expansive sincerity](expansive_sincerity.md) |

## Which one am I looking at?

Four questions, in order — the first "yes" names it:

1. **Is someone above my true favorite?** → *strong insincerity* (favorite betrayal).
2. **Is anyone below someone I like less?** → *weak insincerity* (burial).
3. **Did I flatten people down to the same low mark?** → *restrictive sincerity*.
4. **Did I flatten people up to the same high mark?** → *expansive sincerity*.

The second pair looks harmless — you never claimed to prefer anyone you don't — which is exactly why it's the pair most voters actually commit, usually without thinking of it as strategy at all.

## What each method is exposed to

| Strategy | Choose-One | RCV-IRV | Ranked Robin | Approval | STAR |
|---|---|---|---|---|---|
| **Favorite betrayal** | **structural** — the only defence against vote-splitting | possible ([center squeeze](../center_squeeze/README.md)) | rare | not needed | rare, [conceded](../../../01_STAR/03_Criteria/favorite_betrayal/README.md) |
| **Burial** | n/a (no order) | largely resisted ([later-no-harm](../../GLOSSARY.md)) | **its named risk** | n/a (no order) | possible, rarely pays |
| **Restrictive** (bullet / truncate) | **forced** — the ballot *is* a bullet vote | truncation, → [exhausted ballots](../../../06_Other/RCV_IRV/concepts/exhausted_ballots_301.md) | truncation | **half the threshold dilemma** | backfires ([worked](../../../01_STAR/05_Practice/ex06_bullet_backfire.md)) |
| **Expansive** (up-vote / hedge) | n/a — one mark | n/a — order is zero-sum | n/a | **the other half** | backfires ([worked](../../../01_STAR/03_Criteria/tactical_maximization/README.md)) |

Two readings of that grid worth stating plainly:

- **A ranked ballot has no volume knob.** Raising one candidate necessarily lowers another, so rows 3–4 barely exist there — a ranked-ballot voter who wants to "support harder" has only inversion available. That's the honest case *for* a rated ballot, and the reason the STAR/Approval strategy conversation is about volume while the RCV-IRV one is about order.
- **A rated ballot's exposure is the pair that backfires.** Both erasure strategies cost the voter information they might have needed, which is what a ~1:1 [help-to-backfire ratio](../strategic_voting.md#what-the-simulations-say) means in practice.

## Runnable here

| Case | Kind | What it shows |
|---|---|---|
| [Honest](../../../01_STAR/03_Criteria/favorite_betrayal/cases/cases_pages/bv2206_7mckyg_fbc_honest_tepid_consensus.md) → [betrayal pays](../../../01_STAR/03_Criteria/favorite_betrayal/cases/cases_pages/bv2207_b6xrdr_fbc_betrayal_pays.md) | strong | nine voters demote their own favorite and get a better result — STAR's conceded FBC failure, live on BetterVoting |
| [Sincere](../../../05_Ranked_Robin/03_Criteria/burial/cases/cases_pages/bv2208_7q6by8_burial_sincere.md) → [burial pays](../../../05_Ranked_Robin/03_Criteria/burial/cases/cases_pages/bv2209_fxhw6g_burial_pays.md) | weak | 15 of 42 voters rank the Condorcet winner last, manufacture a cycle, and win the tiebreak |
| [Honest](../../../01_STAR/05_Practice/cases/cases_pages/ex06_bullet_honest.md) → [bullet backfire](../../../01_STAR/05_Practice/cases/cases_pages/ex06_bullet_backfire.md) | restrictive | four fans zero out their second choice and elect the candidate they scored 0 |
| [Honest](../../../01_STAR/03_Criteria/tactical_maximization/cases/cases_pages/tactical_max_c3_b9_honest.md) → [hedged](../../../01_STAR/03_Criteria/tactical_maximization/cases/cases_pages/tactical_max_c3_b9_hedged.md) | expansive | four voters hedge to a 5, register **Equal Support** in the runoff, and lose it |
| [One opinion, three approval lines](../../../01_STAR/05_Practice/ex13_draw_the_line.md) | both erasures | the same nine honest opinions produce three different Approval winners depending only on where the room draws its line |

## The framing this repo keeps

No method is strategy-proof — [Gibbard–Satterthwaite](../gibbard_satterthwaite_theorem.md) forbids it, so "you can construct a strategy against X" is never news. The questions that separate methods are the ones this taxonomy makes askable: **which kind** of insincerity does it invite, **how many voters** must coordinate, **how good must their polling be**, and **what happens to them when it misfires**. A strategy that needs a third of the electorate and a three-point knife edge is a heist; one that a lone voter commits by instinct on election day is a Tuesday.

---

*This is a **topic hub** (cross-method index). Parent essay: [strategic voting across the Equal Vote methods](../strategic_voting.md). See also [the five strategic pathologies](../strategic_pathologies.md) · [PVSI, the strategic-incentive metric](../pvsi_strategic_incentive.md) · [Gibbard–Satterthwaite](../gibbard_satterthwaite_theorem.md) · [the topics index](../README.md). Glossary: [`bullet voting`, `burial`, `Equal Support`, `favorite betrayal`](../../GLOSSARY.md).*

# file: README.md
