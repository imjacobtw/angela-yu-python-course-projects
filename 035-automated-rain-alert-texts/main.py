from dotenv import dotenv_values
from twilio.rest import Client
import requests
import sys

config = dotenv_values(".env")

OPEN_WEATHER_MAP_API_KEY = config["OPEN_WEATHER_MAP_API_KEY"]
OPEN_WEATHER_MAP_API_URL = config["OPEN_WEATHER_MAP_API_URL"]
TWILIO_ACCOUNT_SID = config["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = config["TWILIO_AUTH_TOKEN"]
TWILIO_PHONE_NUMBER = config["TWILIO_PHONE_NUMBER"]
MY_PHONE_NUMBER = config["MY_PHONE_NUMBER"]
MY_LAT = float(config["MY_LAT"])
MY_LONG = float(config["MY_LONG"])

response = requests.get(OPEN_WEATHER_MAP_API_URL, {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": OPEN_WEATHER_MAP_API_KEY,
    "cnt": 4,
})

try:
    response.raise_for_status()
except requests.HTTPError as err:
    print(f"There was an error accessing the OpenWeather API. - {err}")
    sys.exit()

data = response.json()
is_raining_within_12_hours = False

for forecast in data["list"]:
    for condition in forecast["weather"]:
        if condition["main"] == "Rain":
            is_raining_within_12_hours = True

if is_raining_within_12_hours:
    twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = twilio_client.messages.create(
        body="It's going to rain today. Remember to bring an ☔!",
        from_=f"whatsapp:{TWILIO_PHONE_NUMBER}",
        to=f"whatsapp:{MY_PHONE_NUMBER}"
    )
    print(message.status)