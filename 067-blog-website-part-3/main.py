from config.db import db
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, Response, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from models.add_post_form import AddPostForm
from models.blog_post import BlogPost
import os
import smtplib

load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
Bootstrap5(app)
ckeditor = CKEditor(app)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def get_all_posts() -> str:
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route("/<int:post_id>")
def show_post(post_id: int) -> str:
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route("/new_post", methods=["GET", "POST"])
def add_new_post() -> str | Response:
    add_post_form = AddPostForm()

    if add_post_form.validate_on_submit():
        new_blog_post = BlogPost(
            title=add_post_form.title.data,
            subtitle=add_post_form.subtitle.data,
            date=datetime.now().strftime("%B %d, %Y"),
            body=add_post_form.body.data,
            author=add_post_form.author.data,
            img_url=add_post_form.img_url.data,
        )
        db.session.add(new_blog_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))

    return render_template(
        "make-post.html", form=add_post_form, heading_text="New Post"
    )


@app.route("/edit_post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id: int) -> str | Response:
    post = db.get_or_404(BlogPost, post_id)
    edit_post_form = AddPostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body,
    )

    if edit_post_form.validate_on_submit():
        post.title = edit_post_form.title.data
        post.subtitle = edit_post_form.subtitle.data
        post.img_url = edit_post_form.img_url.data
        post.author = edit_post_form.author.data
        post.body = edit_post_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template(
        "make-post.html", form=edit_post_form, heading_text="Edit Post"
    )


@app.route("/delete/<int:post_id>")
def delete_post(post_id: int) -> Response:
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about() -> str:
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact() -> str:
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
    app.run(debug=True)
