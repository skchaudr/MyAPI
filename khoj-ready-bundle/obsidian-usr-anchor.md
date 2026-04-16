---
type: project
title: Personal Briefing & Capture System
created: 2026-04-16 00:00:00
modified: 2026-04-16 00:00:00
tags: [project, automation, briefing, capture, obsidian, shortcuts, reminders, github, anchor]
category:
project: Personal Briefing & Capture System
status: active
aliases:
  - My_DevInfra
  - Personal Automation Hub
  - Obsidian Automation Hub
  - Daily Ops
  - Personal Ops
  - Briefing & Capture System
  - My Dev Infra
---

## Summary
`Personal Briefing & Capture System` is the canonical project name for the system previously called `My_DevInfra`. It is a personal automation and briefing hub that connects Apple Shortcuts, Obsidian, reminders, GitHub, and shell scripts into a single capture-and-briefing workflow across macOS, iPadOS, and iOS.

The system is designed to turn quick captures, daily briefings, and task routing into reliable terminal-driven automation rather than vague infrastructure tooling.

## Core Tech Stack
- Bash / Shell Scripting (POSIX and Bash)
- Apple Shortcuts
- a-Shell (iOS/iPadOS terminal environment)
- Git (and lg2 on iOS)
- Obsidian
- GitHub API (via curl and gh CLI)
- Apple Reminders
- Shortcut-driven capture flows

## Current State of the Project
The project has established a strong foundational architecture featuring a functional universal router (`core/router.sh` for macOS and `core/router-ios.sh` for iOS). This routing engine dynamically parses arguments to dispatch workflows into specific handlers such as GitHub status briefings (`handlers/briefing`), clipboard sanitization (`handlers/clip`), health tracking (`handlers/health`), reminders/task routing, and Obsidian file appending (`handlers/obsidian`).

The overall design is modular and supports a live pipeline of multi-device interactions initiated by user-defined Apple Shortcuts and shell commands.

## Key Functions
- Morning briefings
- Evening briefings
- Obsidian capture and append workflows
- GitHub and repo-state summaries
- Reminder ingestion and task routing
- Clipboard normalization and cleanup
- Cross-device command routing

## Main Unsolved Problems
- **Cross-Platform Compatibility Issues:** As noted in `.git/hooks/pre-commit.sample`, cross-platform behavior can occasionally result in workflow friction for users sharing code across different environments.
- **Limited GitHub API Handling on iOS:** The iOS router logic (`core/router-ios.sh`) currently lacks parity with macOS for complex tasks, relying on raw `curl` commands and manual `base64` encoding (such as in the `deposit` function) to interact with GitHub, which is harder to maintain than the dedicated `gh` CLI used on macOS.
- **Hardcoded Filepaths and Dependencies:** Environment setups, particularly in `router-ios.sh`, rely heavily on hardcoded path locations (like `$HOME/Documents/SoloDeveloper` and `$HOME/Documents/My_DevInfra`), making it less adaptable out-of-the-box for other users.
