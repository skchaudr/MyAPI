import React from 'react';
import { Upload, Book, MessageSquare, Bot, Briefcase, Folder, FileText, Database, History, Filter, Search } from 'lucide-react';
import { MOCK_SOURCES, MOCK_DOCUMENTS } from '../mockData';
import { Button } from './ui/button';
import { Card } from './ui/card';
import { Badge } from './ui/badge';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from './ui/table';
import { cn } from '@/lib/utils';

export default function ImportView() {
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
          <div className="relative h-full flex flex-col items-center justify-center border-2 border-dashed border-outline-variant/30 rounded-[1.5rem] py-16 px-6 group-hover:border-primary/40 transition-colors bg-surface-container-low/30">
            <div className="w-20 h-20 bg-primary-fixed text-primary rounded-3xl flex items-center justify-center mb-6 shadow-inner">
              <Upload className="w-10 h-10" />
            </div>
            <h3 className="text-2xl font-bold mb-2">Drop data to begin</h3>
            <p className="text-slate-500 text-center mb-8">Support for zip, folder, json, txt, md, csv</p>
            <div className="flex flex-wrap justify-center gap-3">
              {['.ZIP', '.JSON', '.MD', '.CSV'].map((ext) => (
                <span key={ext} className="px-4 py-2 bg-white rounded-full text-xs font-bold text-slate-600 border border-outline-variant/20 shadow-sm">
                  {ext}
                </span>
              ))}
            </div>
            <Button className="mt-10 px-8 py-6 bg-on-surface text-white rounded-xl font-bold hover:bg-slate-800 transition-colors">
              Browse Files
            </Button>
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
            <Button variant="link" className="mt-auto pt-6 text-sm font-bold text-primary flex items-center justify-center gap-2 hover:translate-x-1 transition-transform no-underline">
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
              {MOCK_DOCUMENTS.map((doc) => (
                <TableRow key={doc.id} className="hover:bg-surface-container-low/20 transition-colors group">
                  <TableCell className="px-6 py-5">
                    <div className="flex items-center gap-3">
                      {doc.type.includes('Vault') ? <Folder className="w-5 h-5 text-primary" /> : <FileText className="w-5 h-5 text-secondary" />}
                      <span className="font-semibold text-on-surface">{doc.name}</span>
                    </div>
                  </TableCell>
                  <TableCell className="px-6 py-5 text-sm text-slate-600">{doc.type}</TableCell>
                  <TableCell className="px-6 py-5 text-sm text-slate-600">{doc.size}</TableCell>
                  <TableCell className="px-6 py-5 text-sm text-slate-600">{doc.date}</TableCell>
                  <TableCell className="px-6 py-5 text-right">
                    <Button variant="link" className="text-primary font-bold text-sm opacity-0 group-hover:opacity-100 transition-opacity p-0 h-auto">
                      View Details
                    </Button>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </div>
      </section>
    </div>
  );
}
