from flask_wtf import FlaskForm # type: ignore
from wtforms import StringField, SubmitField, BooleanField # type: ignore
from wtforms.fields.simple import PasswordField # type: ignore
from wtforms.validators import DataRequired, URL # type: ignore
from flask_ckeditor import CKEditorField # type: ignore

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    submit = SubmitField("Login")