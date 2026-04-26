---
title: VM Tailscale SSH Access Anchor
aliases:
  - VM access
  - Tailscale access
  - SSH access
  - GCP VM access
  - instance-20260418-024637
  - khoj-vm-new
source: obsidian
document_kind: synthesized_note
type: anchor
status: active
projects:
  - myapi
  - context-refinery
  - vm-operations
tags:
  - tailscale
  - ssh
  - vm
benchmark_targets:
  - retrieval-benchmark-v0/Q16
related:
  - my-devinfra-system-anchor
  - khoj-deployment-indexing-anchor
  - current-system-end-to-end-anchor
---

# VM Tailscale SSH Access Anchor

## What This Is

This is the access runbook for the GCP VM that runs Khoj and Context Refinery for the My_DevInfra system. It covers how to reach the VM, what machine it is, what the access paths are, and what breaks most often.

This note is the canonical answer to "What notes are tied to Tailscale, SSH, or VM access?"

## Current Access Facts

| Field | Value |
|---|---|
| VM name | `instance-20260418-024637` |
| GCP project | `project-ab32182e-5782-4a9c-939` |
| Zone | `us-central1-a` |
| Machine type | `e2-highmem-4` |
| Tailscale IP | `100.85.100.52` |
| SSH alias | `ssh khoj-vm-new` (via Tailscale) |
| RAM | ~31Gi |
| Auto-shutdown | 6-hour max run duration (`instanceTerminationAction: STOP`) |

## Access Paths

**From Mac via Tailscale (preferred):**
```bash
ssh khoj-vm-new
```
This uses the SSH alias configured in `~/.ssh/config` pointing at `100.85.100.52`. Works from Mac and Antigravity IDE.

**From Mac via gcloud IAP:**
```bash
gcloud compute ssh instance-20260418-024637 --zone us-central1-a --project project-ab32182e-5782-4a9c-939
```

**Check VM status remotely:**
```bash
gcloud compute instances describe instance-20260418-024637 --zone us-central1-a --project project-ab32182e-5782-4a9c-939 --format='table(name,status,machineType.basename(),networkInterfaces[0].accessConfigs[0].natIP)'
```

**Start a stopped VM:**
```bash
gcloud compute instances start instance-20260418-024637 --zone us-central1-a --project project-ab32182e-5782-4a9c-939
```

## Service Checks

Run on the VM after connecting:

```bash
# 1. Are services running?
systemctl is-active khoj.service context-refinery.service

# 2. Khoj health
curl -sS http://localhost:42110/api/health

# 3. Context Refinery health
curl -sS http://localhost:8000/health

# 4. Smoke test query
curl -sS -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"q":"test","n":1}'
```

## Disk Layout

| Mount | Device | Size | Contents |
|---|---|---|---|
| `/` | `/dev/sda1` | 50GB (~49G usable) | OS, system packages |
| `/data` | `/dev/sdb` | 200GB (~197G usable) | repos, khoj venv, persistent data |

- `/data` is mounted via fstab using UUID `1876e9a7-9bce-42a4-ae20-b8655a5ac592` (stable across reboots, doesn't break if device name changes).
- Note corpus lives at `~/khoj-data/notes/` (on root disk, not `/data`).
- Khoj venv at `/data/khoj-venv`.
- MyAPI repo at `/data/repos/MyAPI`.

```bash
# Check disk usage
df -h / /data

# Check block devices
lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS
```

## Recovery Cases

**VM won't start — ZONE_RESOURCE_POOL_EXHAUSTED:**
GCP can refuse to start a stopped VM if the machine family is unavailable. This happened with `n1-highmem-4`. Fix: stop the VM, change machine type to `e2-highmem-4` (or another available family), start again.

**Root disk full:**
Root is `/dev/sda1`. Clean temp files, logs, apt cache. Resize if needed: `sudo growpart /dev/sda 1 && sudo resize2fs /dev/sda1` (requires `cloud-guest-utils` package).

**Data disk full:**
Data is `/dev/sdb` (raw device, no partition table). Clean `/data` contents. Resize: expand disk in GCP console, then `sudo resize2fs /dev/sdb`.

**Services active but queries fail — stale KHOJ_URL:**
Context Refinery health returns OK but `/query` errors because `KHOJ_URL` in `~/MyAPI/.env` points at an old Tailscale IP instead of `http://localhost:42110`. Fix: update `.env`, `sudo systemctl restart context-refinery.service`.

**Services fail after repo relocation:**
Systemd units reference `WorkingDirectory`. If the repo moved (e.g., from `/home/saboor/MyAPI` to `/data/repos/MyAPI`), update the unit files under `/etc/systemd/system/`, run `systemctl daemon-reload`, restart.

**VM stops after 6 hours:**
This is intentional. The VM has a 6-hour auto-shutdown to control compute costs. Start it again when needed.

## Important Commands or Files

VM paths:

- `/etc/systemd/system/khoj.service` — Khoj systemd unit
- `/etc/systemd/system/context-refinery.service` — Context Refinery systemd unit
- `~/MyAPI/.env` — environment variables
- `~/khoj-data/notes/` — indexed note corpus
- `/data/khoj-venv/` — Khoj Python venv
- `/data/repos/MyAPI/` — MyAPI repo on VM

Mac paths:

- `~/.ssh/config` — contains `khoj-vm-new` alias

## Failure Modes / Gotchas

- Device names (`/dev/sdb`) can change after VM stop/start. The fstab UUID mount prevents breakage, but manual `resize2fs` commands should verify the current device with `lsblk` first.
- Tailscale IP is stable (`100.85.100.52`) but external IP may change after stop/start.
- `growpart` is from `cloud-guest-utils`, not installed by default on all Debian images.
- The 6-hour auto-shutdown means the VM is usually off. Budget ~2 minutes for cold start + service initialization.

## Source Evidence

- `project-docs/VM-MIGRATION-SPRINT.md`
- `project-docs/VM-MIGRATION-HANDOFF.md`
- `project-docs/retrieval-benchmark-v0/refinement-queue-2026-04-20.md`
- 2026-04-20 repair session: machine type switch, disk expansion, systemd path repair, KHOJ_URL repair
