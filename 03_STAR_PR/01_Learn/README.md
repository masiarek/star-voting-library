# Proportional Representation — the ideas behind STAR-PR

*New to multi-winner? Start with the plain-language fork: [Electing more than one, simply](../../07_Concepts/topics/electing_more_than_one.md) — majoritarian ("the N best") vs. proportional ("mirror the electorate"). This folder is the proportional half.*

**Proportional representation** means a coalition wins seats **in proportion to its size**, instead of the largest group taking every seat. These are the concept pages for this folder's method — **STAR-PR** — plus the two comparisons you need to place it: the majoritarian method it replaces, and the ranked method it is always measured against.

## What the word actually promises

- **[What "proportional" actually means](what_proportional_means.md)** — read before advocating for any of this. Exact proportionality has one unambiguous definition and almost no real election meets it; quotas are a *guarantee*, not a price, so candidates routinely win on less; without parties there is no longer an obvious thing to be proportional **to**; and proportionality increases descriptive representation without guaranteeing it along any single characteristic. The honest limits, in one place.

## The method here

- **[STAR-PR](STAR_PR/README.md)** — the ordinary 0–5 STAR ballot, counted proportionally by **reweighting**: three tabulations (Allocated Score, Sequentially Spent Score, Reweighted Range Voting), all runnable on the same ballot file by switching `voting_method:`. The mechanics: [the math behind proportional STAR](STAR_PR/the_math_behind_proportional_star.md). Runnable elections: [`03_STAR_PR/`](../README.md).

## The two comparisons

- **Majoritarian, same ballot — [Bloc STAR](../../02_STAR_Bloc/README.md).** The control: identical ballots, counted so a cohesive majority can take *every* seat. If you don't see why that's a problem, nothing on this page has a motive.
- **Proportional, *ranked* ballot — STV.** This is why a method with "STAR" in its name has an STV page in its concepts folder: **STV is the established proportional method**, the one your audience has already heard of, and the vocabulary of PR — *quota*, *surplus*, *transfer* — is STV's vocabulary. STAR-PR reaches the same goal with scores and reweighting instead of ranks and transfers, so the honest way to explain it is side by side: **[STV vs STAR-PR](stv/proportional_stv_vs_star.md)** counts one shared 100-voter, 3-seat electorate both ways (the proportional methods agree; the majoritarian one doesn't).

  That page is a *comparison*, not STV's home — the STV method itself, its runnable cases, and the BetterVoting STV bug lab live in **[06_Other/STV](../../06_Other/STV/README.md)**. (And don't fold STV into "RCV" meaning IRV: same ranked ballot, different count — [terminology](../../07_Concepts/tips/TIPS_terminology.md).)

Both proportional families are **Voting 301** material — see [Voting 301](../../07_Concepts/curriculum/CURRICULUM_301.md) (301.1), or the [curriculum hub](../../07_Concepts/CURRICULUM.md) for the whole map. For the single-winner methods, stay in [STAR](../../01_STAR/01_Learn/README.md) and [RCV-IRV](../../06_Other/RCV_IRV/concepts/README.md).
