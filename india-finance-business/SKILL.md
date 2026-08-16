---
name: india-finance-business
description: Financial analysis for an Indian private company or MSME, from the messy documents the business actually has. Reads audited financial statements, Tally trial balances, Form 3CD tax audit reports, GST returns and scanned PDFs, builds a provenance-tagged multi-year series, and computes the ratios that matter for a private business — working capital cycle, capital productivity, incremental margin, PAT versus PAT plus depreciation. Classifies MSME/Udyam status and the benefits attached. Maps related parties and inter-company funding from statutory schedules. Use this whenever someone wants to understand a company's financial position, compare years, work out where cash is going, benchmark against a competitor, size a capex decision, or make sense of a balance sheet, P&L, trial balance or auditor's report — including when the numbers arrive as scans or Tally exports rather than clean data. Also use it when someone asks why reported profit looks low, whether a business can afford an investment, or how their company compares with a rival. Company scope only. For one person's own money, use india-finance instead. Every figure is computed in Python.
---

# India business finance

You analyse a real company's actual books. Audited statements, Tally exports, tax audit reports —
whatever the business has, in whatever state it arrives.

**Two rules that govern everything here.**

**Every number comes from Python, never from you.** You read documents and interpret results; the
arithmetic happens in `scripts/analyse.py`. A model doing mental maths on a balance sheet will be
wrong occasionally and confident always, and someone will make a capital decision on it. When you
need a figure, compute it and show the command.

**Say where every number came from.** A figure from an audited statement and a figure from an
unaudited trial balance are not the same kind of fact, and conclusions built on the second one
deserve a hedge. Carry the provenance through to the output — see `references/document-types.md`.

---

## The shape of the work

Most requests are one of four things. Identify which before you start, because they need different
depth.

| Request | What it needs |
|---|---|
| "What do these accounts say?" | Series + ratios + a written read |
| "Can we afford X?" | Cash generation, working capital, existing gearing |
| "How do we compare to a competitor?" | Declared-to-declared ratios, both sides |
| "Why is our profit so low?" | Depreciation, finance cost, working capital, mix |

---

## Workflow

### 1. Find out what documents exist before asking for anything

People rarely know what they have. Ask what's available and offer the list — audited statements,
Tally exports, tax audit report, GST returns, bank sanction letters — rather than asking an open
question. `references/document-types.md` explains what each one proves and what it cannot.

If documents are scanned, say so early and OCR them. Scans are normal for anything before about
2018 and for many small-firm audit packs.

### 2. Extract, and record provenance per year

Build a table with one row per financial year and a provenance tag on each: **audited**,
**provisional**, or **trial balance**. This single discipline prevents most bad conclusions.

Two checks worth running immediately, because they catch the two most common extraction errors:

- **Does the balance sheet balance?** If total assets ≠ total equity and liabilities, extraction
  failed somewhere. Find it before computing anything.
- **Does the year-on-year reserves movement equal PAT?** If it does, both figures are probably read
  correctly. This is a free cross-check and it's invaluable on OCR'd pages.

### 3. Compute

Run `scripts/analyse.py`. It takes a JSON file of per-year figures and emits the series, the ratios
and the derived measures. Never hand-compute what the script already does.

```bash
python scripts/analyse.py company.json --benchmark
```

`references/ratios.md` explains which ratios earn their place for a private company and which are
dead on arrival — roughly a quarter of any standard ratio set needs a market price the company
doesn't have.

### 4. Interpret, and be honest about what the numbers can carry

This is where the value is. A ratio table is not analysis. Some things worth saying plainly when the
data shows them:

- **Reported profit is not the same as cash generation.** Depreciation is non-cash, and a business
  mid-capex will show falling PAT while cash improves. Read PAT + depreciation alongside PAT before
  concluding anything about performance.
- **In owner-managed private companies, reported profit is shaped by depreciation policy and tax
  planning as much as by trading.** This isn't a reason to distrust the accounts; it's a reason to
  lean on figures that are harder to shape — revenue (GST-corroborated), balance sheet items, the
  asset register — and to prefer comparisons *between* companies on the same declared basis over
  judgements about one company's absolute margin.
- **A single year means little if the order book is lumpy.** Project businesses routinely swing
  ±40%. Check the series shape before quoting any year, and prefer a three-year average.

`references/traps.md` carries the specific errors that produce wrong answers here. Read it before
the first substantive analysis — most of the entries cost someone real time to discover.

### 5. Report

Structure the output like this. Adapt freely, but keep provenance and keep the caveats attached to
the numbers they qualify rather than dumped at the end.

```markdown
## The series
[table: year, revenue, EBITDA, PAT, provenance tag]

## What the ratios say
[table with benchmark comparison, flagged strong / acceptable / weak]

## Working capital
[cycle in days, and what growth costs in cash]

## The read
[3–6 paragraphs. What is actually happening and what it means.]

## What I could not verify
[missing years, unaudited figures, unreconciled items]
```

---

## MSME status is not a footnote

For an Indian company under the Udyam thresholds, classification changes real money — payment
protection under MSMED, and in public procurement, exemptions and preferences. It also erodes as
the business grows, which is a strategic fact worth surfacing rather than a compliance detail.

See `references/msme.md` for current thresholds and what attaches to each tier. Verify thresholds
before relying on them; they have been revised more than once.

---

## Related parties and inter-company funding

Group companies frequently fund each other in ways the P&L does not show. If a tax audit report
(Form 3CD) is available, its schedules disclose payments to specified persons and every loan taken
or repaid above the threshold — which is how you find a sister company acting as an undocumented
working-capital line.

`references/related-parties.md` explains the technique, including how to reverse-engineer what a
counterparty billed from TDS entries in Form 26AS.

---

## Scope

**In:** private limited companies, LLPs, partnerships and proprietorships in India; historical
analysis; ratio and competitor benchmarking; working capital; capital-allocation framing.

**Out:** personal finance — use `india-finance`. Statutory filing, tax computation and audit
opinions — those need a chartered accountant, and you should say so rather than approximate them.
Listed-company valuation — the market-price ratios don't apply and the disclosure regime is
different.

**Never present analysis as an audit opinion or a filing position.** You are reading accounts, not
signing them.

---

## Reference files

| File | Read it when |
|---|---|
| `references/document-types.md` | Always, before extraction — what each document proves |
| `references/traps.md` | Before the first analysis — the errors that produce wrong answers |
| `references/ratios.md` | Computing or interpreting ratios |
| `references/msme.md` | Udyam classification comes up |
| `references/related-parties.md` | A Form 3CD or 26AS is available, or group structure matters |
