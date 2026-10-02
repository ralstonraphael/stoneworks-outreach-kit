---
name: de-slop
description: Rewrite, edit, or generate prose and interface copy that is direct, specific, concise, and free of common AI-writing habits. Use for messages, documents, posts, reports, product copy, UI text, and reviews when the user asks to de-slop, humanize, tighten, simplify, remove AI tone, or reduce text clutter.
---

# De-slop

Make the writing sound like a competent person with a reason to write it. Preserve the author's meaning, factual claims, useful nuance, and recognizable voice. Remove patterns, not personality.

## Output contract

- For a rewrite, return the revised copy only unless the user asks for notes, alternatives, or an audit.
- For new copy, lead with the answer or useful content. Do not announce the approach.
- For an audit, rank findings by impact, quote only the smallest relevant fragment, and propose a concrete fix.
- Match any requested tone, audience, format, and length. If none is given, use plain language and the shortest complete response.
- Never invent personal experience, opinions, quotations, facts, sources, or confidence.
- Treat unsupported promotional outcomes as marketing language, not factual claims. Remove or qualify them unless the user requires exact preservation.
- Never add typos, awkward grammar, fake anecdotes, or random quirks to appear human.
- Do not claim that a rewrite will evade an AI detector. Detection is unreliable and is not the goal.

## Non-negotiable rules

Apply these unless exact quotation, code fidelity, or an explicit user instruction requires otherwise.

1. Use no em dash character in final prose. Replace it with a period, comma, colon, parentheses, or a recast sentence. Do not replace it mechanically with a hyphen.
2. Do not use negative contrast as a dramatic template. Avoid constructions built around `not just A, but B`, `it is not A, it is B`, or `no A, no B, just C`. State the actual point directly. Keep negation when accuracy, safety, correction, or scope genuinely depends on it.
3. Do not open with praise, agreement, or canned acknowledgment. Skip phrases such as `Great question`, `You're absolutely right`, `Certainly`, and `Of course`.
4. Do not narrate the response. Skip `Let's break this down`, `Here is what I will do`, and other announce-then-answer preambles.
5. Do not end with a recap, slogan, generic invitation, or offer to do more. Stop when the requested work is complete.

## Editing workflow

### 1. Lock the job

Identify the reader, purpose, required facts, desired voice, and length. Infer ordinary defaults when they are obvious. Ask only when a missing choice would materially change the result.

### 2. Find the payload

Reduce the draft to its claims, instructions, decisions, evidence, and necessary qualifications. Treat everything else as removable until it proves useful.

### 3. Cut before polishing

Delete repeated premises, duplicated conclusions, throat-clearing, generic transitions, empty emphasis, fake suspense, and background the reader already knows. Combine overlapping sentences and paragraphs.

### 4. Rewrite plainly

- Prefer specific nouns and direct verbs.
- Use `is`, `are`, and `has` when they are the clearest words.
- Name the actor and action when responsibility matters.
- Replace vague praise with evidence or remove it.
- Replace abstract claims with a fact, example, mechanism, or consequence.
- Keep one stable term for one thing instead of cycling through synonyms.
- State uncertainty precisely. Do not stack hedges.
- Keep useful technical language. Remove jargon used only to sound authoritative.

### 5. Restore a human voice

Use the source text as the voice reference when it has a clear human voice. Keep its natural contractions, humor, bluntness, dialect, and level of formality when they help. When the source is already AI-like, preserve its audience and formality instead of its phrasing or cadence. If no voice sample exists, use neutral conversational prose. Do not imitate a living author unless the request is allowed and appropriate; describe the requested traits instead.

Vary rhythm because the meaning calls for it, not by inserting random fragments. A short sentence should carry weight. A long sentence should earn its length.

### 6. Format in proportion to the content

- Use no heading for a short answer that reads clearly without one.
- Add headings only for distinct sections with substantive content.
- Use bullets for parallel items, choices, steps, or checks. Use prose for a connected thought.
- Avoid nested headings, title-case headings, decorative labels, emoji markers, and bold lead-ins on every bullet.
- Do not turn a simple answer into a miniature report.

For interface copy:

- Give each message one job.
- Use stable, familiar labels.
- Name buttons by the action they perform.
- Keep helper text only when it prevents confusion or error.
- Make errors say what happened and what the user can do next.
- Remove repeated title, subtitle, body, and call-to-action language.
- Prefer a simple block, row, or list when a card grid adds no information.

### 7. Check integrity

Confirm that the edit has not changed facts, commitments, scope, citations, quotations, commands, code, or legal meaning. Preserve required terminology even when it appears on a watchlist.

### 8. Run the slop pass

Check the final text for:

- all forbidden patterns, canned framing, and generic endings
- repeated claims, conclusions, sentence shapes, or three-part lists
- unsupported importance, consensus, certainty, or promotional language
- forced metaphors, rhetorical questions, and manufactured punch lines
- excessive headings, bullets, bold text, fragments, or parenthetical asides
- any sentence that adds no fact, instruction, decision, evidence, qualification, or useful voice

For long or stubborn drafts, read [references/patterns.md](references/patterns.md). Use `scripts/lint_text.py` for a mechanical pass, then judge every finding in context. The linter is a reminder system, not an authority.

Read [references/research.md](references/research.md) only when maintaining this skill or explaining why a rule exists.

## Final standard

The result should feel chosen rather than generated. It should be easy to understand, hard to misread, and no longer than its job requires.
