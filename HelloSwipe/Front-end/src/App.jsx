import { useState, useEffect } from 'react'
import './App.css'
import Navbar from './Navbar'
import Carousel from './Carousel'
import Button from 'react-bootstrap/Button';


function App() {
  const [isLoading, setLoading] = useState(false);
  const [cuisines,setCuisines] = useState(new Array(9).fill(0));
  const [selectedDishes, setSelectedDishes] = useState({
    'Chinese' : 0,
    'Georgian' : 0,
    'Italian': 0,
    'Indian': 0,
    'Japanese': 0,
    'Mexican': 0,
    'Spanish': 0,
    'Thai': 0,
    'Greek':0
  });
console.log(selectedDishes)
  console.log(cuisines);

  useEffect(()=>{
    const fetchData = async ()=>{
      await fetch("http://localhost:5000/carousel")
      .then((response) => {
        if(response.ok){
          return response.json()
        }
        else{
          throw new Error(`Error: ${response.status} ${response.statusText}`);
        }}).then((data)=>{
          console.log(data);
          // console.log(selectedDishes);
          setCuisines(()=>[...data['cuisines']]);
          return
        })
        .catch((e) => {
          console.log (`Error: ${e.message}`);
          setLoading(false);
        })
    }
    fetchData();
  },[]);

  function handleClick(){
    setLoading(true);
    const sendData = async()=> {
      await fetch("http://localhost:5000/preffered_styles", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(selectedDishes),
      })
      .then((response) => {
        if(response.ok){
          console.log("success");
          return
        }
        else{
          throw new Error(`Error: ${response.status} ${response.statusText}`);
        }}).then((data)=>{
          console.log(data);
          setLoading(false);

          return
        })
        .catch((e) => {
          console.log (`Error: ${e.message}`);
          setLoading(false);
        })
    }
    sendData();
    }
  
  return (
      <div id="rootDiv">
        <Navbar/>
        <div id="body">
        {/* <DemoCarousel/> */}
        {(cuisines[0]!=0)?
        <Carousel cuisinesArray={cuisines} selectedDishes={selectedDishes} setSelectedDishes={setSelectedDishes} />:''}
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
