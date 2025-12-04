import data_fetcher

with open("animals_template.html", "r") as f:
    template = f.read()

animal_name = input("Enter a name of an animal: ")

animal_list = data_fetcher.fetch_data(animal_name)

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

output = ""
if animal_list:
    for animal in animal_list:
        output += serialize_animal(animal)
else:
    output = f'<h2>The animal "{animal_name}" does not exist.</h2>'

new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as f:
    f.write(new_html)

print("Website successfully generated: animals.html")