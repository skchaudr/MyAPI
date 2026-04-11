const API_BASE = (import.meta as any).env?.VITE_API_URL ?? 'http://localhost:8000';

export interface EnrichResponse {
  summary: string | null;
  doc_type: string;
  tags: string[];
}

// POST /enrich
export async function distillContent(content: string): Promise<string> {
  const res = await fetch(`${API_BASE}/enrich`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ content }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail ?? `Enrich failed: ${res.status}`);
  }
  const data: EnrichResponse = await res.json();
  return data.summary ?? 'No summary generated.';
}

// POST /import/obsidian
export async function importObsidianFile(file: File): Promise<any> {
  const form = new FormData();
  form.append('file', file);
  const res = await fetch(`${API_BASE}/import/obsidian`, { method: 'POST', body: form });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail ?? `Import failed: ${res.status}`);
  }
  return res.json();
}

// POST /import/chatgpt — returns list of canonical docs
export async function importChatGPTFile(file: File): Promise<any[]> {
  const form = new FormData();
  form.append('file', file);
  const res = await fetch(`${API_BASE}/import/chatgpt`, { method: 'POST', body: form });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(err.detail ?? `Import failed: ${res.status}`);
  }
  return res.json();
}
