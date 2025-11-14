import json

def load_data(file_path):


    with open(file_path, "r") as handle:
        return json.load(handle)

animal_list = load_data('animals_data.json')

for animal in animal_list:
    name = animal["name"]
    diet = animal["characteristics"].get("diet")
    location = animal["locations"][0]  if animal["locations"] else None
    type_animal = animal["characteristics"].get("type")

    print(f"Name: {name}")

    if diet:
        print(f"Diet: {diet}")
    if location:
        print(f"Location: {location}")
    if type_animal:
        print(f"Type: {type_animal}")


    print()


