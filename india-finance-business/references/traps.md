# Traps

Specific errors that produce wrong answers when reading Indian company accounts. Each one has cost
somebody real time. They are ordered roughly by how often they bite.

---

## 1. A trial balance is not audited accounts, and the period line proves it

Tally exports look authoritative and are frequently handed over as "the accounts". Two problems.

**They are unaudited.** Figures move between a trial balance and the signed statement — provisions,
depreciation and closing stock adjustments all land at audit. Differences of 10–20% in PAT are
routine.

**The period is often not a full year.** Tally prints the actual date range, and it is regularly
something like `1-Apr-2021 to 11-Mar-2022` — twenty days short. Anyone comparing that to a full-year
audited figure will report a decline that never happened.

**Always read the period line before using a Tally figure.** If it is short, say so and do not
annualise silently.

---

## 2. UDIN tells you the year the audit was signed

Every audited financial statement in India carries a UDIN. The first two digits are the year of
signing: `24XXXXXXBKHTYK7606` was signed in 2024, so it is the FY2023-24 audit.

This is the fastest provenance check available, and it settles arguments about which year a loose
PDF belongs to. An audit report with no UDIN, or a blank UDIN field, is a provisional or unaudited
document however it is labelled.

---

## 3. The CIN encodes incorporation year and state, and beats any other claim

`U26914AP1987PTC0XXXXX` decomposes as: `U` unlisted · `26914` industry code · `AP` Andhra Pradesh ·
**`1987` year of incorporation** · `PTC` private limited · a registration number.

When a company profile, a website or a summary claims a different founding year, the CIN wins. The
other figure is often the year the current works commenced or the year of a reconstitution.

---

## 4. Reserves movement equals PAT — use it as a free cross-check

Closing reserves minus opening reserves equals profit after tax, absent dividends, bonus issues or
prior-period adjustments.

This is enormously useful on OCR'd or badly scanned statements where the P&L is mangled but the
balance sheet is legible. If the movement matches the PAT you read, both are almost certainly right.
If it doesn't, find out why before proceeding — the gap is usually a dividend, and occasionally an
extraction error.

---

## 5. Pre-qualification and "turnover" packs are often bundled audited statements

Documents named things like *bidder turnover*, *PQ pack* or *credentials* are frequently not
certificates at all. They are several years of complete audited statements stapled together for a
tender submission.

**Open them before concluding a year is missing.** An entire audited year can be sitting inside a
file whose name suggests it holds nothing but a turnover figure.

---

## 6. Read PAT + depreciation on any business mid-capex

A company that has just bought plant will show depreciation stepping up sharply, which depresses
PAT without touching cash. Reading PAT alone produces the conclusion "profit is flat" about a
business whose cash generation is growing strongly.

Compute **PAT + depreciation** across the series alongside PAT. If revenue is up 130% and PAT is up 50%,
but PAT + depreciation is up 140%, the business is performing fine and the depreciation charge
is doing the work.

The same logic explains apparently terrible years: a business can see revenue fall by a third while
cash generation holds flat, which is a sign of a genuinely variable cost base rather than distress.

---

## 7. Compare declared-to-declared across companies rather than judging one company's margin

Reported margins in owner-managed private companies reflect accounting policy and tax planning as
well as trading. That makes an absolute margin, and a margin *trend* over years, weaker evidence
than it appears — the basis may not be constant.

What survives is the **relative** comparison. Two companies in the same sector, both filing under
the same regime, both facing the same incentives: the gap between their declared margins is
meaningful even if neither absolute level is. A competitor earning three times your net margin on the same
basis is telling you something real.

Prefer figures that are harder to shape: revenue (corroborated by GST filings), balance sheet items,
the fixed asset register, and physical measures like capacity and utilisation.

---

## 8. Form 26AS reverse-engineers what a counterparty billed

Form 26AS lists tax deducted at source by everyone who paid the company. Divide the TDS by the
applicable rate and you recover the amount billed.

At 2% under s.194C (contracts and job work), TDS of ₹40,000 implies ₹20 L billed. At 0.1%
under s.194Q (purchase of goods) the same TDS implies a far larger figure — so **identify the
section before dividing**, and treat the result as an estimate. Cross-check it against a known
figure where one exists.

This is often the only way to size a relationship with a related party or a customer whose invoices
you cannot see.

---

## 9. Form 3CD schedules reveal inter-company funding the P&L hides

The tax audit report is the most underused document in an Indian company's file. Two schedules matter:

- **Clause 23, s.40A(2)(b)** — payments to specified persons: directors, relatives, associated
  enterprises, with amounts and the nature of each transaction.
- **Clause 31, s.269SS / 269T** — every loan or deposit accepted and repaid above the threshold,
  with the lender's name, PAN, amount and the maximum outstanding during the year.

A sister company appearing repeatedly in clause 31 with rising amounts is functioning as a
working-capital line. That will not be obvious anywhere in the P&L, and it is usually unsecured and
uncommitted — a real concentration risk that no ratio captures.

---

## 10. A sanction is not an asset

A bank sanction letter and an installed asset are different numbers, and they are routinely
conflated. A ₹3 Cr term-loan sanction against a ₹1.25 Cr installation is a normal outcome: the
facility was sized generously, part was drawn, and the undrawn balance was cancelled.

When someone quotes a project size, establish whether it is the sanction, the contract value, the
drawn amount or the capitalised asset. Ask which, rather than assuming.

---

## 11. Never quote a single year from a lumpy order book

Project and tender businesses are driven by a handful of large orders. Year-on-year moves of −35%
followed by +65% are normal and say nothing about underlying health.

Check the series shape first. If it oscillates, quote a three-year average and say why. A single
year from such a business is close to meaningless, and quoting the good one invites an obvious
question from anyone holding the accounts.

The usual cause is customer concentration — check it before diagnosing anything else.

---

## 12. Pre-GST and post-GST revenue need care to compare

Before July 2017, excise duty was often included in gross revenue and shown as a deduction. Use
**revenue net of excise** for any series spanning the transition, or the pre-GST years will look
inflated.

Similarly, a Tally "Sales" figure may or may not include GST depending on how the ledger is set up.
Reconcile it against the audited "revenue from operations" for any overlapping year before trusting
the standalone figure.

---

## 13. OCR at 300 DPI, and validate every figure structurally

Scanned statements are common. Rasterise at 300 DPI before OCR — lower resolution silently
transposes digits, which is worse than failing outright.

Then validate structurally rather than by eye:

- Does the balance sheet balance?
- Does reserves movement equal PAT? (trap 4)
- Do the expense lines sum to total expenses?
- Does EBITDA − depreciation − finance cost equal PBT?

Any figure that fails one of these is misread. OCR errors that survive all four are rare.

---

## 14. Ratio benchmarks published for listed companies mislead for an SME

Most benchmark tables circulating online are drawn from listed or US company data. An Indian SME
operates with different working capital norms, different gearing, and different margin structures.

Treat published "ideal" ranges as orientation, not as a verdict, and say so in the output. The most
useful benchmark is almost always the same company's own history plus a direct competitor.
