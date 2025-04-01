from flask_wtf import FlaskForm
from wtforms.fields.numeric import FloatField
from wtforms.fields.simple import SubmitField, StringField
from wtforms.validators import DataRequired, NumberRange


class EditMovieForm(FlaskForm):
    rating_validators = (DataRequired(), NumberRange(min=0, max=10))
    review_validators = (DataRequired(),)

    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=rating_validators)
    review = StringField("Your Review", validators=review_validators)
    submit = SubmitField("Done")
