# Proportional Representation — the ideas behind STAR-PR

*New to multi-winner? Start with the plain-language fork: [Electing more than one, simply](../../07_Concepts/topics/electing_more_than_one.md) — majoritarian ("the N best") vs. proportional ("mirror the electorate"). This folder is the proportional half.*

**Proportional representation** means a coalition wins seats **in proportion to its size**, instead of the largest group taking every seat. These are the concept pages for this folder's method — **STAR-PR** — plus the two comparisons you need to place it: the majoritarian method it replaces, and the ranked method it is always measured against.

## What the word actually promises

- **[Proportional to *what*?](proportional_to_what.md)** (101) — the question party-list PR never has to answer. STAR-PR divides seats among **quotas of voters**, not parties, so the groups are discovered by the ballots rather than declared in advance. Start here if proportionality makes sense to you with parties and stops making sense without them.

- **[STAR-PR — a voter's FAQ](star_pr_faq.md)** (101) — the kitchen-table questions, answered by tracing one ballot: how 0–5 stars become three winners, whether a blank spoils anything, why a spent ballot is not a punishment, whether you should bullet vote, and who checks the math. Includes the two things people most often get wrong — Bloc STAR is not "top N by points", and Allocated Score does not shade everyone's weight.

- **[What "proportional" actually means](what_proportional_means.md)** — read before advocating for any of this. Exact proportionality has one unambiguous definition and almost no real election meets it; quotas are a *guarantee*, not a price, so candidates routinely win on less; without parties there is no longer an obvious thing to be proportional **to**; and proportionality increases descriptive representation without guaranteeing it along any single characteristic. The honest limits, in one place.

- **[Simulating proportional systems](simulating_pr.md)** (401) — where the quantitative claims come from. The four voter models, the parameters a study must fix, the metrics, and the two variables that dominate results — plus the clustered spatial model the peer-reviewed STAR paper actually uses, and why it was chosen over impartial culture and plain Gaussian spatial.

## The method here

- **[STAR-PR](STAR_PR/README.md)** — the ordinary 0–5 STAR ballot, counted proportionally by **reweighting**: three tabulations (Allocated Score, Sequentially Spent Score, Reweighted Range Voting), all runnable on the same ballot file by switching `voting_method:`. The mechanics: [the math behind proportional STAR](STAR_PR/the_math_behind_proportional_star.md). Runnable elections: [`03_STAR_PR/`](../README.md).

## The two comparisons

- **Majoritarian, same ballot — [Bloc STAR](../../02_STAR_Bloc/README.md).** The control: identical ballots, counted so a cohesive majority can take *every* seat. If you don't see why that's a problem, nothing on this page has a motive.
- **Proportional, *ranked* ballot — [STV](../../06_Other/STV/README.md).** You cannot explain STAR-PR without it: **STV is the established proportional method**, the one your audience has already heard of, and the vocabulary of PR — *quota*, *surplus*, *transfer* — is STV's vocabulary. STAR-PR reaches the same goal with scores and reweighting instead of ranks and transfers, so the honest way to explain it is side by side: **[STV vs STAR-PR](../../method_comparisons/stv_vs_star_pr/README.md)** counts one shared 100-voter, 3-seat electorate both ways (the proportional methods agree; the majoritarian one doesn't).

  Note where each thing lives. The **method** is at [06_Other/STV](../../06_Other/STV/README.md) — its runnable cases and the BetterVoting STV bug lab. The **comparison** is in [method_comparisons](../../method_comparisons/README.md), on neutral ground, because a page that weighs two methods against each other shouldn't sit inside one of them. Neither is here. (And don't fold STV into "RCV" meaning IRV: same ranked ballot, different count — [terminology](../../07_Concepts/tips/TIPS_terminology.md).)

Both proportional families are **Voting 301** material, and they get **a rung each** — see [Voting 301](../../07_Concepts/curriculum/CURRICULUM_301.md): 301.1 proportional STAR, 301.2 STV. Or the [curriculum hub](../../07_Concepts/CURRICULUM.md) for the whole map. For the single-winner methods, stay in [STAR](../../01_STAR/01_Learn/README.md) and [RCV-IRV](../../06_Other/RCV_IRV/concepts/README.md).
