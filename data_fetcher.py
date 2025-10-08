import os
from dotenv import load_dotenv
import requests

# .env laden
load_dotenv()

# API Key aus der Umgebung holen
API_KEY = os.getenv("API_KEY")
URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {...},
      'locations': [...],
      'characteristics': {...}
    }
    """
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(URL, headers=headers, params={"name": animal_name})
    if response.status_code == 200:
        return response.json()
    else:
        return []
