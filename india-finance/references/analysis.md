# Analysis and advice

## What to compute

All of it via `scripts/analyse.py`. The script is the source of truth for every figure
that reaches the person.

**Monthly spine** — income, spend, savings, savings rate, per month across the window.
Everything else hangs off this.

**Category movement** — this month, trailing three-month average, trailing twelve where
available, and the delta. The delta is the story; the level rarely is.

**Movers** — largest increases and decreases in absolute rupees, not percentage. A 300%
rise on ₹200 is noise; a 15% rise on ₹40,000 is the thing worth their attention.

**Recurring detection** — cluster by merchant and amount, then look at the interval. A
merchant appearing monthly at roughly the same amount is a subscription or a bill, and
should be separated from one-off spend before any trend is read.

**Subscription audit** — every detected recurring discretionary charge, with annualised
cost. People consistently underestimate this. Show the annual figure, since ₹499 a month
reads as nothing and ₹5,988 a year does not.

**Only annualise what recurs.** Require a charge to land in at least three distinct
months before multiplying it out, and use the median month rather than the mean. Otherwise
a one-off annual invoice paid in a single month becomes twelve times itself and the total
is fiction. A ₹6,000 licence renewal charged once turns into ₹72,000 of imaginary
subscription cost, which is larger than most people's real subscription bill. List
the one-offs separately and say plainly that they are not subscriptions — a subscription
audit that inflates the number is worse than none, because the one real cancellation gets
lost among six imaginary ones.

Report the **first and last charge date** for each. A subscription whose last charge was
five months ago has already been cancelled or has lapsed, and belongs in the report as
history rather than as a saving still available.

**Card behaviour** — whether statements are cleared in full, and any interest or late fee
charged. Revolving credit at Indian card rates is the single most expensive thing most
people do with money, and it hides inside "card payment" as a category.

**Concentration** — share of discretionary spend in the top five merchants. Usually
surprising, and it makes a recommendation concrete because it names them.

**Cash visibility** — cash withdrawals as a share of outflow. Above roughly 10%, say
explicitly that the analysis has a blind spot that size. Do not model what the cash did.

## How to frame it

**Open with the delta, not the level.** They know roughly what they earn and spend. They
do not know what moved.

**Name the number and the driver together.** "Delivery averaged ₹18,400 a month over the
last six against ₹11,200 in the six before, and the entire increase sits in three apps"
is usable. "Your food spending has increased" is not.

**Separate the structural from the seasonal.** Diwali, weddings and travel produce spikes
that are not trends. Compare to the same period last year where the window allows;
otherwise mark it as seasonal and exclude it from the trend read.

**Check the rail before you call a movement behaviour.** A category that drops to zero
usually means the payments moved, not that they stopped: UPI Lite switched on, a new card,
a bill taken over by a spouse, a merchant changing its settlement route. The tell is
abruptness — genuine behaviour change is gradual, a rail change is a cliff, and a category
that ran every month for a year does not go to exactly zero on its own. Say which one it
was, and never publish a "biggest movers" list without checking the cliffs in it.

**Strip the one-offs before quoting a run-rate.** A wedding, a house move, a deposit or a
single foreign trip can dominate a year and tell you nothing about next month. Report the
headline honestly, then report it again with identified one-offs removed, and label which
is which. The second number is the one that predicts anything.

**Say when the data cannot answer.** Cash-heavy months, an unparsed statement, a missing
card — name the gap and its size rather than reporting around it.

## Recommendations

Three at most. A list of twelve gets none of them done.

Each one needs: the specific behaviour, the rupee value of changing it, and the first
concrete step. If you cannot put a number on it, it is an observation, not a
recommendation, and should be labelled as such.

**Rank by rupees, not by virtue.** A forgotten ₹1,200-a-month subscription bundle beats
a lecture about coffee, and it takes ten minutes to fix.

**Do not moralise.** Someone who spends a lot on eating out and knows it does not need
telling. Report it, size it, and move on. The moment this reads as judgement, they stop
opening the statements and the whole thing dies.

**Leave the tradeoffs to them.** "This is ₹22,000 a month, which is your entire equity
SIP" is the useful framing. Whether that is the wrong choice is not yours to decide.

## Quarterly review

The question nobody's tool asks: **did last quarter's recommendations change anything?**

Pull the prior report, take the three recommendations, and compute what actually happened
to those categories. Report it flatly, whichever way it went. A recommendation that was
ignored twice should either be dropped or re-examined, because the constraint is
something other than awareness.

## Tone

Flat and specific. No praise for a good savings rate, no concern about a bad month. The
same rule that governs a coaching conversation applies here for the same reason: the
moment the reporting sounds like judgement, the person starts managing the report instead
of the money.

Numbers, drivers, options. They decide.
