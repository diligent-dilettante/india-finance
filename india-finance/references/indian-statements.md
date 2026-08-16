# Parsing Indian bank and card statements

The traps here cost more time than the parsing itself.

## The structural difference

Most Western statement formats carry a single signed `Amount` column. **Indian bank
statements almost always carry separate `Withdrawal`/`Debit` and `Deposit`/`Credit`
columns**, one of which is blank per row. Normalise to a signed amount early: debit
negative, credit positive. Getting this wrong flips the sign on half the ledger and the
totals still look plausible, which is why it survives review.

## Column names by convention

Names vary per bank and per export path. Map, never assume.

| Meaning | Names seen |
|---|---|
| Date | `Txn Date`, `Transaction Date`, `Date`, `Value Date`, `Tran Date` |
| Description | `Narration`, `Description`, `Particulars`, `Transaction Remarks`, `Details` |
| Debit | `Withdrawal Amt.`, `Debit`, `Withdrawal (Dr)`, `Dr` |
| Credit | `Deposit Amt.`, `Credit`, `Deposit (Cr)`, `Cr` |
| Balance | `Closing Balance`, `Balance`, `Running Balance` |
| Reference | `Chq./Ref.No.`, `Ref No`, `Cheque Number`, `UTR` |

**Value date versus transaction date.** They differ, sometimes across a month boundary.
Use transaction date for spending analysis; value date matters only for interest.

## Dates

`DD/MM/YYYY` and `DD-MM-YY` dominate. Never let a parser infer month-first — `03/04/2026`
is 3 April in India and 4 March to a US-defaulting parser. Set `dayfirst=True` explicitly
and assert on it. This single bug will silently mis-bucket a quarter of the year.

## Amounts

- Indian digit grouping: `1,23,456.78` is one lakh twenty-three thousand. A naive
  thousands-separator strip handles it, but a locale-aware parse does not.
- Some exports carry a trailing `Cr` or `Dr` on the amount itself.
- Negatives occasionally appear as `(1,234.00)`.
- Watch for a stray `₹` or `INR` prefix inside the cell.

## Credit card statements

Different enough to deserve their own path.

**Sign convention is usually inverted.** On a card statement a purchase is a positive
number and a payment or refund is negative or marked `Cr`. If you normalise cards the
same way as bank accounts, every card spend lands as income. Detect the statement type
first.

**Never double-count the payment.** The bank statement shows a debit for the card
payment; the card statement shows the individual purchases those settle. Count one or the
other, not both. Convention: count the card's purchases as the spend, and tag the bank's
card payment as an internal transfer excluded from spend totals.

**Statement period is not a calendar month.** Cards cycle on a billing date. Bucket card
transactions by transaction date, not statement, or month-on-month comparisons drift.

## UPI, the hard part

UPI narrations bury the counterparty and the format is inconsistent:

```
UPI/DR/412345678901/JOHN DOE/HDFC/johndoe@okhdfcbank/Payment from ph
UPI/512345678901/Paytm-12345/PYTM/paytmqr@paytm/UPI
```

Extract the payee name and the VPA handle where present. The handle is usually a better
category key than the display name, since merchants keep a stable VPA and change their
display string.

**Aggregator handles hide the real merchant.** Anything routing through Paytm, PhonePe,
BharatPe or a Razorpay QR shows the aggregator, not the shop. These need either a
user-supplied mapping or an honest "unknown merchant" bucket. Do not invent a merchant.

## Other narration prefixes

| Prefix | Means |
|---|---|
| `NEFT`, `RTGS`, `IMPS` | interbank transfer; counterparty usually present |
| `ACH`, `NACH` | mandated recurring debit — SIP, EMI, insurance |
| `ATW`, `ATM`, `NWD` | cash withdrawal |
| `POS`, `ECOM` | card transaction, merchant usually readable |
| `SI`, `ECS` | standing instruction |
| `CHRG`, `GST` | bank fees; small, recurring, worth surfacing |
| `INT.PD`, `CREDIT INTEREST` | interest credited |
| `SAL`, `SALARY` | salary credit, though many employers use their own string |

## PDF extraction

`pdfplumber` handles most Indian e-statements better than `pypdf` because it preserves
table structure. Fall back to `extract_words` with positional clustering when
`extract_table` returns nothing usable.

**Password-protected PDFs are the norm**, not the exception — usually PAN plus date of
birth in some order, or customer ID. Ask for the password; never try to crack it.

Multi-page statements repeat headers per page. Strip repeated header rows or they enter
the ledger as junk transactions.

## The reconciliation check that catches everything

After parsing, verify the arithmetic against the statement's own running balance:

```
opening_balance + sum(signed_amounts) == closing_balance
```

If it does not reconcile to the rupee, something was dropped, duplicated or sign-flipped.
Report the discrepancy and its size. Do not proceed to analysis on a ledger that does not
balance, and do not quietly plug the difference.
