import json
import requests

preffered_url = "https://someGiorgiLink"
ingredients_url = "https://someGiorgiLink"
recipes_url = "http://localhost:5000/recipes"
user_url = "../Front-end/src/user.json"

def get_json_to_dict(request_url):
    r= requests.get(request_url)
    return r.json()

def send_post(json_value, url):
    x = requests.post(url, json = json_value)

def ingredients_on_cuisines(style_dict):
    ingredients_set = set()
    for recipe in style_dict:
        ingredients_set.update(recipe["recipe"]["ingredients"])
    return list(ingredients_set)

def common_ingredients(recipes, user_ingredients, exclusions):
    list_recipe = []
    for recipe in recipes:
        counter = sum(1 for ingredient in user_ingredients if ingredient in recipe["recipe"]["ingredients"])
        if all(exclusion not in recipe["recipe"]["ingredients"] for exclusion in exclusions):
            list_recipe.append([counter, recipe["recipe"]])

    list_recipe.sort(key=lambda x: x[0], reverse=True)
    return list_recipe

def list_to_json(value):
    # Convert list to JSON
    json_data = json.dumps(value, indent=None) 
    json_data = json_data.replace("\\", "")
    return json_data

def get_cuisines(preferred_styles, recipes):
    return [recipe for recipe in recipes if recipe["recipe"]["style"] in preferred_styles]
    
def main():
    #preffered_styles = get_json_to_dict(preffered_url)
    """ingredients = ['pork', 'tomato', 'avocado'] #get_json_to_dict(ingredients_url)
    recipes = get_json_to_dict(recipes_url)
    preffered_styles = ["Mexican", "Chinese", "Indian"]
    exclusions = ["pineapple"]
    user_choice = get_cuisines(preffered_styles, recipes)
    send_post(list_to_json(ingredients_on_cuisines(user_choice)),'http://localhost:5000/ingredients_on_recipes')
    print(common_ingredients(user_choice, ingredients,exclusions))"""
    r = requests.get('http://localhost:5000/ingredients_recipes')
    print(r.json())

if __name__ == '__main__':
    main()