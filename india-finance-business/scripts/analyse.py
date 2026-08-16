#!/usr/bin/env python3
"""
Financial analysis for an Indian private company.

Input is a JSON file: one object per financial year, plus optional peers for
benchmarking. Every figure in the output is computed here, never by a model.

    python analyse.py company.json
    python analyse.py company.json --peers peers.json
    python analyse.py --template > company.json

Input schema (all amounts in rupees, all fields optional except year/revenue):

{
  "company": "Example Pvt Ltd",
  "years": [
    {
      "year": "FY24",
      "provenance": "audited",          audited | provisional | trial_balance
      "revenue": 300000000,             revenue from operations
      "other_income": 1200000,
      "ebitda": 20000000,
      "depreciation": 3200000,
      "finance_cost": 6800000,
      "pbt": 10000000,
      "pat": 7200000,
      "net_worth": 48000000,
      "borrowings": 64000000,
      "receivables": 128000000,
      "payables": 84000000,
      "inventory": 40000000,
      "materials": 205000000,           cost of materials consumed
      "total_assets": 216000000
    }
  ]
}
"""

import argparse, json, sys

RUPEE_CR = 1e7
TIERS = {"audited": "audited", "provisional": "PROVISIONAL", "trial_balance": "TRIAL BALANCE"}


def cr(x):
    return None if x is None else round(x / RUPEE_CR, 2)


def pct(num, den):
    if num is None or not den:
        return None
    return round(num / den * 100, 1)


def days(bal, flow):
    if bal is None or not flow:
        return None
    return round(bal / flow * 365)


def ratios(y):
    """Per-year ratios. Anything needing a market price is deliberately absent —
    an unlisted company has no price, so P/E, P/B, EV/EBITDA cannot be computed."""
    rev, eb = y.get("revenue"), y.get("ebitda")
    dep, fin = y.get("depreciation"), y.get("finance_cost")
    pat, nw = y.get("pat"), y.get("net_worth")
    debt, mat = y.get("borrowings"), y.get("materials")
    ce = (nw + debt) if (nw is not None and debt is not None) else None
    ebit = (eb - dep) if (eb is not None and dep is not None) else None

    r = {
        "ebitda_margin_pct": pct(eb, rev),
        "net_margin_pct": pct(pat, rev),
        "pat_plus_dep": (pat + dep) if (pat is not None and dep is not None) else None,
        "roce_pct": pct(ebit, ce),
        "roe_pct": pct(pat, nw),
        "roa_pct": pct(pat, y.get("total_assets")),
        "debt_equity": round(debt / nw, 2) if (debt is not None and nw) else None,
        "interest_cover": round(ebit / fin, 2) if (ebit is not None and fin) else None,
        "fin_cost_pct_of_ebitda": pct(fin, eb),
        "receivable_days": days(y.get("receivables"), rev),
        "inventory_days": days(y.get("inventory"), mat),
        "payable_days": days(y.get("payables"), mat),
        "revenue_per_rupee_ce": round(rev / ce, 2) if (rev and ce) else None,
        "ebitda_per_rupee_ce_pct": pct(eb, ce),
    }
    rd, idd, pd_ = r["receivable_days"], r["inventory_days"], r["payable_days"]
    r["cash_conversion_days"] = (rd + idd - pd_) if None not in (rd, idd, pd_) else None

    wc = None
    if None not in (y.get("receivables"), y.get("inventory"), y.get("payables")):
        wc = y["receivables"] + y["inventory"] - y["payables"]
    r["working_capital"] = wc
    r["growth_tax_pct_of_revenue"] = pct(wc, rev)
    return r


def series_table(years):
    out, prev = [], None
    for y in years:
        rev = y.get("revenue")
        row = {
            "year": y.get("year"),
            "provenance": TIERS.get(y.get("provenance", ""), y.get("provenance", "?")),
            "revenue_cr": cr(rev),
            "yoy_pct": round((rev / prev - 1) * 100, 1) if (prev and rev) else None,
            "ebitda_cr": cr(y.get("ebitda")),
            "ebitda_margin_pct": pct(y.get("ebitda"), rev),
            "pat_cr": cr(y.get("pat")),
            "pat_margin_pct": pct(y.get("pat"), rev),
        }
        r = ratios(y)
        row["pat_plus_dep_cr"] = cr(r["pat_plus_dep"])
        out.append(row)
        if rev:
            prev = rev
    return out


def shape(years):
    """Is the series a trend or a sawtooth? A single year from a lumpy order book
    is close to meaningless, so this decides whether averaging is required."""
    revs = [y["revenue"] for y in years if y.get("revenue")]
    if len(revs) < 3:
        return {"verdict": "too few years to judge"}
    moves = [(revs[i] / revs[i - 1] - 1) * 100 for i in range(1, len(revs))]
    swings = sum(1 for m in moves if abs(m) > 25)
    signs = sum(1 for i in range(1, len(moves)) if moves[i] * moves[i - 1] < 0)
    osc = swings >= 2 and signs >= 1
    return {
        "yoy_moves_pct": [round(m, 1) for m in moves],
        "large_moves_over_25pct": swings,
        "direction_reversals": signs,
        "verdict": "OSCILLATES — quote a multi-year average, never one year" if osc
                   else "reasonably trending",
        "last_3yr_avg_revenue_cr": round(sum(revs[-3:]) / 3 / RUPEE_CR, 2),
    }


def incremental_margin(years):
    """What the GROWTH earned, as distinct from the base. Highly endpoint-sensitive,
    so report the range across endpoints rather than a single number."""
    pts = [y for y in years if y.get("revenue") and y.get("ebitda")]
    if len(pts) < 2:
        return None
    base, out = pts[0], []
    for end in pts[1:]:
        dr = end["revenue"] - base["revenue"]
        de = end["ebitda"] - base["ebitda"]
        if dr:
            out.append({
                "from": base["year"], "to": end["year"],
                "revenue_growth_pct": round((end["revenue"] / base["revenue"] - 1) * 100, 1),
                "ebitda_growth_pct": round((end["ebitda"] / base["ebitda"] - 1) * 100, 1)
                                     if base["ebitda"] else None,
                "incremental_margin_pct": round(de / dr * 100, 1),
            })
    vals = [o["incremental_margin_pct"] for o in out]
    return {"base_year": base["year"],
            "base_ebitda_margin_pct": pct(base["ebitda"], base["revenue"]),
            "by_endpoint": out,
            "range_pct": [min(vals), max(vals)] if vals else None,
            "note": "Endpoint-sensitive. Quote the range, not one figure."}


def checks(years):
    """Structural validation. A figure failing one of these is misread —
    OCR errors that survive all of them are rare."""
    out = []
    for y in years:
        yr, msgs = y.get("year"), []
        eb, dep, fin, pbt = (y.get(k) for k in ("ebitda", "depreciation", "finance_cost", "pbt"))
        if None not in (eb, dep, fin, pbt):
            d = eb - dep - fin - pbt
            if abs(d) > max(1000, abs(pbt) * 0.01):
                msgs.append(f"EBITDA-dep-finance != PBT, off by Rs {d:,.0f}")
        nw, debt, ta = y.get("net_worth"), y.get("borrowings"), y.get("total_assets")
        if None not in (nw, debt, ta) and (nw + debt) > ta:
            msgs.append("net worth + borrowings exceeds total assets — check extraction")
        if y.get("provenance") not in TIERS:
            msgs.append(f"provenance '{y.get('provenance')}' not one of {list(TIERS)}")
        out.append({"year": yr, "issues": msgs or ["ok"]})
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", nargs="?", help="JSON file of company figures")
    ap.add_argument("--peers", help="JSON file of peer companies for benchmarking")
    ap.add_argument("--template", action="store_true", help="print a blank input template")
    a = ap.parse_args()

    if a.template:
        print(json.dumps({"company": "", "years": [{
            "year": "FY24", "provenance": "audited", "revenue": 0, "ebitda": 0,
            "depreciation": 0, "finance_cost": 0, "pbt": 0, "pat": 0, "net_worth": 0,
            "borrowings": 0, "receivables": 0, "payables": 0, "inventory": 0,
            "materials": 0, "total_assets": 0}]}, indent=2))
        return

    if not a.input:
        ap.error("give an input file, or --template")

    data = json.load(open(a.input, encoding="utf-8"))
    years = data.get("years", [])
    if not years:
        sys.exit("no years in input")

    result = {
        "company": data.get("company", ""),
        "validation": checks(years),
        "series": series_table(years),
        "series_shape": shape(years),
        "ratios_by_year": {y.get("year"): ratios(y) for y in years},
        "incremental_margin": incremental_margin(years),
        "note": ("Market-price ratios (P/E, P/B, EV/EBITDA) are omitted deliberately — "
                 "an unlisted company has no price. See references/ratios.md."),
    }

    if a.peers:
        peers = json.load(open(a.peers, encoding="utf-8"))
        result["peers"] = {
            p.get("company", f"peer{i}"): {"year": p.get("year"), **ratios(p)}
            for i, p in enumerate(peers.get("companies", []))
        }
        result["peer_note"] = ("Both sides declared under the same regime, so the RELATIVE gap is "
                              "more reliable than either absolute margin. See traps.md #7.")

    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
