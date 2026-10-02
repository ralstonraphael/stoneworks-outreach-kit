---
name: cold-email
description: Write cold outreach emails that get replies. Use when drafting a cold email, first-touch outreach, a follow-up sequence, an intro request, a warm-ish contextual email (same event, same school, mutual connection), or when auditing outreach copy that is not getting responses. Covers structure, length, the ask, personalization, sequencing, and deliverability.
license: MIT
metadata:
  version: "1.0.0"
  domain: gtm
  role: specialist
  triggers: cold email, outreach, first touch, follow up, sequence, prospecting, intro email, reply rate, cold outreach, email template
  related-skills: de-slop
---

# Cold email

Write the email a busy stranger will actually answer. Every rule here comes from
response-rate data, not taste. The research is in `references/research.md`.

## Before writing, get four things

Ask only for what you cannot infer. Never stall the draft on questions you can answer yourself.

1. **Who they are.** Name, role, company, and one specific true thing about their
   situation. If you cannot name that one thing, stop and research. A cold email
   without it is a waste of the send.
2. **Why you.** The sender's standing to write: shared event, mutual connection,
   relevant work history, a customer in their world. Standing is what converts.
3. **What you want.** The real outcome, not the polite version.
4. **Relationship temperature.** Cold, contextual (a real shared reference point),
   or warm (introduced). This changes the opener, not the structure.

## The structure

Five parts, in this order, 50 to 125 words total.

```
1. Standing        one line, why this email is not spam
2. Them            what you see about their situation, in second person
3. You             one clause of credibility, framed as why you are asking
4. Gift            something they get whether or not they reply (optional, strong)
5. Ask             a question about interest, not a request for time
```

Every part earns its place or gets cut. Most bad cold emails fail because part 3
swallows parts 1, 2, 4 and 5.

## Hard rules

These are non-negotiable unless the user overrides them.

| Rule | Target | Why |
|------|--------|-----|
| Word count | 50 to 125 (follow-ups 15 to 70) | 200+ words drops reply rate to 3.9%. 50 to 125 hits 8.2% |
| Sentences | 3 to 5 | 6 to 8 sentences drops reply rate by a third |
| Paragraphs | 3 to 4, short | Whitespace makes it scannable on a phone |
| you : I ratio | 1.5 : 1 minimum, 2 : 1 ideal | Below 1 : 1 the email is about you. This is the most common failure |
| Reading level | Grade 3 to 5 | Writing at that level gets 67% more replies |
| Calls to action | Exactly 1 | Single-CTA emails get 35 to 42% higher response |
| Subject words | 2 to 4 | 46% open rate. Lowercase, specific, no colon-and-hook |
| Links | 0 on first touch | No-link beat linked by 26% on reply rate |
| Attachments | 0 | Spam filters, and it presumes they already care |
| Images, logos, tracking pixels | 0 | Makes it look like marketing, not a person |

Run `scripts/check_email.py` on the draft. It measures every row in that table.

## The ask is where most emails die

Do **not** ask for a meeting on the first touch. Gong studied 304,174 emails: asking
for interest beat asking for a meeting by a wide margin. Interest-based CTAs hit
roughly 30% success, about double any other type. A reply costs seconds. A meeting
costs half an hour, so the meeting ask triggers loss aversion.

Ask for interest. Book the calendar after they reply.

Good: `Worth a conversation?` / `Curious?` / `Want me to send it over?` /
`Is this a real problem for you or am I off?` / `Who owns this at [company]?`

Bad: `Do you have 20 minutes Thursday?` / `Book time here: [link]` /
`Let me know a few times that work.`

The best variant on a research-led email is offering the research: *"I'll send you
what I find either way."* They get value for a one-word reply, which is the whole
point.

## Personalization that counts

Name tokens are not personalization. Reply rates go from 3% with none to 7% with
real personalization, and deep research pushes it near 18%.

The test: **could this sentence be sent to anyone else in their industry?** If yes,
it is not personalization.

Ranked by strength:

1. Something they did or said. A talk, a post, a hire, a filing, an award.
2. Something structurally true of their position that they would agree with.
   *"You work across enough operators to know what's normal and what isn't."*
3. A shared reference point. Same event, same school, same former employer.
4. Company facts anyone could look up. Weakest. Use only as support.

When writing several emails to one company, give each person a different line.
Colleagues forward emails to each other, and identical text reads as a mail merge.

## Poke the bear, do not pitch

Your real competitor is inertia. Ask a neutral question that makes them think about
how the job gets done now, without an agenda attached. Shine a light on the problem,
never on the product.

Anchor on the **category** of problem, not a specific diagnosis. Naming their exact
use case before they have told you anything makes you a vendor who did not listen,
and if you guess wrong you are done. Broad enough that they fill it in, specific
enough that they know you are not lost.

## Voice

Inherit every rule from the `de-slop` skill. On top of those, for email:

- **No em dashes.** Replace with a period or comma. Recast if needed.
- **No `not just X, but Y`** and no negative-contrast drama.
- No `I hope this finds you well`, `I wanted to reach out`, `quick question` as the
  whole subject, `circling back`, `touching base`, `synergies`, `leverage` as a verb,
  `solutions` as a noun for what you sell, `passionate about`, `game-changer`,
  `revolutionize`, `in today's fast-paced`, `at the end of the day`.
- No exclamation marks. One is tolerable in a genuinely warm reply. Zero on a cold send.
- Do not hedge-stack: `I was just wondering if maybe you might possibly`.
- Do not protest innocence. `I'm not trying to sell you anything` makes people
  suspicious. Show it instead: `I'd mostly listen`.
- Contractions are good. Write how you talk.
- Give them an easy no. `Either way, good to have crossed paths` outperforms
  pressure, because a graceful exit makes yes feel cheaper.
- Sign with a first name only above the block.

Run the de-slop linter too:
`python3 ~/skills/catalog/de-slop/scripts/lint_text.py --strict draft.md`

## Sequencing

- 58% of replies come from email one. Follow-ups produce the other 42%.
- 68% of positive replies land after touch two, 89% by touch five.
- 4 to 6 touches gets roughly 3x a single send.
- Cadence: day 0, day 3, day 10, day 17 captures about 93% of replies.
- Reply in the **same thread**. New threads read as a new pitch.
- Each follow-up adds something. Never `just bumping this to the top of your inbox`
  alone. Add a fact, a shorter ask, or a redirect: *"If this isn't yours, who owns it?"*
- Last touch is a clean break, not guilt. *"I'll leave it here. Door's open if it
  becomes relevant."*
- Send Tuesday to Thursday, 8 to 11am **their** local time.

## Deliverability

At any real volume this matters more than the copy.

- Use a **dedicated sending domain**, never the primary one. A blacklisting takes
  the whole company's email with it.
- SPF, DKIM and DMARC before the first send.
- Warm the domain. Ramp slowly. Keep bounces under 2% and complaints under 0.3%.
- Verify addresses before sending. Pattern-derived addresses bounce.
- Under about 30 recipients, send by hand from a normal inbox. Sequencer tracking
  pixels and link wrappers hurt deliverability, and hand-sent beats automated at
  that scale anyway.
- Cold commercial email needs a physical postal address and a working opt-out,
  honored within 10 days. `Reply "stop" and you won't hear from me` counts.

## Calibrate expectations

Platform average reply rate is 3.43% and falling. Good is 8 to 12%. Well-researched
lists hit 15 to 25%. From 30 well-personalized sends, expect 3 or 4 replies. That is
success, not failure. Do not rewrite a working email after two sends.

## Workflow

1. Gather the four inputs. Research until you have the specific true thing.
2. Draft the five parts in order. Write part 2 before part 3, always.
3. Cut to 125 words. Then cut to 90.
4. Count pronouns. If `I` beats `you`, rewrite, do not tinker.
5. Run `scripts/check_email.py` and the de-slop linter.
6. Read it aloud. Anything you would not say out loud gets cut.
7. Check the ask is one question about interest.

## Variants

`references/patterns.md` has worked structures for: same-event or contextual,
mutual-connection intro, research or learning outreach, hiring, investor, partnership,
re-engaging a dead thread, and the break-up email. Read it when the scenario is not a
straight first-touch sales email.
