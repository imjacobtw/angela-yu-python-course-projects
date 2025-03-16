from config.db import db
from flask import Flask, render_template, redirect, url_for, request, Response
from flask_bootstrap import Bootstrap5
from models.add_movie_form import AddMovieForm
from models.edit_movie_form import EditMovieForm
from models.movie import Movie
from sqlalchemy import asc
import os
import requests

MOVIE_DB_API_KEY = os.getenv("MOVIE_DB_API_KEY")

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
Bootstrap5(app)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home_route() -> str:
    result = db.session.execute(db.select(Movie).order_by(asc(Movie.rating)))
    movies = result.scalars().all()

    for index, movie in enumerate(movies):
        movie.ranking = len(movies) - index

    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=["GET", "POST"])
def edit_route() -> str | Response:
    id = int(request.args.get("id"))
    edit_movie_form = EditMovieForm()
    result = db.session.execute(db.select(Movie).where(Movie.id == id))
    movie = result.scalar()

    if request.method == "POST" and edit_movie_form.validate_on_submit():
        new_rating = edit_movie_form.rating.data
        new_review = edit_movie_form.review.data
        movie.rating = new_rating
        movie.review = new_review
        db.session.commit()
        return redirect(url_for("home_route"))

    return render_template("edit.html", form=edit_movie_form, movie=movie)


@app.route("/delete")
def delete_route() -> Response:
    id = int(request.args.get("id"))
    result = db.session.execute(db.select(Movie).where(Movie.id == id))
    movie = result.scalar()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home_route"))


@app.route("/add", methods=["GET", "POST"])
def add_route() -> str | Response:
    add_movie_form = AddMovieForm()

    if request.method == "POST" and add_movie_form.validate_on_submit():
        title = add_movie_form.title.data.strip()
        headers = {"accept": "application/json"}
        params = {"api_key": MOVIE_DB_API_KEY, "query": title}
        response = requests.get(
            "https://api.themoviedb.org/3/search/movie", params=params, headers=headers
        )
        data = response.json()
        movies: list[dict[str, any]] = []

        for result in data["results"]:
            movies.append(
                {
                    "id": result["id"],
                    "title": result["title"],
                    "release_date": result["release_date"],
                }
            )

        return render_template("select.html", movies=movies)

    return render_template("add.html", form=add_movie_form)


@app.route("/find")
def find_route() -> Response:
    movie_id = int(request.args.get("id"))
    headers = {"accept": "application/json"}
    params = {"api_key": MOVIE_DB_API_KEY}
    response = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}", params=params, headers=headers
    )
    data = response.json()

    movie = Movie(
        title=data["title"],
        year=data["release_date"][:4],
        description=data["overview"],
        img_url=f"https://image.tmdb.org/t/p/w600_and_h900_bestv2/{data["poster_path"]}",
    )

    db.session.add(movie)
    db.session.commit()
    return redirect(url_for("edit_route", id=movie.id))


if __name__ == "__main__":
    app.run()
