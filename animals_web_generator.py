import data_fetcher

def serialize_animal(animal):
    """Convert a single animal dictionary into HTML list item"""
    name = animal.get("name", "Unknown")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet", "Unknown")
    animal_type = characteristics.get("type", "Unknown")
    locations = animal.get("locations", [])
    location = locations[0] if locations else "Unknown"

    return (
        '<li class="cards__item">\n'
        f'  <div class="card__title">{name}</div>\n'
        '  <p class="card__text">\n'
        f'      <strong>Diet:</strong> {diet}<br/>\n'
        f'      <strong>Location:</strong> {location}<br/>\n'
        f'      <strong>Type:</strong> {animal_type}<br/>\n'
        '  </p>\n'
        '</li>\n'
    )


def build_html(animals_data, template_path, output_path, query=None):
    """Generate HTML file with animal data or error message"""
    if animals_data and len(animals_data) > 0:
        output = ''.join(serialize_animal(animal) for animal in animals_data)
    else:
        output = f'<h2>The animal "{query}" doesn\'t exist.</h2>'

    with open(template_path, "r") as file:
        html_template = file.read()

    html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open(output_path, "w") as file:
        file.write(html_content)


def main():
    animal_name = input("Please enter an animal: ")
    animals_data = data_fetcher.fetch_data(animal_name)
    build_html(animals_data, "animals_template.html", "animals.html", query=animal_name)
    print("animals.html generated successfully")


if __name__ == "__main__":
    main()
