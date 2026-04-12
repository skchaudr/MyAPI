import React, { useState, useEffect, useRef } from 'react';
import { Upload, Book, MessageSquare, Bot, Briefcase, Folder, FileText, Database, History, Filter, Search, Loader2 } from 'lucide-react';
import { MOCK_SOURCES, MOCK_DOCUMENTS } from '../mockData';
import { Button } from './ui/button';
import { Card } from './ui/card';
import { Badge } from './ui/badge';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from './ui/table';
import { cn } from '@/lib/utils';
import { importObsidianFile, importChatGPTFile } from '../services/apiService';

export default function ImportView() {
  const [importedDocs, setImportedDocs] = useState<any[]>([]);
  const [isUploading, setIsUploading] = useState(false);
  const [uploadError, setUploadError] = useState<string | null>(null);
  const [userEmail, setUserEmail] = useState<string>('');
  const [emailSaved, setEmailSaved] = useState(false);

  const fileInputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    // Phase 4 Fix: Always restore from the default session so email isn't a blocker
    const savedDocs = localStorage.getItem('cr_docs_default');
    if (savedDocs) {
      try {
        setImportedDocs(JSON.parse(savedDocs));
      } catch (e) {
        console.error("Failed to parse saved docs");
      }
    }
  }, []);

  useEffect(() => {
    // Always save to the default session key
    localStorage.setItem('cr_docs_default', JSON.stringify(importedDocs));
  }, [importedDocs]);

  const handleSaveSession = () => {
    if (userEmail.trim()) {
      localStorage.setItem('cr_session_email', userEmail.trim());
      setEmailSaved(true);
    }
  };

  const handleClearSession = () => {
    localStorage.removeItem('cr_session_email');
    localStorage.removeItem('cr_docs_default');
    setUserEmail('');
    setEmailSaved(false);
    setImportedDocs([]);
  };

  const handleFileUpload = async (files: FileList | null) => {
    if (!files || files.length === 0) return;
    setIsUploading(true);
    setUploadError(null);
    const newDocs: any[] = [];

    for (const file of Array.from(files)) {
      try {
        if (file.name.endsWith('.md')) {
          const doc = await importObsidianFile(file);
          newDocs.push(doc);
        } else if (file.name.endsWith('.json')) {
          const docs = await importChatGPTFile(file);
          newDocs.push(...docs);
        } else {
          setUploadError(`Unsupported file type: ${file.name}. Use .md or .json`);
        }
      } catch (err: any) {
        setUploadError(err.message ?? 'Upload failed');
      }
    }

    setImportedDocs(prev => [...prev, ...newDocs]);
    setIsUploading(false);
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    handleFileUpload(e.dataTransfer.files);
  };

  const displayDocs = importedDocs;

  return (
    <div className="px-8 py-12">
      {/* Header Section */}
      <section className="mb-10 max-w-6xl mx-auto">
        <div className="flex flex-col gap-1">
          <span className="text-xs font-bold tracking-[0.2em] text-secondary uppercase">Ingestion Engine</span>
          <h1 className="text-5xl font-extrabold tracking-tight text-on-surface font-headline">Source Lab</h1>
          <p className="text-slate-500 mt-2 max-w-xl">High-volume data ingestion for contextual intelligence. Distill raw directories and history exports into structured refinery nodes.</p>
        </div>
      </section>

      {/* Bento Layout: Drop Zone & Detected Sources */}
      <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-8 mb-12">
        {/* Central Drop Zone */}
        <div className="lg:col-span-8 bg-white rounded-[2rem] p-8 shadow-sm relative overflow-hidden group border border-outline-variant/10">
          <div className="absolute -top-24 -right-24 w-64 h-64 bg-primary-fixed opacity-20 blur-[80px] pointer-events-none"></div>
          <div
            className="relative h-full flex flex-col items-center justify-center border-2 border-dashed border-outline-variant/30 rounded-[1.5rem] py-16 px-6 group-hover:border-primary/40 transition-colors bg-surface-container-low/30"
            onDragOver={handleDragOver}
            onDrop={handleDrop}
          >
            <div className="w-20 h-20 bg-primary-fixed text-primary rounded-3xl flex items-center justify-center mb-6 shadow-inner">
              {isUploading ? <Loader2 className="w-10 h-10 animate-spin" /> : <Upload className="w-10 h-10" />}
            </div>
            <h3 className="text-2xl font-bold mb-2">Drop data to begin</h3>
            <p className="text-slate-500 text-center mb-8">
              {isUploading ? "Importing files..." : "Support for zip, folder, json, txt, md, csv"}
            </p>
            <div className="flex flex-wrap justify-center gap-3">
              {['.ZIP', '.JSON', '.MD', '.CSV'].map((ext) => (
                <span key={ext} className="px-4 py-2 bg-white rounded-full text-xs font-bold text-slate-600 border border-outline-variant/20 shadow-sm">
                  {ext}
                </span>
              ))}
            </div>

            <input
              type="file"
              multiple
              accept=".md,.json"
              className="hidden"
              ref={fileInputRef}
              onChange={(e) => handleFileUpload(e.target.files)}
            />
            <Button
              className="mt-10 px-8 py-6 bg-on-surface text-white rounded-xl font-bold hover:bg-slate-800 transition-colors"
              onClick={() => fileInputRef.current?.click()}
              disabled={isUploading}
            >
              {isUploading ? "Uploading..." : "Browse Files"}
            </Button>
            {uploadError && <div className="mt-4 text-red-500 font-bold">{uploadError}</div>}
          </div>
        </div>

        {/* Detected Sources Panel */}
        <div className="lg:col-span-4 flex flex-col gap-4">
          <div className="bg-surface-container-low rounded-[2rem] p-6 flex flex-col h-full border border-outline-variant/10">
            <div className="flex items-center justify-between mb-6">
              <h3 className="font-bold text-on-surface">Detected Sources</h3>
              <Badge className="bg-secondary-container text-on-secondary-container text-[10px] font-bold rounded-md border-none">AUTO-SCAN ON</Badge>
            </div>
            <div className="flex flex-col gap-3">
              {MOCK_SOURCES.map((source) => (
                <div key={source.id} className="bg-white p-4 rounded-2xl flex items-center justify-between shadow-sm border border-outline-variant/10">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-slate-100 rounded-xl flex items-center justify-center text-slate-600">
                      {source.icon === 'book' && <Book className="w-5 h-5" />}
                      {source.icon === 'chat' && <MessageSquare className="w-5 h-5" />}
                      {source.icon === 'smart_toy' && <Bot className="w-5 h-5" />}
                      {source.icon === 'work' && <Briefcase className="w-5 h-5" />}
                    </div>
                    <div>
                      <div className="text-sm font-bold">{source.name}</div>
                      <div className={cn(
                        "text-[10px] font-bold uppercase tracking-wider",
                        source.confidence === 'high' ? "text-secondary" : "text-amber-600"
                      )}>
                        {source.confidence} Confidence
                      </div>
                    </div>
                  </div>
                  <Button variant="ghost" size="icon" className="h-8 w-8 text-slate-400">
                    <Filter className="w-4 h-4" />
                  </Button>
                </div>
              ))}
            </div>

            {/* Email Session UI */}
            <div className="mt-6 pt-6 border-t border-outline-variant/20 flex flex-col gap-2">
              {!emailSaved ? (
                <>
                  <input
                    type="email"
                    placeholder="Enter email to save/restore session"
                    className="w-full text-sm p-2 rounded border border-outline-variant/30"
                    value={userEmail}
                    onChange={(e) => setUserEmail(e.target.value)}
                    onKeyDown={(e) => e.key === 'Enter' && handleSaveSession()}
                  />
                  <Button onClick={handleSaveSession} variant="secondary" size="sm" className="w-full">
                    Save Session
                  </Button>
                </>
              ) : (
                <div className="text-sm text-green-600 flex flex-col gap-2">
                  <span>✓ Session saved for {userEmail}</span>
                  <Button onClick={handleClearSession} variant="link" size="sm" className="text-red-500 p-0 h-auto self-start">
                    Clear Session
                  </Button>
                </div>
              )}
            </div>

            <Button variant="link" className="mt-auto pt-4 text-sm font-bold text-primary flex items-center justify-center gap-2 hover:translate-x-1 transition-transform no-underline">
              Review Mapping <Upload className="w-4 h-4 rotate-90" />
            </Button>
          </div>
        </div>
      </div>

      {/* Recently Uploaded Table */}
      <section className="max-w-6xl mx-auto">
        <div className="flex items-end justify-between mb-6">
          <div>
            <h2 className="text-2xl font-bold tracking-tight font-headline">Recently Uploaded</h2>
            <p className="text-slate-500 text-sm">Review ingestion logs and processing status.</p>
          </div>
          <div className="flex gap-2">
            <Button variant="secondary" size="icon" className="bg-surface-container-high hover:bg-surface-container-highest">
              <Filter className="w-4 h-4 text-slate-600" />
            </Button>
            <Button variant="secondary" size="icon" className="bg-surface-container-high hover:bg-surface-container-highest">
              <Search className="w-4 h-4 text-slate-600" />
            </Button>
          </div>
        </div>
        <div className="bg-white rounded-[1.5rem] overflow-hidden shadow-sm border border-outline-variant/10">
          <Table>
            <TableHeader className="bg-surface-container-low/50">
              <TableRow>
                <TableHead className="px-6 py-4 text-xs font-bold text-slate-500 uppercase tracking-widest">Source Name</TableHead>
                <TableHead className="px-6 py-4 text-xs font-bold text-slate-500 uppercase tracking-widest">Type</TableHead>
                <TableHead className="px-6 py-4 text-xs font-bold text-slate-500 uppercase tracking-widest">Size</TableHead>
                <TableHead className="px-6 py-4 text-xs font-bold text-slate-500 uppercase tracking-widest">Date</TableHead>
                <TableHead className="px-6 py-4 text-xs font-bold text-slate-500 uppercase tracking-widest text-right">Action</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody className="divide-y divide-outline-variant/10">
              {displayDocs.length === 0 ? (
                <TableRow>
                  <TableCell colSpan={5} className="px-6 py-12 text-center text-slate-400 text-sm">
                    No documents imported yet. Drop a <code>.md</code> or <code>.json</code> file above to get started.
                  </TableCell>
                </TableRow>
              ) : displayDocs.map((doc: any, index: number) => {
                const name = doc.title;
                const type = doc.source?.system;
                const size = (doc.content?.cleaned_markdown?.length ?? 0) + " chars";
                const date = doc.timestamps?.ingested_at || "just now";

                return (
                  <TableRow key={doc.id + index} className="hover:bg-surface-container-low/20 transition-colors group">
                    <TableCell className="px-6 py-5">
                      <div className="flex items-center gap-3">
                        {String(type).toLowerCase().includes('obsidian') ? <Folder className="w-5 h-5 text-primary" /> : <FileText className="w-5 h-5 text-secondary" />}
                        <span className="font-semibold text-on-surface">{name}</span>
                      </div>
                    </TableCell>
                    <TableCell className="px-6 py-5 text-sm text-slate-600">{type}</TableCell>
                    <TableCell className="px-6 py-5 text-sm text-slate-600">{size}</TableCell>
                    <TableCell className="px-6 py-5 text-sm text-slate-600">{date}</TableCell>
                    <TableCell className="px-6 py-5 text-right">
                      <Button variant="link" className="text-primary font-bold text-sm opacity-0 group-hover:opacity-100 transition-opacity p-0 h-auto">
                        View Details
                      </Button>
                    </TableCell>
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </div>
      </section>
    </div>
  );
}
