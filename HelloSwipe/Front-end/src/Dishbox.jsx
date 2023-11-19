
export default function Dishbox({name, img, recipe}){
    let total = ''
    recipe.map((value, index)=>{
        if(recipe.length!=(index+1)){
            total += `${value}, `
        }
        else{
            total += value;
        }
        return total
        
    })

    return(
        <div className="boxDish">
            <img src={img}/>
            <h3 className="dishTitleName">{name}</h3>
            <hr/>
            <h2 id="ingredientTitle">Ingredients</h2>
            <p id="ingredientList">{total}</p>
        </div>
    )
}