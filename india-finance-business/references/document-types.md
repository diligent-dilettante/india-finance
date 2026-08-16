# Document types

What each document an Indian company holds actually proves, what it cannot, and how much weight to
put on it. Establish provenance before analysis, because the same number carries different authority
depending on where it came from.

---

## The provenance ladder

Tag every year in the series with one of these. Carry the tag into the output.

| Tier | Document | Authority |
|---|---|---|
| 1 | **Audited financial statements** | Signed, UDIN, auditor's opinion. The reference figure. |
| 2 | **Provisional / unaudited statements** | Prepared by the auditor, not signed off. Usually close, occasionally revised at audit. |
| 3 | **Tally trial balance / P&L export** | Internal books. No provisions, no audit adjustments, and check the period. |
| 4 | **A number in a summary, deck or email** | Unverified. Trace it to one of the above before using it. |

A conclusion resting on tier 3 or 4 needs a hedge attached to it in the output. Saying "on the
unaudited trial balance" costs six words and prevents a misplaced decision.

---

## Audited financial statements

**Contains:** balance sheet, statement of profit & loss, cash flow, notes, significant accounting
policies, related-party disclosures, and the auditor's report.

**Format:** Schedule III of the Companies Act 2013. P&L lines read *revenue from operations · other
income · cost of materials consumed · changes in inventories · employee benefits expense · finance
costs · depreciation and amortisation · other expenses*. Not "revenue, COGS, opex" — if you
restructure into a generic format, anyone official has to rebuild it.

**Key checks:**
- **UDIN** — first two digits are the signing year. No UDIN means it isn't final.
- **Signature block** — auditor firm, FRN, membership number, place, date.
- **Comparative column** — every statement carries the prior year, so one document gives two years.
  This is the cheapest way to extend a series backwards.

**What it cannot tell you:** anything about the current year if it is more than a year old, and
nothing about cash position today. Audited accounts are a historical record with a long lag —
FY-end March, signed around September.

---

## Provisional / unaudited statements

Usually issued mid-year for a bank or a tender deadline. Same format, no UDIN, often stamped
"provisional".

Treat the figures as directionally right and subject to change. Depreciation, provisions and closing
stock are the lines most likely to move at audit, so PBT and PAT are the least stable numbers in the
document while revenue is usually reliable.

---

## Tally trial balance and P&L export

Internal accounting output. Extremely useful because it is current — often the only view of a recent
year — but it is not accounts.

**Read the period line first.** It prints the actual date range and it is frequently not a full year.

**What it gives you that audited statements don't:** ledger-level detail. Individual raw material
lines, specific customer advances, named director balances, conversion charges, individual expense
heads. When you need to know *what* something is rather than how big, the trial balance is where to
look.

**What to distrust:** anything requiring judgement. Depreciation is often a round number plugged in.
Closing stock may be a management estimate. Provisions are frequently absent entirely.

---

## Form 3CD — the tax audit report

Filed under s.44AB. The single most underused document in a company file, because it discloses
things that appear nowhere in the financial statements.

**Clause 23 (s.40A(2)(b))** — payments to specified persons. Directors, their relatives, and
associated enterprises, each with amount and nature of transaction. This names the group.

**Clause 31 (s.269SS / 269T)** — every loan or deposit accepted, and every repayment, above the
threshold. Lender name, PAN, address, amount taken, maximum outstanding during the year, and mode.
This is where inter-company funding becomes visible.

**Also useful:** clause 21 (inadmissible expenses), clause 26 (s.43B items — statutory dues paid and
unpaid), clause 34 (TDS compliance), and the quantitative details in clause 35 where applicable.

See `related-parties.md` for how to work it.

---

## Form 26AS / AIS

The tax credit statement. Lists every deductor who paid the company and deducted TDS.

**Use:** reverse-engineer customer billings. TDS ÷ applicable rate = amount billed. Identify the
section first — 2% under s.194C is a very different divisor from 0.1% under s.194Q.

**Also:** it names customers. A company that says it has no idea who its top payers were three years
ago has the answer in 26AS.

---

## GST returns

**GSTR-1** — outward supplies, invoice level. **GSTR-3B** — summary return.

**Use:** corroborate revenue. GST turnover and audited revenue from operations should reconcile
allowing for exempt supplies, exports and the excise transition. Revenue is the hardest figure in
the accounts to shape precisely because of this cross-check, which is why it carries more analytical
weight than margin.

Also gives monthly granularity, where the audited statements give only a year.

---

## Bank sanction letters and loan statements

**Sanction letter:** facility type, sanctioned limit, rate, tenor, security, covenants.
**Statement:** actual drawn and outstanding.

**These are different numbers** and conflating them is trap 10. A sanction is permission to borrow;
it tells you what a lender was willing to underwrite, which is itself useful information about how
the business is seen. It does not tell you what was spent.

---

## Udyam registration certificate

States the classification (micro / small / medium), the registration number, and the declared
investment and turnover. Determines eligibility for MSMED payment protection and public-procurement
benefits. See `msme.md`.

---

## Purchase orders and track-record schedules

Often maintained as a spreadsheet for tender pre-qualification: PO number, date, client, item,
material grade, value, quantity, weight.

**Analytically this is the richest document a manufacturing company has**, because it reveals
customer concentration, product mix, order size distribution and what the business genuinely
delivers — none of which appears in the financial statements.

Two things to check:
- **Is a copy of each PO actually on file?** A line in a spreadsheet is data; a PO document is
  evidence. The gap between them matters wherever proof is required.
- **When does it stop?** These schedules are built for a specific bid and then not maintained.
  A record ending three years ago is a documentation gap, not necessarily a gap in the work.

---

## What to ask for, in order

When someone says "I want to understand the business", ask for these rather than asking an open
question. Most people don't know what they have until they see the list.

1. Audited financial statements, last 3–5 years (each gives two years via the comparative column)
2. The most recent trial balance or provisional figures, for currency
3. Form 3CD for any year, if group structure or funding matters
4. Udyam certificate
5. Bank sanction letters
6. Purchase order or track-record schedule, for a manufacturing or project business
7. Competitor financials, if benchmarking — these are obtainable from the MCA portal for any Indian
   private limited company
