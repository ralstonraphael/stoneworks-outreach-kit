#!/usr/bin/env python3
"""Measure a cold email draft against response-rate benchmarks.

Usage:
    python3 check_email.py draft.txt
    cat draft.txt | python3 check_email.py
    python3 check_email.py --subject "aapl salt lake" draft.txt
"""
import argparse, re, sys

BANNED = [
    "i hope this finds you well", "i hope this email finds you", "i wanted to reach out",
    "circling back", "touching base", "just following up", "per my last email",
    "synergy", "synergies", "game-changer", "game changer", "revolutioniz",
    "cutting-edge", "best-in-class", "world-class", "passionate about",
    "in today's fast-paced", "at the end of the day", "low-hanging fruit",
    "move the needle", "boil the ocean", "i'm not trying to sell",
    "not trying to sell you", "quick question for you", "hope you're doing well",
    "i trust this message", "delve", "it's not just", "not just a", "but rather",
]
MEETING_ASK = [
    r"\b\d+\s*(?:-|\s)?minute", r"\bdo you have (?:some )?time\b", r"\bbook (?:a|some) time\b",
    r"\bcalendly\b", r"\bgrab (?:15|20|30)\b", r"\bschedule a call\b",
    r"\bare you (?:free|available)\b", r"\bwhat does your calendar\b",
]
INTEREST_ASK = [
    r"worth a (?:\w+ )?(?:conversation|chat|call|look|reply)", r"\bcurious\??$", r"open to\b",
    r"want me to send", r"should i send", r"interested\??", r"is (?:this|that) a (?:real )?problem",
    r"who (?:owns|handles|runs)\b", r"am i off\b", r"does (?:this|that) sound",
    r"up for a (?:\w+ )?(?:conversation|chat|call)", r"would (?:that|this) be useful",
    r"any interest", r"worth (?:me )?(?:sending|writing)", r"make sense to",
]

def strip_sig(t):
    """Drop greeting, signature block and contact lines so we measure the message."""
    for marker in ("\n--\n", "\n-- \n"):
        if marker in t: t = t.split(marker)[0]
    lines = t.strip().split("\n")
    # greeting: "Hi Name," / "Hey Name," / "Name,"
    while lines and (not lines[0].strip() or re.match(r"^(hi|hey|hello|dear)?\s*[A-Z][\w'.-]*(\s+[A-Z][\w'.-]*)?\s*[,:]\s*$", lines[0].strip(), re.I)):
        lines.pop(0)
    # trailing sign-off: blank lines, contact block, and a bare name
    contact = re.compile(r"\[?(phone|street address|address|city, state)\]?|\d{3}[-.)]\s?\d{3}|reply \"?stop|unsubscribe|@|\|", re.I)
    while lines and (not lines[-1].strip() or contact.search(lines[-1])):
        lines.pop()
    # bare name line(s) at the end: 1-3 capitalised words, no sentence punctuation
    while lines and re.match(r"^[A-Z][\w'.-]*(\s+[A-Z][\w'.-]*){0,2}$", lines[-1].strip()):
        lines.pop()
        while lines and not lines[-1].strip(): lines.pop()
    return "\n".join(lines).strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?")
    ap.add_argument("--subject", default=None)
    ap.add_argument("--type", default="first", choices=["first","followup","breakup"],
                    help="first touch (default), a follow-up, or the break-up email")
    a = ap.parse_args()
    raw = open(a.path).read() if a.path else sys.stdin.read()
    body = strip_sig(raw)

    words = len(body.split())
    sents = [s for s in re.split(r"[.!?]+[\s\n]", body) if s.strip()]
    paras = [p for p in body.strip().split("\n\n") if p.strip()]
    me  = len(re.findall(r"\b(i|i'm|i'd|i'll|i've|me|my|mine|we|we're|our|ours|us)\b", body, re.I))
    you = len(re.findall(r"\b(you|you're|you'd|you'll|you've|your|yours)\b", body, re.I))
    ratio = you / me if me else 99.0
    avg_sent = words / len(sents) if sents else 0

    fails, warns = [], []
    def chk(ok, msg, hard=True):
        (fails if hard else warns).append(msg) if not ok else None

    lo, hi, smax = (50, 125, 6) if a.type == "first" else (15, 70, 5)
    chk(lo <= words <= hi, f"Word count {words}. Target {lo}-{hi} for a {a.type} email. "
                           + ("Cut it." if words > hi else "Too thin, reads templated."))
    chk(len(sents) <= smax, f"{len(sents)} sentences. Target 3-5.")
    chk(len(paras) <= 4, f"{len(paras)} paragraphs. Target 3-4.")
    # 2:1 is the blog-advice ideal. Below 1:1 the email is genuinely about the sender,
    # which is the failure that actually costs replies. Between 1 and 1.5 is a nudge.
    chk(ratio >= 1.0, f"you:I ratio is {ratio:.2f} ({you} you / {me} I). Below 1.0 the email is "
                      f"about you, not them. Rewrite, do not tinker.")
    chk(ratio >= 1.5, f"you:I ratio is {ratio:.2f}. Aim for 1.5+, ideally 2.0. Every 'I' you can "
                      f"turn into a 'you' is worth more than any other edit.", hard=False)
    chk(avg_sent <= 20, f"Average sentence {avg_sent:.0f} words. Keep under 20 for a grade 3-5 read.", hard=False)

    if "—" in body or "–" in body:
        fails.append("Em dash found. Recast with a period or comma.")
    if body.count("!") > 0:
        warns.append(f"{body.count('!')} exclamation mark(s). Use zero on a cold send.")
    if re.search(r"https?://|www\.", body):
        fails.append("Link found. First touch should have no links (no-link wins by 26%).")

    hits = [p for p in BANNED if p in body.lower()]
    if hits: fails.append("Banned phrasing: " + ", ".join(repr(h) for h in hits))

    m = [p for p in MEETING_ASK if re.search(p, body, re.I)]
    i = [p for p in INTEREST_ASK if re.search(p, body, re.I|re.M)]
    if m and not i:
        fails.append("Asks for a meeting, not interest. Gong (304K emails): interest CTAs win by a wide margin.")
    elif not i and not m and a.type != "breakup":
        warns.append("No clear ask found. Every email needs exactly one.")
    qs = body.count("?")
    if qs > 2: warns.append(f"{qs} question marks. More than one ask splits the reply.")

    if a.subject:
        sw = len(a.subject.split())
        if not (2 <= sw <= 4): fails.append(f"Subject is {sw} words. Target 2-4 (46% open rate).")
        if a.subject != a.subject.lower() and a.subject.istitle():
            warns.append("Title Case subject reads like marketing. Lowercase it.")

    print(f"words {words} | sentences {len(sents)} | paragraphs {len(paras)} | you:I {ratio:.2f} | avg sentence {avg_sent:.0f}w\n")
    for f in fails: print(f"  FAIL  {f}")
    for w in warns: print(f"  warn  {w}")
    if not fails and not warns: print("  clean. send it.")
    elif not fails: print("\n  no blockers.")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
