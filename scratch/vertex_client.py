import ssl
import sys
import json
import pathlib
import subprocess
import urllib.request
import urllib.error
import uuid
import certifi

SSL_CTX = ssl.create_default_context(cafile=certifi.where())

PROJECT_ID = "sb-info-notes-2026"
AGENT_ID = "b4ae994b-3e33-405f-843d-ad47fbab6981"
DATA_STORES = {
    "portfolio": "portfolio-200_1782634877044",
    "code": "code-corpus_1782634759080",
    "personal": "personal-corpus_1782632408901"
}

DISCO_BASE = f"https://us-discoveryengine.googleapis.com/v1/projects/{PROJECT_ID}/locations/us/collections/default_collection"
DF_BASE = f"https://us-west1-dialogflow.googleapis.com/v3beta1/projects/{PROJECT_ID}/locations/us-west1/agents/{AGENT_ID}"
SESSION_FILE = pathlib.Path.home() / ".cache" / "vertex_session_id"

def get_access_token():
    try:
        result = subprocess.run(
            ["gcloud", "auth", "print-access-token", "--account=sb.info.you@gmail.com"],
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

def get_or_create_session(new=False):
    if not new and SESSION_FILE.exists():
        return SESSION_FILE.read_text().strip()
    session_id = str(uuid.uuid4())
    SESSION_FILE.parent.mkdir(parents=True, exist_ok=True)
    SESSION_FILE.write_text(session_id)
    return session_id

def reset_session():
    if SESSION_FILE.exists():
        SESSION_FILE.unlink()
        print("Session cleared. Next `chat` will start a fresh thread.")
    else:
        print("No active session to clear.")

def run_search(corpus, query):
    if corpus not in DATA_STORES:
        print(f"Invalid corpus '{corpus}'. Available: {list(DATA_STORES.keys())}")
        sys.exit(1)
        
    token = get_access_token()
    ds_id = DATA_STORES[corpus]
    url = f"{DISCO_BASE}/dataStores/{ds_id}/servingConfigs/default_search:search"
    data = {
        "query": query,
        "pageSize": 5,
        "contentSearchSpec": {
            "summarySpec": {"summaryResultCount": 3, "ignoreAdversarialQuery": True}
        },
    }
    res = _request("POST", url, token, data)
    print(f"\n🔍 SEARCH RESULTS FOR '{query}' IN CORPUS '{corpus}'\n" + "=" * 50)
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
    session_id = get_or_create_session(new=new)
    url = f"{DF_BASE}/sessions/{session_id}:detectIntent"
    data = {
        "queryInput": {
            "text": {
                "text": query
            },
            "languageCode": "en"
        }
    }
    res = _request("POST", url, token, data)
    print(f"\n💬 CHATBOT ANSWER FOR: '{query}'\n" + "=" * 50)
    
    query_result = res.get("queryResult", {})
    response_messages = query_result.get("responseMessages", [])
    
    found_text = False
    for msg in response_messages:
        if "text" in msg and "text" in msg["text"]:
            for text_val in msg["text"]["text"]:
                print(text_val)
                found_text = True
                
    if not found_text:
        print("No answer generated.")
        
    print(f"\n(session: {session_id} — use `reset` for a fresh thread)")

def show_doc(corpus, doc_id):
    if corpus not in DATA_STORES:
        print(f"Invalid corpus '{corpus}'. Available: {list(DATA_STORES.keys())}")
        sys.exit(1)
        
    token = get_access_token()
    ds_id = DATA_STORES[corpus]
    url = f"{DISCO_BASE}/dataStores/{ds_id}/branches/0/documents/{doc_id}"
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
    print("Usage: ask <command> [args]")
    print("\nShortcuts:")
    print("  ask \"Q\"            Chat with the unified Tri-Corpus agent")
    print("  ask p \"Q\"          Search only the Portfolio corpus")
    print("  ask c \"Q\"          Search only the Code corpus")
    print("  ask me \"Q\"         Search only the Personal corpus")
    print("\nAdvanced:")
    print("  ask --new \"Q\"      Start a fresh chat session")
    print("  ask doc c <id>     View a document from a specific corpus")
    print("  ask reset          Clear the active chat session")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    cmd = sys.argv[1].lower()
    
    corpus_map = {
        "p": "portfolio", "port": "portfolio", "portfolio": "portfolio",
        "c": "code", "code": "code",
        "me": "personal", "per": "personal", "personal": "personal"
    }

    if cmd in corpus_map and len(sys.argv) >= 3:
        run_search(corpus_map[cmd], sys.argv[2])
    elif cmd == "reset":
        reset_session()
    elif cmd == "doc" and len(sys.argv) >= 4:
        corpus = corpus_map.get(sys.argv[2].lower(), sys.argv[2].lower())
        show_doc(corpus, sys.argv[3])
    elif cmd == "chat" and len(sys.argv) >= 3:
        new = "--new" in sys.argv
        query = next((a for a in sys.argv[2:] if not a.startswith("--")), None)
        if query:
            run_chat(query, new=new)
        else:
            print_help()
            sys.exit(1)
    else:
        new = "--new" in sys.argv
        query = next((a for a in sys.argv[1:] if not a.startswith("--")), None)
        if query:
            run_chat(query, new=new)
        else:
            print_help()
            sys.exit(1)
