import React, { createContext, useContext, useState, useEffect } from 'react';

interface DocumentContextType {
  importedDocs: any[];
  setImportedDocs: React.Dispatch<React.SetStateAction<any[]>>;
  userEmail: string;
  setUserEmail: React.Dispatch<React.SetStateAction<string>>;
  emailSaved: boolean;
  setEmailSaved: React.Dispatch<React.SetStateAction<boolean>>;
  handleSaveSession: () => void;
  handleClearSession: () => void;
}

const DocumentContext = createContext<DocumentContextType | undefined>(undefined);

export function DocumentProvider({ children }: { children: React.ReactNode }) {
  const [importedDocs, setImportedDocs] = useState<any[]>([]);
  const [userEmail, setUserEmail] = useState<string>('');
  const [emailSaved, setEmailSaved] = useState(false);

  useEffect(() => {
    const savedEmail = localStorage.getItem('cr_session_email');
    if (savedEmail) {
      setUserEmail(savedEmail);
      setEmailSaved(true);
      const savedDocs = localStorage.getItem('cr_docs_' + savedEmail);
      if (savedDocs) {
        try {
          setImportedDocs(JSON.parse(savedDocs));
        } catch (e) {
          console.error("Failed to parse saved docs", e);
        }
      }
    }
  }, []);

  useEffect(() => {
    if (emailSaved && userEmail) {
      localStorage.setItem('cr_docs_' + userEmail, JSON.stringify(importedDocs));
    }
  }, [importedDocs, userEmail, emailSaved]);

  const handleSaveSession = () => {
    if (userEmail.trim()) {
      localStorage.setItem('cr_session_email', userEmail.trim());
      setEmailSaved(true);
    }
  };

  const handleClearSession = () => {
    localStorage.removeItem('cr_session_email');
    setUserEmail('');
    setEmailSaved(false);
    setImportedDocs([]);
  };

  return (
    <DocumentContext.Provider
      value={{
        importedDocs,
        setImportedDocs,
        userEmail,
        setUserEmail,
        emailSaved,
        setEmailSaved,
        handleSaveSession,
        handleClearSession,
      }}
    >
      {children}
    </DocumentContext.Provider>
  );
}

export function useDocuments() {
  const context = useContext(DocumentContext);
  if (context === undefined) {
    throw new Error('useDocuments must be used within a DocumentProvider');
  }
  return context;
}
