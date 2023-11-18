import { useState, useEffect } from 'react'
import './App.css'
import Navbar from './Navbar'
import DemoCarousel from './DemoCarousel'
import Carousel from './Carousel'
import Button from 'react-bootstrap/Button';
import logo1 from "./assets/georgian.png"; //import images for now
import logo2 from "./assets/chinese.png";
import logo3 from "./assets/japanese.png";

const imgArray = [logo1,logo2, logo3];

function App() {
  const [currentSlide, setCurrentSlide] = useState(1);
  const [isLoading, setLoading] = useState(false);

  function fetchFunc(){
    fetch("http://localhost:5000")
      .then((response) => response.json().then(data=>console.log(data)))
  }

  function handleClick(){
    setLoading(true);
    fetch("https://localhost:5000")
      .then((response) => {
        if(response.ok){
          console.log(response);
          setLoading(false);
        }
        else{
          throw new Error(`Error: ${response.status} ${response.statusText}`);
        }})
        .catch((e) => {
          console.log (`Error: ${e.message}`);
          setLoading(false);
        })
  }
  
  return (
      <div id="rootDiv">
        <Navbar/>
        <div id="body">
        {/* <DemoCarousel/> */}
        <Carousel imgArray={imgArray} length={imgArray.length} currentSlide={currentSlide} setCurrentSlide={setCurrentSlide}/>
        <Button
        id = "nextBtn"
      variant="primary"
      disabled={isLoading}
      onClick={!isLoading ? handleClick : null}
    >
      {isLoading ? 'Loading…' : 'Next'}
    </Button>

        </div>        
      </div>
  )
}

export default App
