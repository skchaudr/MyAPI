import { Source, Document, OutputFile } from './types';

export const MOCK_SOURCES: Source[] = [
  { id: '1', name: 'Obsidian Vault', type: 'Markdown Vault', confidence: 'high', icon: 'book' },
  { id: '2', name: 'ChatGPT History', type: 'JSON Export', confidence: 'high', icon: 'chat' },
  { id: '3', name: 'Claude Conversations', type: 'JSON Export', confidence: 'medium', icon: 'smart_toy' },
  { id: '4', name: 'LinkedIn Data', type: 'CSV Table', confidence: 'medium', icon: 'work' },
];

export const MOCK_DOCUMENTS: Document[] = [
  {
    id: 'doc1',
    name: 'Q3 Market Strategy.md',
    source: 'Obsidian Personal Vault',
    type: 'Markdown Vault',
    size: '12.4 MB',
    date: '2 mins ago',
    content: `# Q3 Market Strategy.md

This document outlines the strategic pivot for our context-aware tools moving into the third quarter. We are seeing a significant trend in RAG-based systems requiring cleaner data input.

### Current Obstacles

- High levels of noise in scraped documentation leading to hallucinations.
- Inconsistent metadata tagging across legacy vault structures.

> "The quality of the context is the ceiling of the model's intelligence." — Internal Engineering Memo

To address this, the **Context Refinery** must implement a more aggressive scrub cycle. We need to remove boilerplate headers, footers, and repetitive legal text that consumes token budget without providing semantic value.`,
    status: 'mature',
    tags: ['STRATEGY', 'Q3'],
  },
  {
    id: 'doc2',
    name: 'AI Project Discovery.txt',
    source: 'Gemini Generated',
    type: 'Text File',
    size: '2.1 MB',
    date: '1 hour ago',
    content: 'Discovery notes for the AI project...',
    status: 'scratchpad',
    tags: ['AI', 'DISCOVERY'],
  },
  {
    id: 'doc3',
    name: 'Product Roadmap 2025',
    source: 'Obsidian Work',
    type: 'Markdown',
    size: '45.8 MB',
    date: 'Yesterday',
    content: 'Roadmap for 2025...',
    status: 'mature',
    tags: ['ROADMAP'],
  },
];

export const MOCK_OUTPUT_FILES: OutputFile[] = [
  {
    id: 'out1',
    name: 'Consolidated_Context.json',
    type: 'Structured data graph',
    size: '24.8 MB',
    description: 'UTF-8 Encoding',
  },
  {
    id: 'out2',
    name: 'Refined_Insights.pdf',
    type: 'Executive summary',
    size: '4.2 MB',
    description: '12 Pages',
  },
  {
    id: 'out3',
    name: 'RAG_Breadcrumb_Package.zip',
    type: 'Hierarchical MD',
    size: '128.5 MB',
    description: '4,200 Files',
  },
];
