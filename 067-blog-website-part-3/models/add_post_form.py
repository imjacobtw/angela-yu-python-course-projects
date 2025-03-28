from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms.fields.simple import SubmitField, StringField, URLField
from wtforms.validators import DataRequired


class AddPostForm(FlaskForm):
    title_validators = (DataRequired(),)
    subtitle_validators = (DataRequired(),)
    author_validators = (DataRequired(),)
    img_url_validators = (DataRequired(),)
    body_validators = (DataRequired(),)

    title = StringField("Blog Post Title", validators=title_validators)
    subtitle = StringField("Subtitle", validators=subtitle_validators)
    author = StringField("Your Name", validators=author_validators)
    img_url = URLField("Blog Image URL", validators=img_url_validators)
    body = CKEditorField("Blog Content", validators=body_validators)
    submit = SubmitField("Submit Post")
