# Stoneworks outreach kit

A kit for a small team that books discovery calls with land services firms and energy operators by cold email, with each person working alongside their own Claude agent. It includes the agent's operating manual, the ICP, the email and reply playbooks, a lead and email research guide, small checker tools, and five skills.

**Start with [START_HERE.md](START_HERE.md).** The agent reads [CLAUDE.md](CLAUDE.md) automatically when you open Claude Code in this folder.

| Path | What it is |
|---|---|
| `CLAUDE.md` | Operating manual for the agent: hard rules, daily loop, draft format |
| `MY_PROFILE.md` | Each sender's details, filled in once (`{{FILL: ...}}` fields) |
| `playbook/` | ICP, email playbook, finding leads and emails, replies and booking |
| `tools/` | `check_email.py`, `lint_text.py`, `check_claimed.py` |
| `skills/` | cold-email, de-slop, chat-voice, lead-research, call-prep-onepager, plus `install.sh` |

## Not in this repo

The list of companies already being worked (`Claimed_Companies.xlsx`) is private prospect data, so it lives in a private Google Sheet and is listed in `.gitignore`. Teammates get access from Ralston. `tools/check_claimed.py` needs that file in the kit folder, or CSV exports of the sheet.

## Conventions

- No em dashes or en dashes in anything that gets sent.
- Agents draft; people send, from their own Gmail.
- No prices, no promises of results, and no claims of work that has not been done.
