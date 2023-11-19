import Dishbox from "./Dishbox";

export default function Final({allDishes}){
    console.log(allDishes);
let cardBoxes = allDishes.map((value,index)=>{
    return <Dishbox key={index} img={value[1]['image']} name={value[1]['headline']} recipe={value[1]['ingredients']}/>
})

   
        return (
            <div>
            <hr id="hr2"/>
            <h3>Enjoy a little taste of the world!</h3>
            <div id="cardGrid">
            {cardBoxes}
            </div>

        </div>

        )
    }

