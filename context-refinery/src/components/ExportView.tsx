import React from 'react';
import { Database, BookOpen, CheckCircle, Download, FileJson, FileText, Archive, RefreshCw, FileCode, Printer } from 'lucide-react';
import { MOCK_OUTPUT_FILES } from '../mockData';
import { Button } from './ui/button';
import { Card } from './ui/card';
import { Badge } from './ui/badge';
import { cn } from '@/lib/utils';

export default function ExportView() {
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
              <span className="text-3xl font-extrabold text-primary">2,450</span>
              <span className="text-xs text-secondary font-medium">Ready</span>
            </div>
          </Card>
          <Card className="p-6 rounded-xl shadow-sm flex flex-col justify-between bg-white">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-4">Processed Tokens</span>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-on-surface">1.2M</span>
              <span className="text-xs text-slate-400">Distilled</span>
            </div>
          </Card>
          <Card className="p-6 rounded-xl shadow-sm flex flex-col justify-between bg-white">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-4">Active Sources</span>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-on-surface">4</span>
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
            <Button className="w-full py-6 bg-gradient-to-br from-primary to-primary-container text-white rounded-xl font-bold flex items-center justify-center gap-3 hover:scale-[1.02] active:scale-[0.98] transition-all">
              <Archive className="w-5 h-5" />
              Generate Zipped MD
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
              <Button variant="secondary" className="bg-surface-container-high text-on-surface py-6 rounded-xl font-bold flex items-center justify-center gap-3 hover:bg-surface-container-highest active:scale-[0.98] transition-all">
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
