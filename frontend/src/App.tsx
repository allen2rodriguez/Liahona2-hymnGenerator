import SpaceBetween from "@cloudscape-design/components/space-between";
import HistoryTable from './components/table.tsx'
import Hymns from './components/new_hymns.tsx'
import './App.css'

import "@cloudscape-design/global-styles/index.css";
import { applyMode } from "@cloudscape-design/global-styles";

// Set dark mode at runtime
applyMode('dark'); // or 'light'

function App() {
  return (
    <>
      <h1 className="title">Liahona II Hymn Dashboard</h1>
      <p>Arden if you're reading this I hope you're having a good day</p>
      <SpaceBetween size="l" direction="vertical">
        <Hymns />
        <div style={{ overflowX: 'auto' }}>
          <HistoryTable />
        </div>
      </SpaceBetween>
    </>
  )
}

export default App
