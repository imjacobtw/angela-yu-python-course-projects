from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email_validators = (
        DataRequired(),
        Email(),
    )

    password_validators = (
        DataRequired(),
        Length(min=8),
    )

    email = StringField(label="Email", validators=email_validators)
    password = PasswordField(label="Password", validators=password_validators)
    submit = SubmitField(label="Log In")
