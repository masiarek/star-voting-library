# Electing a committee — making sure people have a voice (a gentle intro)

*Beginner level (101). When you elect **one** winner, "most support wins" is easy. But when you elect a **committee** — several seats at once — "who should win?" suddenly has several reasonable answers, and they can disagree sharply. This walks through one small example to build the intuition, using only counting. The formal version is the [301 companion](abc_rules_spectrum.md).*

## The setup

An academic society elects a **4-person steering committee** (so **k = 4** seats). Seven people run: **a, b, c, d, e, f, g**. Every member votes with an **approval ballot** — they check off *everyone they'd be happy to have on the committee* (as many or as few as they like). Twelve ballots come in:

```
3 people voted {a, b}      3 people voted {a, c}      2 people voted {a, d}
1 person voted {b, c, f}   1 person voted {e}         1 person voted {f}      1 person voted {g}
```

First, count how many voters approved each candidate:

| candidate | a | b | c | d | e | f | g |
|-----------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| approvals | **8** | 4 | 4 | 2 | 1 | 2 | 1 |

Candidate **a** is wildly popular (8 of 12). Everyone else is niche.

## The obvious rule: seat the most-approved (Approval Voting)

The natural move is: **fill the 4 seats with the 4 most-approved candidates.** That's called **Approval Voting (AV)** for committees. The top three are clear — **a, b, c**. The fourth seat is a **tie**: **d** and **f** both have 2 approvals. So AV actually gives *two* equally-good committees:

- **{a, b, c, d}**
- **{a, b, c, f}**

(When a rule can't pick a single winner, we call it *tied* or *irresolute*; a real election breaks the tie with a coin toss decided **ahead of time** — the same "published lot" idea STAR uses.)

## The catch: who got left out?

Look at **{a, b, c, d}** and ask a different question — *how many voters have nobody they approved on the committee?*

- the 3 `{a,b}`, 3 `{a,c}`, 2 `{a,d}` voters → all got **a** ✓
- the `{b,c,f}` voter → got b and c ✓
- the `{e}` voter → **nobody** ✗
- the `{f}` voter → **nobody** ✗
- the `{g}` voter → **nobody** ✗

Three voters end up **completely unrepresented**. AV maximized *total* approvals, but it did it by piling the big popular candidates together and shrugging at the small groups. Picking **{a, b, c, f}** instead rescues the `{f}` voter, leaving only 2 people out — which is why, of AV's two tied committees, `{a,b,c,f}` is arguably the kinder one.

## A different goal: leave nobody out (Chamberlin–Courant)

What if our goal were *"give as many voters as possible at least one person they like"*? A rule called **Approval Chamberlin–Courant (CC)** optimizes exactly that. On this election it picks:

- **{a, e, f, g}** — and now **every single voter** has someone they approved.

But notice the price: CC seats **e** and **g**, each liked by only *one* person, and **drops b and c**, each liked by *four*. So it swung the opposite way — it covers everyone once, but gives the big groups thin representation. That's not obviously "fairer" either.

## The middle ground: fair shares (proportional)

Between "most total approval" (AV) and "cover everyone" (CC) sits the **proportional** idea: give each group of voters a share of the seats roughly matching its size. The best-known such rule, **Proportional Approval Voting (PAV)**, picks:

- **{a, b, c, f}** — the popular a/b/c, *plus* f to represent the f-liking voters, leaving only 2 people uncovered.

## The point

"Which four should win?" has **at least three defensible answers on the very same ballots**:

| Goal | Rule | Committee | Voters left with nobody |
|------|------|-----------|:--:|
| Most total approval | **AV** | {a,b,c,d} *or* {a,b,c,f} | 3 *or* 2 |
| Fair shares | **PAV** | {a,b,c,f} | 2 |
| Leave nobody out | **CC** | {a,e,f,g} | **0** |

None is "the right answer" — each optimizes a *different value*. Choosing a multi-winner rule is really choosing **what you want the committee to be good at**: broad popularity, proportional fairness, or covering everyone.

## Next

- The formal treatment — the scoring formulas, the utilitarian↔egalitarian spectrum, Thiele methods, and how STAR's committee rules line up — is in **[ABC rules and the utilitarian–egalitarian spectrum (301)](abc_rules_spectrum.md)**.
- The runnable files and a "shadow STAR" of this same election: [Lackner & Skowron — approval and its shadow STAR](../../../04_Approval/multiwinner/lackner_skowron_shadow_star.md).
- Source: Lackner & Skowron, [*Multi-Winner Voting with Approval Preferences*](https://link.springer.com/book/10.1007/978-3-031-09016-5) (open access), Example 2.1–2.3.
