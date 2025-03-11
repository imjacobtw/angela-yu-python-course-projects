from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, request
from post import Post
from requests import Response, get
import os
import smtplib

load_dotenv()

EMAIL_ADDRESS: str = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD: str = os.getenv("EMAIL_PASSWORD")

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


@app.route("/contact", methods=["GET", "POST"])
def contact_route() -> str:
    heading_text: str = "Contact Me"

    if request.method == "POST":
        name: str = request.form["name"]
        email: str = request.form["email"]
        phone_number: str = request.form["phone"]
        message: str = request.form["message"]

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
            email_message: str = (
                f"Subject:New Message\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone_number}\n"
                f"Message: {message}"
            )
            connection.sendmail(
                from_addr=EMAIL_ADDRESS, to_addrs=EMAIL_ADDRESS, msg=email_message
            )

        heading_text = "Successfully Sent Your Message"

    return render_template("contact.html", heading_text=heading_text)


if __name__ == "__main__":
    app.run()
