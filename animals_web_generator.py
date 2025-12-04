import json
import requests

with open("animals_template.html", "r") as f:
    template = f.read()

animal_name = input("Enter a name of an animal: ")

url = "https://api.api-ninjas.com/v1/animals"
api_key= "O3DXXGR57uYbbGGjyVAjDg==NKO7AlaM1Z0zr6wM"
headers = {
    "X-Api-Key": api_key
}
params = {
    "name": animal_name
}

response = requests.get(url, headers=headers, params=params)

print("Status code:", response.status_code)

if response.status_code == 200:
    animal_list = response.json()
else:
    animal_list = []


output = ""

def serialize_animal(animal):
    name = animal["name"]
    diet = animal["characteristics"].get("diet")
    location = animal["locations"][0] if animal["locations"] else None
    type_animal = animal["characteristics"].get("type")

    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'
    if diet:
        output += f'      <strong>Diet:</strong> {diet}<br/>\n'
    if location:
        output += f'      <strong>Location:</strong> {location}<br/>\n'
    if type_animal:
        output += f'      <strong>Type:</strong> {type_animal}<br/>\n'
    output += '  </p>\n'
    output += '</li>\n\n'
    return output

if animal_list:
    for animal in animal_list:
        output += serialize_animal(animal)
else:
    output = f'<h2>The animal "{animal_name}" does not exist.</h2>'

new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as f:
    f.write(new_html)
