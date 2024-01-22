from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length, IPAddress