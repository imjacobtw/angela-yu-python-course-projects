from flask import Flask, render_template
from post import Post
import requests

blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_data = blog_response.json()
posts = []

for post in blog_data:
    posts.append(Post(post["id"], post["title"], post["subtitle"], post["body"]))

app = Flask(__name__)


@app.route("/")
def home_route() -> str:
    return render_template("index.html", posts=posts)


@app.route("/post/<int:id>")
def post_route(id: int) -> str:
    selected_post = posts[id - 1]
    return render_template("post.html", post=selected_post)


if __name__ == "__main__":
    app.run()
