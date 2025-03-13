from flask_wtf import FlaskForm
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import StringField, SubmitField, URLField
from wtforms.validators import DataRequired


def create_select_field_choices(emoji: str) -> list[tuple[str, str]]:
    choices = [("✘", "✘")]
    choices += [(emoji * i, emoji * i) for i in range(1, 6)]
    return choices


class CafeForm(FlaskForm):
    name_validators = (DataRequired(),)
    location_validators = (DataRequired(),)
    opening_time_validators = (DataRequired(),)
    closing_time_validators = (DataRequired(),)
    coffee_rating_validators = (DataRequired(),)
    wifi_rating_validators = (DataRequired(),)
    power_rating_validators = (DataRequired(),)

    coffee_rating_choices = create_select_field_choices("☕")
    wifi_rating_choices = create_select_field_choices("💪")
    power_rating_choices = create_select_field_choices("🔌")

    name = StringField("Cafe Name", validators=name_validators)
    location = URLField(
        "Cafe Location on Google Maps (URL)", validators=location_validators
    )
    opening_time = StringField(
        "Opening Time e.g. 8AM", validators=opening_time_validators
    )
    closing_time = StringField(
        "Closing Time e.g. 5:30PM", validators=closing_time_validators
    )
    coffee_rating = SelectField(
        "Coffee Rating",
        choices=coffee_rating_choices,
        validators=coffee_rating_validators,
    )
    wifi_rating = SelectField(
        "Wifi Strength Rating",
        choices=wifi_rating_choices,
        validators=wifi_rating_validators,
    )
    power_rating = SelectField(
        "Power Socket Availability",
        choices=power_rating_choices,
        validators=power_rating_validators,
    )
    submit = SubmitField("Submit")
