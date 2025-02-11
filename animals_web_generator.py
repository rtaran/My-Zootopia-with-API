import data_fetcher  # Import our data fetching module

# Step 1: Ask the user for an animal name
animal_name = input("Please enter an animal: ").strip()

# Step 2: Fetch data using the API
animals = data_fetcher.fetch_data(animal_name)

# Step 3: Read the existing HTML template
with open("animals_template.html", "r") as file:
    html_template = file.read()

# Step 4: Handle missing animals gracefully
if animals and len(animals) > 0:
    animals_html = ""
    for animal in animals:
        image_url = animal.get("image_url", "https://via.placeholder.com/300")  # Use placeholder if no image
        animal_block = f"""
        <div class="animal-card">
            <img src="{image_url}" alt="{animal['name']}" style="width:100%; border-radius: 10px;">
            <h2>{animal['name']}</h2>
            <h3>Scientific Name: {animal['taxonomy'].get('scientific_name', 'Unknown')}</h3>
            <p><strong>Category:</strong> {animal['taxonomy'].get('kingdom', 'Unknown')} → {animal['taxonomy'].get('family', 'Unknown')}</p>
            <p><strong>Location:</strong> {', '.join(animal.get('locations', []))}</p>
            <p><strong>Diet:</strong> {animal['characteristics'].get('diet', 'Unknown')}</p>
            <p><strong>Habitat:</strong> {animal['characteristics'].get('habitat', 'Unknown')}</p>
        </div>
        """
        animals_html += animal_block
else:
    # Custom error message if no animals were found
    animals_html = f"""
    <div class="error-message">
        <h2>🐾 The animal "{animal_name}" doesn't exist.</h2>
        <p>Try searching for a different animal or check your spelling!</p>
        <img src="https://via.placeholder.com/300?text=No+Animal+Found" alt="Not Found">
    </div>
    """

# Step 5: Replace the placeholder in the template with the content
html_output = html_template.replace("{{ animals_content }}", animals_html)

# Step 6: Write the final HTML output to a file
with open("animals.html", "w") as file:
    file.write(html_output)

print("✅ Website was successfully generated to the file animals.html.")