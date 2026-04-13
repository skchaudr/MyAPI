import React, { useState, useEffect } from 'react';
import { Database, CheckCircle, Download, Archive, Loader2 } from 'lucide-react';
import { Button } from './ui/button';
import { Card } from './ui/card';
import { Badge } from './ui/badge';
import { exportToKhojBundle } from '../services/exportService';
import type { CanonicalDocument } from '../types/schema';
import { saveAs } from 'file-saver';

export default function ExportView() {
  const [docs, setDocs] = useState<CanonicalDocument[]>([]);
  const [isExporting, setIsExporting] = useState(false);
  const [exportError, setExportError] = useState<string | null>(null);
  const [exportSuccess, setExportSuccess] = useState(false);
  const [generatedBlob, setGeneratedBlob] = useState<Blob | null>(null);

  useEffect(() => {
    const saved = localStorage.getItem('cr_docs_default');
    if (saved) {
      try { setDocs(JSON.parse(saved)); } catch {}
    }
  }, []);

  const handleExport = async () => {
    setIsExporting(true);
    setExportError(null);
    setExportSuccess(false);
    try {
      const blob = await exportToKhojBundle(docs);
      setGeneratedBlob(blob);
      setExportSuccess(true);
    } catch (err: any) {
      setExportError(err.message ?? 'Export failed.');
    } finally {
      setIsExporting(false);
    }
  };

  return (
    <div className="px-8 py-12">
      <div className="max-w-6xl mx-auto">
        <header className="mb-12">
          <h1 className="text-5xl font-extrabold font-headline tracking-tighter text-on-surface mb-2">Delivery Lab</h1>
          <p className="text-slate-500 text-lg max-w-2xl">Finalize your workspace extractions. Choose your delivery vector and review the generated manifest.</p>
        </header>

        <section className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-12">
          <Card className="p-6 rounded-xl shadow-sm flex flex-col justify-between border-l-4 border-primary bg-white">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-4">Total Items</span>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-primary">{docs.length}</span>
              <span className="text-xs text-secondary font-medium">Ready</span>
            </div>
          </Card>
          <Card className="p-6 rounded-xl shadow-sm flex flex-col justify-between bg-white">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-4">Processed Chars</span>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-on-surface">
                {docs.reduce((acc, d) => acc + (d.content.cleaned_markdown?.length ?? 0), 0).toLocaleString()}
              </span>
              <span className="text-xs text-slate-400">chars</span>
            </div>
          </Card>
          <Card className="p-6 rounded-xl shadow-sm flex flex-col justify-between bg-white">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-4">Active Sources</span>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-on-surface">{new Set(docs.map(d => d.source?.system)).size}</span>
              <span className="text-xs text-slate-400">Channels</span>
            </div>
          </Card>
          <Card className="bg-secondary-container/20 p-6 rounded-xl shadow-sm flex flex-col justify-center items-center text-center border-none">
            <CheckCircle className="w-6 h-6 text-secondary mb-2 fill-secondary/20" />
            <span className="text-sm font-bold text-on-secondary-container">Integrity Verified</span>
            <span className="text-[10px] text-on-secondary-container/70">Schema-validated on import</span>
          </Card>
        </section>

        <section className="grid grid-cols-1 md:max-w-2xl gap-8 mb-12">
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
              Optimized for Large Language Models. Outputs <code className="text-xs bg-surface-container-high px-1 rounded">.md</code> files with structural YAML frontmatter in a zipped archive. 100% client-side — no server required.
            </p>
            <ul className="space-y-3 mb-8">
              <li className="flex items-center gap-2 text-sm text-on-surface-variant">
                <CheckCircle className="w-4 h-4 text-secondary" /> Strict YAML frontmatter per taxonomy contract
              </li>
              <li className="flex items-center gap-2 text-sm text-on-surface-variant">
                <CheckCircle className="w-4 h-4 text-secondary" /> Relationship Preservation
              </li>
              <li className="flex items-center gap-2 text-sm text-on-surface-variant">
                <CheckCircle className="w-4 h-4 text-secondary" /> Works offline — shareable with anyone
              </li>
            </ul>
            {exportError && <div className="text-red-500 text-sm font-bold mb-4">{exportError}</div>}
            {exportSuccess && <div className="text-green-600 text-sm font-bold mb-4">✓ khoj-ready-bundle.zip downloaded!</div>}
            {docs.length === 0 && (
              <p className="text-amber-600 text-xs font-bold mb-4">⚠ No documents loaded. Import files on the Import tab first.</p>
            )}
            <Button
              className="w-full py-6 bg-gradient-to-br from-primary to-primary-container text-white rounded-xl font-bold flex items-center justify-center gap-3 hover:scale-[1.02] active:scale-[0.98] transition-all disabled:opacity-50 disabled:cursor-not-allowed"
              onClick={handleExport}
              disabled={isExporting || docs.length === 0}
            >
              {isExporting ? <Loader2 className="w-5 h-5 animate-spin" /> : <Archive className="w-5 h-5" />}
              {isExporting ? 'Generating ZIP...' : 'Generate Zipped MD'}
            </Button>
          </Card>
        </section>

        <section className="bg-surface-container-low rounded-2xl p-8 border border-outline-variant/10">
          <div className="flex items-center justify-between mb-8">
            <div>
              <h2 className="text-xl font-bold font-headline mb-1">Output Manifest</h2>
              <p className="text-xs text-slate-500">Staged files ready for transfer</p>
            </div>
          </div>
          <div className="space-y-3">
            {!generatedBlob ? (
              <div className="text-sm text-slate-500 italic p-4 text-center">No files generated yet.</div>
            ) : (
              <div className="bg-white p-4 rounded-xl flex items-center justify-between hover:translate-x-1 transition-all duration-300 shadow-sm border border-outline-variant/5">
                <div className="flex items-center gap-4">
                  <div className="w-10 h-10 rounded-lg flex items-center justify-center bg-blue-50 text-blue-400">
                    <Archive className="w-5 h-5" />
                  </div>
                  <div>
                    <h4 className="text-sm font-bold">khoj-ready-bundle.zip</h4>
                    <p className="text-[10px] text-slate-400">Hierarchical MD • {docs.length} Files</p>
                  </div>
                </div>
                <div className="flex items-center gap-6">
                  <span className="text-xs font-medium text-slate-500">
                    {(generatedBlob.size / 1024 / 1024).toFixed(2)} MB
                  </span>
                  <Button
                    variant="ghost"
                    size="icon"
                    className="text-slate-400 hover:text-primary cursor-pointer"
                    onClick={() => saveAs(generatedBlob, 'khoj-ready-bundle.zip')}
                  >
                    <Download className="w-5 h-5" />
                  </Button>
                </div>
              </div>
            )}
          </div>
        </section>
      </div>
    </div>
  );
}
