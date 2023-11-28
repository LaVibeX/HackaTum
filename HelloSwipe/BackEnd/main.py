import os
import json
import requests
import random
from flask import Flask, request, jsonify
from flask_cors import CORS
from func import *

preffered_styles = None
user_ingredients = None

app = Flask(__name__)
CORS(app)
@app.route("/")
# def hello():
#     return "Hello, world"
@app.route('/recipes', methods=['GET'])
def get_recipes():
    with open(r'..\Front-end\src\recipes.json') as file:
        recipes = json.load(file)
    return recipes

@app.route('/carousel', methods=['GET'])
def get_carousel():
    with open(r'..\Front-end\src\carousel.json', 'r') as file:
        json_data = json.load(file)
    # Return the JSON data as a response
    return json_data

@app.route('/preffered_styles', methods=['POST'])
def post_styles():
    if request.method == 'POST':
        data = request.json  # Assuming the data is sent as JSON in the request
        app.preffered_styles = data
        # Process the received data
        app.preffered_styles = ", ".join(key for key, value in app.preffered_styles.items() if value)
        print(app.preffered_styles)
        app.user_choice = get_cuisines(app.preffered_styles, get_recipes())
        return jsonify({'data': ingredients_on_cuisines(app.user_choice)})
    else:
        return jsonify({'message': 'This endpoint only accepts POST requests'})

@app.route('/selected_ingredients', methods=['POST'])
def get_final_recipes():
    if request.method == 'POST':
        exclusions = ["peanuts"]
        user_ingredients = request.json 
        dic_user_ingredients = ", ".join(key for key, value in user_ingredients.items() if value)
        list_user_ingredients = dic_user_ingredients.split(',')
        list_without_spaces = [string.replace(" ", "") for string in list_user_ingredients]
        print(list_without_spaces)
        return ({'data': common_ingredients(app.user_choice, list_without_spaces ,exclusions)})
    else:
        return jsonify({'message': 'This endpoint only accepts POST requests'})

def print_received_data():
    global preffered_styles
    print(preffered_styles)


def main():
    print_received_data()


if __name__ == '__main__':
    app.run(port=500)
    main()