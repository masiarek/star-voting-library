// Compose a Typst document for the ballot and render it to PDF with the embedded
// Typst compiler (typst-as-lib). Fonts come from typst-assets (bundled), the QR SVGs
// are injected as in-memory files, so the binary is self-contained (no headless
// browser, no external typst CLI).

use crate::Ballot;

/// Escape a string for embedding as a Typst string literal ("...").
fn esc(s: &str) -> String {
    s.replace('\\', "\\\\").replace('"', "\\\"").replace('\n', " ")
}

/// Build the Typst source: a data header (#let …) + the ballot layout.
fn build_source(b: &Ballot) -> String {
    let cands = b
        .candidates
        .iter()
        .map(|c| format!("\"{}\"", esc(c)))
        .collect::<Vec<_>>()
        .join(", ");
    let promo = match &b.chapter {
        Some(ch) if !ch.trim().is_empty() => format!(
            "Learn more: starvoting.org · equal.vote · bettervoting.com · {}",
            ch.trim()
        ),
        _ => String::new(),
    };

    format!(
        r##"
#set page(width: 8.5in, height: 11in, margin: 0.4in)
#set text(size: 10pt)
#set par(leading: 0.5em)

#let TITLE = "{title}"
#let QUESTION = "{question}"
#let BLURB = "{blurb}"
#let BVID = "{bvid}"
#let PROMO = "{promo}"
#let HASQR = {hasqr}
#let HASLOGO = {haslogo}
#let LOGOFILE = "{logofile}"
#let SERIALS = {serials}
#let COPIES = {copies}
#let CANDS = ({cands},)

#let bub(n) = box(circle(radius: 8.5pt, stroke: 1.1pt + rgb("#666666"))[
  #set align(center + horizon)
  #text(size: 9pt, weight: "bold", fill: rgb("#444444"))[#n]
])

#let starhead(n) = text(weight: "bold", size: 13pt)[#n]

#let oneballot(serial) = {{
  block(width: 100%, radius: 4pt, inset: 5pt, stroke: 1pt + rgb("#c0392b"),
    align(center, text(fill: rgb("#c0392b"), weight: "bold", size: 9pt,
      "EDUCATION ONLY - A STAR VOTING TEACHING DEMO, NOT A SECRET BALLOT.")))
  v(3pt)
  grid(columns: (1fr, auto, 1fr), align: (center + horizon, center + horizon, center + horizon), column-gutter: 10pt,
    if HASQR {{ align(center)[#image("qr_vote.svg", width: 78pt) \ #text(size: 8pt)[scan to vote]] }} else {{ [] }},
    if HASLOGO {{ align(center + horizon, image(LOGOFILE, height: 56pt)) }} else {{ align(center)[
      #text(weight: "black", size: 27pt)[STAR VOTING] \
      #text(weight: "bold", size: 9pt, fill: rgb("#5a7683"))[SCORE #sym.dot.c THEN #sym.dot.c AUTOMATIC #sym.dot.c RUNOFF]
    ] }},
    if HASQR {{ align(center)[#image("qr_results.svg", width: 78pt) \ #text(size: 8pt)[scan for results]] }} else {{ [] }},
  )
  v(2pt)
  align(center, text(weight: "bold", size: 15pt)[#TITLE])
  if BLURB != "" {{ align(center, text(style: "italic", size: 11pt, fill: rgb("#555555"))[#BLURB]) }}
  align(center, text(size: 11pt, fill: rgb("#333333"))[#QUESTION])
  v(2pt)
  list(
    [Give your favorite candidate(s) five stars.],
    [Give your last choice(s) zero or leave blank.],
    [Equal scores are allowed.],
    [Score other candidates as desired.],
  )
  v(4pt)
  table(
    columns: (2.2fr, 1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
    align: (left + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon, center + horizon),
    stroke: none,
    inset: (x: 2pt, y: 4pt),
    fill: (_, row) => if row >= 2 and calc.odd(row) {{ rgb("#ececec") }} else {{ none }},
    table.hline(y: 2, stroke: 1.5pt + rgb("#bbbbbb")),
    [], text(weight: "bold")[Worst], [], [], [], [], text(weight: "bold")[Best],
    text(weight: "bold", size: 13pt)[Candidate], starhead(0), starhead(1), starhead(2), starhead(3), starhead(4), starhead(5),
    ..CANDS.map(c => (text(weight: "bold", size: 13pt)[#c], bub(0), bub(1), bub(2), bub(3), bub(4), bub(5))).flatten()
  )
  v(2pt)
  line(length: 100%, stroke: 0.8pt)
  v(2pt)
  align(center, text(size: 11pt)[
    The two highest scoring candidates are finalists. \
    Your full vote goes to the finalist you prefer. \
    The finalist with the most votes wins.
  ])
  v(3pt)
  grid(columns: (1fr, 1fr),
    align(left, text(size: 9pt, fill: rgb("#555555"))[
      #if serial != none [Ballot \##serial #sym.dash.em keep this to verify it was counted #sym.dot.c ]
      Election #text(weight: "bold", fill: rgb("#111111"))[#BVID]
    ]),
    align(right, text(size: 9pt, fill: rgb("#555555"))[results: bettervoting.com/#BVID/results]),
  )
  if PROMO != "" {{ v(3pt); align(center, text(size: 8pt, fill: rgb("#5a7683"))[#PROMO]) }}
}}

#for i in range(COPIES) {{
  oneballot(if SERIALS {{ i + 1 }} else {{ none }})
  if i + 1 < COPIES {{ pagebreak() }}
}}
"##,
        title = esc(&b.title),
        question = esc(&b.question),
        blurb = esc(&b.blurb),
        bvid = esc(&b.bv_id),
        promo = esc(&promo),
        hasqr = b.qr_vote_svg.is_some(),
        haslogo = b.logo.is_some(),
        logofile = b.logo.as_ref().map(|(name, _)| name.as_str()).unwrap_or(""),
        serials = b.serials,
        copies = b.copies,
        cands = cands,
    )
}

pub fn render_pdf(b: &Ballot) -> Result<Vec<u8>, String> {
    let source = build_source(b);

    let mut files: Vec<(&str, Vec<u8>)> = Vec::new();
    if let Some(svg) = &b.qr_vote_svg {
        files.push(("qr_vote.svg", svg.clone().into_bytes()));
    }
    if let Some(svg) = &b.qr_results_svg {
        files.push(("qr_results.svg", svg.clone().into_bytes()));
    }
    if let Some((name, bytes)) = &b.logo {
        files.push((name.as_str(), bytes.clone()));
    }

    let engine = typst_as_lib::TypstEngine::builder()
        .main_file(source)
        .fonts(typst_assets::fonts())
        .with_static_file_resolver(files)
        .build();

    let doc = engine
        .compile()
        .output
        .map_err(|e| format!("Typst compile error: {e:?}"))?;

    let pdf = typst_pdf::pdf(&doc, &Default::default())
        .map_err(|e| format!("Typst PDF export error: {e:?}"))?;
    Ok(pdf)
}
