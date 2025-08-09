import SpaceBetween from "@cloudscape-design/components/space-between";
import HistoryTable from './components/table.tsx'
import Hymns from './components/new_hymns.tsx'
import './App.css'

import { Analytics } from '@vercel/analytics/react';
import "@cloudscape-design/global-styles/index.css";
import { applyMode, Mode } from '@cloudscape-design/global-styles';


// Set dark mode at runtime
applyMode('dark' as Mode); // or 'light'

function App() {
  return (
    <>
      <h1 className="title">Liahona II Hymn Dashboard</h1>
      <SpaceBetween size="l" direction="vertical">
        <Hymns />
        <div style={{ overflowX: 'auto' }}>
          <HistoryTable />
        </div>
      </SpaceBetween>
      <Analytics />
    </>
  )
}

export default App
