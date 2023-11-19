
import Button from "react-bootstrap/Button";

export default function Ingredients({listOfIngredients, setListOfIngredients, sendIngredients, Loading, setLoading}){
    const arrayOfIngredients = Object.keys(listOfIngredients);
    // console.log(listOfIngredients   );
    const checkBoxes = arrayOfIngredients.map((value, index)=>{
        return (
            <div key={index} onClick={()=>{setListOfIngredients((oldObj)=>{
                let newObj = {};
                newObj = {...oldObj};
                newObj[value] = !newObj[value];
                return newObj
            })}} 
            className={`checkBoxDiv${listOfIngredients[value]?' ticked':''}`}>
                <p className={value.length>10?'mini':''}>{value.charAt(0).toUpperCase() + value.slice(1)}</p>
                </div>  
        )
    })

    return(
        <div>
            <hr id="hr1"/>
            <h2>Which ingredients do you prefer?</h2>
                    <div id="checkBoxWrap">
                        
           {checkBoxes}
        </div>
        <Button
          id="btn2"
          className = "nextBtn"
          variant="primary"
          disabled={Loading}
          onClick={!Loading ? sendIngredients : null}
        >
          {Loading ? "Loading…" : "Cook!"}
        </Button>
        </div>

    )
}