
export default function Ingredients({listOfIngredients, setListOfIngredients}){
    const arrayOfIngredients = Object.keys(listOfIngredients);

    const checkBoxes = arrayOfIngredients.map((value, index)=>{
        return (
            <div key={index} className="checkBoxDiv"><p>{value}</p></div>  
        )
    })

    return(
        <div>
            <hr id="hr1"/>
                    <div id="checkBoxWrap">
           {checkBoxes}
        </div>
        </div>

    )
}