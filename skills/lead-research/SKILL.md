---
name: lead-research
description: Find B2B prospects, the right decision maker at each, and a verified work email, for cold outreach to land services firms, energy operators or any small services business. Use when asked to build a lead list, find who runs a company, find or verify someone's work email, turn an event attendee export into a ranked shortlist, or research one true specific fact for a personal line. Works with web search and page fetching; never logs in, scrapes LinkedIn, or guesses addresses.
license: MIT
metadata:
  version: "1.0.0"
  domain: gtm
  triggers: find leads, lead list, prospect list, find email, verify email, email pattern, who runs, attendee list, event app, decision maker, research a lead
  related-skills: cold-email, call-prep-onepager
---

# Lead research

Find companies that fit, the person who can say yes, and a work email that will not bounce. Full method with search strings and examples: `references/finding-guide.md`.

## Rules

1. **Check claims first.** If a claimed-companies list exists (in the Stoneworks kit: `python3 tools/check_claimed.py "Company" --domain site.com`), run it before any research. TAKEN means skip the whole company.
2. **Every fact has a URL.** Company facts, titles, emails and personal-line material all carry the page they came from. No URL, no fact.
3. **Mark confidence.** Confirmed (their site, their own post, a filing, a job post), aggregator only (ZoomInfo, RocketReach, revenue estimates), or unknown. Never put an aggregator number in an email.
4. **Never send to a guessed address.** Published, or pattern-built and verified. Accept-all results are risky. Invalid or unknown means drop.
5. **No logins, no scraping, no bought lists.** The human handles anything behind a login (event apps, LinkedIn, member directories) and pastes or exports it. You process what they give you.
6. **Five-minute rule.** If you cannot find one true, specific fact about the person or firm in about five minutes, drop the lead and move on.

## Workflow

1. **Companies.** Search in the user's territory: event exhibitor and sponsor lists, association officer and sponsor pages, job boards (landman, lease analyst, land administrator, right of way agent), state oil and gas regulator case files, maps searches for "land services" in oil towns. Return company, domain, city, why it fits, source URL.
2. **Claim check and fit.** Drop TAKEN companies. Score the rest against the ICP (land services first, then small operator land teams and minerals shops, US, not public, no sale pending, repeating paperwork likely).
3. **Person.** Owner, principal, president, VP or Director of Land, land manager. Sources: their Team or Leadership page, PDFs, press releases. Ask the human to confirm the title on LinkedIn if sources disagree.
4. **Email, in order:** (a) published on their site, (b) published elsewhere (search `"@domain.com"`, `"First Last" "domain.com"`, `site:domain.com filetype:pdf`), (c) an event directory the human legitimately has, (d) pattern from any confirmed address at the domain, then verify with Hunter, NeverBounce, ZeroBounce, MillionVerifier or similar, (e) the human calls the main line. Nothing works: drop.
5. **Personal line.** Three candidates, each one sentence under 20 words, each with a URL: something they did or said, a true fact about their position, a job post, a shared reference point, a plain company fact. No flattery, no diagnosis.

## Output

One block per lead:

```text
COMPANY: {name} ({domain}), {city}   CLAIM: FREE
FIT: {one line, with the ICP points it meets}
PERSON: {first last}, {title}   SOURCE: {URL}
EMAIL: {address}   HOW: {published at URL | pattern from URL, verified by TOOL: result}
PERSONAL LINE OPTIONS:
1. {line} ({URL})
2. {line} ({URL})
3. {line} ({URL})
CONFIDENCE: {confirmed / aggregator / unknown, per fact}
```

## Event app exports

When the human pastes or attaches an attendee export: clean it into name, title, company, email, LinkedIn, location; run the claim check on every company (`check_claimed.py --file companies.txt`); score against the ICP; return the top 20 ranked with a reason each; then find each shortlisted person's email on their company's own site where possible. Remind the human to check the event's terms on using attendee data, and to mention the event in an email only if they actually attended.
