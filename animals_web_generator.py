import json

with open("animals_template.html", "r") as f:
    template = f.read()


def load_data(file_path):

    with open(file_path, "r") as handle:
        return json.load(handle)


animal_list = load_data("animals_data.json")

output = ""

for animal in animal_list:
    name = animal["name"]
    diet = animal["characteristics"].get("diet")
    location = animal["locations"][0] if animal["locations"] else None
    type_animal = animal["characteristics"].get("type")

    output += '<li class="cards__item">'

    output += f' <div class="card__title">{name}</div>\n'
    output += ' <p class="card__text">\n'

    if diet:
        output += f" <strong>Diet:</strong> {diet}<br/>\n"
    if location:
        output += f" <strong>Location:</strong> {location}<br/>\n"
    if type_animal:
        output += f" <strong>Type:</strong> {type_animal}<br/>\n"

    output += "</p>\n"
    output += "</li>\n\n"


new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as f:
    f.write(new_html)
