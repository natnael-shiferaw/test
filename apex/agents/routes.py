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
  if current_user.is_authenticated:
    return redirect(url_for('home_agent'))
  form = RegistrationForm()
  if form.validate_on_submit():
      hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      agent = Agent(username=form.username.data, email=form.email.data, password=hashed_password)
      db.session.add(agent)
      db.session.commit()
      flash('Your account has been created! You are now able to log in', 'success')
      return redirect(url_for('agents.login'))
  return render_template('register.html', title='Register', form=form)

@agents.route("/agents/login", methods=['GET', 'POST'])
def login():
      if current_user.is_authenticated:
          return redirect(url_for('agents.home_agent'))
      form = LoginForm()
      if form.validate_on_submit():
          agent = Agent.query.filter_by(email=form.email.data).first()
          if agent and bcrypt.check_password_hash(agent.password, form.password.data):
              login_user(agent, remember=form.remember.data)
              next_page = request.args.get('next')
              return redirect(next_page) if next_page else redirect(url_for('agents.home_agent'))
          else:
              flash('Login Unsuccessful. Please check email and password', 'danger')
      return render_template('login.html', title='Login', form=form)