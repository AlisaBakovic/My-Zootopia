import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

url = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):

    headers = {"X-Api-Key": api_key}
    params = {"name": animal_name}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return []