import os
import json
import requests

api_url = "https://someGiorgiLink"

def main():

    
    response = requests.get(api_url)
    response.json()
