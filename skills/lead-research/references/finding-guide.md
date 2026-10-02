# 03. Finding leads and emails

How to find companies in your territory, the right person at each, and a work email that will not bounce. The agent does most of this with web search and page fetching. The sender handles anything that needs a login.

Every company, before any research: `python3 tools/check_claimed.py "Company" --domain site.com`. TAKEN means skip.

## Part 1. Where to find companies

The AAPL 72nd Annual Meeting attendee list is Ralston's, and every company on it is claimed. Find your own in your territory (`MY_PROFILE.md`). Good sources, roughly in order of quality:

1. **Industry events you can actually attend.** This is how Ralston built his list: registering for the AAPL annual meeting gave him the event app, and the app's attendee directory listed names, companies, and often emails and LinkedIn links. Regional landman association meetings, luncheons and expos work the same way. Each regional association (Tulsa, Oklahoma City, Fort Worth, Dallas, Houston, Denver, the Permian Basin and others) has a site with an events page. Larger expos such as NAPE publish exhibitor lists. See Part 4 for how the agent helps with an event app.
2. **Association websites.** Officer and board pages, committee pages, sponsor lists and past event programs name real people at real firms. Sponsors of a local landman luncheon are often exactly our buyers.
3. **Job boards.** Search EnergyHire, Rigzone, Indeed and LinkedIn Jobs for "landman", "lease analyst", "land administrator", "title analyst", "right of way agent" in your territory. A small firm hiring for back-office roles is a strong signal (01, stronger signals).
4. **State oil and gas regulators.** Pooling, spacing and hearing applications are public in most producing states (for example the New Mexico OCD case files, the Oklahoma Corporation Commission, the North Dakota Industrial Commission, Colorado's ECMC). Applications show which operators are active, and often name the operator's landman. Land services firms show up there too.
5. **Maps and directories.** Search Google Maps for "land services", "landman", "right of way services" or "abstract company" in Midland, Oklahoma City, Tulsa, Houston, Denver, Pittsburgh, Shreveport, Bismarck and other oil towns. Check each site.
6. **Your own network.** Former coworkers, classmates and family in the industry. A warm introduction beats any cold email: ask for the intro first, then email.

Do not buy lead lists, do not scrape LinkedIn, and do not use anything that needed someone else's login.

## Part 2. Finding the right person

Write to the person who feels the hours and can say yes to a call: owner, principal, president, VP or Director of Land, land manager, COO at a small firm (01, the client we want).

- **Their own site first:** About, Team, Leadership, Our People pages, and bios in PDFs (statements of qualifications, brochures).
- **LinkedIn** for current title and tenure. The sender looks it up. The agent does not log in. If the site and LinkedIn disagree on the title, hold until you know.
- **News and press releases** for recent hires and promotions.
- One person per company. If the owner is unreachable, the next best is whoever runs land administration or operations.

## Part 3. Finding a work email

Work down this list and stop at the first one that gives a confirmed address. Write down which step worked: it goes in the draft block as the email source.

1. **Published on their site.** Team page, contact page, `mailto:` links, bios, PDFs. Ask the agent to fetch the pages and search for "@theirdomain.com".
2. **Published elsewhere.** Search, for example:
   - `"@theirdomain.com"` (with quotes)
   - `"First Last" "theirdomain.com"`
   - `site:theirdomain.com filetype:pdf`
   - `"First Last" landman email`
   Association pages, event programs, regulator filings, and conference speaker pages often show a work email.
3. **The event app or directory you legitimately have access to** (Part 4).
4. **Pattern plus verification.** Find any confirmed address at the same domain (a job post saying "send resumes to jane.doe@...", a filing, a press contact). That gives the pattern: first.last, flast, first, firstl. Build the address for your person, then **verify it** before using it:
   - Free or cheap verifiers: Hunter (finder plus verifier, free monthly searches), NeverBounce, ZeroBounce, MillionVerifier, Apollo's free credits.
   - "Valid" or "deliverable": usable. Record "pattern from {source URL}, verified by {tool}".
   - "Accept-all" or "catch-all": the server accepts everything, so the check proves nothing. Use only if the pattern came from a confirmed address at that domain, and count it as risky.
   - "Invalid" or "unknown": do not send.
5. **Call the main line.** "Hi, I'm trying to send a note to {name}, what's the best email for them?" Landmen pick up the phone. The sender does this, not the agent.
6. **Nothing works:** drop the lead. Never send to a guessed address, and never use a generic info@ address for a first email.

**Bounce rule.** Bounces must stay under 2% of sends. One bounce in a day: stop and recheck the rest of that day's addresses. More than 2% in a week, or any "blocked" notice: everyone pauses and tells Ralston.

## Part 4. Using the agent with an event app or directory

Event apps (Whova, Cvent, Swapcard and similar) and member directories sit behind a login, and many do not let you click through or export everything. The agent cannot log in for you. Here is the split:

1. **The sender** registers for an event they will genuinely attend, opens the attendee directory, and gets the data out the honest way: the app's own export if it has one, copy and paste of the list view, or screenshots of the directory pages.
2. **The agent** turns that into a clean table: name, title, company, email if shown, LinkedIn link if shown, location.
3. **The agent** runs every company through `check_claimed.py --file` (one company per line) and drops anything TAKEN.
4. **The agent** scores the rest against `01_ICP.md` and returns a ranked shortlist with a reason for each.
5. **For each shortlisted person**, the agent finds the work email on the company's own site where it can (Part 3), even if the app showed one. A published address is the safest source.

Rules for event data:

- Read the event's terms. Some prohibit using the attendee list for solicitation. When in doubt, use the app only to learn names and companies, and find the work email from the company's own site.
- Only mention the event in an email if the sender actually attended. Never "great meeting you" unless you met.
- Event data stays on the sender's machine. Do not put attendee emails in shared files.

## Part 5. Prompts the sender can give the agent

Paste these and fill the braces.

**Build a lead list.**
> Using playbook/03 Part 1, find 15 land services firms or small operators in {territory} that fit playbook/01_ICP.md. For each: company, website domain, city, why it fits, and the source URL. Run tools/check_claimed.py on each and drop anything TAKEN. Rank by fit.

**Find the person and email.**
> For {company} ({domain}): find the owner, president or land manager using playbook/03 Part 2. Then find their work email using Part 3, step by step, and tell me which step worked, with the URL. If you only have a pattern, give me the address to verify and stop there.

**Research the personal line.**
> Spend about five minutes on {person} at {company}. Give me three candidate personal lines for the first email, each one sentence under 20 words, each with its source URL, ranked by playbook/02 section 4. No flattery, no guesses about their problems.

**Draft the email.**
> Draft the first email to {person} at {company} using playbook/02 and my why-me line from MY_PROFILE.md. Use personal line {n}. Run the checker and the linter and give me the draft block from CLAUDE.md.

**Process an event export.**
> Here is the attendee list I copied from {event} (pasted below or attached). Follow playbook/03 Part 4: clean it, check claims, score against the ICP, and give me the top 20 with reasons.

**Morning check.**
> Run the daily loop in CLAUDE.md. Start with replies, then follow-ups due today, then queue tomorrow's 8 new leads.

## Part 6. What to record for every lead

Keep this in your own notes (not the shared claims sheet): name, title, company, domain, email, email source (step number and URL), personal line source URL, time zone, first email date, follow-up dates, status. The shared sheet only gets company, domain, your name, date, and status.
