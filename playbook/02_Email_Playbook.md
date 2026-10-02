# 02. Email playbook

How to write the first email and the follow-ups. The agent drafts. The sender reads, edits and schedules from their own Gmail. Every email passes `tools/check_email.py` and `tools/lint_text.py` before the sender sees it as final.

Fill-in markers look like `{{FILL: ...}}` (the sender answers once, in `MY_PROFILE.md`) or `{curly}` (the agent fills per email).

## 1. The rules in ten lines

1. 50 to 125 words, 3 to 5 sentences, three short paragraphs. Aim for 85 to 105 words.
2. "You" at least as often as "I". The checker counts "we", "us" and "our" as "I", so watch them. Aim for 1.5 times as many "you".
3. First paragraph: why the sender is writing, one true sentence (the ladder in section 2).
4. Second paragraph: one true, specific fact about them, from a page you read. No flattery, no diagnosis, no guess at their problems.
5. Third paragraph: the offer (section 3) and one soft question about interest. No day or time, no meeting link.
6. Subject: 2 to 4 words, lowercase, specific. Never "quick question".
7. No links, attachments, images, exclamation marks, em dashes or en dashes.
8. Signature: the sender's first name, then their phone. Nothing else.
9. Send Tuesday to Thursday, 8 to 11 AM in their time zone, from the sender's own Gmail, 8 new emails a day per sender.
10. Follow up in the same thread on day 3, 10 and 17. Any reply stops the sequence.

## 2. The why-me ladder

A stranger answers when the sender has a real reason to be writing. It must be true, because they may ask about it on the call. Use the highest level the sender can stand behind. One sentence, 28 words or fewer. The sender's lines are in `MY_PROFILE.md`.

**Level 1: the sender's own relevant experience.** What they built or ran, for whom, how long. Shape: "I [built / ran / shipped] [what] for [who], for [how long]." Fill only the blanks that are true.

**Level 2: a real personal tie.** Family or past work in land or energy, a shared school or employer, or an event the prospect was also at. State it plainly. Never "great meeting you" if you did not meet.

**Level 3: the team line.** When the sender has no level 1 or 2, borrow the team's background, worded so nobody could think the sender did it:

> I work with a small team, and one of us built AI tools for construction companies at Datagrid and then Procore.

Wrong, never write these:

- "I built AI tools at Datagrid and Procore." Only Ralston did. Other senders never say this in the first person.
- "We've built AI for land companies" or "for energy teams". Nothing has been built for a land or energy company yet.
- "My team has deployed AI at companies like yours." It claims more than is true.
- "I was at the AAPL meeting in Salt Lake." Only true for Ralston, and AAPL attendee companies are his anyway.

Senders on level 3 write "we" and "us" when talking about the team, but keep those words few, because the checker counts them against the you:I ratio.

## 3. The first email

```text
Subject: {2 to 4 words, lowercase}

Hi {first name},

{why-me line from MY_PROFILE.md}

{personal line: one sentence, 20 words or fewer, one fact about them, from a page you read}

{offer paragraph: one of the versions below, about 60 words}

{sender first name}
{sender phone}
```

### The offer paragraph

Three sentences, in this order:

1. **The read.** In return for hearing how their team's week goes, they get a free, honest read on which parts of their work AI could take off their plate and which it can't.
2. **The rundown.** They also get a one page rundown in November of which AI tools land teams have tried and what stuck, with no company names. (Ralston owns the rundown and sends it to everyone we talk with.)
3. **The ask.** One soft question about interest, last.

Rotate between these so four senders do not send identical text, which reads as a mail merge and hurts deliverability. You may also write your own version that keeps the three points.

Version A:
> If you walk us through where your team's hours go, you'll get a free, honest read on what AI could and couldn't take off your plate. You'll also get a one page rundown in November of which AI tools land teams have tried and what stuck, with no company names. Would you be open to a short call?

Version B:
> A short call would get you a free, honest read on what AI could and couldn't take off your plate, whether or not it leads anywhere. You'd also get a one page November rundown of which AI tools land teams have tried and what stuck, with no company names. Would you be open to that?

Version C:
> On a short call you'd get a free, honest read on which parts of your team's work AI could take off your plate and which it can't. I'll also send everyone I talk with a one page rundown in November of which AI tools land teams have tried and what stuck, with no company names. Would you be up for a call like that?

For operators and midstream companies, say "energy teams" instead of "land teams". Version A suits level 3 senders (one "us"). Version C uses "I", so it suits level 1 or 2 senders.

### Subject lines

- One distinctive word from the firm's name plus "and ai": "cedar ridge and ai" for Cedar Ridge Land Services. Drop words like Land, Energy, Resources, Company, LLC.
- Or a real shared reference: "okc landmen dinner", "ou petroleum land". Only if it is true for the sender.
- Lowercase, 2 to 4 words, no colon, no emoji, never "quick question". The checker does not scan the subject for dashes, so look yourself.

### Three worked examples

The names, firms and facts below are invented, to show the shape. The level 1 and level 2 lines are samples: each sender uses their own true line from `MY_PROFILE.md`. Each example passes the checker and the linter.

**Level 3 sender, land services firm, fact from their careers page.**

```text
Subject: cedar ridge and ai

Hi Dana,

I work with a small team, and one of us built AI tools for construction companies at Datagrid and then Procore.

You're hiring a lease analyst and two field landmen for the Permian this fall.

If you walk us through where your team's hours go, you'll get a free, honest read on what AI could and couldn't take off your plate. You'll also get a one page rundown in November of which AI tools land teams have tried and what stuck, with no company names. Would you be open to a short call?

Ethan
(555) 555-0100
```
Checker: words 93, sentences 5, you:I 2.33, clean.

**Level 1 sender, operator's land director, fact from the leadership page.**

```text
Subject: harbor peak and ai

Hi Morgan,

I build automation tools for operations teams, mostly the unglamorous back-office kind.

Land and land administration both report to you at Harbor Peak.

On a short call you'd get a free, honest read on which parts of your team's work AI could take off your plate and which it can't. I'll also send everyone I talk with a one page rundown in November of which AI tools land teams have tried and what stuck, with no company names. Would you be up for a call like that?

Joud
(555) 555-0100
```
Checker: words 87, sentences 5, you:I 1.67, clean.

**Level 2 sender, right-of-way firm, fact from a project page.**

```text
Subject: prairie row and ai

Hi Casey,

My family has worked in Oklahoma oil and gas for two generations, so I grew up hearing about leases and title.

Your firm has handled right-of-way on three pipeline projects across Kansas since last year.

A short call would get you a free, honest read on what AI could and couldn't take off your plate, whether or not it leads anywhere. You'd also get a one page November rundown of which AI tools land teams have tried and what stuck, with no company names. Would you be open to that?

Andrew
(555) 555-0100
```
Checker: words 90, sentences 5, you:I 2.50, clean.

## 4. The personal line

This sentence decides whether they read the rest. Five tests, in order:

1. Could it go to anyone else in their industry? If yes, rewrite it.
2. Can you point to the page it came from? Keep the URL with the draft. Never put the URL in the email.
3. Does it stay at the shape of their work? No "your invoicing must be a mess". If you guess wrong, you are done.
4. Is it free of praise? A fact makes them feel noticed. A compliment feels like a pitch.
5. Is it one sentence of 20 words or fewer?

Where good lines come from, strongest first:

- Something they did or said: a talk, a post, a hire, an award, a quote in the news.
- A true fact about their position they would agree with: they serve many operators at once, they run several regions, they just opened an office.
- A job post: what they are hiring for says where the work is piling up.
- A real shared reference point with the sender.
- Last, a plain company fact from their site.

Weak lines to avoid:

| Line | Problem | Instead |
|---|---|---|
| "so you've probably seen it all" | Fits anyone | One fact about that firm |
| "your team clearly takes the craft seriously" | Flattery | Say what they do |
| "Cedar Ridge keeps coming to mind" | Manufactured | Delete it |
| "we might have crossed paths" | A hedge | Say where you were, or nothing |
| "I bet your team is buried in lease paperwork" | A diagnosis | Name their role or a company event |
| Any figure you cannot source ("over $1 billion") | Could be wrong | Find the page or cut it |

The optional "so you probably..." tail is fine when it stays light. When the fact is strong on its own, stop at the fact.

## 5. Follow-ups

Same thread: reply to the sender's own first email. Each follow-up adds something new. Day 17 is a clean goodbye with no ask. Any reply, even a no, stops the sequence.

**Timing.** Count calendar days from the first email, then send on the first Tuesday, Wednesday or Thursday on or after that day, 8 to 11 AM their time. If they are out of office, pause until they are back.

### Day 3: one new fact

```text
Hi {first name},

Adding one thing to {weekday}'s email. {A new fact about them, one sentence, 20 words or fewer.}

Would you be up for a short call? You'd get {my / our} honest take on what AI could and couldn't do for your team.

Everyone {I / we} talk with gets the one page rundown in November of which AI tools land teams have tried and what stuck.

{sender first name}
{sender phone}
```

Example (passes, 64 words, you:I 2.00):

```text
Hi Dana,

Adding one thing to Tuesday's email. Your site says Cedar Ridge now covers New Mexico as well as Texas.

Would you be up for a short call? You'd get our honest take on what AI could and couldn't do for your team.

Everyone we talk with gets the one page rundown in November of which AI tools land teams have tried and what stuck.

Ethan
(555) 555-0100
```

### Day 10: a way out, or a new angle

When you are not sure you have the right person:

```text
Hi {first name},

If this isn't yours, who handles the back office or land work at {company}? A name from you would help.

{sender first name}
{sender phone}
```

When you have another new fact:

```text
Hi {first name},

One more thing I came across: {new fact, one short sentence}. A short call would cover how that shows up in your team's week and whether AI could take any of it off your plate. Would you be open to that?

If not, no worries.

{sender first name}
{sender phone}
```

### Day 17: the last email

```text
Hi {first name},

I'll stop writing after this one so I'm not cluttering your inbox. If AI ever comes up on your list, you're welcome to reply here.

Good luck with the rest of the year.

{sender first name}
{sender phone}
```

After day 17 the person is done. A second person at the same firm may now be written to, with a different personal line.

### Optional: LinkedIn

The day after the first email, the sender may send a LinkedIn connection request with no note, or a one-line note that does not pitch ("Sent you a note by email, happy to connect either way."). Never paste the email into LinkedIn. The agent does not log in to LinkedIn or automate it.

## 6. Pre-send checklist

Before drafting:

- [ ] `tools/check_claimed.py` says FREE for the company and its domain.
- [ ] The lead passes the fit check in `01_ICP.md`.
- [ ] The email address is published or verified, and its source is written down (`03_Finding_Leads_and_Emails.md`).
- [ ] The personal line has a source URL.

The email:

- [ ] 50 to 125 words, 3 to 5 sentences, three short paragraphs, one question mark.
- [ ] The why-me line is the sender's own, from `MY_PROFILE.md`.
- [ ] The offer says the read is free, names the November rundown, and ends with the ask.
- [ ] No links, attachments, images, "!", em dashes or en dashes.
- [ ] None of: "I hope this finds you well", "reaching out", "circling back", "touching base", "just checking in", "leverage", "unlock", "streamline", "game-changer", "synergy".
- [ ] Subject is 2 to 4 words, lowercase, not "quick question".
- [ ] Signature is first name and phone only.

Before it goes:

- [ ] Checker shows no FAIL. Linter shows no findings.
- [ ] Scheduled for Tuesday to Thursday, 8 to 11 AM their time, from the sender's own Gmail.
- [ ] Company claimed in Team Claims (or posted in the team chat).
- [ ] Follow-up dates noted: day 3, 10, 17.

## 7. The commands

Save the body as `draft.txt` with no Subject line inside. Write the phone like (555) 555-0100. From the kit folder:

```bash
python3 tools/check_email.py --type first --subject "cedar ridge and ai" draft.txt
```

```bash
python3 tools/check_email.py --type followup draft.txt
```

```bash
python3 tools/check_email.py --type breakup draft.txt
```

```bash
python3 tools/lint_text.py --strict draft.txt
```

Exit code 0 means no FAIL. A "warn" is a nudge and does not block a send. A FAIL blocks it: rewrite, do not tinker. The checker does not look at the subject for dashes, and the linter catches a few words the checker misses, so run both.
