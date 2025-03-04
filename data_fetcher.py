import os
import requests
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals?name="
HEADERS = {'X-Api-Key': API_KEY}


def fetch_animal_data(animal_name):
    """Fetch all matching animal data from API Ninja's Animals API."""
    response = requests.get(API_URL + animal_name, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        if data:  # Ensure response contains data
            return data  # Return all matching animals

    return []  # Return an empty list if API fails or no data found


if __name__ == "__main__":
    test_animal = input("Enter an animal name: ")
    print(fetch_animal_data(test_animal))