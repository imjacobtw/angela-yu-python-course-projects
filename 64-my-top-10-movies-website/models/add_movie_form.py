from flask_wtf import FlaskForm
from wtforms.fields.simple import SubmitField, StringField
from wtforms.validators import DataRequired


class AddMovieForm(FlaskForm):
    title_validators = (DataRequired(),)

    title = StringField("Movie Title", validators=title_validators)
    submit = SubmitField("Add Movie")
