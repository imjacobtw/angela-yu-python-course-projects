from dotenv import load_dotenv
from internet_speed_twitter_bot import InternetSpeedTwitterBot
import os

load_dotenv()

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
PROMISED_DOWN = float(os.getenv("PROMISED_DOWN"))
PROMISED_UP = float(os.getenv("PROMISED_UP"))

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD, PROMISED_DOWN, PROMISED_UP)
