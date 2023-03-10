import requests
from datetime import datetime
import os

GENDER = os.environ["GENDER"]
WEIGHT = os.environ["WEIGHT"]
HEIGHT = os.environ["HEIGHT"]
AGE = os.environ["AGE"]

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

HEADERS = {
    "x-app-id": os.environ["x-app-id"],
    "x-app-key": os.environ["x-app-key"]
}

NUTRITIONIX_PARAMS = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=HEADERS, json=NUTRITIONIX_PARAMS)
result = response.json()
