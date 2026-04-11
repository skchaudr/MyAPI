import React from 'react';
import { View } from '../types';
import { 
  LayoutDashboard, 
  BarChart3, 
  Users, 
  Bell, 
  Settings, 
  Upload, 
  Wand2, 
  FileOutput, 
  Plus, 
  BookOpen, 
  HelpCircle 
} from 'lucide-react';
import { cn } from '@/lib/utils';
import { Button } from './ui/button';

interface LayoutProps {
  children: React.ReactNode;
  currentView: View;
  onViewChange: (view: View) => void;
}

export default function Layout({ children, currentView, onViewChange }: LayoutProps) {
  return (
    <div className="min-h-screen bg-surface">
      {/* Top Navigation */}
      <header className="fixed top-0 w-full z-50 glass-nav shadow-sm shadow-on-surface/5">
        <div className="flex justify-between items-center px-8 h-16 w-full">
          <div className="flex items-center gap-4">
            <div className="text-xl font-bold tracking-tighter text-primary font-headline">Context Refinery</div>
            <nav className="hidden md:flex items-center gap-8 ml-8">
              <a className="text-sm font-medium text-slate-500 hover:text-primary transition-all cursor-pointer">Dashboard</a>
              <a className="text-sm font-medium text-slate-500 hover:text-primary transition-all cursor-pointer">Analytics</a>
              <a className="text-sm font-medium text-slate-500 hover:text-primary transition-all cursor-pointer">Team</a>
            </nav>
          </div>
          <div className="flex items-center gap-4">
            <Button variant="ghost" size="icon" className="rounded-full text-slate-500">
              <Bell className="w-5 h-5" />
            </Button>
            <Button variant="ghost" size="icon" className="rounded-full text-slate-500">
              <Settings className="w-5 h-5" />
            </Button>
            <div className="w-8 h-8 rounded-full bg-surface-container-high overflow-hidden border border-outline-variant/20">
              <img 
                src="https://picsum.photos/seed/user/100/100" 
                alt="User Profile" 
                className="w-full h-full object-cover"
                referrerPolicy="no-referrer"
              />
            </div>
          </div>
        </div>
      </header>

      {/* Sidebar */}
      <aside className="h-screen w-64 fixed left-0 top-0 bg-surface-container-low flex flex-col p-6 pt-20 gap-4 hidden lg:flex border-r border-outline-variant/10">
        <div className="flex items-center gap-3 mb-6 px-2">
          <div className="w-2 h-2 rounded-full bg-secondary"></div>
          <div>
            <div className="text-sm font-bold text-on-surface">Lab Workspace</div>
            <div className="text-[10px] text-slate-500 uppercase tracking-widest">System: Optimal</div>
          </div>
        </div>

        <nav className="flex flex-col gap-1">
          <button 
            onClick={() => onViewChange('import')}
            className={cn(
              "flex items-center gap-3 p-3 rounded-lg transition-all duration-300 font-medium text-sm",
              currentView === 'import' 
                ? "bg-white text-primary shadow-sm font-bold" 
                : "text-slate-600 hover:bg-surface-container-high"
            )}
          >
            <Upload className={cn("w-5 h-5", currentView === 'import' && "fill-primary/10")} />
            <span>Import</span>
          </button>
          <button 
            onClick={() => onViewChange('refine')}
            className={cn(
              "flex items-center gap-3 p-3 rounded-lg transition-all duration-300 font-medium text-sm",
              currentView === 'refine' 
                ? "bg-white text-primary shadow-sm font-bold" 
                : "text-slate-600 hover:bg-surface-container-high"
            )}
          >
            <Wand2 className={cn("w-5 h-5", currentView === 'refine' && "fill-primary/10")} />
            <span>Refine</span>
          </button>
          <button 
            onClick={() => onViewChange('export')}
            className={cn(
              "flex items-center gap-3 p-3 rounded-lg transition-all duration-300 font-medium text-sm",
              currentView === 'export' 
                ? "bg-white text-primary shadow-sm font-bold" 
                : "text-slate-600 hover:bg-surface-container-high"
            )}
          >
            <FileOutput className={cn("w-5 h-5", currentView === 'export' && "fill-primary/10")} />
            <span>Export</span>
          </button>
        </nav>

        <Button className="mt-4 w-full py-6 bg-gradient-to-br from-primary to-primary-container text-white rounded-xl font-bold flex items-center justify-center gap-2 shadow-lg shadow-primary/20 hover:scale-[1.02] active:scale-[0.98] transition-all">
          <Plus className="w-4 h-4" />
          New Project
        </Button>

        <div className="mt-auto flex flex-col gap-1 pt-4 border-t border-outline-variant/10">
          <a className="flex items-center gap-3 p-3 text-slate-600 hover:bg-surface-container-high rounded-lg transition-all text-sm cursor-pointer">
            <BookOpen className="w-4 h-4" />
            <span>Documentation</span>
          </a>
          <a className="flex items-center gap-3 p-3 text-slate-600 hover:bg-surface-container-high rounded-lg transition-all text-sm cursor-pointer">
            <HelpCircle className="w-4 h-4" />
            <span>Support</span>
          </a>
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="lg:ml-64 pt-16 min-h-screen">
        {children}
      </main>
    </div>
  );
}
