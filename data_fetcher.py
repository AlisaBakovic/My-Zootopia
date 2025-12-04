import requests

url = "https://api.api-ninjas.com/v1/animals"
api_key = "O3DXXGR57uYbbGGjyVAjDg==NKO7AlaM1Z0zr6wM"

def fetch_data(animal_name):

    headers = {"X-Api-Key": api_key}
    params = {"name": animal_name}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return []