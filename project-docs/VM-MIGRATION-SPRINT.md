# VM Migration Sprint

Goal: move Context Refinery and Khoj off the expiring VM before the billing deadline, without trying to solve every future optimization in the same cutover.

## Strategy

- Move the application and notes corpus first.
- Keep the stateful database decision separate unless it is provably low-risk.
- Verify the new VM before touching the old one.
- Shut down or delete anything billable on the old VM as soon as the new path is healthy.

## Noon's Critical Path

1. Provision or confirm the destination VM.
2. Copy `MyAPI` to the destination VM.
3. Copy the notes corpus to the expected `KHOJ_NOTES_DIR`.
4. Recreate `context-refinery.service`.
5. Recreate `khoj.service`.
6. Export env vars and secrets.
7. Start Khoj first, then Context Refinery.
8. Confirm:
   - `curl http://localhost:42110/api/health`
   - `curl http://localhost:8000/health`
9. Run the benchmark.
10. Only after the above is green, evaluate whether the PostgreSQL trial should replace the VM-local DB.

## What To Move

- Repository checkout for `MyAPI`
- Branch: `feat/claude-web-adapter`
- `context-refinery.service`
- `khoj.service`
- Notes corpus under `~/khoj-data/notes`
- Any benchmark scripts or manifests needed for validation

## What Not To Overdo Today

- Do not migrate to a new database platform if that slows the app cutover.
- Do not rebuild the retrieval logic while migrating.
- Do not spend time perfecting long-term topology before the app is safe.

## Database Decision

Current posture:

- `context-refinery` does not need its own SQL database.
- Khoj uses PostgreSQL today.

Recommended order:

1. Keep the current DB arrangement through the cutover if that is the fastest way to get off the expiring VM.
2. After the app is live on the new host, evaluate moving Khoj to managed PostgreSQL 18 if it reduces ongoing VM risk.
3. If the migration to managed PostgreSQL slows the cutover, defer it.

Why:

- The billing deadline makes uptime and shutdown safety more important than architecture elegance.
- The managed PostgreSQL offer is attractive, but it is optional compared with the need to stop the old VM from accruing charges.

## Shutdown Checklist For The Old VM

- Confirm the new VM is healthy.
- Confirm the benchmark runs successfully on the new VM.
- Confirm any static IP, disk, or other billed resource attached to the old VM is no longer needed.
- Stop the old services.
- Delete or deallocate the old VM if you are sure the replacement is good.

## Command Pack

Use these once the destination VM details are known.

```bash
# Copy repo state
gcloud compute scp --zone ZONE --project PROJECT \
  --recurse /Users/saboor/repos/MyAPI DEST_USER@DEST_VM:~/MyAPI

# Or clone on the new host and pull the branch
git clone git@github.com:skchaudr/MyAPI.git ~/MyAPI
cd ~/MyAPI
git pull origin feat/claude-web-adapter

# Copy the notes corpus
gcloud compute scp --zone ZONE --project PROJECT \
  --recurse /path/to/notes DEST_USER@DEST_VM:~/khoj-data/notes

# Restart services on the new VM
sudo systemctl restart khoj.service
sudo systemctl restart context-refinery.service

# Verify
curl http://localhost:42110/api/health
curl http://localhost:8000/health
python3 /tmp/run_benchmark.py
```

## Fast Decision Matrix

- If the step is needed to get off the current VM, do it now.
- If the step only improves the long-term architecture, defer it until after cutover.
- If the step could break the migration and does not reduce billing risk, skip it for today.

## Deployment Command Sheet

Assumptions:

- Destination VM name: `my-api-vm`
- Destination VM project/zone: fill in if different from the current `gen-lang-client-0824562549` / `us-central1-a`
- User: `sbkchaudry_gmail_com`

### 1) Confirm the new VM is reachable

```bash
gcloud compute ssh --zone us-central1-a --project gen-lang-client-0824562549 my-api-vm --tunnel-through-iap
```

If the zone/project differs, swap those values before running.

### 2) On the new VM, prepare the directories

```bash
mkdir -p ~/MyAPI
mkdir -p ~/khoj-data/notes
mkdir -p ~/khoj-data/ai-exports
```

### 3) Copy the repo and branch

If the repo is not already present on the VM:

```bash
cd ~
git clone git@github.com:skchaudr/MyAPI.git
cd ~/MyAPI
git pull origin feat/claude-web-adapter
```

If the repo is already there and just needs sync:

```bash
cd ~/MyAPI
git fetch origin
git checkout feat/claude-web-adapter
git pull origin feat/claude-web-adapter
```

### 4) Copy the notes corpus

From the local machine:

```bash
gcloud compute scp --zone us-central1-a --project gen-lang-client-0824562549 \
  --recurse /home/sbkchaudry_gmail_com/khoj-data/notes \
  my-api-vm:/home/sbkchaudry_gmail_com/khoj-data/
```

### 5) Restore the service units

Create or replace these files on `my-api-vm`:

- `/etc/systemd/system/khoj.service`
- `/etc/systemd/system/context-refinery.service`

Current service content to mirror:

- [khoj.service](/Users/saboor/repos/MyAPI/project-docs/VM-MIGRATION-SPRINT.md#khojservice-template)
- [context-refinery.service](/Users/saboor/repos/MyAPI/project-docs/VM-MIGRATION-SPRINT.md#context-refineryservice-template)

### 6) Bring up the services

```bash
sudo systemctl daemon-reload
sudo systemctl enable khoj.service
sudo systemctl enable context-refinery.service
sudo systemctl restart khoj.service
sudo systemctl restart context-refinery.service
```

### 7) Verify health

```bash
curl http://localhost:42110/api/health
curl http://localhost:8000/health
ss -tlnp | grep 42110
ss -tlnp | grep 8000
```

### 8) Run the benchmark

```bash
python3 /tmp/run_benchmark.py
```

### 9) After validation, decide on PostgreSQL 18

If you want to move Khoj to managed PostgreSQL after the app is healthy:

- export the current DB
- import into the managed PostgreSQL 18 instance
- update the Khoj environment variables on `my-api-vm`
- restart `khoj.service`
- re-run the benchmark

## Service Templates

### `khoj.service` template

```ini
[Unit]
Description=Khoj AI Engine
After=network.target tailscaled.service postgresql.service

[Service]
Type=simple
User=sbkchaudry_gmail_com
WorkingDirectory=/home/sbkchaudry_gmail_com/khoj-engine
ExecStart=/home/sbkchaudry_gmail_com/khoj-engine/venv/bin/khoj --host 0.0.0.0 --no-gui --anonymous-mode
Restart=always
RestartSec=5
Environment=HOME=/home/sbkchaudry_gmail_com
Environment=POSTGRES_HOST=localhost
Environment=POSTGRES_PORT=5432
Environment=POSTGRES_NAME=khoj
Environment=POSTGRES_USER=khoj
Environment=POSTGRES_PASSWORD=khoj
Environment=KHOJ_ADMIN_EMAIL=sbkchaudry@gmail.com
Environment=KHOJ_ADMIN_PASSWORD=myapi2769!@

[Install]
WantedBy=multi-user.target
```

### `context-refinery.service` template

```ini
[Unit]
Description=Context Refinery API
After=network.target

[Service]
Type=simple
User=sbkchaudry_gmail_com
WorkingDirectory=/home/sbkchaudry_gmail_com/MyAPI
Environment=PYTHONUNBUFFERED=1
ExecStart=/home/sbkchaudry_gmail_com/.local/bin/uvicorn api.main:app --host 0.0.0.0 --port 8000
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

## Decision Rule

If a step does not directly help you:

- move traffic
- preserve data
- verify health
- or prevent billing

then it should not block the migration today.
