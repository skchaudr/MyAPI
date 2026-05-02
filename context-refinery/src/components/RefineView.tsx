import React, { useState, useEffect } from 'react';
import { Search, FileText, Bot, History, Circle, ChevronRight, FileSearch, Verified, Edit3, Archive, CheckCircle, Sparkles, Wand2, Trash2, X, Folder } from 'lucide-react';
import { CanonicalDocument } from '../types/schema';
import { cn } from '@/lib/utils';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { Badge } from './ui/badge';
import { Switch } from './ui/switch';
import { ScrollArea } from './ui/scroll-area';
import { distillContent } from '../services/apiService';
import ReactMarkdown, { Components } from 'react-markdown';


const markdownComponents: Components = {
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
};

export default function RefineView() {
  const [docs, setDocs] = useState<CanonicalDocument[]>([]);
  const [selectedDoc, setSelectedDoc] = useState<CanonicalDocument | null>(null);
  const [isDistilling, setIsDistilling] = useState(false);
  const [apiError, setApiError] = useState<string | null>(null);
  const [backendOnline, setBackendOnline] = useState<boolean | null>(null);

  useEffect(() => {
    // Phase 3: Check backend availability for graceful degradation
    fetch('http://localhost:8000/health', { signal: AbortSignal.timeout(2000) })
      .then(r => setBackendOnline(r.ok))
      .catch(() => setBackendOnline(false));
  }, []);

  useEffect(() => {
    // Load from universal default key instead of MOCK_DOCUMENTS
    const saved = localStorage.getItem('cr_docs_default');
    if (saved) {
      try {
        const parsed = JSON.parse(saved);
        setDocs(parsed);
        if (parsed.length > 0) {
          setSelectedDoc(parsed[0]);
        }
      } catch {}
    }
  }, []);

  const saveDocs = (newDocs: CanonicalDocument[]) => {
    setDocs(newDocs);
    localStorage.setItem('cr_docs_default', JSON.stringify(newDocs));
  };

  const updateDoc = (updates: Partial<CanonicalDocument>) => {
    if (!selectedDoc) return;
    const updated = { ...selectedDoc, ...updates };
    setSelectedDoc(updated);
    const updatedDocs = docs.map(d => d.id === updated.id ? updated : d);
    saveDocs(updatedDocs);
  };

  const handleDistill = async () => {
    if (!selectedDoc) return;
    setIsDistilling(true);
    setApiError(null);
    try {
      const result = await distillContent(selectedDoc.content.cleaned_markdown || selectedDoc.content.raw_text);
      updateDoc({ content: { ...selectedDoc.content, summary: result } });
    } catch (err: any) {
      setApiError(err.message ?? "API unavailable — is the server running?");
    } finally {
      setIsDistilling(false);
    }
  };

  const handleToggleSummary = (checked: boolean) => {
    if (checked && !selectedDoc?.content.summary) handleDistill();
    else if (!checked) updateDoc({ content: { ...selectedDoc!.content, summary: undefined } });
  };

  if (docs.length === 0) {
    return (
      <div className="flex h-[calc(100vh-4rem)] items-center justify-center bg-surface w-full">
        <div className="text-center max-w-md">
          <h2 className="text-2xl font-bold font-headline mb-2">No documents found</h2>
          <p className="text-slate-500 mb-6">Drop some files in the Import tab first, then come here to refine them.</p>
        </div>
      </div>
    );
  }

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
          {docs.map((doc) => {
            const isObsidian = String(doc.source.system).toLowerCase().includes('obsidian');
            return (
              <div 
                key={doc.id}
                onClick={() => setSelectedDoc(doc)}
                className={cn(
                  "p-3 rounded-xl cursor-pointer transition-all group mb-1",
                  selectedDoc?.id === doc.id 
                    ? "bg-white shadow-sm border border-outline-variant/30" 
                    : "hover:bg-surface-container-low border border-transparent"
                )}
              >
                <div className="flex items-start gap-3">
                  <div className={cn(
                    "p-1.5 rounded-lg",
                    isObsidian ? "bg-purple-50 text-purple-600" : "bg-secondary/10 text-secondary"
                  )}>
                    {isObsidian ? <Folder className="w-4 h-4" /> : <Bot className="w-4 h-4" />}
                  </div>
                  <div className="flex-1 min-w-0">
                    <h4 className={cn(
                      "text-sm truncate mb-0.5",
                      selectedDoc?.id === doc.id ? "font-bold text-on-surface" : "font-medium text-slate-600"
                    )}>
                      {doc.title}
                    </h4>
                    <p className="text-[10px] text-slate-400 truncate flex items-center gap-1">
                      Source: {doc.source.system}
                      {doc.status === 'incubating' && <span className="w-1.5 h-1.5 rounded-full bg-blue-400 ml-1"></span>}
                      {doc.status === 'mature' && <span className="w-1.5 h-1.5 rounded-full bg-green-400 ml-1"></span>}
                      {doc.status === 'scratchpad' && <span className="w-1.5 h-1.5 rounded-full bg-gray-300 ml-1"></span>}
                    </p>
                  </div>
                  {selectedDoc?.id === doc.id && <div className="w-1.5 h-1.5 bg-secondary rounded-full mt-1.5"></div>}
                </div>
              </div>
            );
          })}
        </ScrollArea>
      </section>

      {/* Preview Panel (Center) */}
      <section className="flex-1 bg-white overflow-y-auto no-scrollbar border-r border-outline-variant/10">
        {selectedDoc && (
          <div className="max-w-3xl mx-auto px-12 py-16 relative">
            <div className="flex items-center justify-between mb-8">
              <div className="flex items-center gap-2">
                <Badge className={cn("px-3 py-1 rounded-full text-[10px] font-bold tracking-widest uppercase border-none", 
                  selectedDoc.status === 'mature' ? "bg-green-100 text-green-700" :
                  selectedDoc.status === 'incubating' ? "bg-blue-100 text-blue-700" :
                  selectedDoc.status === 'deprecated' ? "bg-red-100 text-red-700" :
                  "bg-slate-100 text-slate-600"
                )}>
                  {selectedDoc.status}
                </Badge>
                <span className="text-slate-300">•</span>
                <span className="text-xs text-slate-400">Imported {new Date(selectedDoc.timestamps.ingested_at || '').toLocaleDateString()}</span>
              </div>
              <Button variant="outline" size="sm" onClick={() => {
                const newDocs = docs.filter(d => d.id !== selectedDoc.id);
                saveDocs(newDocs);
                setSelectedDoc(newDocs.length > 0 ? newDocs[0] : null);
              }} className="text-red-500 border-red-100 hover:bg-red-50 text-xs">
                Delete Doc
              </Button>
            </div>
            <h1 className="font-headline text-4xl font-bold tracking-tight text-on-surface mb-8 leading-tight">
              {selectedDoc.title}
            </h1>
            
            <div className="prose prose-slate max-w-none text-on-surface-variant leading-relaxed space-y-6">
              <ReactMarkdown
                components={markdownComponents}
              >
                {selectedDoc.content.cleaned_markdown || selectedDoc.content.raw_text}
              </ReactMarkdown>
            </div>

            {selectedDoc.content.summary && (
              <div className="mt-12 p-6 bg-primary/5 rounded-2xl border border-primary/10">
                <div className="flex items-center gap-2 mb-3 text-primary">
                  <Sparkles className="w-4 h-4" />
                  <span className="text-xs font-bold uppercase tracking-wider">AI Distillation</span>
                </div>
                <p className="text-sm text-slate-700 leading-relaxed">{selectedDoc.content.summary}</p>
              </div>
            )}

            {/* Decorative background glow */}
            <div className="fixed top-0 right-0 w-1/3 h-1/2 bg-gradient-radial from-primary-fixed/10 to-transparent pointer-events-none -z-10"></div>
          </div>
        )}
      </section>

      {/* RAG Optimization Panel (Right) */}
      {selectedDoc && (
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
              
              <div className="bg-white p-4 rounded-xl shadow-sm space-y-4 border border-outline-variant/10">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-3">
                  <FileSearch className="w-5 h-5 text-primary" />
                    <span className="text-sm font-semibold">Distill Gemini</span>
                  </div>
                  <Switch 
                    checked={!!selectedDoc.content.summary} 
                    onCheckedChange={handleToggleSummary}
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
                  value={selectedDoc.title}
                  onChange={(e) => updateDoc({ title: e.target.value })}
                />
              </div>
              <div className="space-y-2">
                <label className="text-[11px] font-bold text-slate-500 ml-1">Projects</label>
                <div className="flex flex-wrap gap-2 mb-2">
                  {selectedDoc.projects?.map(proj => (
                    <Badge key={proj} className="bg-secondary-container/40 text-on-secondary-container px-2 py-0.5 rounded-full text-[10px] font-bold flex items-center gap-1 border-none">
                      #{proj} 
                      <X 
                        className="w-3 h-3 cursor-pointer" 
                        onClick={() => updateDoc({ projects: selectedDoc.projects?.filter(p => p !== proj) })}
                      />
                    </Badge>
                  ))}
                </div>
                <Input 
                  className="w-full bg-surface-container-highest border-none rounded-lg py-2 text-sm focus:ring-2 focus:ring-primary/20" 
                  placeholder="Type and hit enter..." 
                  onKeyDown={(e) => {
                    if (e.key === 'Enter' && e.currentTarget.value) {
                      const newProj = e.currentTarget.value.replace('#', '');
                      updateDoc({ projects: [...(selectedDoc.projects || []), newProj] });
                      e.currentTarget.value = '';
                    }
                  }}
                />
              </div>
            </div>

            {/* Maturity Section */}
            <div className="space-y-4">
              <h4 className="text-[10px] font-bold uppercase tracking-widest text-slate-500">Maturity Tagging</h4>
              <div className="grid grid-cols-1 gap-2">
                <Button 
                  onClick={() => updateDoc({ status: 'mature' })}
                  variant="ghost"
                  className={cn(
                    "flex items-center justify-start gap-3 px-4 py-6 rounded-xl text-sm font-bold text-left shadow-sm transition-all",
                    selectedDoc.status === 'mature' ? "bg-white border-2 border-secondary/30 text-secondary hover:bg-white" : "bg-surface-container-highest/50 text-slate-500 font-medium hover:bg-surface-container-highest"
                  )}
                >
                  <Verified className={cn("w-5 h-5", selectedDoc.status === 'mature' && "fill-secondary/20")} />
                  Mature
                </Button>
                <Button 
                  onClick={() => updateDoc({ status: 'incubating' })}
                  variant="ghost"
                  className={cn(
                    "flex items-center justify-start gap-3 px-4 py-6 rounded-xl text-sm font-medium text-left transition-all",
                    selectedDoc.status === 'incubating' ? "bg-white border-2 border-blue-400/30 text-blue-600 font-bold shadow-sm" : "bg-surface-container-highest/50 text-slate-500 hover:bg-surface-container-highest"
                  )}
                >
                  <Edit3 className="w-5 h-5" />
                  Incubating
                </Button>
                <Button 
                  onClick={() => updateDoc({ status: 'scratchpad' })}
                  variant="ghost"
                  className={cn(
                    "flex items-center justify-start gap-3 px-4 py-6 rounded-xl text-sm font-medium text-left transition-all",
                    selectedDoc.status === 'scratchpad' ? "bg-white border-2 border-slate-400/30 text-slate-700 font-bold shadow-sm" : "bg-surface-container-highest/50 text-slate-500 hover:bg-surface-container-highest"
                  )}
                >
                  <History className="w-5 h-5" />
                  Scratchpad
                </Button>
                <Button 
                  onClick={() => updateDoc({ status: 'deprecated' })}
                  variant="ghost"
                  className={cn(
                    "flex items-center justify-start gap-3 px-4 py-6 rounded-xl text-sm font-medium text-left transition-all",
                    selectedDoc.status === 'deprecated' ? "bg-white border-2 border-red-400/30 text-red-600 font-bold shadow-sm" : "bg-surface-container-highest/50 text-slate-500 hover:bg-surface-container-highest"
                  )}
                >
                  <Archive className="w-5 h-5" />
                  Deprecated
                </Button>
              </div>
            </div>
          </div>
        </section>
      )}
    </div>
  );
}
