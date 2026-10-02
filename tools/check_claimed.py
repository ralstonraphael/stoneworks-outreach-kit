#!/usr/bin/env python3
"""Is this company already taken? Run before researching or emailing anyone.

Usage:
  python3 tools/check_claimed.py "Cedar Ridge Land Services"
  python3 tools/check_claimed.py "Cedar Ridge" --domain cedarridgeland.com
  python3 tools/check_claimed.py --file my_leads.txt        (one company per line, optional ",domain")
  python3 tools/check_claimed.py "Cedar Ridge" --csv team_claims_export.csv   (extra list, e.g. the shared sheet exported as CSV)

Checks the Claimed, Team Claims and Do Not Contact tabs of Claimed_Companies.xlsx
(needs openpyxl), falling back to tools/claimed_snapshot.csv if openpyxl is missing.
Matching is fuzzy on purpose: "Cedar Ridge Land Services, LLC" and "Cedar Ridge Land" match.
Exit code 0 = free, 1 = taken or possible match (skip or ask in the team chat).
"""
import argparse, csv, difflib, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
KIT = os.path.dirname(HERE)
XLSX = os.path.join(KIT, "Claimed_Companies.xlsx")
SNAP = os.path.join(HERE, "claimed_snapshot.csv")

SUFFIX = {"llc", "inc", "lp", "llp", "ltd", "co", "corp", "corporation", "company", "the", "pllc", "plc", "and"}
GENERIC = {"land", "lands", "services", "service", "resources", "resource", "energy", "management", "minerals",
           "mineral", "operating", "midstream", "petroleum", "exploration", "production", "group", "holdings",
           "partners", "consulting", "oil", "gas", "royalty", "royalties", "ii", "iii", "iv", "usa", "us"}


def norm(name):
    t = re.sub(r"[^a-z0-9 ]", " ", (name or "").lower().replace("&", " and "))
    return [w for w in t.split() if w not in SUFFIX]


def core(name):
    words = [w for w in norm(name) if w not in GENERIC]
    return " ".join(words) if words else " ".join(norm(name))


def clean_domain(d):
    d = re.sub(r"^https?://", "", (d or "").strip().lower())
    return re.sub(r"^www\.", "", d).split("/")[0]


def load():
    rows = []
    try:
        import openpyxl
        wb = openpyxl.load_workbook(XLSX, read_only=True, data_only=True)
        for r in list(wb["Claimed"].iter_rows(values_only=True))[1:]:
            if r[0]: rows.append((r[0], r[1] or "", f"{r[2]}: {r[3]}"))
        for r in list(wb["Team Claims"].iter_rows(values_only=True))[1:]:
            if r[0]: rows.append((r[0], r[1] or "", f"{r[2] or '?'} (Team Claims): {r[4] or ''}"))
        for r in list(wb["Do Not Contact"].iter_rows(values_only=True))[1:]:
            if r[0]: rows.append((r[0], "", f"DO NOT CONTACT: {r[1] or ''}"))
    except Exception as e:
        if not os.path.exists(SNAP):
            sys.exit(
                f"Could not read {XLSX} ({e}) and there is no snapshot CSV.\n"
                "The claimed-company list is private and not in the public repo. Download the live Google Sheet "
                "(link in MY_PROFILE.md) as .xlsx, save it in the kit folder as Claimed_Companies.xlsx, "
                "or export its Claimed and Team Claims tabs as CSV and pass them with --csv.")
        print(f"(reading snapshot CSV, openpyxl unavailable: {e.__class__.__name__})", file=sys.stderr)
        for r in csv.DictReader(open(SNAP)):
            rows.append((r["company"], r["domain"], f"{r['owner']}: {r['status']}"))
    return rows


def extra(path):
    out = []
    for r in csv.reader(open(path)):
        if r and r[0].strip() and r[0].lower() != "company":
            out.append((r[0], r[1] if len(r) > 1 else "", f"from {os.path.basename(path)}"))
    return out


def check(name, domain, rows):
    hits = []
    c, d = core(name), clean_domain(domain)
    for co, dom, who in rows:
        cc, dd = core(co), clean_domain(dom)
        why = None
        if d and dd and d == dd:
            why = "same domain"
        elif c and cc and c == cc:
            why = "same name"
        elif c and cc and (f" {c} " in f" {cc} " or f" {cc} " in f" {c} ") and min(len(c), len(cc)) >= 4:
            why = "name contains"
        elif c and cc and difflib.SequenceMatcher(None, c, cc).ratio() >= 0.88:
            why = "similar name"
        if why:
            hits.append((why, co, dom, who))
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("company", nargs="?")
    ap.add_argument("--domain", default="")
    ap.add_argument("--file")
    ap.add_argument("--csv", action="append", default=[])
    a = ap.parse_args()
    rows = load()
    for p in a.csv:
        rows += extra(p)
    todo = []
    if a.file:
        for line in open(a.file):
            parts = [x.strip() for x in line.split(",")]
            if parts and parts[0]:
                todo.append((parts[0], parts[1] if len(parts) > 1 else ""))
    if a.company:
        todo.append((a.company, a.domain))
    if not todo:
        ap.error("give a company name or --file")
    taken = 0
    for name, dom in todo:
        hits = check(name, dom, rows)
        if hits:
            taken += 1
            print(f"TAKEN  {name}")
            for why, co, d, who in hits[:5]:
                print(f"       {why}: {co} {('(' + d + ')') if d else ''} -> {who}")
        else:
            print(f"FREE   {name}  (claim it in Team Claims before you send)")
    sys.exit(1 if taken else 0)


if __name__ == "__main__":
    main()
