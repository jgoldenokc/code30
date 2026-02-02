# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a "30 Days of Code" learning project with daily coding exercises in multiple programming languages.

## Structure

```
code30/
├── day1/          # Hello World
├── day2/          # Variables, user input, date/time
├── day3/          # Conditionals (if/elif/else)
├── day4/          # Loops (for, while, break, continue)
├── day5/
│   └── sideproject/   # Twitter/X affirmation bot using Tweepy
```

Each day folder contains subdirectories by language:
- `Python/` - Python 3 scripts
- `JS/` or `JSC/` - Node.js scripts
- `Ruby/` - Ruby scripts

## Running Code

**Python:**
```bash
python day2/Python/bio.py
```

**JavaScript (Node.js):**
```bash
node day2/JSC/hello.js
```

**Ruby:**
```bash
ruby day1/Ruby/day1/hello
```

## Side Project: Twitter Bot (day5/sideproject)

Uses Tweepy to post random affirmations to Twitter/X. Requires:
- `tweepy` and `python-dotenv` packages
- Twitter API credentials in environment variables
