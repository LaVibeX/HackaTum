import { useEffect, useState} from 'react'
import { v4 as uuidv4 } from 'uuid';
import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';
import 'swiper/css/effect-cards';
import { EffectCards } from 'swiper/modules';
import heart from "./assets/heart.png"
import Button from "react-bootstrap/Button"
import Chinese from "./assets/chinese.png"
import Georgian from "./assets/georgian.png"
import Italian from "./assets/italian.png"
import Indian from "./assets/indian.png"
import Japanese from "./assets/japanese.png"
import Mexican from "./assets/mexican.png"
import Spanish from "./assets/spanish.png"
import Thai from "./assets/thai.png"
import Greek from "./assets/greek.png"


export default function Carousel({cuisinesArray, selectedDishes, setSelectedDishes}) {

const imageSrc = {
    'Chinese' : Chinese,
    'Georgian' : Georgian,
    'Italian': Italian,
    'Indian': Indian,
    'Japanese': Japanese,
    'Mexican': Mexican,
    'Spanish': Spanish,
    'Thai': Thai,
    'Greek':Greek

}

console.log(cuisinesArray);

const preSlides = cuisinesArray.map((value,index)=>{
    return(
            <SwiperSlide key={index} className="slideAll" id={`currentSlide${index}`} onDoubleClick={() => {
            setSelectedDishes((prevObj)=>{
                let newObj = {...prevObj};
                newObj[value['name']] = !newObj[value['name']];
                console.log(newObj);
                return newObj
            })
            // console.log(`clicked${index}`);
         }}><img className = "slideImg" src={imageSrc[value['name']]}/>
         
         <div className={`heartOverlay${selectedDishes[value['name']]?' show':''}`} id={`heart${index}`}>
          <img src={heart} alt="heart" />
        </div>

        <div className='cuisineNames' id={`name${index}`}>
         <p>{value['name']}</p>
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
