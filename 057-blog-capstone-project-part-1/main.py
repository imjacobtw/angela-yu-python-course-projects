from dotenv import load_dotenv
from flask import Flask, render_template
from post import Post
import requests
import os

load_dotenv()
API_URL = os.getenv("API_URL")
app = Flask(__name__)
posts = []


@app.route("/blog")
def blog():
    posts_response = requests.get(API_URL)

    for post_json in posts_response.json():
        post = Post(
            post_json["id"],
            post_json["title"],
            post_json["subtitle"],
            post_json["body"],
        )
        posts.append(post)

    return render_template("index.html", posts=posts)


@app.route("/post/<int:id>")
def post(id):
    for post in posts:
        if post.id == id:
            return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run()
