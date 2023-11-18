import { useEffect, useState} from 'react'
import { v4 as uuidv4 } from 'uuid';
import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';
import 'swiper/css/effect-cards';
import { EffectCards } from 'swiper/modules';
import heart from "./assets/heart.png"
import Button from "react-bootstrap/Button"


export default function Carousel({imgArray, length, currentSlide, setCurrentSlide}) {
const [selectedDishes, setSelectedDishes] = useState(new Array(7).fill(0));



console.log(selectedDishes);

const preSlides = imgArray.map((value,index)=>{
    return(
            <SwiperSlide key={index} className="slideAll" id={`currentSlide${index}`} onDoubleClick={() => {
            setSelectedDishes((prevArray)=>{
                let newArray = [...prevArray];
                console.log(newArray);
                newArray[index] = !newArray[index];
                return newArray
            })
            // console.log(`clicked${index}`);
         }}><img className = "slideImg" src={imgArray[index]}/>
         
         <div className={`heartOverlay${selectedDishes[index]?' show':''}`} id={`heart${index}`}>
          <img src={heart} alt="heart" />
        </div>

        <div className='cuisineNames' id={`name${index}`}>
         <p>Georgia</p>
        </div>
         </SwiperSlide>
    )
})

  return (
    <div id="carouselComponent">
        <h1 id="componentTitle">Choose your favorite cuisines!</h1>
      <Swiper
        effect={'cards'}
        grabCursor={true}
        modules={[EffectCards]}
        className="mySwiper"
      >
        {preSlides}
        {/* <div id="heart1">
            <img  src={heart}/> </div> */}
      </Swiper>
      
    </div>
  );
}
