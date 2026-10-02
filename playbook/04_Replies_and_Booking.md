# 04. Replies and booking

A reply is the whole point. Handle it fast, kindly and in the same thread. Ralston runs every call, with one technical teammate (Ethan or Joud) on the line. The sender's job is to get the prospect to a confirmed time and hand over cleanly.

## Speed

- Answer a positive reply within **2 hours** if it lands between 7 AM and 9 PM the sender's time. Later than that, answer by 9 AM the next morning.
- Answer no's, questions and "not now" the same day. Short is fine.
- During send windows, keep Gmail open with notifications on. Our fastest yes came 23 minutes after the email went out.

## The moment a reply lands

1. **Stop the sequence.** In Gmail open `in:scheduled` and delete any scheduled follow-up in that thread. Do this even when the reply is a no.
2. **Update the claim** in Team Claims: Status = Replied, Positive, Not now, Declined or Bounced.
3. **If it is positive:** post it in the team chat ({{FILL: team chat from MY_PROFILE.md}}) and copy Ralston ({{FILL: Ralston's email from MY_PROFILE.md}}) on your first reply.
4. **Draft the reply** from the scripts below, changed to fit what they actually wrote. Mirror how formal they are. Plain text, their first name, short.

## Booking a call

1. Get Ralston's open windows from {{FILL: where Ralston posts availability, from MY_PROFILE.md}}. If none are posted, ask in the team chat before you offer anything.
2. Offer **three specific times in their time zone**, Tuesday to Thursday mornings first. Never "let me know what works".
3. When they pick, Ralston sends the calendar invite with a Google Meet link. The prospect and the technical teammate are guests. The sender confirms in the thread.
4. The agent builds a one-page brief for Ralston with the `call-prep-onepager` skill (no money section) and the sender posts it in the team chat.
5. Calls are about 20 minutes and mostly questions. Ralston sends the recap within 24 hours.

## Reply scripts

All of these passed `tools/check_email.py --type followup` as a length and banned-word check. A "no ask pattern" warning on a reply is expected. `{you}` means the sender.

### 1. "Yes" or "when are you free?"

```text
Thanks, {first name}, glad to hear it. Ralston runs these calls, so I've copied him here. Would {day} at {time}, {day} at {time} or {day} at {time} {their time zone} work for you? It's about twenty minutes, and there's nothing for you to prepare. A colleague who works on the technical side may join to listen.

{sender first name}
```

After they pick:

```text
{day} at {time} {their time zone} it is, {first name}. Ralston is sending a calendar invite with a Google Meet link, so it should reach your inbox shortly. If your plans shift, just say so and you can pick another time.

{sender first name}
```

### 2. "Send me some info"

No attachments, no deck, no links. Two sentences, then keep the door open.

```text
Happy to, {first name}. I'd rather not send a generic deck, because what's useful depends on how your team actually works. The short version is that we look at where your team's hours go and tell you honestly which parts AI could take off your plate and which it can't. Would a short call work, or do you have questions I can answer here first?

{sender first name}
```

### 3. "Wrong person"

```text
Thanks for telling me, {first name}. Who at {company} would be the right person to ask? If you'd like to pass this along, you're welcome to say you pointed me their way, or keep your name out of it, whichever you prefer.

{sender first name}
```

If they give a name, that person gets a fresh first email with their own personal line. Mention who pointed you only if the referrer said that was fine.

### 4. "What does it cost?"

No price, no range, no "starts at". Ever.

```text
Fair question, {first name}. There's no price on a first call, because any number would be a guess before we understand your work. The call is free, and so is the read on what AI could and couldn't do for your team. If something looks worth doing, you'd see the scope and the cost in writing before you decide anything.

{sender first name}
```

If they push again, say once more, kindly, that a number would be a guess, and ask whether a call is a fair next step. Then tell Ralston.

### 5. "Who is this?" or "What exactly do you do?"

```text
Fair question, {first name}. Stoneworks is a small team that does AI implementation work, and land and energy firms are who we're starting with. It's paid work if it goes anywhere, but the call and the read are free, and you'd see the scope and the cost in writing before deciding anything. Would a short call be a fair next step?

{sender first name}
```

### 6. "We already use AI" or "we already have software"

A good sign, not an objection.

```text
That's good to hear, {first name}. What's working well for you so far? I'd want to understand how your team uses it before saying anything about where else AI might help, and I'd tell you plainly if it already covers what you need. Would a short call be worth it?

{sender first name}
```

### 7. "Not now"

```text
Makes sense, {first name}. When would be a better time for you? I'll note the date and stay quiet until then, apart from the one page rundown in November.

{sender first name}
```

Write the date down. The next email must carry something new.

### 8. "Not interested"

```text
Understood, {first name}, and thanks for letting me know. You won't get another email from us about this. All the best to you and your team.

{sender first name}
```

### 9. "Take me off your list"

Stop everything for that person, add the company to Do Not Contact the same day, and send only:

```text
Done, {first name}. You're off the list, so you won't get another email from us. Thanks, and all the best to you and your team.

{sender first name}
```

### 10. "How did you get my email?"

Answer truthfully from your notes. If you do not know, ask the agent to look up the recorded source before replying. Never guess.

```text
Fair question, {first name}, and sorry if it was unwelcome. {True source, for example: Your address is on your firm's team page.} I'll take you off my list if you'd like, just say so.

{sender first name}
```

## Auto-replies and bounces

| What comes back | What to do |
|---|---|
| Out of office with a return date | Not a reply. Delete scheduled follow-ups for the thread and send the next touch on the first Tuesday to Thursday after they are back. |
| Out of office naming someone else | Same as above. Note the name. Do not write to them yet (one person per company). |
| "No longer with the company" | Stop. Find who holds the role now on the firm's site. They get a fresh first email. |
| Bounce: address not found | Stop. Do not resend or guess a new pattern. Find a published address or drop the lead. Status = Bounced. Tell Ralston the same day. |
| Bounce: mailbox full or temporary | Try once more with the next scheduled touch. A second bounce means drop it. |
| "Blocked" or spam notice | Stop sending from that Gmail for the day and tell Ralston. Over 2% bounces in a week means everyone pauses. |

## What never gets said, by anyone but Ralston on a call

- A price, a range, or a discount.
- A promise of results, hours saved or money saved.
- That we have built things for land or energy companies.
- Anything about title or runsheet automation beyond "a person would always review the work".
- Anything about another prospect or client by name.
