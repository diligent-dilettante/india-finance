# Categorisation

## The taxonomy

Two levels. Deeper than this and nobody maintains it.

**Income** — salary, business, rental, interest, dividend, capital gains, reimbursement,
refund, gift, other

**Essential** — rent, EMI, utilities, groceries, transport-commute, insurance, medical,
education, domestic-help, phone-internet

**Discretionary** — dining, delivery, entertainment, shopping-clothing, shopping-goods,
travel, fitness, subscriptions, personal-care, gifts-given, hobbies

**Financial** — investment-equity, investment-debt, investment-gold, sip, tax-paid,
loan-principal, loan-interest, savings-transfer

**Internal** — card-payment, self-transfer, cash-withdrawal

**Unknown** — genuinely unidentified

## The Internal category is load-bearing

Everything tagged `internal` is excluded from both income and spend totals. Get this
wrong and the numbers become nonsense — moving ₹50,000 to your own savings account is
not spending, and paying a credit card bill is not a purchase on top of the purchases it
settles.

Three cases to catch:

**Card payments.** Bank debit to a card issuer. Match against the card statement where
you have it. Tag `internal/card-payment`.

**Self-transfers.** Between the person's own accounts. Detectable as a debit and credit
of the same amount within a day or two across two accounts they own. Needs the account
register to identify.

**Cash withdrawals.** `internal/cash-withdrawal` and not a spend category, because you
cannot see what the cash bought. If cash withdrawal is a large share of outflow, say so
plainly — it is a visibility hole in the analysis, not a category of spending.

## India-specific rules

**Salary is not always obvious.** Employers use their own narration strings. Anchor on
the pattern rather than the word: a large credit, monthly, on a similar date, from the
same counterparty. Confirm once, then it is stable.

**Reimbursements are not income.** They arrive from the same employer and look identical
to salary. If counted as income they inflate both income and savings rate. Usually
smaller, irregular, and often carry `REIMB` or an expense-report reference. Ask.

**SIP and NACH mandates** are `financial`, not spend. Someone whose SIPs land in
discretionary will be told they overspend when they are actually saving.

**EMIs split.** The principal portion is `financial/loan-principal`, the interest is
`essential/loan-interest`. Most statements show only the total; unless there is an
amortisation schedule, keep them as `essential/emi` and note the limitation rather than
inventing a split.

**Insurance premiums** are `essential/insurance` for term and health. ULIPs and
endowment policies are mostly `financial/investment-debt` and worth a comment, because
people rarely know the split.

**Gold** — physical, SGB or digital — is `financial/investment-gold`, and common enough
in Indian households to deserve its own line rather than sitting in shopping.

**Festival and wedding spending** is spiky and seasonal. Do not treat a Diwali or
wedding month as a trend break. Flag it as seasonal and compare like for like against the
same period last year where the data reaches back far enough.

## Matching strategy

Order matters. Cheapest and most certain first.

1. **Exact merchant match** against `categories.json`. Free, certain.
2. **VPA handle match** for UPI. More stable than display names.
3. **Narration prefix rules** — `NACH` plus a known AMC name is a SIP, `ATW` is a
   withdrawal.
4. **Fuzzy merchant match** against known mappings, with a high threshold. Ask on
   anything below it.
5. **Ask.** Batch all remaining unknowns into one question, grouped by merchant with the
   count and total for each. One pass, not one at a time.

Never assign a category on a guess you would not defend if asked. `unknown` is an honest
answer and the totals stay true.

## categories.json

```json
{
  "version": 1,
  "merchants": {
    "swiggy": "discretionary/delivery",
    "zomato": "discretionary/delivery",
    "bigbasket": "essential/groceries"
  },
  "vpa": {
    "swiggy@axisbank": "discretionary/delivery"
  },
  "rules": [
    { "match": "^NACH.*NIPPON", "category": "financial/sip" }
  ],
  "excluded_counterparties": ["HDFC CREDIT CARD", "ICICI CC PAYMENT"]
}
```

Write it after every session where something new was learned. It is what makes the second
run fast, and it is the single most valuable artifact this skill produces.

## When they disagree with a category

Take their word immediately and write it to the mappings. They know that "SHREE ENTERPRISES"
is their plumber and you do not. Do not argue, do not ask why, do not offer a competing
classification.
