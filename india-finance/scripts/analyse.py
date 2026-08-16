#!/usr/bin/env python3
"""Deterministic analysis over a normalised transaction ledger.

Every figure the skill reports should come from here. Standard library only.

Input: a CSV with at least these columns.
    date        ISO YYYY-MM-DD
    amount      signed rupees. negative = money out, positive = money in
    description raw narration
    merchant    cleaned counterparty (may be blank)
    category    "group/subcategory", e.g. discretionary/delivery
    account     account or card identifier (last 4 is enough)

Rows whose category group is "internal" are excluded from income and spend
totals but still reported, because card payments and self-transfers are not
spending and counting them makes every ratio wrong.

Usage:
    python analyse.py transactions.csv                 full report
    python analyse.py transactions.csv --json          machine-readable
    python analyse.py transactions.csv --months 6      limit the window
"""

import argparse
import csv
import json
import sys
from collections import defaultdict
from datetime import date, datetime
from statistics import median


def rupees(n):
    """Indian digit grouping: 1,23,456.78"""
    neg = n < 0
    n = abs(round(n))
    s = str(n)
    if len(s) > 3:
        head, tail = s[:-3], s[-3:]
        parts = []
        while len(head) > 2:
            parts.insert(0, head[-2:])
            head = head[:-2]
        if head:
            parts.insert(0, head)
        s = ",".join(parts) + "," + tail
    return ("-" if neg else "") + "₹" + s


def load(path):
    """Returns (rows, stats). stats carries the parse gap into the report,
    because a dropped row that only warns on stderr is a dropped row nobody
    sees when output is piped."""
    rows = []
    stats = {"seen": 0, "skipped": 0, "reasons": []}
    with open(path, newline="", encoding="utf-8-sig") as f:
        for i, r in enumerate(csv.DictReader(f), start=2):
            stats["seen"] += 1
            try:
                d = datetime.strptime(r["date"].strip(), "%Y-%m-%d").date()
                amt = float(str(r["amount"]).replace(",", "").replace("₹", "").strip())
            except (ValueError, KeyError, AttributeError) as e:
                stats["skipped"] += 1
                if len(stats["reasons"]) < 5:
                    stats["reasons"].append(f"row {i}: {e}")
                print(f"  ! row {i} unparseable, skipped: {e}", file=sys.stderr)
                continue
            cat = (r.get("category") or "unknown/unknown").strip().lower()
            group = cat.split("/")[0]
            rows.append({
                "date": d, "month": d.strftime("%Y-%m"), "amount": amt,
                "description": (r.get("description") or "").strip(),
                "merchant": (r.get("merchant") or "").strip().lower(),
                "category": cat, "group": group,
                "account": (r.get("account") or "").strip(),
            })
    return rows, stats


def monthly_spine(rows):
    """Spend excludes the `financial` group. A SIP, a tax payment or a refundable
    deposit is money leaving the account, but it is not consumption, and folding
    it into spend understates the savings rate by exactly the amount being saved.
    Financial outflow is reported on its own line instead."""
    m = defaultdict(lambda: {"income": 0.0, "spend": 0.0, "internal": 0.0,
                             "financial": 0.0})
    for r in rows:
        if r["group"] == "internal":
            m[r["month"]]["internal"] += abs(r["amount"])
        elif r["amount"] > 0:
            m[r["month"]]["income"] += r["amount"]
        elif r["group"] == "financial":
            m[r["month"]]["financial"] += -r["amount"]
        else:
            m[r["month"]]["spend"] += -r["amount"]
    out = []
    for month in sorted(m):
        v = m[month]
        saved = v["income"] - v["spend"]
        out.append({
            "month": month, "income": v["income"], "spend": v["spend"],
            "financial": v["financial"], "saved": saved,
            "savings_rate": (saved / v["income"] * 100) if v["income"] else None,
            "internal": v["internal"],
        })
    return out


def category_movement(rows, months):
    """Latest month against the trailing average of the preceding months."""
    if len(months) < 2:
        return []
    latest, prior = months[-1], months[:-1]
    cur = defaultdict(float)
    hist = defaultdict(float)
    for r in rows:
        if r["group"] in ("internal", "income"):
            continue
        if r["amount"] >= 0:
            continue
        if r["month"] == latest:
            cur[r["category"]] += -r["amount"]
        elif r["month"] in prior:
            hist[r["category"]] += -r["amount"]
    n = len(prior)
    out = []
    for cat in set(cur) | set(hist):
        avg = hist[cat] / n
        out.append({
            "category": cat, "current": cur[cat], "trailing_avg": avg,
            "delta": cur[cat] - avg,
        })
    return sorted(out, key=lambda x: -abs(x["delta"]))


def recurring(rows, min_hits=3, tol=0.12):
    """Merchant + amount clusters appearing at a regular interval."""
    by_merchant = defaultdict(list)
    for r in rows:
        if r["group"] == "internal" or r["amount"] >= 0:
            continue
        key = r["merchant"] or r["description"][:28].lower()
        if key:
            by_merchant[key].append(r)
    found = []
    for merchant, txns in by_merchant.items():
        if len(txns) < min_hits:
            continue
        amounts = sorted(abs(t["amount"]) for t in txns)
        mid = median(amounts)
        if mid == 0:
            continue
        close = [a for a in amounts if abs(a - mid) / mid <= tol]
        if len(close) < min_hits:
            continue
        dates = sorted(t["date"] for t in txns)
        gaps = [(b - a).days for a, b in zip(dates, dates[1:])]
        if not gaps:
            continue
        typical = median(gaps)
        if not (25 <= typical <= 35 or 6 <= typical <= 8 or 88 <= typical <= 95):
            continue
        per_year = 365.0 / typical
        found.append({
            "merchant": merchant, "typical_amount": mid, "hits": len(close),
            "interval_days": typical, "annualised": mid * per_year,
            "category": txns[-1]["category"],
        })
    return sorted(found, key=lambda x: -x["annualised"])


def concentration(rows, months, top=5):
    latest = months[-1] if months else None
    spend = defaultdict(float)
    for r in rows:
        if r["group"] != "discretionary" or r["amount"] >= 0 or r["month"] != latest:
            continue
        spend[r["merchant"] or r["description"][:28].lower()] += -r["amount"]
    total = sum(spend.values())
    ranked = sorted(spend.items(), key=lambda kv: -kv[1])[:top]
    return {
        "month": latest, "total_discretionary": total,
        "top": [{"merchant": m, "amount": a,
                 "share": (a / total * 100) if total else 0} for m, a in ranked],
        "top_share": (sum(a for _, a in ranked) / total * 100) if total else 0,
    }


def cash_visibility(rows, months):
    latest = months[-1] if months else None
    cash = outflow = 0.0
    for r in rows:
        if r["month"] != latest or r["amount"] >= 0:
            continue
        if r["category"] == "internal/cash-withdrawal":
            cash += -r["amount"]
        elif r["group"] != "internal":
            outflow += -r["amount"]
    denom = cash + outflow
    return {"cash": cash, "visible_spend": outflow,
            "blind_share": (cash / denom * 100) if denom else 0}


def report(rows, stats=None, window=None):
    months = sorted({r["month"] for r in rows})
    if window:
        months = months[-window:]
        rows = [r for r in rows if r["month"] in months]
    spine = monthly_spine(rows)
    return {
        "window": {"from": months[0] if months else None,
                   "to": months[-1] if months else None,
                   "months": len(months), "transactions": len(rows)},
        "parse": stats or {},
        "monthly": spine,
        "movement": category_movement(rows, months),
        "recurring": recurring(rows),
        "concentration": concentration(rows, months),
        "cash": cash_visibility(rows, months),
    }


def render(rep):
    w = rep["window"]
    ps = rep.get("parse") or {}
    L = []
    L.append(f"Window: {w['from']} to {w['to']}  ({w['months']} months, {w['transactions']} transactions)")
    if ps.get("skipped"):
        L.append(f"!! {ps['skipped']} of {ps['seen']} rows could not be parsed and are NOT in these totals.")
        for r in ps.get("reasons", []):
            L.append(f"     {r}")
        L.append("   Fix the source rows before trusting any figure below.")
    if w["months"] < 2:
        L.append("   Single month: no trend or movement analysis possible.")
    L.append("")
    L.append("MONTHLY")
    L.append(f"  {'month':<9} {'income':>13} {'spend':>13} {'invested':>13} "
             f"{'saved':>13} {'rate':>7}")
    for m in rep["monthly"]:
        rate = f"{m['savings_rate']:.0f}%" if m["savings_rate"] is not None else "n/a"
        L.append(f"  {m['month']:<9} {rupees(m['income']):>13} {rupees(m['spend']):>13} "
                 f"{rupees(m.get('financial', 0)):>13} "
                 f"{rupees(m['saved']):>13} {rate:>7}")

    mv = [m for m in rep["movement"] if abs(m["delta"]) >= 500][:8]
    if mv:
        L.append("")
        L.append("BIGGEST MOVERS  (latest month vs trailing average)")
        for m in mv:
            arrow = "up  " if m["delta"] > 0 else "down"
            L.append(f"  {arrow} {rupees(abs(m['delta'])):>11}   {m['category']:<32} "
                     f"{rupees(m['current'])} vs {rupees(m['trailing_avg'])}")

    rec = rep["recurring"][:10]
    if rec:
        L.append("")
        L.append("RECURRING  (annualised)")
        for r in rec:
            L.append(f"  {rupees(r['annualised']):>11}/yr   {r['merchant'][:34]:<34} "
                     f"{rupees(r['typical_amount'])} every ~{r['interval_days']:.0f}d")

    c = rep["concentration"]
    if c["top"]:
        L.append("")
        L.append(f"CONCENTRATION  ({c['month']}, discretionary {rupees(c['total_discretionary'])})")
        for t in c["top"]:
            L.append(f"  {t['share']:>5.1f}%  {rupees(t['amount']):>11}   {t['merchant'][:40]}")
        L.append(f"  top {len(c['top'])} = {c['top_share']:.1f}% of discretionary spend")

    cash = rep["cash"]
    if cash["blind_share"] > 10:
        L.append("")
        L.append(f"BLIND SPOT: {rupees(cash['cash'])} withdrawn as cash, "
                 f"{cash['blind_share']:.0f}% of outflow. That spending is not visible here.")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--months", type=int, default=None)
    a = ap.parse_args()
    rows, stats = load(a.csv)
    if not rows:
        print("No parseable transactions.", file=sys.stderr)
        return 1
    rep = report(rows, stats, a.months)
    print(json.dumps(rep, indent=2, default=str) if a.json else render(rep))
    return 0


if __name__ == "__main__":
    sys.exit(main())
