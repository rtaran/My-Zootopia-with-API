import requests
import os
from dotenv import load_dotenv  # Load environment variables

# Load .env file
load_dotenv()

# API Configuration
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    """
    Fetches animal data from API Ninja.
    Returns a list of animals as dictionaries.
    """
    if not API_KEY:
        print("❌ Error: Missing API key. Make sure to set it in the .env file.")
        return None

    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()  # Returns a list of dictionaries
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
        return None