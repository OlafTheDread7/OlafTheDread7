# Jake Chaney

I'm an IT project manager in Richmond, Virginia. I've worked in tech and data for more than ten years. Eight of those were at Amazon, where I started on the floor at RIC2 and worked my way into labor-planning analytics. I spent almost three years at Deltek automating data collection from more than 100 government sources for GovWin IQ. That work saved $1.5 million a year. Now I run IT projects at a regulated environmental testing lab.

I also run [RVA Digital Works](https://rvadigitalworks.com), building websites and local search for Richmond small businesses. More than 20 sites shipped so far.

Most of my code is in private repos. It belongs to clients or touches real data. The public repos are tools I built for myself and cleaned up to share, running on sample or public data so I can show the work without exposing anybody.

## What's here

| Repo | What it is |
|---|---|
| [ai-review-gate](https://github.com/OlafTheDread7/ai-review-gate) | A GitHub Action that has Claude check every push for security and architecture problems. The deploy waits until it passes. It gates more than 30 of my repos on Vercel and Railway. Python, Bash, PowerShell. |
| [dev-layout-kit](https://github.com/OlafTheDread7/dev-layout-kit) | I use the same folder layout on three PCs. This PowerShell script builds it, moves projects into place, clones what's missing and writes the index my AI agents read before they touch anything. |
| [sleeper-control-panel](https://github.com/OlafTheDread7/sleeper-control-panel) | Google Apps Script that turns a Sheet into a control panel for a Sleeper fantasy football league. Start/sit uses target and carry share, the opponent and the weather. Not projected points. |
| [a11y-scanner](https://github.com/OlafTheDread7/a11y-scanner) | Crawls a site and fills in the machine half of a 50-criterion WCAG 2.1 AA worksheet. It tells you which 19 criteria still need a person. Python, Playwright, axe. |
| [rva-web-presence-study](https://github.com/OlafTheDread7/rva-web-presence-study) | A random-sample audit of small business websites around Richmond. The sample comes from the state business registry, with a published seed. About a third had no website at all. |
| [nfl-cold-weather-qb-study](https://github.com/OlafTheDread7/nfl-cold-weather-qb-study) | A pre-registered test of whether the shape of a quarterback's release predicts interceptions in games under 40 degrees. Uses 25 years of public nflverse data. The labels are frozen. The 2026 season is the real test. |
| [dodofin](https://github.com/OlafTheDread7/dodofin) | A small personal finance app I built in 2025. Runs in the terminal with Python and SQLite. It imports bank CSVs and handles categorizing, budgets and a snowball or avalanche debt payoff plan. Includes a fake-data generator. |

## How I work

I use Claude as my pair and push straight to `main`. Nothing goes live until the AI Review gate passes. Most of my work is in SQL, Python and PowerShell. I use Power BI and Excel for reporting, and I've built RPA in UiPath.

## Find me

- [jfchaney.com](https://jfchaney.com)
- [LinkedIn](https://www.linkedin.com/in/jfchaney)
- jake@rvadigitalworks.com

The avatar is drawn in code. [`avatar/make_avatar.py`](avatar/make_avatar.py) writes the SVG. The ring around it spells OLAF THE DREAD in Elder Futhark runes.
