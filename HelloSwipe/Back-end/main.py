import os
import json
import requests
import random
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
@app.route("/")
# def hello():
#     return "Hello, world"
@app.route('/recipes', methods=['GET'])
def get_data_2():
    with open(r'D:\Codes\hellofresh\HackaTum\HelloSwipe\Front-end\src\recipes.json') as file:
        json_data_1 = json.load(file)
    return json_data_1

@app.route('/carousel', methods=['GET'])
def get_data_1():
    with open('D:\Codes\hellofresh\HackaTum\HelloSwipe\Front-end\src\carousel.json', 'r') as file:
        json_data = json.load(file)
    # Return the JSON data as a response
    return json_data



@app.route('/ingredients_on_recipes', methods=['POST'])
def post_example():
    if request.method == 'POST':
        data = request.json  # Assuming the data is sent as JSON in the request
        app.ingredients_on_recipes = data
        # Process the received data
        # For example, let's echo back the received data
        return jsonify(data)
    else:
        return jsonify({'message': 'This endpoint only accepts POST requests'})
    
@app.route('/ingredients_recipes', methods=['GET'])
def get_ingredients():
    if hasattr(app, 'ingredients_on_recipes'):
      ingredients_on_recipes = app.ingredients_on_recipes  # Retrieve stored recent data
      return jsonify(ingredients_on_recipes)
    else:
        return jsonify({'message': 'No recent data'})

if __name__ == '__main__':
    app.run(debug=True, port = 5000)

def main():{} 