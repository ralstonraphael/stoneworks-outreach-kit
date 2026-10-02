---
name: chat-voice
description: Write or rewrite short casual messages for group chats, DMs and texts (Discord, Slack, iMessage, WhatsApp, team updates, quick asks, status posts, "here are my thoughts" replies). Use when the user wants a message to send to teammates or friends that sounds like a person typing, not a memo and not an AI. Built on the de-slop and deslop rules, tuned for chat.
---

# Chat voice

Write the message a thoughtful person would actually type into a team chat. Same bar as `de-slop` and `deslop` (no AI tells, no invented facts), but the register is a chat, not a document.

## Output contract

- Return the message alone in a code block so it pastes cleanly. One version unless asked for more.
- After it, add at most two short lines, and only for things the user must check (an unverified claim, a placeholder, a date).
- Never claim the message passes an AI detector.

## Inherit these from de-slop and deslop

No em dashes, ever. No "not just X, but Y" or "it's not A, it's B" templates. No throat-clearing, no recap or slogan endings, no offers of more help. Never invent a fact, number, name or quote. Keep the user's own phrasing and voice when they gave any.

## Chat rules

1. **Lead with the point.** The first line says why you are writing. Greeting is `hey`, `hey team`, or nothing.
2. **Short.** Aim for 40 to 120 words. Past 150, ask whether it belongs in a doc and send a link instead.
3. **Sound spoken.** Contractions always. Lowercase is fine. Plain verbs. A fragment is fine when a person would really say it. Do not stack fragments for punch.
4. **Format lightly.** No headers, no tables, no bold-lead bullets. Plain `-` bullets only for three or more parallel items. Bold at most once, on the ask or the deadline. Backticks for code and names that need them.
5. **One ask.** Say who, what and when: "can you double check the names before thursday". Put it last.
6. **Warm and direct.** Thank once, for something specific. Skip "I hope this finds you well", "just wanted to", "circling back", "touch base", "per my last", "as per", "please find attached", "thanks in advance", "best regards".
7. **Disagree kindly.** Name what you like, then the change, with the reason in a clause: "I'd lean X because Y, open to pushback."
8. **Skip context they already have.** Do not re-explain the project to the people running it.
9. **No sign-off, no signature, no emoji by default.** Use one emoji at most, and only if the user's own messages use them. Never as bullets.
10. **Be exact about the unknown.** Say "not sure yet" instead of smoothing it over.

## Register

| Audience | Style |
|---|---|
| Friends, group text | Loosest: lowercase, fragments, short |
| Team Slack or Discord | Casual but work-clear: this skill's defaults |
| Client, investor, exec thread | Not this skill. Use `deslop` or `cold-email` |

## Process

1. Pin down the channel, the audience, the point and the one ask.
2. Draft from the point outward, then cut to length.
3. Read it aloud. If you would not say or text it, rewrite that line.
4. Run `scripts/check_chat.py` and fix anything marked HIGH.
5. Output the message.

`references/examples.md` has before and after pairs.
