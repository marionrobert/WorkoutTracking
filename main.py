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
exercises = result["exercises"]

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in exercises:
    SHEETY_PARAMS = {
        "workout": {
          "date": today,
          "time": now_time,
          "exercise": exercise['name'].title(),
          "duration": exercise['duration_min'],
          "calories": exercise['nf_calories'],
          "id": 2
        }
    }

    SHEETY_ENDPOINT = "https://api.sheety.co/075a1aa8ceadab13ed826945168b2fff/workoutTracking/workouts"

    # # without authentication
    # response_post = requests.post(SHEETY_ENDPOINT, json=SHEETY_PARAMS)
    # print(response_post.text)


    # # # Basic Authentication
    # bearer_headers = {
    #     "Authorization": os.environ["BASIC_AUTH"]
    #
    # }
    #
    # response_post = requests.post(
    #     SHEETY_ENDPOINT,
    #     json=SHEETY_PARAMS,
    #     headers=bearer_headers
    # )
    # print(response_post.text)


    # # Bearer Token Authentication
    bearer_headers = {
        "Authorization": os.environ["BEARER_AUTH"]
    }

    response_post = requests.post(
        url=SHEETY_ENDPOINT,
        headers=bearer_headers,
        json=SHEETY_PARAMS
    )
    print(response_post.text)




