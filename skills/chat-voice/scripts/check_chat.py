#!/usr/bin/env python3
"""Check a draft chat message for memo-voice and AI tells.

Usage: python3 check_chat.py message.txt   (or pipe text on stdin)
Exit code 1 when any HIGH finding exists.
"""
import re, sys

FORMAL = ["i hope this", "i wanted to reach out", "just wanted to", "circling back", "touch base", "touching base",
          "per my last", "as per", "synergy", "going forward", "please find attached", "kindly", "thanks in advance",
          "best regards", "warm regards", "dear ", "at your earliest convenience", "do not hesitate",
          "feel free to reach out", "i would like to", "i am writing to"]
AI_WORDS = re.compile(r"\b(delve|leverage|leveraging|streamline|robust|seamless|seamlessly|ensure|additionally|furthermore|"
                      r"moreover|in conclusion|worth noting|tapestry|landscape|navigate|holistic|utilize|facilitate|"
                      r"comprehensive|optimize)\b", re.I)
NEG = re.compile(r"\bnot just\b[^.\n]{0,40}\bbut\b|\bit'?s not\b[^.\n]{0,40},\s*it'?s\b", re.I)
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")

def main():
    text = open(sys.argv[1]).read() if len(sys.argv) > 1 else sys.stdin.read()
    text = re.sub(r"^```\w*\n|\n```\s*$", "", text.strip())
    lines = text.split("\n")
    words = len(re.findall(r"[\w'$%.,-]+", text))
    sents = [s for s in re.split(r"(?<=[.!?])\s+|\n+", text) if len(s.split()) > 2]
    avg = sum(len(s.split()) for s in sents) / max(len(sents), 1)
    low = text.lower()
    high, warn = [], []

    if "—" in text or "–" in text: high.append("Em or en dash. Use a comma, period or recast.")
    if any(re.match(r"\s*#{1,6}\s", l) for l in lines): high.append("Markdown header. Chats do not use headers.")
    if any(re.match(r"\s*\|.*\|\s*$", l) for l in lines): high.append("Table. Use plain lines instead.")
    bl = [l for l in lines if re.match(r"\s*[-*]\s+\*\*.+?\*\*", l)]
    if len(bl) >= 2: high.append(f"{len(bl)} bold-lead bullets. Drop the bold.")
    if any(re.match(r"\s*\*\*[^*]+\*\*:?\s*$", l) for l in lines): high.append("Bold line used as a header. Chats do not need headers.")
    nb = len(re.findall(r"\*\*[^*]+\*\*", text))
    if nb > 1: warn.append(f"Bold used {nb} times. Limit is one, on the ask or the deadline.")
    hits = [p for p in FORMAL if p in low]
    if hits: high.append("Memo phrasing: " + ", ".join(repr(h) for h in hits))
    if NEG.search(text): high.append("'Not just X but Y' template. State the point directly.")
    if words > 220: high.append(f"{words} words. This is a doc, not a chat message.")
    elif words > 150: warn.append(f"{words} words. Aim for 40 to 120.")
    ai = sorted(set(m.group(0).lower() for m in AI_WORDS.finditer(text)))
    if ai: warn.append("AI-flavored words: " + ", ".join(ai))
    if text.count("!") > 1: warn.append(f"{text.count('!')} exclamation marks.")
    if len(EMOJI.findall(text)) > 1: warn.append("More than one emoji.")
    if avg > 22: warn.append(f"Average sentence {avg:.0f} words. Break it up.")
    if text.count("?") > 2: warn.append(f"{text.count('?')} questions. Keep to one ask.")
    if re.search(r"^(best|thanks|cheers|regards|sincerely)[,!]?\s*$", low.split("\n")[-1].strip()):
        warn.append("Sign-off line. Chats do not need one.")

    print(f"words {words} | sentences {len(sents)} | avg sentence {avg:.0f}w")
    for h in high: print("  HIGH ", h)
    for w in warn: print("  warn ", w)
    if not high and not warn: print("  clean. paste it.")
    sys.exit(1 if high else 0)

if __name__ == "__main__":
    main()
