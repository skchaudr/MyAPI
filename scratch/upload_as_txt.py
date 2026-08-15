import fnmatch
import os
import shutil
import subprocess

VAULT_DIR = "/Users/saboor/Obsidian/SoloDeveloper"
TEMP_DIR = "/Users/saboor/repos/MyAPI/scratch/sync_temp"
GCS_BUCKET = "gs://sb-myapi-corpus/obsidian/SoloDeveloper"

# Relative-to-VAULT_DIR subtrees to exclude entirely.
# When you trust the corpus enough to include confidential notes, delete that entry.
EXCLUDE_REL_DIRS = {"02 Areas/Confidential"}

# Directory basenames to exclude wherever they appear (plugin caches, etc.).
EXCLUDE_DIR_NAMES = {"_database"}

# Filename globs to exclude (session/run artifacts).
EXCLUDE_FILE_GLOBS = {"run-*.md"}

def main():
    print(f"Starting preparation of files from {VAULT_DIR}...")

    # 1. Clean and recreate temp directory
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
    os.makedirs(TEMP_DIR, exist_ok=True)

    md_count = 0
    pdf_count = 0
    ignored_count = 0

    # 2. Walk local vault
    for root, dirs, files in os.walk(VAULT_DIR):
        rel_root = os.path.relpath(root, VAULT_DIR)
        # Exclude hidden dirs, plugin/cache dir names, and any configured subtree
        dirs[:] = [
            d for d in dirs
            if not d.startswith('.')
            and d not in EXCLUDE_DIR_NAMES
            and os.path.normpath(os.path.join(rel_root, d)) not in EXCLUDE_REL_DIRS
        ]

        for file in files:
            # Exclude hidden files
            if file.startswith('.'):
                ignored_count += 1
                continue

            # Exclude configured filename patterns (e.g. run-*.md)
            if any(fnmatch.fnmatch(file, pat) for pat in EXCLUDE_FILE_GLOBS):
                ignored_count += 1
                continue

            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, VAULT_DIR)

            if file.endswith('.md'):
                # Map to .txt in target path to satisfy Vertex AI mime-type rule
                target_rel_path = os.path.splitext(rel_path)[0] + '.txt'
                target_path = os.path.join(TEMP_DIR, target_rel_path)
                
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                shutil.copy2(file_path, target_path)
                md_count += 1
                
            elif file.endswith('.pdf'):
                # Copy as-is
                target_path = os.path.join(TEMP_DIR, rel_path)
                
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                shutil.copy2(file_path, target_path)
                pdf_count += 1
            else:
                ignored_count += 1
                
    print(f"Preparation complete!")
    print(f"Total .md notes converted to .txt: {md_count}")
    print(f"Total .pdf files copied: {pdf_count}")
    print(f"Total files ignored (non-md/pdf, configs, or dotfiles): {ignored_count}")
    
    # 3. Synchronize to GCS
    print(f"Running rsync to GCS bucket: {GCS_BUCKET}...")
    # -d deletes objects in GCS that are not in the temp folder, ensuring a perfectly clean sync
    cmd = ["gsutil", "-m", "rsync", "-d", "-r", TEMP_DIR, GCS_BUCKET]
    print(f"Running: {' '.join(cmd)}")
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print("Successfully synchronized to Google Cloud Storage!")
        # 4. Clean up temp folder
        shutil.rmtree(TEMP_DIR)
        print("Cleaned up local temporary directory.")
    else:
        print("Error synchronizing to GCS:")
        print(result.stderr)
        
if __name__ == "__main__":
    main()
