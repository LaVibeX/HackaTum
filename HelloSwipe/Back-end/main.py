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

@app.route('/get_data', methods=['GET'])
def get_data():
    # Logic to read data from the JSON file
    with open('D:\Codes\hellofresh\HackaTum\HelloSwipe\Front-end\src\carousel.json', 'r') as file:
        json_data = json.load(file)

    # Return the JSON data as a response
    return json_data

@app.route('/post-example', methods=['POST'])
def post_example():
    if request.method == 'POST':
        data = request.json  # Assuming the data is sent as JSON in the request
        # Process the received data
        # For example, let's echo back the received data
        return jsonify(data)
    else:
        return jsonify({'message': 'This endpoint only accepts POST requests'})

if __name__ == '__main__':
    app.run(debug=True, port = 5000)

def main():{} 