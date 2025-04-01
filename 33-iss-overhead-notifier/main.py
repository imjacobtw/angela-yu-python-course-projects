from datetime import datetime
from dotenv import dotenv_values
import requests
import smtplib
import sys
import time

config = dotenv_values(".env")

MY_LAT = float(config["MY_LAT"])
MY_LONG = float(config["MY_LONG"])
EMAIL_APP_ADDRESS = config["EMAIL_APP_ADDRESS"]
EMAIL_APP_PASSWORD = config["EMAIL_APP_PASSWORD"]

def is_iss_overhead() -> bool:
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    is_in_latitude_range = MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
    is_in_longitude_range = MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    return is_in_latitude_range and is_in_longitude_range

def is_nighttime(time_now: datetime) -> bool:
    response = requests.get("https://api.sunrise-sunset.org/json", {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "tzid": "America/Chicago",
        "formatted": 0,
    })
    response.raise_for_status()
    data = response.json()

    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now_hour = time_now.hour

    is_before_sunrise = now_hour < sunrise_hour
    is_after_sunset = now_hour > sunset_hour
    return is_before_sunrise or is_after_sunset

while True:
    now = datetime.now()

    try:
        if is_iss_overhead() and is_nighttime(now):
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(EMAIL_APP_ADDRESS, EMAIL_APP_PASSWORD)
                message = "Subject:The ISS is Overhead!\n\nGo outside and look up in the sky!"
                connection.sendmail(EMAIL_APP_ADDRESS, EMAIL_APP_ADDRESS, message)
            print(f"[{now}] The ISS is above you! Email sent!")
        else:
            print(f"[{now}] It is either daytime, or the ISS is not near you. Checking again in 60 seconds...")
    except requests.HTTPError:
        print(f"[{now}] There was an error accessing one of the APIs. Please check for changes in the APIs' documentations.")
        sys.exit(1)

    time.sleep(60)