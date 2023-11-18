import os
import json
import requests
import random

preffered_url = "https://someGiorgiLink"
ingredients_url = "https://someGiorgiLink"
recipes_url = "http://localhost:5000/recipes"
user_url = "../Front-end/src/user.json"



def get_json_to_dict(request_url):
    r= requests.get(request_url)
    return r.json()


def send_post(json_value, url):
    x = requests.post(url, json = json_value)

def list_to_json(value):
    # Convert list to JSON
    json_data = json.dumps(value, indent=None) 
    json_data = json_data.replace("\\", "")
    return json_data

def common_ingredients(recipes, user_ingredients,exclusions):
    list_recipe = []
    for recipe in recipes:
        counter = 0
        for user_ingredient in user_ingredients:
            if user_ingredient in recipe["recipe"]["ingredients"]:
                counter += 1
        for exclusion in exclusions:
            if(exclusion not in recipe["recipe"]["ingredients"]):
                list_recipe.append([counter,recipe["recipe"]["name"]])
        list_recipe = sorted(list_recipe, key=lambda x: x[0],reverse=True)

    return list_recipe
            



def ingredients_on_cuisines(style_dict):
    ingredients_set = set()
    for recipe in style_dict:
        for ingredient in recipe["recipe"]["ingredients"]:
            ingredients_set.add(ingredient)
    # Convert set to list (optional, for better readability)
    ingredient_list = list(ingredients_set)
    return ingredient_list

def get_cuisines(preffered_styles, recipes):
    user_choice = []
    for preffered_style in preffered_styles:
        for recipe in recipes:
            if recipe["recipe"]["style"] == preffered_style:
                user_choice.append(recipe)
    return user_choice

def main():

    #preffered_styles = get_json_to_dict(preffered_url)
    ingredients = ['pork', 'tomato', 'avocado'] #get_json_to_dict(ingredients_url)
    recipes = get_json_to_dict(recipes_url)
    preffered_styles = ["Mexican", "Chinese", "Indian"]
    exclusions = ["pineapple"]

    user_choice = get_cuisines(preffered_styles, recipes)
    print(list_to_json(ingredients_on_cuisines(user_choice)))


    #send_post(list_to_json(ingredients_on_cuisines(user_choice)),'http://localhost:5000/ingredients_on_recipes')


    #print(filter_from_ingredient_list(user_choice, ingredients))
    print(common_ingredients(user_choice, ingredients,exclusions))
 

if __name__ == '__main__':
    main()