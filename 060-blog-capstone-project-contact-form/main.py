from dotenv import load_dotenv
from flask import Flask, render_template, request
import os
import requests
import smtplib

load_dotenv()
API_URL = os.getenv("API_URL")
MY_EMAIL_ADDRESS = os.getenv("MY_EMAIL_ADDRESS")
MY_EMAIL_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")
app = Flask(__name__)

posts_response = requests.get(API_URL)
posts = posts_response.json()


@app.route("/")
def home():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:id>")
def post(id):
    for post in posts:
        if post["id"] == id:
            return render_template("post.html", post=post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    is_message_sent = False

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone_number = request.form["phone"]
        message = request.form["message"]

        send_email(name, email, phone_number, message)
        is_message_sent = True

    return render_template("contact.html", is_message_sent=is_message_sent)


def send_email(name, sender_email, phone_number, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {sender_email}\nPhone Number: {phone_number}\nMessage: {message}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL_ADDRESS, MY_EMAIL_PASSWORD)
        connection.sendmail(MY_EMAIL_ADDRESS, MY_EMAIL_ADDRESS, email_message)


if __name__ == "__main__":
    app.run()
