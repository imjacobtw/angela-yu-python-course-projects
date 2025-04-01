from flask import Flask, render_template, request, redirect, url_for, Response
from config.db import db
from models.book import Book

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home_route() -> str:
    result = db.session.execute(db.select(Book))
    books = result.scalars().all()
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add_route() -> str | Response:
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = float(request.form["rating"])
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home_route"))

    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit_route() -> str | Response:
    if request.method == "POST":
        book_id = int(request.form["id"])
        rating = float(request.form["rating"])
        result = db.session.execute(db.select(Book).where(Book.id == book_id))
        book = result.scalar()
        book.rating = rating
        db.session.commit()
        return redirect(url_for("home_route"))

    book_id = int(request.args.get("id"))
    result = db.session.execute(db.select(Book).where(Book.id == book_id))
    book = result.scalar()
    return render_template("edit.html", book=book)


@app.route("/delete")
def delete_route() -> Response:
    book_id = int(request.args.get("id"))
    result = db.session.execute(db.select(Book).where(Book.id == book_id))
    book = result.scalar()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home_route"))


if __name__ == "__main__":
    app.run()
