export type View = 'import' | 'refine' | 'export';

export interface Source {
  id: string;
  name: string;
  type: string;
  confidence: 'high' | 'medium' | 'low';
  icon: string;
}

export interface Document {
  id: string;
  name: string;
  source: string;
  type: string;
  size: string;
  date: string;
  content: string;
  status: 'mature' | 'scratchpad' | 'deprecated';
  tags: string[];
  summary?: string;
}

export interface OutputFile {
  id: string;
  name: string;
  type: string;
  size: string;
  description: string;
}
