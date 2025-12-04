import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    response = requests.get(URL, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return []