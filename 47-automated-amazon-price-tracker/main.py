from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import requests
import smtplib

def get_item_price():
    price_dollars = soup.select_one("#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole").text[:-1]
    price_cents = soup.select_one("#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-fraction").text
    price = f"{price_dollars}.{price_cents}"
    return float(price)

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
# The live website cannot be used as prices are dynamically loaded by JavaScript after the response markup loads. Use Selenium instead.
URL = "https://appbrewery.github.io/instant_pot/" # "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
DESIRED_PRICE = 100.0

response = requests.get(URL)
soup = BeautifulSoup(response.text, "lxml")
price = get_item_price()

if price <= DESIRED_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        subject = "Instant Pot Price Alert"
        message = f"The product price is now ${price}, below your target price. Buy now!"
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f"Subject:{subject}\n\n{message}"
        )