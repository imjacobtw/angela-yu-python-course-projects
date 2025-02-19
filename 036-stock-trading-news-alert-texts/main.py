from dotenv import dotenv_values
from twilio.rest import Client
import datetime
import requests
import sys

config = dotenv_values(".env")

ALPHA_VANTAGE_API_KEY = config["ALPHA_VANTAGE_API_KEY"]
ALPHA_VANTAGE_API_URL = "https://www.alphavantage.co/query"
NEWS_API_API_KEY = config["NEWS_API_API_KEY"]
NEWS_API_API_URL = "https://newsapi.org/v2/everything"
TWILIO_ACCOUNT_SID = config["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = config["TWILIO_AUTH_TOKEN"]
TWILIO_PHONE_NUMBER = config["TWILIO_PHONE_NUMBER"]
MY_PHONE_NUMBER = config["MY_PHONE_NUMBER"]

STOCK = "SMCI"
COMPANY_NAME = "Super Micro Computer, Inc."
DESIRED_PERCENTAGE_CHANGE = 5


def format_article(article) -> str:
    messageBody = f"{STOCK}: {"📈" if close_difference_percentage > 0 else "📉"}{close_difference_percentage}%\n"
    messageBody += f"Headline: {article["title"]}\n"
    messageBody += f"Brief: {article["description"]}"
    return messageBody


response = requests.get(
    ALPHA_VANTAGE_API_URL,
    {"function": "TIME_SERIES_DAILY", "symbol": STOCK, "apikey": ALPHA_VANTAGE_API_KEY},
)

try:
    response.raise_for_status()
    data = response.json()
    daily_stock_data = data["Time Series (Daily)"]
except Exception as e:
    print("There was an error accessing the Alpha Vantage API.")
    sys.exit()

yesterday_date = datetime.datetime.now() + datetime.timedelta(days=-1)

while yesterday_date.strftime("%Y-%m-%d") not in daily_stock_data:
    yesterday_date = yesterday_date + datetime.timedelta(days=-1)

ereyesterday_date = yesterday_date + datetime.timedelta(days=-1)

while ereyesterday_date.strftime("%Y-%m-%d") not in daily_stock_data:
    ereyesterday_date = ereyesterday_date + datetime.timedelta(days=-1)

yesterday_date_key = yesterday_date.strftime("%Y-%m-%d")
ereyesterday_date_key = ereyesterday_date.strftime("%Y-%m-%d")
yesterday_closing_price = float(daily_stock_data[yesterday_date_key]["4. close"])
ereyesterday_closing_price = float(daily_stock_data[ereyesterday_date_key]["4. close"])
close_difference = yesterday_closing_price - ereyesterday_closing_price
close_difference_percentage = round((close_difference / yesterday_closing_price) * 100)

if abs(close_difference_percentage) >= DESIRED_PERCENTAGE_CHANGE:
    response = requests.get(
        NEWS_API_API_URL,
        {
            "q": COMPANY_NAME,
            "from": yesterday_date_key,
            "sortBy": "popularity",
            "apiKey": NEWS_API_API_KEY,
        },
    )

    try:
        response.raise_for_status()
        data = response.json()
        articles = data["articles"][:3]
    except Exception as e:
        print("There was an error accessing the News API.")
        sys.exit()

    article_message_bodies = [format_article(article) for article in articles]

    twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for message_body in article_message_bodies:
        message = twilio_client.messages.create(
            body=message_body,
            from_=f"whatsapp:{TWILIO_PHONE_NUMBER}",
            to=f"whatsapp:{MY_PHONE_NUMBER}",
        )
        print(message.status)
