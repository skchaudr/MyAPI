# Jules Task: Fix Export Tab Buttons

## Summary
The Export view ("Delivery Lab") in the React frontend has non-functional buttons and mock data that need to be wired up or cleaned out.

## Current State
- **RAG Export (ZIP)** — WORKS. Calls `exportToKhojBundle(docs)` in `src/services/exportService.ts`, generates a `khoj-ready-bundle.zip` via JSZip + file-saver. No changes needed here.
- **Personal Read Export** — DEAD. "Web HTML" and "Print PDF" buttons have no onClick handlers.
- **Output Manifest** — MOCK DATA. Uses `MOCK_OUTPUT_FILES` from `src/mockData.ts`. Download buttons have no onClick handlers. Shows fake file sizes (24.8 MB, 4.2 MB, 128.5 MB) that don't correspond to anything real.

## Requirements

### 1. Wire up the Output Manifest to real data
After the user clicks "Generate Zipped MD" and the RAG export succeeds, the Output Manifest section should show the **actual generated bundle** (not mock data):
- Show the `khoj-ready-bundle.zip` file with its real size
- The Download button should re-trigger a download of the same ZIP blob
- Remove `MOCK_OUTPUT_FILES` from `mockData.ts` (or the entire file if nothing else uses it)

### 2. Remove or gate the Personal Read Export card
The HTML and PDF exports are not implemented and there's no backend for them. Two acceptable approaches:
- **Option A (preferred):** Remove the Personal Read Export card entirely. It's misleading.
- **Option B:** Keep the card but disable the buttons with a "Coming soon" badge. No placeholder onClick handlers.

### 3. Remove the fake Consolidated_Context.json and Refined_Insights.pdf from the manifest
These files are never generated. The only real export artifact is the ZIP bundle.

## Key Files
- `src/components/ExportView.tsx` — main component
- `src/services/exportService.ts` — `exportToKhojBundle()` function (working, don't break it)
- `src/mockData.ts` — contains `MOCK_OUTPUT_FILES` to remove
- `src/types/schema.ts` — `CanonicalDocument` type definition

## Data Flow
Documents are stored in `localStorage` under key `cr_docs_default`. ExportView reads them on mount:
```tsx
useEffect(() => {
  const saved = localStorage.getItem('cr_docs_default');
  if (saved) {
    try { setDocs(JSON.parse(saved)); } catch {}
  }
}, []);
```

## Testing
- Load some docs via the Import tab
- Navigate to Export tab
- Click "Generate Zipped MD" — should produce a real ZIP download
- Output Manifest should update to show the actual generated file
- No mock data should appear anywhere in the Export tab

## Do NOT
- Modify `exportService.ts` export logic (it works)
- Add new backend endpoints
- Change the localStorage key or data format
- Add new npm dependencies unless absolutely necessary
