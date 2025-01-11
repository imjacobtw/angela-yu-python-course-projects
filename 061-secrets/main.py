from flask import Flask, render_template, request, redirect
from flask_wtf import CSRFProtect
from login_form import LoginForm
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
app.secret_key = "some secret string"
csrf = CSRFProtect(app)
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if not login_form.validate_on_submit():
        return render_template("login.html", form=login_form)

    if (
        login_form.email.data == "admin@email.com"
        and login_form.password.data == "12345678"
    ):
        return render_template("success.html")

    return render_template("denied.html")


if __name__ == "__main__":
    app.run()
