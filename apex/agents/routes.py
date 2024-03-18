from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from apex import db, bcrypt
from apex.models import Agent
from apex.agents.forms import RegistrationForm, LoginForm

agents = Blueprint('agents', __name__)

@agents.route("/agents", methods=['GET', 'POST'])
def home_agent():
  return "<h1>Home Page Agent</h1>"

@agents.route("/agents/register", methods=['GET', 'POST'])
def register():
  #if current_user.is_authenticated:
    #return redirect(url_for('home_agent'))
  form = RegistrationForm()
  if form.validate_on_submit():
      flash(f'Account created for {form.username.data}!', 'success')
      return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)

@agents.route("/agents/login", methods=['GET', 'POST'])
def login():
      form = LoginForm()
      if form.validate_on_submit():
          if form.email.data == 'admin@blog.com' and form.password.data == 'password':
              flash('You have been logged in!', 'success')
              return redirect(url_for('home'))
          else:
              flash('Login Unsuccessful. Please check username and password', 'danger')
      return render_template('login.html', title='Login', form=form)