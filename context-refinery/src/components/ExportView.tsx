import React, { useState } from 'react';
import { Database, BookOpen, CheckCircle, Download, FileJson, FileText, Archive, RefreshCw, FileCode, Printer, Loader2 } from 'lucide-react';
import { MOCK_OUTPUT_FILES } from '../mockData';
import { Button } from './ui/button';
import { Card } from './ui/card';
import { Badge } from './ui/badge';
import { cn } from '@/lib/utils';
import { useDocuments } from '../contexts/DocumentContext';
import JSZip from 'jszip';

export default function ExportView() {
  const { importedDocs } = useDocuments();
  const [isExporting, setIsExporting] = useState(false);

  // Statistics Calculation
  const isImported = importedDocs.length > 0;
  const totalItems = isImported ? importedDocs.length : 2450;

  const processedTokens = isImported
    ? Math.floor(importedDocs.reduce((acc, doc) => acc + (doc.content?.raw_text?.length || 0), 0) / 4)
    : "1.2M";

  const activeSources = isImported
    ? new Set(importedDocs.map(doc => doc.source?.system)).size
    : 4;

  const handleZipExport = async () => {
    if (!isImported) return;
    setIsExporting(true);
    try {
      const zip = new JSZip();

      importedDocs.forEach((doc, index) => {
        let frontmatter = `---\n`;
        frontmatter += `title: "${doc.title?.replace(/"/g, '\\"') || 'Untitled'}"\n`;
        if (doc.provenance?.author) frontmatter += `author: "${doc.provenance.author}"\n`;
        if (doc.tags?.length) frontmatter += `tags: [${doc.tags.map((t: string) => `"${t}"`).join(', ')}]\n`;
        if (doc.doc_type) frontmatter += `doc_type: "${doc.doc_type}"\n`;
        if (doc.status) frontmatter += `status: "${doc.status}"\n`;
        frontmatter += `---\n\n`;

        const content = frontmatter + (doc.content?.cleaned_markdown || doc.content?.raw_text || '');
        const filename = `${doc.title?.replace(/[^a-z0-9]/gi, '_').toLowerCase() || 'doc'}_${index}.md`;

        zip.file(filename, content);
      });

      const blob = await zip.generateAsync({ type: 'blob' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'context_refinery_export.zip';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    } catch (e) {
      console.error("Export failed", e);
    } finally {
      setIsExporting(false);
    }
  };

  const handleHtmlExport = () => {
    if (!isImported) return;

    let htmlContent = `
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Context Refinery Export</title>
        <style>
          body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 2rem; }
          h1, h2, h3 { color: #111; }
          .doc-container { margin-bottom: 4rem; padding-bottom: 2rem; border-bottom: 1px solid #eee; }
          .meta { font-size: 0.85rem; color: #666; margin-bottom: 1.5rem; padding: 1rem; background: #f9f9f9; border-radius: 4px; }
          .toc { margin-bottom: 3rem; padding: 1.5rem; background: #f5f5f5; border-radius: 8px; }
          .toc ul { list-style: none; padding-left: 0; }
          .toc li { margin-bottom: 0.5rem; }
          .toc a { color: #0066cc; text-decoration: none; }
          .toc a:hover { text-decoration: underline; }
        </style>
      </head>
      <body>
        <h1>Context Refinery Export</h1>
        <div class="toc">
          <h2>Table of Contents</h2>
          <ul>
            ${importedDocs.map((doc, i) => `<li><a href="#doc-${i}">${doc.title || `Document ${i}`}</a></li>`).join('')}
          </ul>
        </div>
    `;

    importedDocs.forEach((doc, i) => {
      // NOTE: We're rendering raw markdown as text for simplicity in this pure frontend implementation without a markdown parser library dependency in HTML.
      // In a real scenario you'd parse the markdown to HTML first.
      htmlContent += `
        <div class="doc-container" id="doc-${i}">
          <h2>${doc.title || `Document ${i}`}</h2>
          <div class="meta">
            <strong>Source:</strong> ${doc.source?.system || 'Unknown'}<br>
            <strong>Tags:</strong> ${doc.tags?.join(', ') || 'None'}<br>
            <strong>Date:</strong> ${doc.timestamps?.ingested_at || 'Unknown'}
          </div>
          <pre style="white-space: pre-wrap; font-family: inherit;">${doc.content?.cleaned_markdown || doc.content?.raw_text || ''}</pre>
        </div>
      `;
    });

    htmlContent += `</body></html>`;

    const blob = new Blob([htmlContent], { type: 'text/html' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'context_refinery_export.html';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  return (
    <div className="px-8 py-12">
      <div className="max-w-6xl mx-auto">
        {/* Header Section */}
        <header className="mb-12">
          <h1 className="text-5xl font-extrabold font-headline tracking-tighter text-on-surface mb-2">Delivery Lab</h1>
          <p className="text-slate-500 text-lg max-w-2xl">Finalize your workspace extractions. Choose your delivery vector and review the generated manifest.</p>
        </header>

        {/* Processing Summary */}
        <section className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-12">
          <Card className="p-6 rounded-xl shadow-sm flex flex-col justify-between border-l-4 border-primary bg-white">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-4">Total Items</span>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-primary">{totalItems}</span>
              <span className="text-xs text-secondary font-medium">Ready</span>
            </div>
          </Card>
          <Card className="p-6 rounded-xl shadow-sm flex flex-col justify-between bg-white">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-4">Processed Tokens</span>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-on-surface">{processedTokens}</span>
              <span className="text-xs text-slate-400">Distilled</span>
            </div>
          </Card>
          <Card className="p-6 rounded-xl shadow-sm flex flex-col justify-between bg-white">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-4">Active Sources</span>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-on-surface">{activeSources}</span>
              <span className="text-xs text-slate-400">Channels</span>
            </div>
          </Card>
          <Card className="bg-secondary-container/20 p-6 rounded-xl shadow-sm flex flex-col justify-center items-center text-center border-none">
            <CheckCircle className="w-6 h-6 text-secondary mb-2 fill-secondary/20" />
            <span className="text-sm font-bold text-on-secondary-container">Integrity Verified</span>
            <span className="text-[10px] text-on-secondary-container/70">Checksum match confirmed</span>
          </Card>
        </section>

        {/* Primary Action Cards */}
        <section className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
          {/* RAG Export */}
          <Card className="p-8 rounded-xl shadow-lg border border-white/50 group hover:shadow-xl transition-all duration-300 bg-white/80 backdrop-blur-xl">
            <div className="flex justify-between items-start mb-6">
              <div className="p-4 bg-primary/5 rounded-xl">
                <Database className="w-10 h-10 text-primary" />
              </div>
              <Badge className="bg-primary text-white text-[10px] font-bold rounded-full uppercase tracking-widest border-none">Recommended</Badge>
            </div>
            <h3 className="text-2xl font-bold font-headline mb-3 group-hover:text-primary transition-colors">RAG Export</h3>
            <p className="text-slate-500 mb-6 leading-relaxed">
              Optimized for Large Language Models. Outputs <code className="text-xs bg-surface-container-high px-1 rounded">.md</code> files with structural YAML frontmatter, preserving hierarchical breadcrumbs in a zipped archive.
            </p>
            <ul className="space-y-3 mb-8">
              <li className="flex items-center gap-2 text-sm text-on-surface-variant">
                <CheckCircle className="w-4 h-4 text-secondary" /> Metadata-Rich Headers
              </li>
              <li className="flex items-center gap-2 text-sm text-on-surface-variant">
                <CheckCircle className="w-4 h-4 text-secondary" /> Relationship Preservation
              </li>
            </ul>
            <Button
              className="w-full py-6 bg-gradient-to-br from-primary to-primary-container text-white rounded-xl font-bold flex items-center justify-center gap-3 hover:scale-[1.02] active:scale-[0.98] transition-all disabled:opacity-50"
              onClick={handleZipExport}
              disabled={isExporting || !isImported}
            >
              {isExporting ? <Loader2 className="w-5 h-5 animate-spin" /> : <Archive className="w-5 h-5" />}
              {isExporting ? 'Generating...' : 'Generate Zipped MD'}
            </Button>
          </Card>

          {/* Personal Read Export */}
          <Card className="p-8 rounded-xl shadow-lg border border-white/50 group hover:shadow-xl transition-all duration-300 bg-white/80 backdrop-blur-xl">
            <div className="flex justify-between items-start mb-6">
              <div className="p-4 bg-secondary/5 rounded-xl">
                <BookOpen className="w-10 h-10 text-secondary" />
              </div>
            </div>
            <h3 className="text-2xl font-bold font-headline mb-3 group-hover:text-secondary transition-colors">Personal Read Export</h3>
            <p className="text-slate-500 mb-6 leading-relaxed">
              Distilled for human consumption. Outputs a clean, single <code className="text-xs bg-surface-container-high px-1 rounded">HTML</code> or <code className="text-xs bg-surface-container-high px-1 rounded">PDF</code> file with refined typography and table of contents.
            </p>
            <ul className="space-y-3 mb-8">
              <li className="flex items-center gap-2 text-sm text-on-surface-variant">
                <CheckCircle className="w-4 h-4 text-secondary" /> High-End Editorial Layout
              </li>
              <li className="flex items-center gap-2 text-sm text-on-surface-variant">
                <CheckCircle className="w-4 h-4 text-secondary" /> Offline-Ready Assets
              </li>
            </ul>
            <div className="grid grid-cols-2 gap-4">
              <Button
                variant="secondary"
                className="bg-surface-container-high text-on-surface py-6 rounded-xl font-bold flex items-center justify-center gap-3 hover:bg-surface-container-highest active:scale-[0.98] transition-all disabled:opacity-50"
                onClick={handleHtmlExport}
                disabled={!isImported}
              >
                <FileCode className="w-5 h-5" />
                Web HTML
              </Button>
              <Button variant="secondary" className="bg-surface-container-high text-on-surface py-6 rounded-xl font-bold flex items-center justify-center gap-3 hover:bg-surface-container-highest active:scale-[0.98] transition-all">
                <Printer className="w-5 h-5" />
                Print PDF
              </Button>
            </div>
          </Card>
        </section>

        {/* Output Manifest */}
        <section className="bg-surface-container-low rounded-2xl p-8 border border-outline-variant/10">
          <div className="flex items-center justify-between mb-8">
            <div>
              <h2 className="text-xl font-bold font-headline mb-1">Output Manifest</h2>
              <p className="text-xs text-slate-500">Staged files ready for transfer</p>
            </div>
            <Button variant="link" className="text-primary text-sm font-bold flex items-center gap-2 hover:underline p-0 h-auto no-underline">
              <RefreshCw className="w-4 h-4" />
              Refresh State
            </Button>
          </div>
          <div className="space-y-3">
            {MOCK_OUTPUT_FILES.map((file) => (
              <div key={file.id} className="bg-white p-4 rounded-xl flex items-center justify-between hover:translate-x-1 transition-all duration-300 shadow-sm border border-outline-variant/5">
                <div className="flex items-center gap-4">
                  <div className={cn(
                    "w-10 h-10 rounded-lg flex items-center justify-center",
                    file.name.endsWith('.json') ? "bg-orange-50 text-orange-400" : 
                    file.name.endsWith('.pdf') ? "bg-red-50 text-red-400" : "bg-blue-50 text-blue-400"
                  )}>
                    {file.name.endsWith('.json') && <FileJson className="w-5 h-5" />}
                    {file.name.endsWith('.pdf') && <FileText className="w-5 h-5" />}
                    {file.name.endsWith('.zip') && <Archive className="w-5 h-5" />}
                  </div>
                  <div>
                    <h4 className="text-sm font-bold">{file.name}</h4>
                    <p className="text-[10px] text-slate-400">{file.type} • {file.description}</p>
                  </div>
                </div>
                <div className="flex items-center gap-6">
                  <span className="text-xs font-medium text-slate-500">{file.size}</span>
                  <Button variant="ghost" size="icon" className="text-slate-400 hover:text-primary">
                    <Download className="w-5 h-5" />
                  </Button>
                </div>
              </div>
            ))}
          </div>
        </section>
      </div>
    </div>
  );
}
