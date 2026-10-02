---
name: call-prep-onepager
description: Build a one-page PDF call-prep brief for a prospect who replied to cold outreach (land services, energy, or any small services firm). Use when a lead says yes to a call and the user needs to know who they are, where AI could fit, what to ask, how the 3-call path to a pilot goes, and what to watch for. Produces a single Letter page, checked for page count.
license: MIT
metadata:
  version: "1.0.0"
  domain: gtm
  role: specialist
  triggers: call prep, prep brief, one pager, discovery call, prospect brief, lead replied, prep for call
  related-skills: cold-email, de-slop
---

# Call prep one-pager

The brief the sender reads in the five minutes before a first call. One page, two columns,
no filler. Worked example: `references/example-brief.html` (a fictional land services firm).

## Rules that make it useful

1. **Facts carry a source tier.** Mark each claim as confirmed (their site, their job posts,
   their own reply), aggregator-only (ZoomInfo, RocketReach, revenue estimates), or unknown.
   The footer lists all three. Never present an aggregator number as fact.
2. **Say what is thin.** If research finds little, the page says "unknown" and turns it into a
   call-1 question. Do not pad with invented headcount, revenue, clients or tools.
3. **Bottom line first.** A shaded box: where to start, what to avoid, the one question to ask
   first. Everything below supports it.
4. **Conditional framing.** The team does not want to look like it is rushing to money. The page
   says everything assumes the first call confirms a real fit, and no price is quoted on call 1.
5. **Billing model decides the wedge.** Day-rate firms lose revenue when work gets faster, so
   lead with timesheet-to-invoice and QC. Per-tract or fixed-fee firms gain, so lead with
   project status and reporting. Ask how they bill before anything else.
6. **Stay out of title automation.** Enverus + Tracts, Quorum, Landman.ai, Rowland.ai,
   TitleTrackr and nuEra already sell it. Pitch the firm-specific layer: intake to invoice, QC
   rules, client reporting, contractor onboarding.
7. **Sender voice.** Plain, no em dashes, no hype. Sender background line: the team line from the playbook (one of us built AI tools for construction companies at Datagrid, then Procore).

## Sections (in order)

Left column: Who they are / People (verify) / Where AI fits, ranked (3 items, plus the billing
rule and the avoid-list). Right column: Three calls to a signed pilot (table) / Ask on call 1
(5 questions plus a good-sign line) / If they push back (3 rows) / On the call (roles, never-say list). Footer: confirmed vs aggregator vs unknown.

## The path: three calls

1. 20 min, decision-maker plus sender. Questions only. No price, deck, data request or title talk.
2. 30 min, add the day-to-day owner. Pick ONE workflow and put a number on it. Ask for redacted
   examples. Bring a one-page scope and a data-handling note.
3. 30 min, same group plus a technical partner. Demo on fake data, scope, pass/fail metric, NDA.
   Ask: "If I send the agreement and invoice, can we start Monday?"
A 4th call only if IT or an attorney needs another pass.

## Money

Pricing is held by Ralston and is not in this kit. A teammate's brief has no money section: put an "On the call" block there instead (who runs it, what the technical seat does, what never to say). Never quote or estimate a price for a prospect.

## Workflow

1. Gather inputs: the reply text, company site, job posts, and any notes the sender has.
2. Research (WebSearch + WebFetch on their site and job boards). Budget a few calls. Record the
   source tier of each fact.
3. Fill `references/example-brief.html` as the template: copy it, replace content, keep the CSS.
4. Render and check: `scripts/render.sh brief.html out.pdf` (Chrome headless, then pdfinfo page
   count; it fails if the PDF is not exactly 1 page).
5. If it spills past one page, cut words, not font size below 8.3pt.
6. Hand back the PDF path, the wedge in one sentence, and what is unknown.
