from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField,FileField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
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

class PropertyForm(FlaskForm):
  address = StringField('Address', validators=[DataRequired()])
  city = StringField('City', validators=[DataRequired()])
  property_size = IntegerField('Property Size (sqft)', validators=[DataRequired(), NumberRange(min=0)])
  num_bedrooms = IntegerField('Number of Bedrooms', validators=[DataRequired(), NumberRange(min=0)])
  num_bathrooms = IntegerField('Number of Bathrooms', validators=[DataRequired(), NumberRange(min=0)])
  num_carspaces = IntegerField('Number of Carspaces', validators=[DataRequired(), NumberRange(min=0)])
  description = TextAreaField('Description')
  images = FileField('Images')
  listing_type = SelectField('Listing Type', choices=[('1', 'For Sale'), ('2', 'For Rent')], coerce=int, validators=[DataRequired()])
  submit = SubmitField('Add Property')

class UpdateProfileForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired()])
  profile_pic = FileField('Profile Picture')
  submit = SubmitField('Update')