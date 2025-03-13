from cafe_form import CafeForm
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, Response
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
import csv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
csrf = CSRFProtect(app)
bootstrap = Bootstrap5(app)


@app.route("/")
def home_route() -> str:
    return render_template("index.html")


@app.route("/cafes")
def cafes_route() -> str:
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows: list[list[str]] = []

        for row in csv_data:
            list_of_rows.append(row)

    return render_template("cafes.html", cafes=list_of_rows)


@app.route("/add", methods=["GET", "POST"])
def add_cafe_route() -> str | Response:
    cafe_form = CafeForm()

    if cafe_form.validate_on_submit():
        with open("cafe-data.csv", newline="", encoding="utf-8", mode="a") as csv_file:
            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow(
                [
                    cafe_form.name.data,
                    cafe_form.location.data,
                    cafe_form.opening_time.data,
                    cafe_form.closing_time.data,
                    cafe_form.coffee_rating.data,
                    cafe_form.wifi_rating.data,
                    cafe_form.power_rating.data,
                ]
            )

        return redirect(url_for("cafes_route"))

    return render_template("add.html", form=cafe_form)


if __name__ == "__main__":
    app.run(debug=True)
