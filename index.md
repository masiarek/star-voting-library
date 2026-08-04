---
hide:
  - toc
---

<!-- Homepage of the MkDocs website (https://masiarek.github.io/star-voting-library/).
     GitHub's repo view renders readme.md and ignores this file; MkDocs needs an index.md
     and doesn't recognize the lowercase readme.md as one.

     The page opens on what the library IS, beside the official EVC ballot image — the
     one graphic that earns its place above the fold (styled by
     07_Concepts/about_this_repo/site_extra.css). A pitch headline and a four-stop
     "New to STAR?" path used to live up here; both are gone (removed 2026-08-04), so a
     visitor meets the library rather than the sales copy.

     Both halves are inlined from readme.md via its snippet-section markers — the hero
     paragraph from [start:what-this-is], everything below it from [start:below-hero] —
     so the repo front page and the site homepage share one source and can't drift.
     Keep the two includes adjacent in that order: together they are readme.md read
     straight through. -->

<div class="star-hero" markdown="1">

<div class="star-hero-text" markdown="1">

<p class="star-hero-kicker">⭐ STAR Voting — Score, Then Automatic Runoff</p>

# What this library is

--8<-- "readme.md:what-this-is"

</div>

<div class="star-hero-img" markdown="1">
<img src="07_Concepts/img/star_ballot_example.png" alt="A real STAR ballot: five candidates (Andre, Blake, Carmen, David, Ella) each rated 0–5 stars, with the instructions — give your favorite(s) five stars, your last choice(s) zero; equal scores mean no preference; blanks count as zero; the two highest-scoring candidates are finalists and your full vote goes to the finalist you prefer.">
</div>

</div>

--8<-- "readme.md:below-hero"
