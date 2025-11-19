import json

with open("animals_template.html", "r") as f:
    template = f.read()


def load_data(file_path):


    with open(file_path, "r") as handle:
        return json.load(handle)

animal_list = load_data('animals_data.json')

output = ""

for animal in animal_list:
    name = animal["name"]
    diet = animal["characteristics"].get("diet")
    location = animal["locations"][0]  if animal["locations"] else None
    type_animal = animal["characteristics"].get("type")

    output += f"Name: {name}\n"

    if diet:
        output += f"Diet: {diet}\n"
    if location:
        output += f"Location: {location}\n"
    if type_animal:
        output += f"Type: {type_animal}\n"


    output += "\n"


new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as f:
    f.write(new_html)

