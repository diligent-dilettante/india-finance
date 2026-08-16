# Ratios

Which ratios earn their place for an unlisted Indian company, which are dead on arrival, and how to
read the ones that matter. `scripts/analyse.py` computes all of these — this file is for interpreting
them.

---

## Dead on arrival for a private company

Roughly a quarter of any standard ratio set needs a market price. An unlisted company has none, so
these cannot be computed and should not be quoted:

**P/E · P/B · P/S · EV/EBITDA · PEG · market capitalisation · dividend yield**

Standard financial-analyst tooling computes these anyway and returns nulls or nonsense. If a
valuation is genuinely needed, it comes from DCF or a comparable-transaction multiple applied to
EBITDA, and both need assumptions stated openly rather than a ratio.

---

## Profitability

| Ratio | Formula | Reading |
|---|---|---|
| EBITDA margin | EBITDA / revenue | The cleanest profitability measure. Unaffected by depreciation policy, gearing or tax. |
| Net margin | PAT / revenue | Shaped by depreciation and tax planning — see traps 6 and 7. Use for comparison, not for judgement in isolation. |
| ROE | PAT / net worth | Distorted when net worth is small relative to activity, which is common. |
| ROCE | EBIT / (net worth + debt) | Better than ROE for an owner-managed company. |
| ROA | PAT / total assets | Useful cross-check on ROCE. |

**The one to compute that standard sets omit: PAT + depreciation.** It approximates operating cash
before working capital and it is the honest read on a business mid-capex. Compare its growth against
revenue growth across the series.

**Incremental margin** — (EBITDA_end − EBITDA_start) / (revenue_end − revenue_start) — tells you what
the *growth* earned, as distinct from the base. A business growing revenue at a much lower margin
than its base is buying volume, and that is worth knowing. Note it is highly sensitive to the
endpoints chosen; compute it for several and report the range rather than one figure.

---

## Working capital — usually the most important section

| Measure | Formula |
|---|---|
| Receivable days | trade receivables / revenue × 365 |
| Inventory days | inventories / cost of materials × 365 |
| Payable days | trade payables / cost of materials × 365 |
| **Cash conversion cycle** | receivable + inventory − payable days |

**The growth tax.** Net working capital as a percentage of revenue tells you what each rupee of new
revenue costs in cash. A business at 17% of revenue must find ₹0.17 of funding for every ₹1 of extra
sales, before any profit arrives. This is the single most useful number for anyone asking "can we
grow?" and it rarely appears in standard ratio sets.

A **negative** cycle — customer cash arriving before supplier payment — means growth funds itself.
That is structurally safer than any margin advantage and deserves saying explicitly.

Watch for a receivable spike in a peak-revenue year. It is usually timing rather than deterioration,
and it resolves the following year. Check the next year before calling it a problem.

---

## Liquidity and leverage

| Ratio | Orientation |
|---|---|
| Current ratio | 1.5–2.0 is comfortable for a manufacturer. Below 1 warrants attention. |
| Quick ratio | Excludes inventory. Matters where stock is slow-moving. |
| Debt / equity | Wide sector variation. Compare to a competitor rather than to a textbook range. |
| Interest coverage | EBIT / finance cost. Below 2 is uncomfortable. |
| DSCR | Cash available / debt service. Below 1 means the schedule cannot be met from operations. |

**Finance cost as a share of EBITDA** is worth computing and is not standard. It answers "how much
of what the business earns goes to lenders before anyone else sees it?" Above about a third is
heavy, and a falling trend is one of the clearest signs of genuine balance-sheet repair.

---

## Efficiency and capital productivity

| Measure | Formula | Reading |
|---|---|---|
| Revenue per ₹1 capital employed | revenue / (net worth + debt) | How hard capital turns over. |
| EBITDA per ₹1 capital employed | EBITDA / capital employed | The comparison figure for capital allocation. |
| Asset turnover | revenue / total assets | |
| Inventory turnover | cost of materials / inventories | |
| Receivables turnover | revenue / trade receivables | |

**Capital productivity is the right basis for comparing a business against an alternative use of the
same money** — a new venture, an acquisition, or simply repaying debt. Revenue per rupee and EBITDA
per rupee together tell you whether a business turns capital hard, converts it well, or neither.

Two cautions. **Accounting return is not IRR** — a going concern's ROCE and a project's projected
DCF IRR are different objects and must not be placed side by side without saying so. And where a
business is materially under-utilised, **the marginal return on more fixed assets is near zero**;
the useful figure is the return on the working capital needed to fill existing capacity.

---

## Benchmarking

Three sources, in descending order of usefulness:

1. **The company's own history.** Always available, always relevant, no comparability problem.
2. **A direct competitor's filed accounts.** For any Indian private limited company these are
   obtainable from the MCA portal. Both sets are declared under the same regime and face the same
   incentives, which makes the comparison more reliable than either absolute figure — see trap 7.
3. **Published industry ranges.** Orientation only. Most are drawn from listed or US data and
   mislead for an Indian SME.

Classify each ratio **strong / acceptable / weak** against whichever benchmark you used, and name
which one you used. A classification against an unstated benchmark is not information.

---

## Presenting

Ratios are the input to analysis, not the output. A table of twenty numbers with traffic lights
tells the reader nothing they can act on.

Lead with the two or three findings that would change a decision, support each with the specific
ratio and its trend, and put the full table below for reference. If nothing in the table would change
a decision, say that — it is a legitimate and useful finding.
