import os
import json
import requests
import random

preffered_url = "https://someGiorgiLink"
ingredients_url = "https://someGiorgiLink"
recipes_url = "../Front-end/src/recipes.json"
user_url = "../Front-end/src/user.json"



def get_json_to_dict(request_url):
    #r= requests.get(request_url)
    # Opening JSON file
    with open(request_url) as json_file:
        r_dict = json.load(json_file)
    return r_dict

def send_post(json_value, url):
    x = requests.post(url, json = json_value)

def list_to_json(value, url):
    # Convert list to JSON
    json_data = json.dumps(value, indent=2)  
    return json_data

def check_any_ingredient(choice_dict, word):
    #boolean_list = []
    list_recipes = []
    for recipe in choice_dict:
        for ingredient in recipe["recipe"]["ingredients"]:
            #boolean_list.append([recipe["recipe"]["name"], ingredient == word])
            if ingredient == word:
                list_recipes.append(recipe["recipe"]["name"])
    return list_recipes#any(boolean_list)

def mock_erase_before_deploy(choice_dict, word_list):
    boolean_list = []
    not_in_list= []
    for word in word_list:
        is_ingredient = check_any_ingredient(choice_dict, word)
        boolean_list.append(is_ingredient)
        if not is_ingredient:
            not_in_list.append(word)
    print(not_in_list)
    return all(boolean_list)

def filter_from_ingredient_list(choice_dict, word_list):
    recipe_list = []
    final_recipe_list = []
    for word in word_list:
        recipe_list.append(check_any_ingredient(choice_dict, word))
    
    for recipe in recipe_list:
        final_recipe_list.append(random.choice(recipe))
    return final_recipe_list#all(boolean_list)

def ingredients_on_cuisines(style_dict):
    ingredients_set = set()
    for recipe in style_dict:
        for ingredient in recipe["recipe"]["ingredients"]:
            ingredients_set.add(ingredient)
    # Convert set to list (optional, for better readability)
    ingredients_list = list(ingredients_set)
    return ingredients_list

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
    preffered_styles = ["Mediterranean", "Chinese", "Indian"]

    user_choice = get_cuisines(preffered_styles, recipes)

    #send_post(list_to_json(ingredients_on_cuisines(user_choice)))


    print(filter_from_ingredient_list(user_choice, ingredients))
   
 

if __name__ == '__main__':
    main()