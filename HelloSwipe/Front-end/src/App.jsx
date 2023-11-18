import { useState } from 'react'
import './App.css'
import Navbar from './Navbar'
import DemoCarousel from './Carousel'

function App() {
  function fetchFunc(){
    fetch("https://localhost:5000")
      .then((response) => console.log(response))
  }
  
  return (
      <div id="rootDiv">
        <Navbar/>
        <div id="body">
        <DemoCarousel/>
        <button onClick={fetchFunc}>
          
        </button>
        </div>        
      </div>
  )
}

export default App
