from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


def create_select_choices(emoji, can_be_null):
    choices = ["✘"] if can_be_null else []
    return choices + [emoji * i for i in range(1, 6)]


class CafeForm(FlaskForm):
    cafe = StringField("Cafe Name", validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    opening_time = StringField("Opening Time e.g. 8AM")
    closing_time = StringField("Closing Time e.g. 5:30PM")
    coffee_rating = SelectField("Coffee Rating", choices=create_select_choices("☕️", False))
    wifi_strength_rating = SelectField("Wifi Strength Rating", choices=create_select_choices("💪", True))
    power_socket_availability = SelectField("Power Socket Availability", choices=create_select_choices("🔌", True))
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()

    if not form.validate_on_submit():
        return render_template("add.html", form=form)

    with open("cafe-data.csv", "a", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow(list(form.data.values())[:-2])
    
    return redirect("/cafes")


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []

        for row in csv_data:
            list_of_rows.append(row)

    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run()
