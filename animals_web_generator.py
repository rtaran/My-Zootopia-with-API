import os
from data_fetcher import fetch_animal_data


def generate_animal_card(animal):
    """Generate an HTML card for an animal, omitting missing fields."""
    fields = [
        ("Scientific Name", animal.get("taxonomy", {}).get("scientific_name")),
        ("Category", " → ".join([
            animal.get("taxonomy", {}).get("kingdom", ""),
            animal.get("taxonomy", {}).get("family", "")
        ]).strip(" → ")),
        ("Location", ", ".join(animal.get("locations", []))),
        ("Diet", animal.get("characteristics", {}).get("diet")),
        ("Habitat", animal.get("characteristics", {}).get("habitat")),
        ("Type", animal.get("characteristics", {}).get("type")),
        ("Skin Type", animal.get("characteristics", {}).get("skin_type")),
    ]

    # Only keep fields with values
    info = "".join(f'<p><strong>{key}:</strong> {value}</p>' for key, value in fields if value)

    return f'''<div class="animal-card">
        <h2>{animal.get("name", "Unknown")}</h2>
        {info}
    </div>'''


def generate_webpage():
    """Generate the animals.html webpage using API data."""
    animal_name = input("Enter an animal name: ").strip()
    animals = fetch_animal_data(animal_name)

    if not animals:
        print("No animals found.")
        return

    cards = "".join(generate_animal_card(animal) for animal in animals)

    with open("animals_template.html", "r") as template_file:
        template = template_file.read()

    html_content = template.replace("{{ animals_content }}", cards)

    with open("animals.html", "w") as output_file:
        output_file.write(html_content)

    print("✅ animals.html generated successfully!")


if __name__ == "__main__":
    generate_webpage()