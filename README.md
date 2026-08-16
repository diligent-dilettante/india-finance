# India Finance

**A free, open-source Claude skill that reads your Indian bank and credit card statements, tells you where the money actually went, and compares the old and new tax regimes on your real numbers.** Every figure is computed in Python, never guessed by a model. Nothing leaves your machine.

MIT licensed. Works in Claude Code, Claude Desktop and Claude.ai.


## Two skills in this repo

| Skill | Scope |
|---|---|
| [`india-finance/`](india-finance/) | **One person's own money.** Bank and card statements, spending and income trends, assets, allocation and liquidity, goals, borrowing against holdings, old vs new tax regime. |
| [`india-finance-business/`](india-finance-business/) | **An Indian private company or MSME.** Audited statements, Tally trial balances, Form 3CD and scanned PDFs into a provenance-tagged series; working capital, capital productivity, MSME/Udyam status, related-party and inter-company funding. |

They are separate skills with separate scopes — install either or both. Neither reads the other's
data. Every figure in both comes from Python rather than from the model.


## What it does

Point it at your statements. PDF, CSV or Excel, bank accounts and credit cards, as many as you have.

It parses them, categorises the transactions, asks about the ones it cannot identify, and then reports what changed. Not a table of this month's spending, which you can already guess. The delta, the outlier, and the thing you had forgotten you were paying for.

Recommendations come with a rupee figure attached. "Reduce dining out" is not advice. "Delivery averaged ₹18,400 a month over the last six against ₹11,200 in the six before, and the whole increase sits in three apps" is advice, because it names the thing and the number.

## Why the arithmetic is in Python

A language model doing mental maths on your savings rate will be wrong occasionally and confident always, and you will act on it. So the model parses and interprets; `scripts/analyse.py` computes. Standard library only, nothing to install.

## Built for Indian statements

The parsing is where most tools quietly break, because Indian formats differ from the ones they were written for.

Separate debit and credit columns rather than one signed amount. `DD/MM/YYYY` dates, which a US-defaulting parser silently reads month-first and mis-buckets a quarter of the year. Lakh-crore digit grouping. UPI narrations that bury the counterparty behind an aggregator handle. Credit card statements where the sign convention inverts, so a naive merge books every card purchase as income.

It also refuses to proceed on a ledger that does not reconcile against the statement's own running balance. A spending analysis missing four percent of transactions is worse than useless, because it looks complete.

## Tax

Old regime against new, computed from your actual numbers rather than reasoned about, with both totals shown side by side.

The slabs are dated in `references/tax-regimes.md` and the skill verifies them with you before computing, because Indian tax law changes at every Budget and a stale slab produces a confidently wrong number.

For planning, use this. For actually filing an ITR, use [shivprime94/file-itr](https://github.com/shivprime94/file-itr), which is purpose-built for it and parses Form 16, AIS and 26AS. Anything with capital gains, foreign income or business income wants a CA.

## Privacy

Local only. No uploads, no web calls carrying transaction data, no writing balances into any shared store.

It never records a full account or card number. Last four digits identify an account for a human perfectly well.

## Install

Copy the `india-finance` folder into `~/.claude/skills/`. On Claude web, upload it as a skill or drop it into a project.

Then say what you want:

- *"here are my statements, where did my money go last quarter"*
- *"am I saving enough"*
- *"which tax regime should I be on"*
- *"what changed in my spending this month"*

First run takes about 45 minutes, mostly categorising. It saves what it learns, so later runs take ten.

## What is in it

```
SKILL.md                          the method
references/
  indian-statements.md            parsing, column conventions, the traps
  categorisation.md               taxonomy and the internal-transfer rules
  tax-regimes.md                  old vs new, dated and verifiable
  analysis.md                     what to compute, how to frame it
scripts/
  analyse.py                      the deterministic engine
```

## What it will not do

It will not moralise. Someone who spends a lot on eating out already knows. Reporting it, sizing it and moving on is the job; the moment this reads as judgement, people stop opening their statements and the whole thing dies.

It is not a budgeting app, not a net worth dashboard, and not investment advice. It reads what happened and tells you what it means.

## Related

[business-planner](https://github.com/diligent-dilettante/business-planner) for stress-testing a business idea. [life-planning](https://github.com/diligent-dilettante/life-planning) for values, goals and a weekly check-in.
