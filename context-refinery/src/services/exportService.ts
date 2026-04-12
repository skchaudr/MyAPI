// src/services/exportService.ts
// Converts CanonicalDocument objects into .md files matching docs/02-target-output.md exactly.
// This is a pure client-side service — no Python backend required.

import JSZip from 'jszip';
import { saveAs } from 'file-saver';
import type { CanonicalDocument } from '../types/schema';

/**
 * Formats a single CanonicalDocument into a .md string.
 * CRITICAL: The --- fence MUST be the first character. Do not add any whitespace above it.
 * Field order is mandatory per docs/02-target-output.md.
 */
export function formatDocumentAsMarkdown(doc: CanonicalDocument): string {
  const createdAt = doc.timestamps.created_at ?? doc.timestamps.ingested_at;
  const tagsYaml = `[${doc.tags.join(', ')}]`;
  const projectsYaml = `[${doc.projects.join(', ')}]`;

  const frontmatter = `---
id: ${doc.id}
title: ${doc.title}
source: ${doc.source.system}
created_at: ${createdAt}
author: ${doc.author}
status: ${doc.status}
doc_type: ${doc.doc_type}
tags: ${tagsYaml}
projects: ${projectsYaml}
---`;

  const titleLine = `# ${doc.title}`;
  const summaryLine = doc.content.summary
    ? `*Summary: ${doc.content.summary}*`
    : null;
  const body = doc.content.cleaned_markdown ?? doc.content.raw_text ?? '';

  const parts = [frontmatter, titleLine];
  if (summaryLine) parts.push(summaryLine);
  parts.push(body);

  return parts.join('\n');
}

/**
 * Sanitizes a document title into a safe filename.
 */
function toFilename(title: string): string {
  return title
    .replace(/[^a-zA-Z0-9\-_ ]/g, '')
    .trim()
    .replace(/\s+/g, '-')
    .toLowerCase() + '.md';
}

/**
 * Takes an array of CanonicalDocuments, packages them into a ZIP, and triggers a browser download.
 * The ZIP will be named khoj-ready-bundle.zip.
 * Returns the generated ZIP blob.
 */
export async function exportToKhojBundle(documents: CanonicalDocument[]): Promise<Blob> {
  if (documents.length === 0) {
    throw new Error('No documents to export.');
  }

  const zip = new JSZip();
  const folder = zip.folder('khoj-ready-bundle');
  if (!folder) throw new Error('Failed to create zip folder.');

  for (const doc of documents) {
    const content = formatDocumentAsMarkdown(doc);
    const filename = toFilename(doc.title);
    folder.file(filename, content);
  }

  const blob = await zip.generateAsync({ type: 'blob' });
  saveAs(blob, 'khoj-ready-bundle.zip');
  return blob;
}
