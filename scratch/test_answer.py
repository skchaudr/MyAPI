import json
import urllib.request
import urllib.error
import subprocess
import sys

PROJECT_ID = "sb-genai-2026"

def get_access_token():
    try:
        result = subprocess.run(
            ["gcloud", "auth", "print-access-token", "--account=sbkchaudry@gmail.com"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        print("Error getting token.")
        sys.exit(1)

def main():
    token = get_access_token()
    # Let's hit the benchmark-search engine's :answer endpoint!
    url = f"https://discoveryengine.googleapis.com/v1/projects/{PROJECT_ID}/locations/global/collections/default_collection/engines/benchmark-search/servingConfigs/default_search:answer"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "x-goog-user-project": PROJECT_ID
    }
    
    # Vertex AI Search :answer payload structure
    data = {
        "query": {"text": "What is graph-driven development?"}
    }
    
    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            
            print("\n✨ ANSWER FROM VERTEX:")
            answer = res_data.get("answer", {})
            print(answer.get("answerText", "No answer Text"))
            
            print("\n🔬 ANSWER KEYS:")
            print(list(answer.keys()))
            
            print("\n📄 REFERENCES FOUND:")
            steps = answer.get("steps", [])
            seen_uris = set()
            for step in steps:
                actions = step.get("actions", [])
                for action in actions:
                    observation = action.get("observation", {})
                    results = observation.get("searchResults", [])
                    for r in results:
                        uri = r.get("uri", "")
                        title = r.get("title", "")
                        if uri and uri not in seen_uris:
                            seen_uris.add(uri)
                            filename = uri.split('/')[-1]
                            print(f"- {title} ({filename})")
    except urllib.error.HTTPError as e:
        print(f"API Error: {e.code} {e.reason}")
        print(e.read().decode("utf-8"))

if __name__ == "__main__":
    main()
