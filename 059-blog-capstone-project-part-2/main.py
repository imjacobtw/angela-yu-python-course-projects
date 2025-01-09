from dotenv import load_dotenv
from flask import Flask, render_template
import requests
import os

load_dotenv()
API_URL = os.getenv("API_URL")
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


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
