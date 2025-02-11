import requests
import os
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration (Now using .env)
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    """
    Fetches the animals data for the given 'animal_name'.
    Returns a list of animals, where each animal is a dictionary.
    """
    if not API_KEY:
        print("❌ Error: Missing API key. Make sure to set it in the .env file.")
        return None

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()  # Return the fetched data
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
        return None