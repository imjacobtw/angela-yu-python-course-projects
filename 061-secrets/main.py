from dotenv import load_dotenv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
from login_form import LoginForm
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
csrf = CSRFProtect(app)
bootstrap = Bootstrap5(app)


@app.route("/")
def home() -> str:
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login() -> str:
    login_form = LoginForm()

    if login_form.validate_on_submit():
        is_correct_email = login_form.email.data == "admin@email.com"
        is_correct_password = login_form.password.data == "12345678"

        if is_correct_email and is_correct_password:
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run()
