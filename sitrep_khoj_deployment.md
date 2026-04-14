# 📡 SITREP: Context Refinery -> Khoj Deployment

> **Date:** 2026-04-12
> **Status:** Backend Configured & Stable. Blocked on Deployment IP target.
> **Mission:** Deploy sanitized local Obsidian bundles to a headless Khoj RAG engine on a remote GCP VM via a Tailscale bridge.

---

## 🟢 1. What We Conquered (The Good News)

The GCP Linux VM (`khoj-headless-engine`) backend is now formally cured and primed. We executed three critical configuration fixes directly on the host:

1. **Busted the Ghost Process:** Khoj was stuck in a massive crash loop preventing any HTTP connections because a dead Python process was silently clinging to port `42110`. We successfully executed a hard kill, allowing `systemd` to seamlessly bind the application to `0.0.0.0`.
2. **Defeated the Auth Wall:** Khoj natively forces a Bearer API token validation on all headless requests. We bypassed this by successfully modifying `/etc/systemd/system/khoj.service` to boot the application containing the `--anonymous-mode` flag.
3. **Firewall Permitted:** We updated `ufw` rules to explicitly allow `42110/tcp` inbound traffic from the Tailscale overlay.

**Current BackEnd Status:** The GCP engine is perfectly healthy and awaiting queries without port tunnels or proxies.

---

## 🟡 2. The Great Matrix Twist (Why It Failed At The End)

Despite hitting absolute perfection on the Linux backend, all queries from the Mac were mysteriously returning `exit 7` (Connection refused) or executing locally. 

**The Revelation:** The Tailscale IP `100.109.233.105` currently hard-coded inside `deploy_to_brain.sh` does NOT belong to the GCP VM. It belongs to the User's local Mac laptop. 

When the user ran the `rsync` deployment script, the Mac dutifully opened an SSH connection to itself, packed up the 6 "Anchor Notes," and deposited them in a local folder called `/Users/saboor/khoj-data/notes`.

Consequently, while the headless GCP engine is fully stable and waiting, its `~/khoj-data` directory is completely empty because the payload was accidentally delivered to the local laptop.

---

## 🚀 3. Handoff Action Items (The Final Steps)

When you return (or for the next operative taking the wheel), execute this exact sequence to complete the pipeline:

### Step 1: Discover the True GCP IP
1. Jump into the SSH terminal pane logged into the actual Linux VM (`khoj-headless-engine`) where we ran `systemctl`.
2. Run `hostname -I -all` or `tailscale ip -4` to print the true Tailscale interface IP of the GCP Linux machine.

### Step 2: Route the Bridge correctly
1. Open the local `deploy_to_brain.sh` script.
2. Replace `TAILSCALE_IP="100.109.233.105"` with the newly discovered True IP.
3. Rerun `./deploy_to_brain.sh` from the Mac to successfully beam the ZIP payload into the actual remote VM.

### Step 3: Bask in the JSON
1. From any standard Mac terminal tab, execute a curl request using the True IP:
```bash
curl -s "http://[TRUE_GCP_IP]:42110/api/search?q=What%20is%20the%20BDR%20Project" | jq
```

> [!SUCCESS] Expected Outcome
> The pipeline will execute flawlessly. The `-s | jq` block will format the unauthenticated text chunks, validating end-to-end integration of the client-side Car Wash into the remote Khoj sink.
