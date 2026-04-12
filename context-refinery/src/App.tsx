/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState } from 'react';
import { View } from './types';
import Layout from './components/Layout';
import ImportView from './components/ImportView';
import RefineView from './components/RefineView';
import ExportView from './components/ExportView';
import { TooltipProvider } from './components/ui/tooltip';
import { DocumentProvider } from './contexts/DocumentContext';

export default function App() {
  const [currentView, setCurrentView] = useState<View>('import');

  return (
    <TooltipProvider>
      <DocumentProvider>
        <Layout currentView={currentView} onViewChange={setCurrentView}>
          {currentView === 'import' && <ImportView />}
          {currentView === 'refine' && <RefineView />}
          {currentView === 'export' && <ExportView />}
        </Layout>
      </DocumentProvider>
    </TooltipProvider>
  );
}

