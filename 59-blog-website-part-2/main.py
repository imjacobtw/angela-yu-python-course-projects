from datetime import datetime
from flask import Flask, render_template
from post import Post
from requests import Response, get

blog_response: Response = get("https://api.npoint.io/674f5423f73deab1e9a7")
posts: list[Post] = []

for post_json in blog_response.json():
    new_post: Post = Post(
        id=post_json["id"],
        title=post_json["title"],
        subtitle=post_json["subtitle"],
        body=post_json["body"],
        image_url=post_json["image_url"],
        author="Jacob Wilkerson",
        date=datetime.now(),
    )
    posts.append(new_post)

app: Flask = Flask(__name__)


@app.route("/")
def index_route() -> str:
    return render_template("index.html", posts=posts)


@app.route("/post/<int:id>")
def post_route(id: int) -> str:
    selected_post: Post = posts[id - 1]
    return render_template("post.html", post=selected_post)


@app.route("/about")
def about_route() -> str:
    return render_template("about.html")


@app.route("/contact")
def contact_route() -> str:
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
