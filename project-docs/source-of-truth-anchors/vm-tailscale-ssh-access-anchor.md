---
title: VM Tailscale SSH Access Anchor
aliases:
  - VM access
  - Tailscale access
  - SSH access
  - GCP VM access
  - instance-20260418-024637
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
  - gcp
  - vm
  - operations
  - runbook
benchmark_targets:
  - retrieval-benchmark-v0/Q16
related:
  - my-devinfra-system-anchor
  - khoj-deployment-indexing-anchor
  - current-system-end-to-end-anchor
---

# VM Tailscale SSH Access Anchor

## What This Is

This note is the source-of-truth access runbook for the current Google Cloud VM that runs Khoj and Context Refinery.

It exists so VM, SSH, Tailscale, service-health, and disk-recovery queries retrieve a compact operational anchor instead of raw command transcripts.

## Current State

As of 2026-04-20:

- VM name: `instance-20260418-024637`
- GCP project: `project-ab32182e-5782-4a9c-939`
- Zone: `us-central1-a`
- Machine type: `e2-highmem-4`
- External IP: `34.29.11.95`
- Tailscale IP: `100.85.100.52`
- RAM: about `31Gi`
- Boot disk: `50GB` disk, `/` filesystem about `49G`
- Data disk: `200GB` disk, `/data` filesystem about `197G`
- Khoj service: `active`
- Context Refinery service: `active`

## Decisions Made

- Switched from `n1-highmem-4` to `e2-highmem-4` after GCP returned `ZONE_RESOURCE_POOL_EXHAUSTED` for `n1-highmem-4` in `us-central1-a`.
- Resized `/data` from `100GB` to `200GB`.
- Resized root `/` from `10GB` to `50GB`.
- Corrected service working directories from `/home/saboor/MyAPI` to `/data/repos/MyAPI`.
- Corrected Context Refinery runtime configuration so it calls local Khoj at `http://localhost:42110`.

## Important Commands or Files

Run on Mac:

```bash
gcloud compute ssh instance-20260418-024637 --zone us-central1-a --project project-ab32182e-5782-4a9c-939
```

Run on Mac:

```bash
gcloud compute instances describe instance-20260418-024637 --zone us-central1-a --project project-ab32182e-5782-4a9c-939 --format='table(name,status,machineType.basename(),networkInterfaces[0].accessConfigs[0].natIP)'
```

Run in VM shell:

```bash
tailscale ip -4
```

Run in VM shell:

```bash
df -h / /data
```

Run in VM shell:

```bash
lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS
```

Run in VM shell:

```bash
systemctl is-active khoj.service context-refinery.service
```

## Failure Modes / Gotchas

- GCP can refuse to start a stopped VM if the selected machine family is unavailable in the zone.
- `ZONE_RESOURCE_POOL_EXHAUSTED` for `n1-highmem-4` was resolved by switching the stopped VM to `e2-highmem-4`.
- `/data` is mounted directly from raw device `/dev/sdb`, so its filesystem growth command was `sudo resize2fs /dev/sdb`.
- Root `/` is mounted from partition `/dev/sda1`, so its growth commands were `sudo growpart /dev/sda 1` and `sudo resize2fs /dev/sda1`.
- `growpart` came from the Debian package `cloud-guest-utils`.
- Services can be active while query routing is wrong if `KHOJ_URL` is stale.

## Related Notes

- `khoj-deployment-indexing-anchor`
- `my-devinfra-system-anchor`
- `api-deployment-status-anchor`
- `current-system-end-to-end-anchor`

## Source Evidence

- `project-docs/VM-MIGRATION-SPRINT.md`
- `project-docs/VM-MIGRATION-HANDOFF.md`
- `sitrep_khoj_deployment.md`
- `project-docs/retrieval-benchmark-v0/refinement-queue-2026-04-20.md`
- 2026-04-20 VM repair session: machine type switch, disk expansion, systemd path repair, `KHOJ_URL` repair, service smoke checks.
