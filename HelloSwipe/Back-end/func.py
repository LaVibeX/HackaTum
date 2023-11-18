import os
import json
import requests
import random

preffered_url = "https://someGiorgiLink"
ingridients_url = "https://someGiorgiLink"
recipes_url = "\\wsl.localhost\Ubuntu\home\alpico\HackaTum\HelloSwipe\Front-end\src\recipes.json"
user_url = "../Front-end/src/user.json"



def get_json_to_dict(request_url):
    #r= requests.get(request_url)
    # Opening JSON file
    with open(request_url) as json_file:
        r_dict = json.load(json_file)
    return r_dict

def main():

    #preffered_styles = get_json_to_dict(preffered_url)
    #ingridients = get_json_to_dict(ingridients)
    recipes = get_json_to_dict(recipes)
    preffered_styles = ["Mediterranean", "Chinese", "Indian"]

    user_choice = []
    for preffered_style in preffered_styles:
        user_choice.append([dish for dish in recipes if dish["style"] == preffered_style])
                
    print(user_choice)
    

