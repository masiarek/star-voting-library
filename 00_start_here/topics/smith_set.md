# The Smith Set — the Smallest Club That Beats Everyone Outside It

*What "the strongest candidate" means when no single candidate beats everyone. When a cycle erases the Condorcet winner, the principled fallback isn't a person — it's a **set**: the smallest group whose every member beats every outsider head-to-head. Once you have that club, "any decent method should at least pick from inside it" becomes a testable criterion — and it neatly sorts the Condorcet family.*

→ **Level: Voting 301** — Curriculum [301.4](../CURRICULUM.md) (limits & theory) · Glossary: [`Smith set`](../GLOSSARY.md) · the tournament math: [The math behind Condorcet](../RCV_Ranked_Robin/the_math_behind_condorcet.md)

---

## The problem: "beats everyone head-to-head" can come up empty

A [Condorcet winner](condorcet/) beats every rival one-on-one, and when one exists it's a natural "correct answer" for majority rule. But majority preference isn't guaranteed to be transitive: a majority can prefer A over B, B over C, *and* C over A — a rock-paper-scissors **cycle**, and suddenly "the candidate who beats everyone" doesn't exist. That's the [Condorcet paradox](../RCV_Ranked_Robin/cycle_resolution.md), and every Condorcet method needs an answer to it.

The Smith set is the *principled* part of that answer. Before asking "who wins the cycle?", it asks a more modest question with a provably clean answer: **who is even in contention?**

## The definition: the smallest club that beats everyone outside

Call a group of candidates a **dominating set** if every member beats every non-member head-to-head. The whole field is trivially dominating (there's no one outside), so dominating sets always exist — and a neat theorem says they're **nested**: of any two, one contains the other. That means there is always a unique *smallest* one:

> **The Smith set is the smallest non-empty group of candidates such that every member beats every candidate outside the group in a head-to-head matchup.**

Three consequences fall straight out of the definition:

- **If a Condorcet winner exists, the Smith set is just `{that winner}`** — a one-member club. The set only grows when a cycle appears, which is why it's called the *generalized* Condorcet winner.
- **In a cycle, the whole cyclic clump at the top is in the club.** You can't admit "just the strongest one" — whoever you pick, someone else in the cycle beats them.
- **A [Condorcet loser](../GLOSSARY.md) can never make the club** — everyone beats them, so the club works fine without them.

One set, several names — the literature is messy: **Smith set** (after mathematician John H. Smith, 1973 — no relation to Warren D. Smith of [range voting](../Range_Voting/range_voting.md)), **top cycle**, **GETCHA** ("Generalized Top-Choice Assumption," Schwartz's older coinage), and textbook framings like **"generalized Condorcet candidates"** (Börgers, [*Mathematics of Social Choice*](../books/social_choice_theory.md)).

## See it: a cycle plus an outsider (runnable)

Take the [Ada/Ben/Cara cycle](../../05_Ranked_Robin/condorcet_vs_ranked_robin/condorcet_vs_ranked_robin_pages/02_cycle_no_condorcet.md) and change one thing: add a fourth candidate, **Dave**, whom every voter ranks last ([`04_smith_set_c4_b7`](../../05_Ranked_Robin/condorcet_vs_ranked_robin/condorcet_vs_ranked_robin_pages/04_smith_set_c4_b7.md), counted by [Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md)):

```text
--- Ranked Robin (RCV-RR / Copeland) Method (single winner) ---
 Tabulating 7 ballots (ranked ballots).

Ballots:
     3 × Ada > Ben > Cara > Dave
     2 × Ben > Cara > Ada > Dave
     2 × Cara > Ada > Ben > Dave

Round-Robin — every pair, head-to-head (For – Against):
   Ada   beats Ben    5 – 2
   Cara  beats Ada    4 – 3
   Ada   beats Dave   7 – 0
   Ben   beats Cara   5 – 2
   Ben   beats Dave   7 – 0
   Cara  beats Dave   7 – 0

Win–loss record — Copeland score = wins + ½·ties (most wins wins; ties broken by total margin, then lot order):
    #  Candidate  W–L–T  Copeland  Margin  Beats
    1  Ada        2–1–0         2      +9  Ben, Dave
    2  Ben        2–1–0         2      +7  Cara, Dave
    3  Cara       2–1–0         2      +5  Ada, Dave
    4  Dave       0–3–0         0     -21  —

Winner — Ranked Robin (RCV-RR): Ada
   *** 3 candidates tie for the most wins (Ada, Ben, Cara) — a Condorcet cycle (no candidate beats all others).
```

Now run the club-membership check, smallest group first:

1. **`{Ada}`?** Not dominating — Cara beats Ada (4–3). A club member can't be losing to an outsider.
2. **`{Ada, Cara}`?** Not dominating — Ben beats Cara. Same problem.
3. **`{Ada, Ben, Cara}`?** Dominating — the only outsider is Dave, and all three beat Dave 7–0. ✓

No smaller group works, so **the Smith set is `{Ada, Ben, Cara}`** — and Dave, despite being *on* every ballot, is provably out of contention: to get into the club, Dave would have to stop losing to someone inside it. Notice the shortcut the win–loss table hands you: the club is exactly the top block of the Copeland standings (records 2–1, 2–1, 2–1 vs Dave's 0–3) — that's not a coincidence, it's a theorem (dominating sets are nested *by Copeland score*).

The full pairwise grid, and this exact election as a runnable YAML, are in [`04_smith_set_c4_b7`](../../05_Ranked_Robin/condorcet_vs_ranked_robin/condorcet_vs_ranked_robin_pages/04_smith_set_c4_b7.md). (It's an LH-only case: BetterVoting's Ranked Robin breaks a Copeland tie *randomly*, so a deliberate three-way tie isn't freezable there — see [the tiebreak divergence](../RCV_Ranked_Robin/rr_tiebreak_lh_vs_bv.md).) For a Smith set of four in a *real* library election, see the [no-Condorcet-winner comparison set](../../method_comparisons/no_condorcet_bv2138/bv2138_cxrf8v_no_condorcet.md).

## The criterion: Smith-efficient methods never leave the club

A method satisfies the **Smith criterion** (is **Smith-efficient**) if its winner always comes from the Smith set. Since a lone Condorcet winner *is* the Smith set, Smith-efficiency implies Condorcet-efficiency — it's the strictly stronger promise: *even in a cycle, I won't wander off into the dominated candidates.*

| Method | In the club? | Why |
|--------|:---:|-----|
| **[Ranked Robin](../RCV_Ranked_Robin/ranked_robin.md) / Copeland** | ✅ | the best win–loss records *are* the top of the club — however the tie among them is then broken (margins, lot, or BV's random draw), the winner stays inside |
| **Ranked Pairs, Schulze** | ✅ | the "serious" [cycle resolvers](../RCV_Ranked_Robin/cycle_resolution.md) are Smith-efficient by construction |
| **Minimax** | ❌ | Condorcet-efficient, but in a 4+ candidate cycle its "least bad worst loss" pick can fall *outside* the Smith set — the classic fine-print failure |
| **RCV-IRV (Hare)** | ❌ | not even Condorcet-efficient ([center squeeze](center_squeeze/)), so Smith is out of reach |
| **Borda, Score, Approval, Plurality** | ❌ | point totals can crown a candidate the club collectively beats |
| **STAR** | ❌ | not Condorcet-compliant *by design* — it trades the guarantee for counting preference strength; see [three notions of "winner"](../STAR_Voting/properties_and_limits/STAR_three_winner_notions.md) |

Two footnotes to the table. First, the criterion has spawned a whole construction kit: **Smith//X** methods first *eliminate everyone outside the Smith set*, then run method X on the survivors — Smith//IRV (a.k.a. Tideman's Alternative) and Smith//Minimax are the common ones, bolting Smith-efficiency onto methods that lack it. Equal Vote's own tie-breaking protocol reaches for the same idea ("Smith-Minimax" sits in [Ranked Robin's tiebreak hierarchy](../RCV_Ranked_Robin/ranked_robin.md)). Second, there's a related *independence* criterion, **ISDA** ("Independence of Smith-Dominated Alternatives"): candidates outside the Smith set should be ignorable — delete them from every ballot and the winner shouldn't change. Our demo passes the spot-check: delete Dave and you get exactly [the 02_cycle election](../../05_Ranked_Robin/condorcet_vs_ranked_robin/condorcet_vs_ranked_robin_pages/02_cycle_no_condorcet.md), where Ranked Robin still elects Ada. ([electowiki](https://electowiki.org/wiki/Independence_of_Smith-dominated_alternatives) has the formal statement — advocacy-adjacent wiki, fine for definitions.)

## Fine print: Schwartz, ties, and "Smith's method"

- **The [Schwartz set](https://electowiki.org/wiki/Schwartz_set)** (a.k.a. GOCHA) is the Smith set's slightly tighter cousin: always **Schwartz ⊆ Smith**, and the two differ *only* when pairwise **ties** are involved (a tie is enough to keep you in Smith, not in Schwartz). With an odd number of voters and full rankings — like our 7 ballots — no pairwise ties are possible and the two sets coincide.
- **"Smith's method"** — electing the Smith set *itself* — is set-valued: fine for shortlists, but a single-winner election still needs a rule for inside the club. That's exactly the [cycle-resolution](../RCV_Ranked_Robin/cycle_resolution.md) split, and why the [ranked-ballot method zoo](ranked_ballot_methods_zoo.md) files Smith/Schwartz under "set-valued, usually used as a filter."
- **Computing it is graph theory, and cheap:** the Smith set is the **top strongly connected component** of the pairwise-results tournament — or, equivalently, walk down the Copeland standings until the block above the line beats everyone below it. Standard algorithms, quadratic work; [the math behind Condorcet](../RCV_Ranked_Robin/the_math_behind_condorcet.md) maps this corner (tournaments, SCCs, and friends).

## How big is the club in practice?

Almost always: **one member.** Real electorates that spread along a [spatial](spatial_voting_model.md) spectrum produce Condorcet winners overwhelmingly often — in one dimension the median-voter theorem *guarantees* one — so the Smith set is a singleton and every Condorcet method just elects it. The set only becomes interesting when preferences genuinely cycle: rare, likeliest in small, sharply three-way-divided electorates ([how often?](../RCV_Ranked_Robin/cycle_resolution.md)). The deep-theory footnote is that in **2+ spatial dimensions** the guarantee collapses spectacularly — the McKelvey–Schofield chaos theorem says the top cycle can then wander essentially anywhere, which is *why* theorists wanted a disciplined "still in contention" set in the first place.

So the honest summary matches the repo's [house caveat](../RCV_Ranked_Robin/the_math_behind_condorcet.md): the Smith set is the right *standard* for judging cycle behavior, and knowing it costs nothing — but no voter needs it on election day, and a method's Smith-efficiency is fine print that matters only on the rare day the matrix eats its own tail.

---

## Cross-references

- [`04_smith_set_c4_b7` — the worked demo](../../05_Ranked_Robin/condorcet_vs_ranked_robin/condorcet_vs_ranked_robin_pages/04_smith_set_c4_b7.md) ([source YAML](../../05_Ranked_Robin/condorcet_vs_ranked_robin/04_smith_set_c4_b7.yaml)) · its no-Dave companion [`02_cycle_no_condorcet`](../../05_Ranked_Robin/condorcet_vs_ranked_robin/condorcet_vs_ranked_robin_pages/02_cycle_no_condorcet.md) · a real 4-member Smith set: [BV2138](../../method_comparisons/no_condorcet_bv2138/bv2138_cxrf8v_no_condorcet.md)
- [The math behind Condorcet](../RCV_Ranked_Robin/the_math_behind_condorcet.md) — tournaments, SCCs, Schwartz, and the theorems (this page's mathematical home)
- [Cycle resolution](../RCV_Ranked_Robin/cycle_resolution.md) — what Minimax / Ranked Pairs / Schulze do *inside* the club
- [Condorcet efficiency — topic hub](condorcet/README.md) · [Pairwise counting](pairwise_counting.md) — the matrix all of this reads from
- Books: [Börgers, *Mathematics of Social Choice*](../books/social_choice_theory.md) — the gentlest rigorous treatment ("generalized Condorcet candidates")
- External: [Wikipedia — Smith set](https://en.wikipedia.org/wiki/Smith_set) (the criteria claims) · [electowiki — Smith set](https://electowiki.org/wiki/Smith_set) (mechanics; advocacy-adjacent)
- Glossary: [`Smith set`, `Condorcet winner`, `Condorcet loser`](../GLOSSARY.md)
