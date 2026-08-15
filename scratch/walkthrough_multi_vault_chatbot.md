# Guide: Building a Unified Vertex AI Chatbot over Multiple Obsidian Vaults

> **Status: aspirational — not implemented.** No engine named `unified-vaults-chatbot` exists. The `Personal` and `Coding-Tech` vaults are not synced to GCS. Treat this as a design proposal, not as ground truth. Live deployment uses only the `SoloDeveloper` vault via engine `notes-chatbot`.

This document provides a step-by-step, end-to-end walkthrough for deploying a unified conversational chatbot over multiple Obsidian vaults using Google Cloud Vertex AI Search and Conversation. 

In this setup, we will configure the chatbot over three of your vaults:
1. **SoloDeveloper** (Primary)
2. **Personal**
3. **Coding-Tech** *(Note: You can easily swap this or add `workout-tracker` using the same patterns)*

---

## 📋 Architectural Overview

The multi-vault architecture aggregates multiple local directories, synchronizes them to dedicated GCS prefixes, and indexes them for unified retrieval.

```mermaid
graph TD
    subgraph Local Mac
        V1[SoloDeveloper Vault]
        V2[Personal Vault]
        V3[Coding-Tech Vault]
    end

    subgraph Google Cloud Storage (gs://sb-myapi-corpus/obsidian/)
        G1[(/SoloDeveloper/)]
        G2[(/Personal/)]
        G3[(/Coding-Tech/)]
    end

    subgraph Vertex AI Agent Builder
        DS1[SoloDeveloper Store]
        DS2[Personal Store]
        DS3[Coding-Tech Store]
        UnifiedApp[Unified Chatbot App]
    end

    V1 -->|Convert & Sync| G1
    V2 -->|Convert & Sync| G2
    V3 -->|Convert & Sync| G3

    G1 -->|Index| DS1
    G2 -->|Index| DS2
    G3 -->|Index| DS3

    DS1 -->|Link| UnifiedApp
    DS2 -->|Link| UnifiedApp
    DS3 -->|Link| UnifiedApp

    UnifiedApp <===> CLI[Mac Terminal Client]
```

---

## 🛠️ Step 1: Local Multi-Vault Setup & Syncing

To sync multiple independent vaults while adhering to Google's text indexing requirements, we can adapt the sync script to process each vault into a corresponding subdirectory in your GCS bucket.

### 1. The Multi-Vault Sync Script
You can save this script as `scratch/upload_multi_vault.py`:

```python
import os
import shutil
import subprocess

# Define the local vaults and their corresponding GCS prefixes
VAULTS = {
    "SoloDeveloper": "/Users/saboor/Obsidian/SoloDeveloper",
    "Personal": "/Users/saboor/Obsidian/Personal",
    "Coding-Tech": "/Users/saboor/Obsidian/Coding-Tech"
}

TEMP_BASE_DIR = "/Users/saboor/repos/MyAPI/scratch/sync_temp_multi"
GCS_BUCKET_BASE = "gs://sb-myapi-corpus/obsidian"

def sync_vault(vault_name, local_path):
    temp_dir = os.path.join(TEMP_BASE_DIR, vault_name)
    gcs_dest = f"{GCS_BUCKET_BASE}/{vault_name}"
    
    print(f"\n--- Processing: {vault_name} ---")
    print(f"Source: {local_path}")
    print(f"Staging: {temp_dir}")
    print(f"Destination: {gcs_dest}")
    
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir, exist_ok=True)
    
    md_count = 0
    pdf_count = 0
    ignored_count = 0
    
    for root, dirs, files in os.walk(local_path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.startswith('.'):
                ignored_count += 1
                continue
                
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, local_path)
            
            if file.endswith('.md'):
                target_rel_path = os.path.splitext(rel_path)[0] + '.txt'
                target_path = os.path.join(temp_dir, target_rel_path)
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                shutil.copy2(file_path, target_path)
                md_count += 1
            elif file.endswith('.pdf'):
                target_path = os.path.join(temp_dir, rel_path)
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                shutil.copy2(file_path, target_path)
                pdf_count += 1
            else:
                ignored_count += 1
                
    print(f"Staged {md_count} markdown files and {pdf_count} PDF files.")
    
    # Run gsutil rsync
    print(f"Running rsync to GCS...")
    cmd = ["gsutil", "-m", "rsync", "-d", "-r", temp_dir, gcs_dest]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"Successfully synchronized {vault_name} to GCS!")
    else:
        print(f"Error synchronizing {vault_name}:")
        print(result.stderr)

def main():
    # Clean staging root
    if os.path.exists(TEMP_BASE_DIR):
        shutil.rmtree(TEMP_BASE_DIR)
        
    for vault_name, local_path in VAULTS.items():
        if os.path.exists(local_path):
            sync_vault(vault_name, local_path)
        else:
            print(f"\n[WARNING] Path does not exist, skipping: {local_path}")
            
    # Cleanup staging directory
    if os.path.exists(TEMP_BASE_DIR):
        shutil.rmtree(TEMP_BASE_DIR)
        print("\nCleaned up local temporary staging directory.")

if __name__ == "__main__":
    main()
```

### 2. Run the Multi-Vault Sync
Execute this script from your Mac terminal to upload all three vaults:
```bash
python3 scratch/upload_multi_vault.py
```

---

## ☁️ Step 2: Creating the Vertex AI Data Stores

To index multiple vaults, you have two options depending on how you wish to manage permissions, metadata, or search isolation later.

### Option A: A Single Unified Data Store (Recommended for simplicity)
You can point a single Data Store to the root of your GCS bucket, and Vertex AI will index all vaults inside it under one umbrella.

1. Navigate to **Vertex AI Agent Builder** > **Data Stores** in the GCP Console.
2. Click **Create Data Store** and choose **Cloud Storage**.
3. Set the configurations:
   * **Folder Path**: `gs://sb-myapi-corpus/obsidian/**` (Notice the double asterisk `**` which recursively captures all subfolders like `SoloDeveloper`, `Personal`, and `Coding-Tech`).
   * **Import Type**: **Unstructured documents**
4. Name the Data Store:
   * **Data Store Name**: `unified-obsidian-store`
5. Click **Create**.

---

### Option B: Multiple Distinct Data Stores (Recommended for logical separation)
If you want to keep your vaults structurally isolated (e.g., so you can create a chatbot that *only* looks at `Coding-Tech` later, in addition to your unified chatbot), create separate Data Stores for each vault:

1. **SoloDeveloper Store**:
   * **Folder Path**: `gs://sb-myapi-corpus/obsidian/SoloDeveloper/**`
   * **Data Store Name**: `solodeveloper-vault-store`
2. **Personal Store**:
   * **Folder Path**: `gs://sb-myapi-corpus/obsidian/Personal/**`
   * **Data Store Name**: `personal-vault-store`
3. **Coding-Tech Store**:
   * **Folder Path**: `gs://sb-myapi-corpus/obsidian/Coding-Tech/**`
   * **Data Store Name**: `coding-tech-vault-store`

---

## 🤖 Step 3: Creating the Unified Chatbot App

Vertex AI allows you to link multiple Data Stores to a single Chat Application. The model will search across all linked stores and formulate a grounded answer.

1. Navigate to **Vertex AI Agent Builder** > **Apps** in the GCP Console.
2. Click **Create App** or **New App**.
3. Select **Chat** as the application type.
4. Fill in the App Details:
   * **App Name**: `unified-vaults-chatbot`
   * **Company/Organization Name**: `SoloDeveloper`
   * Click **Continue**.
5. Under **Data Stores**, select the appropriate options based on your Step 2 decision:
   * **If you chose Option A**: Select only the `unified-obsidian-store`.
   * **If you chose Option B**: Select all three boxes: `solodeveloper-vault-store`, `personal-vault-store`, and `coding-tech-vault-store`.
6. Click **Create**.

---

## 💻 Step 4: Querying from the Local Terminal

Configure your client to hit the new unified engine configuration.

1. Open your client file: [vertex_client.py](file:///Users/saboor/repos/MyAPI/scratch/vertex_client.py)
2. In the `run_chat` function (around line 75), update the endpoint URL to point to the new engine ID:
   ```python
   # Replace 'notes-chatbot' or 'solodeveloper-chatbot' with 'unified-vaults-chatbot'
   url = f"https://discoveryengine.googleapis.com/v1/projects/{PROJECT_ID}/locations/global/collections/default_collection/engines/unified-vaults-chatbot/servingConfigs/default_search:answer"
   ```
3. Authenticate your gcloud session on your Mac:
   ```bash
   gcloud auth login sbkchaudry@gmail.com
   ```
4. Query across all three vaults from your terminal:
   ```bash
   python3 scratch/vertex_client.py chat "What is my tech stack, and what are my personal goals for this week?"
   ```

*Vertex AI will seamlessly retrieve relevant text chunks from SoloDeveloper, Personal, and Coding-Tech, merge the context, and respond with a highly unified, grounded answer.*
