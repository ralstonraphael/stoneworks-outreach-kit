# Start here (for the human, 10 minutes)

This kit is for your Claude agent, not for you to read cover to cover. You set it up once, then work with your agent: it finds leads, checks they are not taken, researches them, drafts emails that pass our checkers, and tells you what to send and when. You read, edit and send from your own Gmail.

The goal is meetings booked. Ralston runs every call.

## Setup

1. **Unzip** the kit somewhere you will keep it, for example `~/Stoneworks_Outreach_Kit`.
2. **Install the skills** (cold-email, de-slop, chat-voice, lead-research, call-prep-onepager):

```bash
bash ~/Stoneworks_Outreach_Kit/skills/install.sh
```

3. **Optional but useful:** lets the tools read the spreadsheet directly.

```bash
pip3 install openpyxl
```

4. **Open Claude Code inside the kit folder**, so it reads `CLAUDE.md` automatically:

```bash
cd ~/Stoneworks_Outreach_Kit && claude
```

5. **First message to your agent:**

> Read CLAUDE.md, then interview me to fill in every {{FILL}} in MY_PROFILE.md. Ask one question at a time and write my answers into the file.

6. **Show Ralston your why-me line** before your first send.

If you use Claude in the desktop app or on the web instead, add the kit folder to the session (or upload `CLAUDE.md`, `MY_PROFILE.md` and the `playbook` folder) and send the same first message.

## Your week

| Day | What you and your agent do |
|---|---|
| Monday | Research. Agent builds a lead list in your territory, checks claims, finds people and emails. You claim the companies you will send to. |
| Tuesday to Thursday | Send 8 new first emails a day, 8 to 11 AM their time, plus any follow-ups due. Answer replies within 2 hours. |
| Friday | Research and drafts for next week. Fill in your row on the Scoreboard tab. |

## Every morning, say to your agent

> Run the daily loop in CLAUDE.md.

## The five things that matter most

1. Check the live claims sheet (https://docs.google.com/spreadsheets/d/1wa2dY2RWeeoVqVhM1SpQITJriY1MITOAQDd72gpX5dI/edit) or run `python3 tools/check_claimed.py "Company"` before touching any company, and add your claim to its Team Claims tab before you send. Every AAPL attendee company is Ralston's. Andrew's list is Andrew's.
2. Your why-me line must be true for you. If you did not build it, say "one of us did".
3. Every email gets one real fact about them, from a page you can point to.
4. Never mention price. Never promise results. Ralston handles all of that on the call.
5. A yes gets an answer within 2 hours, Ralston copied, three specific times offered.

## What is in the folder

- `CLAUDE.md`: the agent's operating manual.
- `MY_PROFILE.md`: your details, filled in once.
- `playbook/`: who we target, how to write the emails, how to find leads and emails, how to handle replies.
- `Claimed_Companies.xlsx`: who is taken, plus Do Not Contact and the weekly Scoreboard.
- `tools/`: the email checker, the text linter, and the claimed-company checker.
- `skills/`: the five skills and their installer.
