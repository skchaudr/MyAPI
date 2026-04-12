import React, { useState, useEffect } from 'react';
import { Search, FileText, Bot, History, Circle, ChevronRight, FileSearch, Verified, Edit3, Archive, CheckCircle, Sparkles, Wand2, Trash2, X } from 'lucide-react';
import { MOCK_DOCUMENTS } from '../mockData';
import { Document } from '../types';
import { cn } from '@/lib/utils';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { Badge } from './ui/badge';
import { Switch } from './ui/switch';
import { ScrollArea } from './ui/scroll-area';
import { distillContent } from '../services/apiService';
import ReactMarkdown from 'react-markdown';

export default function RefineView() {
  const [selectedDoc, setSelectedDoc] = useState<Document>(MOCK_DOCUMENTS[0]);
  const [isDistilling, setIsDistilling] = useState(false);
  const [apiError, setApiError] = useState<string | null>(null);
  const [summary, setSummary] = useState<string | undefined>(selectedDoc.summary);
  const [backendOnline, setBackendOnline] = useState<boolean | null>(null);

  useEffect(() => {
    // Phase 3: Check backend availability for graceful degradation
    fetch('http://localhost:8000/health', { signal: AbortSignal.timeout(2000) })
      .then(r => setBackendOnline(r.ok))
      .catch(() => setBackendOnline(false));
  }, []);

  const handleDistill = async () => {
    setIsDistilling(true);
    setApiError(null);
    try {
      const result = await distillContent(selectedDoc.content);
      setSummary(result);
    } catch (err: any) {
      setApiError(err.message ?? "API unavailable — is the server running?");
    } finally {
      setIsDistilling(false);
    }
  };

  return (
    <div className="flex h-[calc(100vh-4rem)] overflow-hidden">
      {/* List Panel (Left) */}
      <section className="w-80 flex flex-col bg-surface border-r border-outline-variant/10 shadow-[4px_0_24px_rgba(0,0,0,0.02)] z-10">
        <div className="p-6 pb-4">
          <div className="relative">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 w-4 h-4" />
            <Input 
              className="w-full bg-surface-container-highest border-none rounded-xl pl-10 py-2.5 text-sm focus:ring-2 focus:ring-primary/20 transition-all" 
              placeholder="Search documents..." 
            />
          </div>
        </div>
        <ScrollArea className="flex-1 px-3 space-y-1 pb-10">
          {MOCK_DOCUMENTS.map((doc) => (
            <div 
              key={doc.id}
              onClick={() => setSelectedDoc(doc)}
              className={cn(
                "p-3 rounded-xl cursor-pointer transition-all group mb-1",
                selectedDoc.id === doc.id 
                  ? "bg-white shadow-sm border border-outline-variant/30" 
                  : "hover:bg-surface-container-low border border-transparent"
              )}
            >
              <div className="flex items-start gap-3">
                <div className={cn(
                  "p-1.5 rounded-lg",
                  doc.type.includes('Vault') ? "bg-purple-50 text-purple-600" : "bg-secondary/10 text-secondary"
                )}>
                  {doc.type.includes('Vault') ? <FileText className="w-4 h-4" /> : <Bot className="w-4 h-4" />}
                </div>
                <div className="flex-1 min-w-0">
                  <h4 className={cn(
                    "text-sm truncate mb-0.5",
                    selectedDoc.id === doc.id ? "font-bold text-on-surface" : "font-medium text-slate-600"
                  )}>
                    {doc.name}
                  </h4>
                  <p className="text-[10px] text-slate-400 truncate">Source: {doc.source}</p>
                </div>
                {selectedDoc.id === doc.id && <div className="w-1.5 h-1.5 bg-secondary rounded-full mt-1.5"></div>}
              </div>
            </div>
          ))}
          <div className="p-3 hover:bg-surface-container-low rounded-xl cursor-pointer transition-all group opacity-60">
            <div className="flex items-start gap-3">
              <div className="bg-slate-100 p-1.5 rounded-lg text-slate-400">
                <History className="w-4 h-4" />
              </div>
              <div className="flex-1 min-w-0">
                <h4 className="text-sm font-medium truncate text-slate-500">Legacy Architecture Docs</h4>
                <p className="text-[10px] text-slate-400 truncate">Deprecated 2 days ago</p>
              </div>
            </div>
          </div>
        </ScrollArea>
      </section>

      {/* Preview Panel (Center) */}
      <section className="flex-1 bg-white overflow-y-auto no-scrollbar border-r border-outline-variant/10">
        <div className="max-w-3xl mx-auto px-12 py-16 relative">
          <div className="flex items-center gap-2 mb-8">
            <Badge className="bg-primary-fixed text-on-primary-fixed px-3 py-1 rounded-full text-[10px] font-bold tracking-widest uppercase border-none">
              Draft Preview
            </Badge>
            <span className="text-slate-300">•</span>
            <span className="text-xs text-slate-400">Last edited {selectedDoc.date}</span>
          </div>
          <h1 className="font-headline text-4xl font-bold tracking-tight text-on-surface mb-8 leading-tight">
            {selectedDoc.name}
          </h1>
          
          <div className="prose prose-slate max-w-none text-on-surface-variant leading-relaxed space-y-6">
            <ReactMarkdown
              components={{
                h3: ({node, ...props}) => <h3 className="text-xl font-bold text-on-surface mt-10 mb-4" {...props} />,
                ul: ({node, ...props}) => <ul className="space-y-4 list-none pl-0" {...props} />,
                li: ({node, ...props}) => (
                  <li className="flex gap-3">
                    <Circle className="w-1.5 h-1.5 bg-primary rounded-full mt-2.5 flex-shrink-0" />
                    <span>{props.children}</span>
                  </li>
                ),
                blockquote: ({node, ...props}) => (
                  <div className="bg-surface-container-low p-6 rounded-xl border-l-4 border-secondary my-8 italic text-slate-600">
                    {props.children}
                  </div>
                ),
                strong: ({node, ...props}) => <strong className="font-bold text-on-surface" {...props} />,
              }}
            >
              {selectedDoc.content}
            </ReactMarkdown>
          </div>

          {summary && (
            <div className="mt-12 p-6 bg-primary/5 rounded-2xl border border-primary/10">
              <div className="flex items-center gap-2 mb-3 text-primary">
                <Sparkles className="w-4 h-4" />
                <span className="text-xs font-bold uppercase tracking-wider">AI Distillation</span>
              </div>
              <p className="text-sm text-slate-700 leading-relaxed">{summary}</p>
            </div>
          )}

          {/* Decorative background glow */}
          <div className="fixed top-0 right-0 w-1/3 h-1/2 bg-gradient-radial from-primary-fixed/10 to-transparent pointer-events-none -z-10"></div>
        </div>
      </section>

      {/* RAG Optimization Panel (Right) */}
      <section className="w-80 bg-surface-container-low p-6 overflow-y-auto no-scrollbar">
        <div className="flex items-center justify-between mb-8">
          <h3 className="font-headline text-lg font-bold">RAG Optimization</h3>
          <Button variant="ghost" size="icon" className="text-slate-400">
            <Wand2 className="w-5 h-5" />
          </Button>
        </div>

        <div className="space-y-8">
          {/* AI Refinement Section */}
          <div className="space-y-4">
            <h4 className="text-[10px] font-bold uppercase tracking-widest text-slate-500">Refinery Actions</h4>
            <Button 
              variant="ghost" 
              className="w-full group bg-white hover:bg-white p-4 h-auto rounded-xl flex items-center justify-between transition-all border border-transparent hover:border-secondary/20 shadow-sm"
            >
              <div className="flex items-center gap-3">
                <Trash2 className="w-5 h-5 text-secondary" />
                <span className="text-sm font-semibold">Scrub Noise</span>
              </div>
              <ChevronRight className="w-4 h-4 text-slate-300 group-hover:text-secondary transition-all" />
            </Button>
            
            <div className="bg-white p-4 rounded-xl shadow-sm space-y-4 border border-outline-variant/10">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                <FileSearch className="w-5 h-5 text-primary" />
                  <span className="text-sm font-semibold">Distill Gemini</span>
                </div>
                <Switch 
                  checked={!!summary} 
                  onCheckedChange={(checked) => {
                    if (checked && !summary) handleDistill();
                    else if (!checked) setSummary(undefined);
                  }}
                  disabled={isDistilling || backendOnline === false}
                />
              </div>
              <p className="text-[10px] text-slate-400 leading-relaxed">
                {backendOnline === false
                  ? 'AI enrichment offline. Start the local API server to enable.'
                  : isDistilling ? 'Processing content...'
                  : 'Auto-generate a 3-sentence semantic summary for embedding indexes.'}
              </p>
              {backendOnline === false && (
                <div className="text-amber-500 text-[10px] font-bold mt-1">⚠ Run ./run_dev.sh to enable AI features</div>
              )}
              {apiError && <div className="text-red-500 text-xs font-bold mt-2">{apiError}</div>}
            </div>
          </div>

          {/* Metadata Section */}
          <div className="space-y-4">
            <h4 className="text-[10px] font-bold uppercase tracking-widest text-slate-500">Document Metadata</h4>
            <div className="space-y-2">
              <label className="text-[11px] font-bold text-slate-500 ml-1">Title Override</label>
              <Input 
                className="w-full bg-surface-container-highest border-none rounded-lg py-2 text-sm focus:ring-2 focus:ring-primary/20" 
                defaultValue={selectedDoc.name.replace('.md', '')}
              />
            </div>
            <div className="space-y-2">
              <label className="text-[11px] font-bold text-slate-500 ml-1">Tags</label>
              <div className="flex flex-wrap gap-2 mb-2">
                {selectedDoc.tags.map(tag => (
                  <Badge key={tag} className="bg-secondary-container/40 text-on-secondary-container px-2 py-0.5 rounded-full text-[10px] font-bold flex items-center gap-1 border-none">
                    #{tag} <X className="w-3 h-3 cursor-pointer" />
                  </Badge>
                ))}
              </div>
              <Input 
                className="w-full bg-surface-container-highest border-none rounded-lg py-2 text-sm focus:ring-2 focus:ring-primary/20" 
                placeholder="Add tag..." 
              />
            </div>
          </div>

          {/* Maturity Section */}
          <div className="space-y-4">
            <h4 className="text-[10px] font-bold uppercase tracking-widest text-slate-500">Maturity Tagging</h4>
            <div className="grid grid-cols-1 gap-2">
              <Button 
                variant={selectedDoc.status === 'mature' ? 'default' : 'ghost'}
                className={cn(
                  "flex items-center justify-start gap-3 px-4 py-6 rounded-xl text-sm font-bold text-left shadow-sm",
                  selectedDoc.status === 'mature' ? "bg-white border-2 border-secondary/30 text-secondary hover:bg-white" : "bg-surface-container-highest/50 text-slate-500 font-medium hover:bg-surface-container-highest"
                )}
              >
                <Verified className={cn("w-5 h-5", selectedDoc.status === 'mature' && "fill-secondary/20")} />
                Mature
              </Button>
              <Button 
                variant="ghost"
                className="flex items-center justify-start gap-3 px-4 py-6 rounded-xl bg-surface-container-highest/50 text-slate-500 text-sm font-medium text-left hover:bg-surface-container-highest transition-all"
              >
                <Edit3 className="w-5 h-5" />
                Scratchpad
              </Button>
              <Button 
                variant="ghost"
                className="flex items-center justify-start gap-3 px-4 py-6 rounded-xl bg-surface-container-highest/50 text-slate-500 text-sm font-medium text-left hover:bg-surface-container-highest transition-all"
              >
                <Archive className="w-5 h-5" />
                Deprecated
              </Button>
            </div>
          </div>

          <Button className="w-full mt-4 bg-primary text-white py-6 rounded-xl font-bold shadow-lg shadow-primary/10 hover:translate-y-[-2px] active:translate-y-[0] transition-all flex items-center justify-center gap-2 group">
            Confirm Changes
            <CheckCircle className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
          </Button>
        </div>
      </section>
    </div>
  );
}
