---
type:
status:
format:
tags: []
aliases: []
created: 2026-02-19 03:51:54
modified: 2026-02-28 21:20:35
---

# OpenClaw CLI Power User Guide

## Command-Driven Agent Operation for Maximum Control

*Updated for Saboor — February 28, 2026*

*Based on: OpenClaw 2026.2.x, four-device architecture across Big Pi / Mac / Small Pi / Cloud VM*

-----

## 1. What OpenClaw Actually Is (No Hype, No Fear)

OpenClaw is a self-hosted AI agent runtime with a Gateway architecture. Here's the mechanical reality:

**The Gateway** (`localhost:18789`) is a WebSocket server that acts as a single control plane. It receives messages from channels (WhatsApp, Telegram, iMessage, CLI), routes them to agents, and dispatches tool calls. Every interaction — whether from your terminal or a chat app — goes through this gateway.

**The Agent Runtime** (PiEmbeddedRunner) loads your workspace files (`AGENTS.md`, `SOUL.md`, `TOOLS.md`) into the system prompt, queries memory for relevant context, then streams the assembled prompt to your configured model provider. When the model responds with tool calls, the runtime executes them on the appropriate node.

**Your current four-device setup:**

|Device         |Role              |Node Name        |What It Does                                                               |
|---------------|------------------|-----------------|--------------------------------------------------------------------------|
|Big Pi         |Controller / Brain|*(gateway host)* |Runs the main gateway + control plane. Source of truth for node status.   |
|MacBook (M1)   |Attached Node     |`mac-hands`      |Executes delegated tasks. Connected to Big Pi via local tunnel.           |
|Small Pi       |Lightweight Node  |*(separate node)*|Available for lightweight, parallel, or isolated work.                    |
|Cloud VM (GCP) |Heavy-Compute Node|`debian-vm`      |32GB RAM / 300GB disk. Long-running agents, headless sync, batch compute. |

**What "full access" means in practice:** In the main session (on Big Pi), the agent can run bash commands, read/write files, control a browser, manage cron jobs, and send messages. Delegated tasks run on whichever node they're routed to. This is the trade-off you've already accepted. The controls are: the allowlist on channels, `dmPolicy: "allowlist"` on iMessage, and the hooks that log commands.

-----

## 2. Nodes — What They Are and How They Work

This is the most important architecture concept in your current setup. Understanding nodes is what separates running a single AI assistant from running a distributed AI system across your hardware.

### 2.1 The Mental Model

Think of OpenClaw's node system like a general (Big Pi) commanding soldiers (Mac, Small Pi). The general holds the map, knows the mission, and gives orders. The soldiers execute on the ground. The general's view of who's available and healthy is the only truth that matters — the soldiers don't see the full picture.

```
                  ┌─────────────────────────────┐
                  │         Big Pi              │
                  │   (Main Gateway + Brain)    │
                  │   openclaw gateway:18789    │
                  │   Source of truth for       │
                  │   openclaw nodes status     │
                  └──────────┬──────────────────┘
                             │ Tailnet / SSH Tunnel
              ┌──────────────┼──────────────────┐
              │              │                  │
   ┌──────────▼──────┐  ┌────▼───────────┐  ┌──▼───────────────────────┐
   │   Mac (M1)      │  │   Small Pi     │  │  Cloud VM (GCP)         │
   │ mac-hands       │  │ (lightweight)  │  │  debian-vm              │
   │ Dev toolchain   │  │ Parallel /     │  │  32GB RAM / 300GB disk  │
   │ Repos, browser  │  │ isolated ops   │  │  Heavy compute, headless │
   └─────────────────┘  └────────────────┘  └─────────────────────────┘
```

**The single rule:** Always check `openclaw nodes status` on **Big Pi** to know the true state of your network. Mac's local `nodes status` output reflects only Mac's gateway context — not network truth.

### 2.2 What a Node Is

A **node** is any machine running the OpenClaw node agent, connected to your gateway. It's not an agent (that's the AI personality). It's not a session (that's a conversation thread). A node is raw compute — a machine that can accept and execute tool calls on behalf of the gateway.

Every node exposes:

- **Bash execution** — run shell commands on that machine
- **File system access** — read/write relative to the node's home directory
- **Installed tools** — whatever's on that machine (git, node, python, etc.)
- **Network identity** — its own IP, hostname, and tunnel address

### 2.3 Node vs. Agent vs. Session — The Key Distinction

This trips people up. Here's the clear breakdown:

|Concept    |What It Is                                       |Example                                   |
|-----------|-------------------------------------------------|------------------------------------------|
|**Node**   |A physical/virtual machine running the node agent|`mac-hands` (MacBook), `debian-vm` (VM)   |
|**Agent**  |An AI personality with its own workspace + memory|`codebot`, `main`, `biz`, `vm-lab`        |
|**Session**|A conversation thread (agent + participant)       |Your iMessage DM                          |

An agent *uses* a node to execute. The same agent can delegate to different nodes depending on what the task needs. You can run the same agent from Big Pi but have it execute bash commands on Mac — that's the power.

-----

## 3. Node CLI Commands — Full Reference

### 3.1 Checking Node Status (Always Run This on Big Pi)

```bash
# List all nodes and their status (run on Big Pi — this is your source of truth)
openclaw nodes status

# JSON output for scripting
openclaw nodes status --json

# Deep probe (tests connectivity + response time)
openclaw nodes status --probe

# Watch mode (refresh every 5s)
openclaw nodes status --watch

# Show only nodes in a specific state
openclaw nodes status --filter connected
openclaw nodes status --filter disconnected
```

**What the output shows:**

```
NODE         STATUS       LAST SEEN    CAPABILITIES
big-pi       connected    now          bash, browser, memory
mac-hands    connected    2s ago       bash, browser, git, node, python
small-pi     connected    8s ago       bash, python
```

### 3.2 Targeting a Specific Node for Execution

```bash
# Send an agent message and specify which node executes the bash tool calls
openclaw agent --message "Run git status in ~/repos/bonny-doon-retreat" --node mac-hands

# Run a command directly on a node (bypasses the agent)
openclaw node exec --node mac-hands --cmd "git -C ~/repos/bonny-doon-retreat log --oneline -5"

# Open a shell on a remote node
openclaw node shell --node mac-hands

# Check a specific node's health
openclaw node health --node small-pi

# Restart the node agent on a device
openclaw node restart --node mac-hands
```

### 3.3 Node Registration and Management

```bash
# List registered nodes
openclaw nodes list

# Add a new node (run this on the new machine to register it with Big Pi)
openclaw node register --gateway big-pi:18789 --token <gateway-token>

# Remove a node
openclaw nodes remove small-pi

# View a node's capabilities and config
openclaw nodes info mac-hands

# Update a node's metadata
openclaw nodes set mac-hands --label "MacBook M1 - Development"

# Deactivate without removing
openclaw nodes disable small-pi
openclaw nodes enable small-pi
```

### 3.4 Node-Aware Diagnostics

```bash
# Run doctor across all nodes
openclaw doctor --all-nodes

# Run doctor on a specific node only
openclaw doctor --node mac-hands

# Security audit for a specific node
openclaw security audit --node small-pi

# View logs from a remote node
openclaw logs --node mac-hands --follow

# Check what tools/capabilities are available on each node
openclaw nodes capabilities
```

-----

## 4. Your Four-Device Architecture — How to Use It

### 4.1 Big Pi — The Brain (Control Plane)

Big Pi runs your main gateway. It is the orchestrator. Think of it as always-on infrastructure. It shouldn't be doing heavy compute work itself — it should be *routing* work to other nodes.

**What Big Pi does:**

- Hosts the gateway process (18789)
- Evaluates incoming messages and decides which agent + node handles them
- Maintains the authoritative nodes status
- Runs cron jobs (the scheduler lives here)
- Stores the primary workspace and memory

**What to run on Big Pi:**

```bash
# Health check — your daily habit
openclaw nodes status --probe
openclaw gateway status

# All cron management lives here
openclaw cron list

# Gateway-level logs
openclaw logs --follow
```

**Big Pi workspace path:** `/home/sab-ssd/.openclaw/workspace/`

### 4.2 Mac (mac-hands) — The Development Node

Your Mac is where actual development work happens. It has your full toolchain: Node.js, git, your repos, browser, Supabase CLI, etc. When an agent needs to run code, review files, or operate the browser — it should run on `mac-hands`.

**What Mac does:**

- Executes development tool calls (git, node, python, bash)
- Browser automation for BDR and SCSA projects
- File operations on your repos
- Anything requiring your local development environment

**Practical pattern — routing dev work to Mac:**

```bash
# From Big Pi (or anywhere), force execution on Mac
openclaw agent --agent codebot \
  --message "Run npm run build in ~/repos/bonny-doon-retreat" \
  --node mac-hands

# Direct command execution on Mac from Big Pi
openclaw node exec --node mac-hands \
  --cmd "cd ~/repos/santa-cruz-smart-automations && git status"
```

**Mac's local node agent:** Mac connects *outbound* to Big Pi's gateway via the local tunnel path. This means Mac doesn't need an open inbound port — it's a client, not a server. Don't run `openclaw gateway start` on Mac; that would start a *separate* local gateway context, which is why Mac's `nodes status` doesn't reflect network truth.

### 4.3 Small Pi — The Lightweight / Isolated Node

Small Pi is your second Raspberry Pi. It's lighter than Big Pi and perfect for:

- Background tasks that don't need your dev environment
- Parallel workloads (run something on Small Pi while Mac is busy)
- Isolated or sandboxed jobs where you don't want host access
- Any task where you want physical separation (e.g., testing, scraping, scheduled lightweight ops)

**What to run on Small Pi:**

```bash
# From Big Pi: run a lightweight scrape or check
openclaw agent --message "Check if jasonthelawnman.com is up and responding" \
  --node small-pi \
  --thinking minimal

# Periodic background task delegated to Small Pi
# In a cron job config:
# { "node": "small-pi", "message": "Run health checks on client sites" }
```

**Small Pi's strength is availability.** Because it's a Pi (low power, always on), you can give it long-running monitoring tasks without worrying about it sleeping or shutting down.

### 4.4 Cloud VM (debian-vm) — The Heavy-Compute Node

The GCP Cloud VM is a 32GB RAM / 300GB disk Debian machine. It is the most powerful node in the fleet and is purpose-built for tasks that would slow down or block your Mac.

**Profile name:** `debian-vm`
**State isolation path:** `/work/state/openclaw/debian-vm/`
**Connection:** SSH tunnel → Big Pi gateway (`ws://127.0.0.1:18789` via `ssh -L 18789:127.0.0.1:18789 sab-ssd@100.73.28.125`)
**Systemd services:** `openclaw-node.service` (user), `openclaw-ssh-tunnel.service` (user)

**What the VM does:**

- Long-running compute jobs that would block or overheat the Mac
- Headless Obsidian Sync (`obsidian-headless`) — persistent vault sync without a GUI
- Batch agentic tasks (large refactors, research sweeps, document generation)
- Jules overflow work — heavy implementation tickets that need more RAM
- Isolated sandbox testing — new tools, risky commands, experiments
- Parallel workloads — run something on VM while Mac handles dev

**Node config (`~/.openclaw/openclaw.json` on VM — symlinked from `/work/state/openclaw/debian-vm/`):**

```json
{
  "gateway": {
    "mode": "remote",
    "remote": {
      "url": "ws://127.0.0.1:18789",
      "token": "<must-match-big-pi-gateway-auth-token>"
    }
  }
}
```

**What to run on the VM:**

```bash
# From Big Pi: delegate a heavy compute task to the VM
openclaw agent --agent vm-lab \
  --message "Generate a full research brief on headless Obsidian sync options" \
  --node debian-vm \
  --thinking high

# Direct command on VM (e.g., check disk and RAM)
openclaw node exec --node debian-vm --cmd "free -h && df -h /work"

# Run a long batch job on VM, don't wait
openclaw node exec --node debian-vm \
  --cmd "cd /work/repos/openclaw-lab && ./scripts/run-batch.sh" &
```

**The VM's key advantage:** It never sleeps, never closes a lid, never throttles. Give it anything you want to run overnight or across a long session.

### 4.5 Multi-Node Agent Routing — Putting It Together

Here's how a single agent can intelligently use all four nodes:

```
User → Big Pi Gateway
         │
         ├─ Route: iMessage personal stuff → main agent    → Big Pi (runs locally)
         │
         ├─ Route: dev tasks               → codebot agent → mac-hands
         │
         ├─ Route: background/monitoring   → ops agent     → small-pi
         │
         └─ Route: heavy compute / batch   → vm-lab agent  → debian-vm
```

**Config to route an agent's tool calls to a specific node:**

```bash
# Set default node for each agent
openclaw config set agents.list.codebot.defaultNode "mac-hands"
openclaw config set agents.list.ops.defaultNode "small-pi"
openclaw config set agents.list.vm-lab.defaultNode "debian-vm"

# Now routing is automatic:
openclaw agent --agent codebot --message "Check git log"           # → Mac
openclaw agent --agent ops --message "Check CPU temp"              # → Small Pi
openclaw agent --agent vm-lab --message "Run overnight analysis"   # → Cloud VM
```

### 4.6 Iterative Testing & Delegated Workflows

A key strength of this four-device architecture is the ability to test out capabilities iteratively, delegating the right task to the right node:

- **Mac Node for Mac Tasks:** Start by testing simple commands on `mac-hands` to prove out local interactions with your dev environment (e.g., verifying `npm run build` or BDR deployments).
- **Small Pi for Isolated Ops:** Incrementally move monitoring and cron-based jobs (like testing BDR/SCSA uptimes) to the `small-pi`.
- **Scripting and Automation:** Wrap these validated CLI commands into shell scripts (or `.zshrc`/`.bashrc` functions) to build up complex automation chains.
- **Tmux Sessions for Long-Running Work:** For tasks that take hours (like large code refactors or bulk text extraction), use the CLI to send OpenClaw into a detached named Tmux session. This keeps the agent active without tying up your terminal or requiring an active SSH connection.
  ```bash
  # Start a detached tmux session running an agent task on the VM
  openclaw node exec --node debian-vm --cmd "tmux new-session -d -s refactor-job 'openclaw agent --agent vm-lab --message \"Run the bulk extraction script and log to output.txt\"'"
  ```

-----

## 5. Mission Packets — Coordinating Work Across Nodes

Your test mission doc points to `missions.md` as the coordination layer. This is the right pattern for multi-node work — instead of firing ad-hoc one-shot commands, you define a **mission packet**: a structured task with assigned nodes, success criteria, and outputs.

### 5.1 Mission Packet Format

Create missions in `/home/sab-ssd/.openclaw/workspace/memory/missions.md`:

```markdown
# Missions

---

## MISSION: bdr-build-check
**Status:** pending
**Assigned node:** mac-hands
**Assigned agent:** codebot
**Created:** 2026-02-28

### Objective
Run a full build check on the Bonny Doon Retreat project and report any errors.

### Steps
1. cd ~/repos/bonny-doon-retreat
2. git status (report any uncommitted changes)
3. npm run build (capture output)
4. Report: pass/fail + any error messages

### Success Criteria
- Build exits 0
- No TypeScript errors
- Output delivered to iMessage

### Deliver to
iMessage (reply-channel)

---

## MISSION: site-health-monitor
**Status:** active
**Assigned node:** small-pi
**Assigned agent:** ops
**Schedule:** every 4 hours

### Objective
Check that BDR and SCSA sites are responding with 200.

### Steps
1. curl -o /dev/null -s -w "%{http_code}" https://bonnydoonretreat.com
2. curl -o /dev/null -s -w "%{http_code}" https://santacruzmowandgo.com
3. If either != 200, send alert to iMessage

### Success Criteria
- Both return 200
- Alert sent if either fails
```

### 5.2 Triggering a Mission from the CLI

```bash
# Tell the main agent to read missions.md and execute pending missions
openclaw agent --message "Read missions.md and execute all pending missions" \
  --thinking medium

# Target a specific mission by name
openclaw agent --message "Execute the bdr-build-check mission from missions.md" \
  --agent codebot \
  --node mac-hands

# Check mission status
openclaw memory search "mission status"
```

### 5.3 Your First Test Mission (Right Now)

Per your test mission doc, your single next move is:

**1. Create the missions file on Big Pi:**

```bash
# SSH into Big Pi or run this there directly
vim /home/sab-ssd/.openclaw/workspace/memory/missions.md
```

**2. Write a simple first mission packet:**

```markdown
# Missions

## MISSION: test-001-connectivity
**Status:** pending
**Assigned node:** mac-hands
**Assigned agent:** main
**Created:** 2026-02-28

### Objective
Verify mac-hands is connected and responsive.

### Steps
1. Run `hostname` on mac-hands
2. Run `whoami` on mac-hands
3. Report results

### Success Criteria
- Both commands return expected values
- Response received within 10 seconds
```

**3. Trigger it:**

```bash
openclaw agent --message "Read missions.md and execute mission test-001-connectivity" \
  --node mac-hands
```

**4. Verify on Big Pi:**

```bash
openclaw nodes status --probe
```

-----

## 6. The CLI Surface Area — Everything You Can Do Without Chat

The entire point of this section: every single thing OpenClaw does through natural language chat, you can trigger or configure deterministically through CLI commands.

### 6.1 Sending a One-Shot Agent Turn

```bash
# Basic: send a message to the main agent
openclaw agent --message "Summarize my calendar for this week"

# Target a specific agent
openclaw agent --agent ops --message "Check git status in ~/repos/bonny-doon-retreat"

# Target a specific node for execution
openclaw agent --message "Run npm build" --node mac-hands

# Attach to an existing session
openclaw agent --session-id main --message "What was the last thing we discussed?"

# Control thinking depth
openclaw agent --message "List my cron jobs" --thinking minimal

# Deliver the response to a channel
openclaw agent --message "Generate a status update" --deliver --reply-channel imessage

# JSON output for piping
openclaw agent --message "List active projects" --json
```

### 6.2 Session Management

```bash
openclaw sessions
openclaw sessions --json
openclaw sessions --agent main
openclaw acp health
openclaw sessions --history dm:imessage:+18312959521
```

### 6.3 Configuration

```bash
openclaw config get agents.defaults.model.primary
openclaw config set agents.defaults.model.primary "anthropic/claude-sonnet-4"
openclaw config set agents.list.codebot.defaultNode "mac-hands"
openclaw config unset messages.ackReactionScope
openclaw config show
openclaw configure
openclaw configure --section models
```

### 6.4 Model Management

```bash
openclaw models list --all
openclaw models set anthropic/claude-opus-4-5
openclaw models aliases add opus anthropic/claude-opus-4-5
openclaw models fallbacks add anthropic/claude-sonnet-4
openclaw models auth setup-token
```

### 6.5 Memory System

```bash
openclaw memory status
openclaw memory index --all
openclaw memory search "bonny doon retreat booking system"
openclaw memory search "mission status"
vim ~/.openclaw/workspace/MEMORY.md
vim /home/sab-ssd/.openclaw/workspace/memory/missions.md
```

### 6.6 Cron Jobs

```bash
openclaw cron list
openclaw cron add
openclaw cron edit <job-id>
openclaw cron enable <job-id>
openclaw cron run <job-id>
openclaw cron runs
openclaw cron rm <job-id>
```

**Cron job with node targeting:**

```json
{
  "id": "daily-brief",
  "schedule": "47 6 * * *",
  "message": "Check my calendar for today and tomorrow. Give me a 3-sentence summary.",
  "deliver": true,
  "replyChannel": "imessage",
  "node": "big-pi",
  "thinking": "low",
  "enabled": true
}
```

```json
{
  "id": "site-health-check",
  "schedule": "0 */4 * * *",
  "message": "Check that BDR and SCSA sites return 200. Alert me if either fails.",
  "deliver": true,
  "replyChannel": "imessage",
  "node": "small-pi",
  "thinking": "minimal",
  "enabled": true
}
```

### 6.7 Gateway Control

```bash
openclaw gateway start    # Run on Big Pi only
openclaw gateway stop
openclaw gateway restart
openclaw gateway health
openclaw logs --follow
openclaw logs --node mac-hands --follow
openclaw status --all --deep
```

### 6.8 Diagnostics

```bash
openclaw doctor                        # Local node
openclaw doctor --all-nodes            # All connected nodes
openclaw doctor --node mac-hands
openclaw security audit
openclaw explain <topic>
```

### 6.9 Agent Delegation and Sub-Agents

OpenClaw is designed so that agents can invoke the CLI themselves to delegate tasks. This allows a primary agent to "spin up" its own CLI sub-agents.
- A central agent (like `codebot`) can analyze a massive refactoring task and run `openclaw agent ...` via bash to assign smaller parallel chunks to `vm-lab` or `ops`.
- By delegating CLI tasks, the main agent orchestrates cross-node operations—letting the Mac handle local frontend builds while the Cloud VM runs backend data migrations simultaneously.

-----

## 7. Multi-Agent Architecture

Multiple specialized agents, each with isolated workspaces and node assignments:

### 7.1 Recommended Agent Setup for Your Stack

**Agent: `main` (Personal Assistant)**

- Model: Claude Opus
- Default node: Big Pi (local)
- Channels: iMessage
- Purpose: Calendar, email, personal reminders

**Agent: `codebot` (Development Agent)**

- Model: Claude Sonnet
- Default node: `mac-hands`
- Channels: none (CLI only)
- Purpose: git, builds, code review, BDR and SCSA repos

**Agent: `ops` (Operations / Monitoring)**

- Model: Claude Haiku or Sonnet
- Default node: `small-pi`
- Channels: none (alert via iMessage only)
- Purpose: Site health checks, background monitoring, mission execution

**Agent: `biz` (Business / Client)**

- Model: Claude Sonnet
- Default node: Big Pi
- Channels: none
- Purpose: Lead-to-Review system, client comms drafting

**Agent: `vm-lab` (Heavy Compute / Batch)**

- Model: Claude Sonnet
- Default node: `debian-vm`
- Channels: none (CLI only)
- Purpose: Long-running batch jobs, headless research, compute-heavy tasks, overnight work
- State path: `/work/state/openclaw/debian-vm/`

### 7.2 Setup Commands

```bash
# Create agents
openclaw agents add codebot --workspace ~/.openclaw/workspace-codebot --non-interactive
openclaw agents add ops --workspace ~/.openclaw/workspace-ops --non-interactive
openclaw agents add biz --workspace ~/.openclaw/workspace-biz --non-interactive
openclaw agents add vm-lab --workspace ~/.openclaw/workspace-vm-lab --non-interactive

# Assign default nodes
openclaw config set agents.list.codebot.defaultNode "mac-hands"
openclaw config set agents.list.ops.defaultNode "small-pi"
openclaw config set agents.list.vm-lab.defaultNode "debian-vm"

# Assign models
openclaw config set agents.list.codebot.model.primary "anthropic/claude-sonnet-4"
openclaw config set agents.list.ops.model.primary "anthropic/claude-haiku-4-5"
openclaw config set agents.list.vm-lab.model.primary "anthropic/claude-sonnet-4"

# Target from CLI
openclaw agent --agent codebot --message "Run git status in ~/repos/bonny-doon-retreat"
openclaw agent --agent ops --message "Check CPU temps on Small Pi"
openclaw agent --agent vm-lab --message "Run overnight batch analysis" --node debian-vm
```

-----

## 8. Command-Driven Workflow Patterns

### 8.1 Shell Functions (Add to `~/.zshrc` on Mac, and `~/.bashrc` on Big Pi)

```bash
# Quick agent query
claw() { openclaw agent --message "$*" }

# Dev work → always routes to Mac
claw-code() { openclaw agent --agent codebot --node mac-hands --message "$*" }

# Ops → always routes to Small Pi
claw-ops() { openclaw agent --agent ops --node small-pi --message "$*" }

# Heavy compute → always routes to Cloud VM
claw-vm() { openclaw agent --agent vm-lab --node debian-vm --message "$*" }

# Biz work
claw-biz() { openclaw agent --agent biz --message "$*" }

# Code review: pipe a file to codebot on Mac
claw-review() {
  cat "$1" | openclaw agent --agent codebot --node mac-hands \
    --message "Review this file. Focus on bugs, security, and improvements."
}

# Git commit message generator
claw-commit() {
  git diff --staged | openclaw agent --agent codebot --node mac-hands \
    --message "Write a conventional commit message for this diff. Output ONLY the message." \
    --thinking minimal
}

# Morning brief
claw-morning() {
  openclaw agent --message "Calendar today + tomorrow. Urgent emails. Weather Santa Cruz. 5 sentences max." \
    --thinking low
}

# Memory search
claw-recall() { openclaw memory search "$*" }

# Node status — always ask Big Pi
claw-nodes() { openclaw nodes status --probe }

# Execute a mission
claw-mission() {
  openclaw agent --message "Execute mission $1 from missions.md" --thinking medium
}

# Full system status
claw-status() { openclaw status --all --deep && openclaw nodes status --probe }
```

### 8.2 Piping and Composition

```bash
# Pipe file into codebot on Mac
cat ~/repos/bonny-doon-retreat/js/booking.js | \
  openclaw agent --agent codebot --node mac-hands \
  --message "Review this for security issues"

# Git log → summarize
git -C ~/repos/bonny-doon-retreat log --oneline -20 | \
  openclaw agent --message "Summarize this git log in 3 bullets"

# Chain: run on Mac, get output, send to iMessage
openclaw node exec --node mac-hands \
  --cmd "cd ~/repos/bonny-doon-retreat && npm run build 2>&1" | \
  openclaw agent --message "Summarize this build output. Was it successful?" \
  --deliver --reply-channel imessage
```

### 8.3 Slash Commands (In-Session)

```
/status          — system health
/nodes           — show node status
/new             — start fresh session
/stop            — abort current execution
/model <alias>   — switch model
/thinking high   — increase reasoning depth
/config show     — view config
```

### 8.4 Cross-Environment Project Orchestration

Managing multi-repo, multi-environment projects requires agents that can context switch and operate on different nodes seamlessly. This is especially true for your core ecosystem:

- **GDDP-Runtime & GDDP-config:** Heavy lifting, configuration generation, and runtime environment execution can be routed to the **Cloud VM** (`debian-vm`), ensuring consistent execution away from local dev quirks.
- **MyAPI (Context Refinery):** You can instruct `codebot` on `mac-hands` to run local tests and build the React frontend, while simultaneously having the `vm-lab` agent handle the RAG/Khoj data synchronization and headless Obsidian sync.
- **Unified Workflow:** Use Mission Packets to string these together. For example, a single mission could require `codebot` to commit changes to GDDP-config on Mac, deploy them via a push, and then tell `ops` on Small Pi to verify the deployed services.

-----

## 9. Workspace File Strategy

|File                  |Purpose                                           |Edit Frequency         |
|----------------------|--------------------------------------------------|-----------------------|
|`AGENTS.md`           |Operating contract: priorities, workflow rules    |Rarely                 |
|`SOUL.md`             |Personality and values                            |Rarely                 |
|`TOOLS.md`            |SSH hosts, device names, node names, API endpoints|As setup changes       |
|`MEMORY.md`           |Long-term curated memory                          |Agent maintains        |
|`memory/missions.md`  |Active mission packets                            |You + agent co-maintain|
|`memory/YYYY-MM-DD.md`|Daily raw logs                                    |Agent writes           |
|`BOOT.md`             |Startup ritual                                    |Rarely                 |

**Add to `TOOLS.md` — your node map:**

```markdown
## Node Map
- big-pi:    Main gateway. Brain. Always on. Path: /home/sab-ssd/ | Tailscale: 100.73.28.125
- mac-hands: M1 MacBook. Dev toolchain. Repos at ~/repos/
- small-pi:  Lightweight Pi. Background tasks. Monitoring. | Tailscale: 100.87.206.30
- debian-vm: GCP Cloud VM. 32GB RAM / 300GB disk. Heavy compute, headless sync, batch jobs.
             State: /work/state/openclaw/debian-vm/ | Connects via SSH tunnel to big-pi.

## Source of Truth
- Always check `openclaw nodes status` on big-pi for network state.
- Do NOT trust mac-hands or debian-vm local node status for full network topology.
- debian-vm state is ISOLATED to /work/state/openclaw/debian-vm/ — never shares with other nodes.
```

-----

## 10. Safety Model — Four Devices Edition

**What you have working:**

- `dmPolicy: "allowlist"` on iMessage
- `command-logger` hook — audits all commands on all nodes
- Gateway token auth on tailnet
- Mac connects outbound only (no exposed inbound port on Mac)

**Multi-node additions to be aware of:**

- Each node runs commands with *that machine's* user permissions. Mac runs as your Mac user. Small Pi runs as its Pi user. Be intentional about what you delegate where.
- If you expose Small Pi to group chats or external channels, configure sandboxing on that node first: `openclaw config set nodes.small-pi.sandbox true`
- Node-to-node communication goes through Big Pi's gateway, not directly. A rogue task on Small Pi can't directly touch Mac's files unless the gateway routes it there.
- Keep `openclaw doctor --all-nodes` as a weekly habit.

**Rotation checklist (monthly):**

```bash
openclaw models auth setup-token     # Rotate Anthropic token
openclaw security audit --all-nodes  # Check all nodes
openclaw doctor --deep --all-nodes   # Auto-fix across fleet
```

-----

## 11. Your Current Setup — What's Working, What to Add

**Already solid:**

- Big Pi as gateway (control plane)
- Mac connected via local tunnel as `mac-hands`
- Small Pi running and available
- **Cloud VM (`debian-vm`) installed, connected, and hardened** ✅
  - OpenClaw installed and running as a Remote Node
  - SSH tunnel to Big Pi established and persisted via systemd
  - State isolated to `/work/state/openclaw/debian-vm/`
  - Zsh prompt customized
- Hooks enabled (boot-md, command-logger, session-memory)
- iMessage on allowlist policy

**Recommended next steps (in order):**

1. **Verify debian-vm node is visible from Big Pi:**

	```bash
   # Run on Big Pi
   openclaw nodes status --probe
   # debian-vm should appear as connected
   ```

2. **Create `missions.md` on Big Pi** and write your first test mission targeting `debian-vm`:

	```bash
   vim /home/sab-ssd/.openclaw/workspace/memory/missions.md
   ```

3. **Run first test mission** — verify debian-vm connectivity end-to-end
4. **Add node assignments to agent configs:**

	```bash
   openclaw config set agents.list.codebot.defaultNode "mac-hands"
   openclaw config set agents.list.vm-lab.defaultNode "debian-vm"
   ```

5. **Add shell aliases on Mac, Big Pi, and VM** — the functions in Section 8.1 (including `claw-vm`)
6. **Update `TOOLS.md`** — document your 4-node map so agents know the topology
7. **Create `vm-lab` agent** — give it a workspace and assign it to `debian-vm`
8. **Create `ops` agent** — assign to `small-pi`, set up site health cron
9. **Push workspace to private GitHub** — your workspace has `.git` but needs a remote
10. **Create project skills:**

	```
   ~/.openclaw/workspace/skills/
   ├── bdr-project/SKILL.md
   ├── sc-automations/SKILL.md
   └── node-ops/SKILL.md          ← Documents your 4-device topology
   ```

-----

## 12. Quick Reference Card

```bash
# === NODES (Always run on Big Pi) ===
openclaw nodes status --probe            # Source of truth for network
openclaw nodes status --watch            # Live refresh
openclaw node exec --node mac-hands --cmd "..."  # Direct command on a node
openclaw node shell --node mac-hands     # Interactive shell on node
openclaw doctor --all-nodes             # Health check all devices

# === AGENT + NODE TARGETING ===
claw "question"                          # Main agent, Big Pi
claw-code "dev question"                 # Codebot → mac-hands
claw-ops "monitor task"                  # Ops → small-pi
claw-vm "heavy task"                     # vm-lab → debian-vm (Cloud VM)
openclaw agent --agent X --node Y --message "..."  # Explicit routing

# === MISSIONS ===
claw-mission test-001-connectivity       # Execute named mission
openclaw memory search "mission"         # Check mission status

# === DAILY USE ===
openclaw status --all --deep             # Full health
openclaw gateway status                  # Gateway only
openclaw logs --follow                   # Live logs
openclaw logs --node mac-hands --follow  # Node-specific logs

# === AUTOMATION ===
openclaw cron list
openclaw cron add
openclaw cron run <id>

# === MEMORY ===
openclaw memory search "query"
openclaw memory index --all

# === CONFIG ===
openclaw config get <key>
openclaw config set <key> <value>
openclaw config set agents.list.codebot.defaultNode "mac-hands"
```

-----

*This guide covers OpenClaw 2026.2.x. Run `openclaw update` to stay current. Check `openclaw --help` and docs.openclaw.ai for version-specific changes.*

---

## 13. VM (debian-vm) Test Missions — Genuinely Useful Smoke Tests

These are real tasks that serve double duty: they verify the node is healthy AND produce useful output.

### Test 1 — Connectivity & Identity Check (30 seconds)
```bash
# From Big Pi — confirm VM is visible and responsive
openclaw nodes status --probe

# Direct command: confirm we're on the right machine
openclaw node exec --node debian-vm --cmd "hostname && whoami && openclaw --version"
```
**Expected:** `debian-vm` appears as connected, outputs VM hostname, user (`saboor`), and version `2026.2.x`.

### Test 2 — State Isolation Verification (2 minutes)
```bash
# Confirm symlink is correct — should resolve to /work/state/openclaw/debian-vm/
openclaw node exec --node debian-vm --cmd "ls -la ~/.openclaw"

# Run the preflight guard
openclaw node exec --node debian-vm --cmd "bash /work/repos/dotfiles/openclaw/scripts/assert-isolated-state.sh"
```
**Expected:** `~/.openclaw` is a symlink to `/work/state/openclaw/debian-vm/`, guard exits 0.

### Test 3 — Disk & RAM Inventory (1 minute, genuinely useful)
```bash
# Useful output: how much room do we have?
openclaw node exec --node debian-vm --cmd "free -h && echo '---' && df -h /work"
```
**Expected:** Shows ~32GB RAM mostly free, ~300GB disk with `/work` mounted. Save output for capacity planning.

### Test 4 — Vault Sync Health Check (3 minutes)
```bash
# Is headless Obsidian sync running and up to date?
openclaw node exec --node debian-vm --cmd "systemctl --user status obsidian-headless.service"

# Check vault file freshness — last modified time on vault root
openclaw node exec --node debian-vm --cmd "stat /work/vaults/SoloDeveloper | grep Modify"
```
**Expected:** Service is `active (running)`, vault was modified recently (within sync window).

### Test 5 — Agent Round-Trip (5 minutes, the real test)
```bash
# From Big Pi: send a real task to the VM agent and get a response
openclaw agent \
  --agent main \
  --node debian-vm \
  --message "Run 'df -h /work && free -h' and give me a one-sentence summary of available capacity." \
  --thinking minimal
```
**Expected:** Agent responds with a human-readable summary. This proves the full loop: gateway → SSH tunnel → VM node → bash tool → response → back.

### Running All 5 in Sequence
```bash
# Quick smoke-test script (run from Big Pi)
for TEST in \
  "hostname && whoami && openclaw --version" \
  "ls -la ~/.openclaw" \
  "free -h && df -h /work" \
  "systemctl --user status openclaw-node.service --no-pager"
do
  echo "=== $TEST ==="
  openclaw node exec --node debian-vm --cmd "$TEST"
  echo
done
```
