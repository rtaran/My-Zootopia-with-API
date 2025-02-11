import requests


# API Configuration
API_KEY = "9raNurS5dRLg5zIB0+/CjQ==YE2HPWQfCLiICTvg"  # API key
BASE_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_animal_data(animal_name):
    """Fetch animal data from the API."""
    if not API_KEY:
        print("❌ Error: API Key is missing. Set it using an environment variable.")
        return None

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if data:
            return data  # Return the entire list of results
        else:
            print(f"No results found for '{animal_name}'.")
            return None
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


# Step 1: Ask the user for an animal name
animal_name = input("Enter a name of an animal: ").strip()

# Step 2: Fetch data from the API
animals = fetch_animal_data(animal_name)

# Step 3: Read the existing HTML template
if animals:
    with open("animals_template.html", "r") as file:
        html_template = file.read()

    # Generate HTML for all returned animals
    animals_html = ""
    for animal in animals:
        animal_block = f"""
        <div class="animal-card">
            <h2>{animal['name']}</h2>
            <h3>Scientific Name: {animal['taxonomy'].get('scientific_name', 'Unknown')}</h3>
            <p><strong>Category:</strong> {animal['taxonomy'].get('kingdom', 'Unknown')} → {animal['taxonomy'].get('family', 'Unknown')}</p>
            <p><strong>Location:</strong> {', '.join(animal.get('locations', []))}</p>
            <p><strong>Diet:</strong> {animal['characteristics'].get('diet', 'Unknown')}</p>
            <p><strong>Habitat:</strong> {animal['characteristics'].get('habitat', 'Unknown')}</p>
        </div>
        """
        animals_html += animal_block

    # Replace the placeholder in the template with the generated animal data
    html_output = html_template.replace("{{ animals_content }}", animals_html)

    # Write the final HTML output to a file
    with open("animals.html", "w") as file:
        file.write(html_output)

    print("✅ Website was successfully generated to the file animals.html.")
else:
    print("⚠️ No data available for the entered animal.")