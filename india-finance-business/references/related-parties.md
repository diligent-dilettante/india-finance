# Related parties and inter-company funding

Group companies fund and trade with each other in ways the financial statements do not show. The
statutory schedules do show it, and reading them is the difference between analysing a company and
analysing a company-shaped fragment of a group.

This matters because inter-company funding is typically **unsecured, uncommitted and undocumented as
a facility**. It behaves like working capital until the day it doesn't, and no standard ratio
captures it.

---

## Where the disclosures live

### Financial statements — related-party note

Under AS-18 / Ind AS 24, the notes list related parties by relationship (associate, key management
personnel, enterprises under common control) and disclose transactions and closing balances.

Useful for **naming** the group. Often thin on amounts, and frequently aggregated.

### Form 3CD clause 23 — payments to specified persons, s.40A(2)(b)

Lists payments made by the company to directors, their relatives and associated enterprises, with
**amount and nature of transaction**.

This is directional: payments *out*. A line reading `ASSOCIATE ENTERPRISE · 1,20,00,000 · INTER
COMPANY` tells you ₹1.2 Cr left the company to a sister entity that year.

### Form 3CD clause 31 — loans accepted and repaid, s.269SS / 269T

The richest schedule. For every loan or deposit above the threshold:

- Name, address and PAN of the lender
- **Amount taken or accepted during the year**
- **Maximum amount outstanding at any time during the year**
- Whether repaid, and the mode

Track this across three or more years and the funding structure becomes visible. A sister company
appearing every year with rising amounts taken is a rolling credit line, not a one-off loan.

### Form 26AS — money coming in

Lists deductors who paid the company and deducted TDS. A related party appearing here is paying the
company, which is the other direction from clause 23.

---

## Technique: sizing a relationship from TDS

Divide TDS by the applicable rate to recover the amount billed.

```
TDS ₹50,000 ÷ 2% (s.194C, contracts / job work) = ₹25 L billed
```

**Identify the section first.** Common rates:

| Section | Applies to | Rate |
|---|---|---|
| 194C | Contracts, job work | 1% individual / 2% company |
| 194J | Professional or technical services | 10% (2% for certain technical) |
| 194Q | Purchase of goods above threshold | 0.1% |
| 194H | Commission, brokerage | 5% |

A 2% assumption applied to a 194Q deduction understates the counterparty by a factor of twenty. Where
the section is not stated, cross-check the derived figure against a known number — a conversion-charge
line in the trial balance, or a disclosed related-party transaction — before relying on it.

Rates change; verify before computing.

---

## Building the group picture

Work through this sequence. Each step uses documents the company already has.

1. **Name the entities.** Related-party note plus clause 23. Record PAN for each — it disambiguates
   entities with similar names and confirms the type (the fourth character of a PAN is `C` for
   company, `F` for firm, `P` for individual).
2. **Map addresses.** Entities sharing an address are usually sharing more than an address —
   premises, plant, sometimes staff. Note that highway and area names get renumbered over time, so
   apparently different addresses can be the same site.
3. **Trace funding across years** from clause 31. Amount taken and maximum outstanding, per lender,
   per year. Compare the total to the company's disclosed external borrowings — if a sister company's
   line is a material fraction of total debt, that is a concentration risk to state explicitly.
4. **Trace trade both ways.** Clause 23 for payments out, 26AS for receipts in. Roughly balanced
   two-way conversion work means shared capacity. One-way and growing usually means something else.
5. **Get the other entities' accounts** if the group total matters. For any Indian private limited
   company these are filed with the MCA and obtainable from the portal.

---

## What to do with it

**Size the dependency.** If a related party provides funding comparable to the company's bank
facilities, the company is more leveraged than its own balance sheet suggests, and on terms nobody
has documented.

**Check whether the group total changes the picture.** A revenue or capability claim that does not
reconcile to one entity often reconciles to the group. That is a labelling problem rather than a
false claim, but it needs establishing before the figure is used anywhere it will be checked.

**Ask how capital is deliberately arranged.** Groups often concentrate assets, borrowing and
invoicing in one entity on purpose — to keep a single balance sheet strong for pre-qualification or
credit. If so, the smaller entities will look thin by design and reading them in isolation misleads.
Ask rather than infer.

**Flag competing claims on the same money.** Where a family or group balance sheet funds several
businesses, they compete in the same bad year. Model the downside for all of them simultaneously,
not each on its own — that is the scenario nobody runs and the one that actually bites.

---

## A caution

Related-party analysis reads like an accusation if written carelessly. It usually isn't one:
inter-company funding, shared premises and group-level capital planning are ordinary and legitimate
in Indian family businesses.

Write it as structure and dependency, not as suspicion. The analytical point is that the company
cannot be understood alone — not that anything is being concealed.
