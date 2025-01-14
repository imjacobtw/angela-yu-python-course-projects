from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from sqlalchemy import desc
from config.database import db
from models.search_movie_form import SearchMovieForm
from models.movie import Movie
from models.edit_movie_form import EditMovieForm
from dotenv import dotenv_values
import requests

config = dotenv_values(".env")
app = Flask(__name__)
app.config["SECRET_KEY"] = config["FLASK_APP_SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = config["SQLALCHEMY_DATABASE_URI"]
Bootstrap5(app)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(desc(Movie.rating))).scalars().all()
    
    for index, movie in enumerate(movies):
        movie.ranking = index + 1
    
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=["GET", "POST"])
def edit_movie():
    movie_id = request.args.get("id")
    edit_movie_form = EditMovieForm()
    print(movie_id)

    if request.method == "POST" and edit_movie_form.validate_on_submit():
        movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        movie.rating = edit_movie_form.rating.data
        movie.review = edit_movie_form.review.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", form=edit_movie_form, id=movie_id)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    search_movie_form = SearchMovieForm()

    if search_movie_form.validate_on_submit():
        movie_title = search_movie_form.movie_title.data
        response_body = requests.get(
            "https://api.themoviedb.org/3/search/movie",
            params={
                "api_key": config["THE_MOVIE_DB_API_KEY"],
                "query": movie_title
            },
        ).json()
        movies = []

        for result in response_body["results"]:
            movies.append({
                "id": result["id"],
                "title": result["title"],
                "release_date": result["release_date"],
            })

        return render_template("select.html", movies=movies)

    return render_template("add.html", form=search_movie_form)


@app.route("/find")
def find_movie():
    movie_id = request.args.get("id")
    response_body = requests.get(
        f"https://api.themoviedb.org/3/movie/{movie_id}",
        params={
            "api_key": config["THE_MOVIE_DB_API_KEY"],
        }
    ).json()

    movie = Movie(
        title=response_body["title"],
        year=response_body["release_date"][:4],
        description=response_body["overview"],
        img_url=f"https://image.tmdb.org/t/p/w600_and_h900_bestv2/{response_body["poster_path"]}"
    )
    
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for("edit_movie", id=movie.id))


if __name__ == "__main__":
    app.run(debug=True)
