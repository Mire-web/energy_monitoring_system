// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'
import Container from './components/Container'
import Header from './components/Header'
import Sidebar from './components/Sidebar'
// import Subheader from './components/Subheader'
import Dashboard from './pages/Dashboard'
import Cost from './pages/Cost'
// import ApplianceUsage from './pages/ApplianceUsage'
import UsageByRoom from './pages/UsageByRoom'
// import Emissions from './pages/Emissions'

import { Route, Routes } from 'react-router-dom'

function App() {

  return (
    <Container>
      <Sidebar />
      <main className='main-content'>
        <Header />
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/cost" element={<Cost />} />
          {/* <Route path="/appliances" element={<ApplianceUsage />} /> */}
          <Route path="/usage-by-rooms" element={<UsageByRoom />} />
          {/* 
           />
          <Route path="/emissions" element={<Emissions />} /> */}
        </Routes>
      </main>
    </Container>
  )
}

export default App
