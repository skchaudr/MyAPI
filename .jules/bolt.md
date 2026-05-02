## 2024-04-12 - Prevented expensive ReactMarkdown re-renders
**Learning:** Found a specific anti-pattern in `RefineView.tsx` where a `components` object was passed inline to `<ReactMarkdown>`. Since `react-markdown` checks if the `components` prop has changed reference to determine if it should re-render and re-parse the markdown, an inline object causes full re-renders on every keystroke in the metadata inputs (like the title override).
**Action:** Always declare the `components` object outside of the component or use `useMemo` when working with `react-markdown`.
