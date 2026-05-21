import ssl
import sys
import json
import pathlib
import subprocess
import urllib.request
import urllib.error

import certifi
SSL_CTX = ssl.create_default_context(cafile=certifi.where())

PROJECT_ID = "sb-genai-2026"
ENGINE_ID = "benchmark-search"
DATA_STORE_ID = "myapi-benchmark"
BASE = f"https://discoveryengine.googleapis.com/v1/projects/{PROJECT_ID}/locations/global/collections/default_collection"
SESSION_FILE = pathlib.Path.home() / ".cache" / "vertex_session_id"

def get_access_token():
    try:
        result = subprocess.run(
            ["gcloud", "auth", "print-access-token", "--account=sbkchaudry@gmail.com"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        print("Error getting gcloud token. Make sure you are authenticated.")
        sys.exit(1)

def _headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "x-goog-user-project": PROJECT_ID,
    }

def _request(method, url, token, body=None):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, headers=_headers(token), method=method)
    try:
        with urllib.request.urlopen(req, context=SSL_CTX) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"API Error: {e.code} {e.reason}")
        print(e.read().decode("utf-8"))
        sys.exit(1)

def get_or_create_session(token, new=False):
    if not new and SESSION_FILE.exists():
        return SESSION_FILE.read_text().strip()
    url = f"{BASE}/engines/{ENGINE_ID}/sessions"
    res = _request("POST", url, token, {"userPseudoId": "sab-cli"})
    session_name = res["name"]
    SESSION_FILE.parent.mkdir(parents=True, exist_ok=True)
    SESSION_FILE.write_text(session_name)
    return session_name

def reset_session():
    if SESSION_FILE.exists():
        SESSION_FILE.unlink()
        print("Session cleared. Next `chat` will start a fresh thread.")
    else:
        print("No active session to clear.")

def run_search(query):
    token = get_access_token()
    url = f"{BASE}/engines/{ENGINE_ID}/servingConfigs/default_search:search"
    data = {
        "query": query,
        "pageSize": 5,
        "contentSearchSpec": {
            "summarySpec": {"summaryResultCount": 3, "ignoreAdversarialQuery": True}
        },
    }
    res = _request("POST", url, token, data)
    print(f"\n🔍 SEARCH RESULTS FOR: '{query}'\n" + "=" * 50)
    summary = res.get("summary", {}).get("summaryText")
    if summary:
        print("\n✨ AI SUMMARY:")
        print(summary)
        print("\n" + "-" * 50)
    print("\n📄 SOURCES FOUND:")
    for i, r in enumerate(res.get("results", []), 1):
        doc = r.get("document", {})
        derived = doc.get("derivedStructData", {})
        struct = doc.get("structData", {})
        title = derived.get("title") or struct.get("title") or doc.get("name", "Unknown").split("/")[-1]
        doc_id = doc.get("id", doc.get("name", "").split("/")[-1])
        print(f"{i}. {title}  [id: {doc_id}]")

def run_chat(query, new=False):
    token = get_access_token()
    session = get_or_create_session(token, new=new)
    url = f"{BASE}/engines/{ENGINE_ID}/servingConfigs/default_search:answer"
    data = {"query": {"text": query}, "session": session}
    res = _request("POST", url, token, data)
    print(f"\n💬 CHATBOT ANSWER FOR: '{query}'\n" + "=" * 50)
    answer = res.get("answer", {})
    print(answer.get("answerText", "No answer generated."))
    refs = answer.get("references", [])
    if refs:
        print("\n" + "-" * 50)
        print("📎 CITED DOCS:")
        seen = set()
        for ref in refs:
            info = ref.get("chunkInfo", {}).get("documentMetadata") or ref.get("unstructuredDocumentInfo", {})
            title = info.get("title", "Unknown")
            doc_id = (info.get("document") or "").split("/")[-1]
            if doc_id and doc_id not in seen:
                seen.add(doc_id)
                print(f"  - {title}  [id: {doc_id}]")
    print(f"\n(session: {session.split('/')[-1]} — use `reset` for a fresh thread)")

def show_doc(doc_id):
    token = get_access_token()
    url = f"{BASE}/dataStores/{DATA_STORE_ID}/branches/0/documents/{doc_id}"
    res = _request("GET", url, token)
    struct = res.get("structData", {})
    uri = struct.get("uri") or res.get("content", {}).get("uri", "")
    title = struct.get("title") or (uri.rsplit("/", 1)[-1] if uri else doc_id)
    print(f"\n📄 DOCUMENT: {title}\n" + "=" * 50)
    print(f"ID:    {res.get('id', doc_id)}")
    print(f"URI:   {uri or '—'}")
    if uri.startswith("gs://"):
        try:
            out = subprocess.run(
                ["gcloud", "storage", "cat", uri],
                capture_output=True, text=True, check=True, timeout=15,
            ).stdout
            print("\n--- CONTENT ---")
            print(out[:4000] + ("\n…[truncated]" if len(out) > 4000 else ""))
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            print(f"\n(Could not fetch GCS content: {e})")

def print_help():
    print("Usage: python3 scratch/vertex_client.py <command> [args]")
    print("\nCommands:")
    print("  search \"Q\"           Search notes (AI summary + 5 sources)")
    print("  chat \"Q\"             Grounded answer; continues prior session by default")
    print("  chat --new \"Q\"       Start a fresh chat session")
    print("  reset                  Clear stored session (next chat starts fresh)")
    print("  doc <id>               Print a document by ID (IDs shown in search/chat output)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "search" and len(sys.argv) >= 3:
        run_search(sys.argv[2])
    elif command == "chat" and len(sys.argv) >= 3:
        new = "--new" in sys.argv
        query = next((a for a in sys.argv[2:] if not a.startswith("--")), None)
        if not query:
            print_help()
            sys.exit(1)
        run_chat(query, new=new)
    elif command == "reset":
        reset_session()
    elif command == "doc" and len(sys.argv) >= 3:
        show_doc(sys.argv[2])
    else:
        print_help()
        sys.exit(1)
