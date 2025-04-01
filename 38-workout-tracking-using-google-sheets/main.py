from datetime import datetime
from dotenv import dotenv_values
import requests

config = dotenv_values(".env")

NUTRITIONIX_API_APP_ID = config["NUTRITIONIX_API_APP_ID"]
NUTRITIONIX_API_APP_KEY = config["NUTRITIONIX_API_APP_KEY"]
NUTRITIONIX_API_BASE_URL = "https://trackapi.nutritionix.com"
SHEETY_API_URL = config["SHEETY_API_URL"]
SHEETY_API_USERNAME = config["SHEETY_API_USERNAME"]
SHEETY_API_PASSWORD = config["SHEETY_API_PASSWORD"]

WEIGHT_KG = 70
HEIGHT_CM = 186
AGE = 24

user_exercise_input = input("Tell me which exercises you did: ")

body = {
    "query": user_exercise_input,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
headers = {"x-app-id": NUTRITIONIX_API_APP_ID, "x-app-key": NUTRITIONIX_API_APP_KEY}
response = requests.post(
    url=f"{NUTRITIONIX_API_BASE_URL}/v2/natural/exercise",
    headers=headers,
    json=body,
)
response.raise_for_status()
data = response.json()

for exercise in data["exercises"]:
    now = datetime.now()
    body = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(
        url=SHEETY_API_URL,
        json=body,
        auth=(SHEETY_API_USERNAME, SHEETY_API_PASSWORD)
    )

    response.raise_for_status()
