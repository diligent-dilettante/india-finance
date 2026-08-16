# Old versus new regime

**Verify before you compute.** The figures below are as understood for **FY 2025-26 /
AY 2026-27** and were written on 2026-08-16. Indian tax law changes at every Budget, and
a stale slab produces a confidently wrong number that someone may act on.

State the assessment year and the slabs you are using before showing any result, and ask
them to confirm. If they cannot, say the number is indicative and stop short of advice.

For anything beyond salary income, or for actually filing, hand off to
`shivprime94/file-itr` (MIT, well maintained) and recommend a CA.

## New regime — default since FY 2023-24

| Slab | Rate |
|---|---|
| up to ₹4,00,000 | nil |
| ₹4,00,001 – ₹8,00,000 | 5% |
| ₹8,00,001 – ₹12,00,000 | 10% |
| ₹12,00,001 – ₹16,00,000 | 15% |
| ₹16,00,001 – ₹20,00,000 | 20% |
| ₹20,00,001 – ₹24,00,000 | 25% |
| above ₹24,00,000 | 30% |

Standard deduction ₹75,000 for salaried. Rebate under 87A makes tax nil up to ₹12,00,000
of taxable income. Employer NPS contribution under 80CCD(2) is still allowed. Almost
nothing else is.

## Old regime

Basic exemption varies with age. The new regime does not.

| Slab | Under 60 | 60 and above | 80 and above |
|---|---|---|---|
| exemption limit | ₹2,50,000 | ₹3,00,000 | ₹5,00,000 |
| next band to ₹5,00,000 | 5% | 5% | nil |
| ₹5,00,001 – ₹10,00,000 | 20% | 20% | 20% |
| above ₹10,00,000 | 30% | 30% | 30% |

**Ask their age band before computing the old regime.** Getting this wrong overstates a
retired person's tax materially, and they are the group least able to absorb the error.

Standard deduction ₹50,000, and it applies to pension as well as salary. Rebate under
87A up to ₹5,00,000 taxable income.

Deductions available: 80C (₹1.5L), 80D, 80CCD(1B) (NPS, ₹50k), 24(b) (home loan
interest, ₹2L self-occupied), HRA, LTA, 80G, 80TTA/80TTB, 80E.

**80D has two limits, not one.** The taxpayer's own premium, and a separate additional
limit for premiums paid for parents, higher again when those parents are senior citizens.
People pay their parents' premiums and routinely fail to claim them. Ask.

**80TTA versus 80TTB.** Under 60, up to ₹10,000 of savings-account interest. At 60 and
above, 80TTB replaces it with up to ₹50,000 covering FD interest too. Retired people hold
large deposits, so this is not a rounding error.

## Both regimes

Surcharge on higher incomes, then health and education cess at 4% on tax plus surcharge.
The new regime caps surcharge at 25% against the old regime's 37%, which matters above
₹2Cr.

## The comparison

Do not reason about it. Compute both from their actual numbers and show the two totals
side by side with the difference.

The break-even intuition: the new regime wins unless deductions are large. For most
salaried people the old regime only wins when they are genuinely using 80C in full, plus
a home loan, plus real HRA. Someone paying rent in a metro with a home loan running often
still comes out ahead on old; someone with a fully-paid house and ₹1.5L of ELSS usually
does not.

**Compute, then say which wins and by how much.** Never assert a winner from the shape of
their situation.

## What the statements can and cannot tell you

**Can** — rent paid (for HRA), insurance premiums (80D), SIP into ELSS (80C), NPS
contributions, home loan EMI total, donations (80G), interest credited (80TTA).

**Cannot** — the principal-interest split on a home loan without the amortisation
schedule or the lender's certificate, employer PF, and anything already deducted at
source. Form 16 has these. Ask for it rather than estimating.

**Never estimate a deduction.** An inflated 80C claim is the taxpayer's liability, not
yours. If a number is unknown, leave it out and say the computation excludes it.

## Advance tax

Due 15 June (15%), 15 September (45%), 15 December (75%), 15 March (100%), cumulative.
Interest under 234B and 234C applies to shortfalls. Relevant here because someone with
foundry or consulting income alongside salary may owe advance tax and not know it —
worth flagging when non-salary income shows in the statements.

## Boundaries

Say this once, plainly, and then don't repeat it every message:

You are not a tax professional. The computation is arithmetic on numbers they supplied.
Capital gains, foreign income, business income, presumptive taxation and anything
involving a company all want a CA. Filing wants `file-itr` or a professional.
