from config.db import db
from flask import Flask, jsonify, render_template, request, Response
from models.cafe import Cafe
import os
import random

API_KEY = os.getenv("API_KEY")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home() -> str:
    return render_template("index.html")


@app.route("/random")
def get_random_cafe() -> Response:
    result = db.session.execute(db.select(Cafe))
    cafes = result.scalars().all()
    random_cafe: Cafe = random.choice(cafes)
    return jsonify(random_cafe.to_dict())


@app.route("/all")
def get_all_cafes() -> Response:
    result = db.session.execute(db.select(Cafe))
    cafes = result.scalars().all()
    return jsonify([cafe.to_dict() for cafe in cafes])


@app.route("/search")
def get_cafes_by_location() -> Response | tuple[Response, int]:
    location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
    cafes = result.scalars().all()

    if len(cafes) > 0:
        return jsonify([cafe.to_dict() for cafe in cafes])
    else:
        return (
            jsonify(
                {
                    "error": {
                        "Not Found": "Sorry, we don't have a cafe at that location."
                    }
                }
            ),
            404,
        )


@app.route("/add", methods=["POST"])
def post_cafe() -> Response:
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify({"response": {"success": "Successfully added the new cafe."}})


@app.route("/update-price/<int:id>", methods=["PATCH"])
def patch_cafe_coffee_price(id: int) -> Response | tuple[Response, int]:
    result = db.session.execute(db.select(Cafe).where(Cafe.id == id))

    try:
        cafe: Cafe = result.scalar_one()
        new_price = request.args.get("new_price")
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify({"success": "Successfully updated the price."})
    except:
        return (
            jsonify(
                {
                    "error": {
                        "Not Found": "Sorry a cafe with that id was not found in the database."
                    }
                }
            ),
            404,
        )


@app.route("/report-closed/<int:id>", methods=["DELETE"])
def delete_cafe(id: int) -> Response | tuple[Response, int]:
    result = db.session.execute(db.select(Cafe).where(Cafe.id == id))

    try:
        cafe: Cafe = result.scalar_one()
        submitted_api_key = request.args.get("api-key")

        if submitted_api_key != API_KEY:
            return (
                jsonify(
                    {
                        "error": "Sorry, that's not allowed. Make sure you have the correct api_key."
                    }
                ),
                403,
            )

        db.session.delete(cafe)
        db.session.commit()
        return jsonify({"success": "Successfully deleted the cafe from the database."})
    except:
        return (
            jsonify(
                {
                    "error": {
                        "Not Found": "Sorry a cafe with that id was not found in the database."
                    }
                }
            ),
            404,
        )


if __name__ == "__main__":
    app.run(debug=True)
