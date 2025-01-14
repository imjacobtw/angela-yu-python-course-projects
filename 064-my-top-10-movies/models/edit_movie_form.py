from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class EditMovieForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")
