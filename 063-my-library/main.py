from flask import Flask, redirect, render_template, request, url_for
from models.book import Book
from config.database import db
from models.book import Book

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")

    new_book = Book(
        title=request.form["title"],
        author=request.form["author"],
        rating=request.form["rating"],
    )

    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    id = request.args.get("id")
    book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()

    if request.method == "GET":
        return render_template("edit.html", book=book)

    book.rating = request.form["rating"]
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete")
def delete():
    id = request.args.get("id")
    book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()
