from dotenv import dotenv_values
import datetime as dt
import pandas
import random
import smtplib

config = dotenv_values(".env")
APP_EMAIL = config["APP_EMAIL"]
APP_PASSWORD = config["APP_PASSWORD"]

birthdays = pandas.read_csv("birthdays.csv").to_dict()
today = dt.datetime.now()
this_month = today.month
this_day = today.day

for index, person in birthdays["name"].items():
    person_birth_month = birthdays["month"][index]
    person_birth_day = birthdays["day"][index]
    person_email = birthdays["email"][index]

    if this_month == person_birth_month and this_day == person_birth_day:
        letter_file_name = f"./letter_templates/letter_{random.randint(1, 3)}.txt"

        with open(letter_file_name) as file:
            email_message = file.read()

        email_message = email_message.replace("[NAME]", person)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=APP_EMAIL, password=APP_PASSWORD)
            connection.sendmail(
                from_addr=APP_EMAIL,
                to_addrs=person_email,
                msg=f"Subject:Happy Birthday!\n\n{email_message}"
            )