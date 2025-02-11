import requests

# API Configuration
API_KEY = "9raNurS5dRLg5zIB0+/CjQ==YE2HPWQfCLiICTvg"
BASE_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    """
    Fetches the animals data for the given 'animal_name'.
    Returns a list of animals, where each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': { ... },
        'locations': [ ... ],
        'characteristics': { ... }
    }
    """
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data  # Could be an empty list []
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
        return None  # Return None in case of API failure