from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from apex.models import Agent
from email_validator import validate_email, EmailNotValidError



class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        agent = Agent.query.filter_by(username=username.data).first()
        if agent:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        try:
          validate_email(email.data)  # Use email_validator here
        except EmailNotValidError:
          raise ValidationError('Invalid email address.')

        agent = Agent.query.filter_by(email=email.data).first()
        if agent:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')