// bv_ballot_sheet (Rust/Typst) — print STAR paper ballots (PDF) from a BetterVoting
// export. Rust port of bv_ballot_sheet.py, Option B: compose a Typst document and
// render it to PDF with the embedded Typst compiler (no headless browser).
//
// Pipeline: BV export JSON --(serde_json)--> {title, candidates, id, descriptions}
//           URLs --(qrcode)--> QR SVGs
//           data + template --(Typst)--> PDF
//
// ONE input route: --bv-export FILE (a BetterVoting export JSON). Same design as the
// Python tool — create on BV, export, print.

use clap::Parser;
use qrcode::render::svg;
use qrcode::QrCode;
use std::path::PathBuf;

mod typst_render;

#[derive(Parser, Debug)]
#[command(name = "bv_ballot_sheet", about = "Print STAR paper ballots (PDF) from a BetterVoting export")]
struct Args {
    /// A BetterVoting export JSON — the only input route.
    #[arg(long)]
    bv_export: PathBuf,
    /// Optional: override the ballot title (e.g. a cleaner name than the verbose BV one).
    #[arg(long)]
    title: Option<String>,
    /// Optional: override the ballot question line.
    #[arg(long)]
    question: Option<String>,
    /// Output PDF path.
    #[arg(long, default_value = "ballots.pdf")]
    out: PathBuf,
    /// How many ballots.
    #[arg(long, default_value_t = 30)]
    copies: usize,
    /// Number each ballot ("Ballot #N — keep this to verify it was counted").
    #[arg(long)]
    serials: bool,
    /// Deliberately print without the QR codes.
    #[arg(long)]
    no_qr: bool,
    /// Append your local chapter to a small promo footer.
    #[arg(long)]
    chapter: Option<String>,
}

/// Everything the ballot needs, pulled from the export.
pub struct Ballot {
    pub title: String,
    pub question: String,
    pub blurb: String, // election description
    pub bv_id: String,
    pub candidates: Vec<String>,
    pub qr_vote_svg: Option<String>,
    pub qr_results_svg: Option<String>,
    pub copies: usize,
    pub serials: bool,
    pub chapter: Option<String>,
}

fn qr_svg(url: &str) -> Result<String, String> {
    let code = QrCode::new(url.as_bytes()).map_err(|e| format!("QR encode failed: {e}"))?;
    Ok(code
        .render::<svg::Color>()
        .min_dimensions(240, 240)
        .quiet_zone(true)
        .dark_color(svg::Color("#000000"))
        .light_color(svg::Color("#ffffff"))
        .build())
}

/// Navigate the BV export: `Election`/`election` (or flat) → title, id, description,
/// races[0].{description, candidates[].candidate_name}.
fn from_export(v: &serde_json::Value) -> Result<(String, String, String, String, Vec<String>), String> {
    let election = v
        .get("Election")
        .or_else(|| v.get("election"))
        .unwrap_or(v);
    let title = election
        .get("title")
        .or_else(|| election.get("name"))
        .and_then(|x| x.as_str())
        .unwrap_or("STAR Voting ballot")
        .trim()
        .to_string();
    let bv_id = election
        .get("election_id")
        .or_else(|| election.get("id"))
        .and_then(|x| x.as_str())
        .unwrap_or("")
        .trim()
        .to_string();
    let blurb = election
        .get("description")
        .and_then(|x| x.as_str())
        .unwrap_or("")
        .trim()
        .to_string();
    let race0 = election
        .get("races")
        .and_then(|r| r.get(0))
        .ok_or("no races[] in export")?;
    let question = race0
        .get("description")
        .and_then(|x| x.as_str())
        .unwrap_or("Score each candidate from 0 (worst) to 5 (best).")
        .trim()
        .to_string();
    let candidates: Vec<String> = race0
        .get("candidates")
        .and_then(|c| c.as_array())
        .map(|arr| {
            arr.iter()
                .filter_map(|c| {
                    c.get("candidate_name")
                        .or_else(|| c.get("name"))
                        .and_then(|n| n.as_str())
                        .map(|s| s.trim().to_string())
                })
                .filter(|s| !s.is_empty())
                .collect()
        })
        .unwrap_or_default();
    if candidates.is_empty() {
        return Err("no candidates found in the export".into());
    }
    Ok((title, bv_id, blurb, question, candidates))
}

fn run() -> Result<(), String> {
    let args = Args::parse();

    let raw = std::fs::read_to_string(&args.bv_export)
        .map_err(|e| format!("could not read {}: {e}", args.bv_export.display()))?;
    let v: serde_json::Value =
        serde_json::from_str(&raw).map_err(|e| format!("invalid JSON in export: {e}"))?;
    let (mut title, bv_id, blurb, mut question, candidates) = from_export(&v)?;

    if let Some(t) = args.title {
        title = t;
    }
    if let Some(q) = args.question {
        question = q;
    }

    // A ballot with a live BV id MUST be scannable — QR unless deliberately suppressed.
    let (qr_vote_svg, qr_results_svg) = if args.no_qr || bv_id.is_empty() {
        (None, None)
    } else {
        (
            Some(qr_svg(&format!("https://bettervoting.com/{bv_id}"))?),
            Some(qr_svg(&format!("https://bettervoting.com/{bv_id}/results"))?),
        )
    };

    let ballot = Ballot {
        title,
        question,
        blurb,
        bv_id,
        candidates,
        qr_vote_svg,
        qr_results_svg,
        copies: args.copies.max(1),
        serials: args.serials,
        chapter: args.chapter,
    };

    let out = if args.out.extension().map(|e| e == "pdf").unwrap_or(false) {
        args.out.clone()
    } else {
        args.out.with_extension("pdf")
    };

    let pdf = typst_render::render_pdf(&ballot)?;
    std::fs::write(&out, &pdf).map_err(|e| format!("could not write {}: {e}", out.display()))?;

    println!(
        "Wrote {} STAR ballots ({} candidates) to {}",
        ballot.copies,
        ballot.candidates.len(),
        out.display()
    );
    println!("Print-ready PDF — send it straight to the printer.");
    if !ballot.bv_id.is_empty() {
        println!(
            "Linked to BetterVoting election {} (results: https://bettervoting.com/{}/results).",
            ballot.bv_id, ballot.bv_id
        );
    }
    Ok(())
}

fn main() {
    if let Err(e) = run() {
        eprintln!("error: {e}");
        std::process::exit(1);
    }
}
