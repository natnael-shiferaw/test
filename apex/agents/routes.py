from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from apex import db, bcrypt
from apex.models import Agent,Property
from apex.agents.forms import RegistrationForm, LoginForm, PropertyForm, UpdateProfileForm

import os
#from werkzeug.utils import secure_filename

# Specify the directory where uploaded images will be stored
#UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'properties_img')
#ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
# helper function to check if the file extension is allowed
#def allowed_file(filename):
 # return '.' in filename and filename.rsplit('.', 1)[1].lower() in #ALLOWED_EXTENSIONS


agents = Blueprint('agents', __name__)

@agents.route("/agents", methods=['GET', 'POST'])
def home_agent():
  for_sale =[]
  for_rent = []
  return render_template("home_agent.html", for_sale=for_sale, for_rent=for_rent)

@agents.route("/agents/register", methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('agents.home_agent'))
  form = RegistrationForm()
  if form.validate_on_submit():
      hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      agent = Agent(username=form.username.data, email=form.email.data, full_name=form.full_name.data, phone_number=form.phone_number.data, password=hashed_password)
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


@agents.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('agents.home_agent'))

# Route to add a new property
@agents.route("/agents/add_property", methods=['GET', 'POST'])
@login_required
def add_property():
    form = PropertyForm()
    if form.validate_on_submit():
        # Extracting data from the form
        address = form.address.data
        city = form.city.data
        property_size = form.property_size.data
        num_bedrooms = form.num_bedrooms.data
        num_bathrooms = form.num_bathrooms.data
        num_carspaces = form.num_carspaces.data
        description = form.description.data
        image_link = form.image_link.data
        agent_id = current_user.id
        price = form.price.data
        listing_status = form.listing_status.data
        listing_type = form.listing_type.data

        # Creating a new Property object and adding it to the database
        property = Property(
            address=address,
            city=city,
            property_size=property_size,
            num_bedrooms=num_bedrooms,
            num_bathrooms=num_bathrooms,
            num_carspaces=num_carspaces,
            description=description,
            image_link=image_link,
            agent_id=agent_id,
            price=price,
            listing_status=listing_status,
            listing_type=listing_type
        )
        db.session.add(property)
        db.session.commit()

        flash('Property has been added successfully!', 'success')
        return redirect(url_for('agents.home_agent'))
    return render_template("add_property.html", title='Add Property', form=form)

@agents.route("/agents/profile", methods=['GET', 'POST'])
@login_required
def view_profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        # Code to handle form submission and update profile information
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('agents.view_profile'))
    return render_template('view_profile.html', title='My Profile', form=form)


@agents.route("/agents/my_ads", methods=['GET'])
@login_required
def my_ads():
    properties = Property.query.filter_by(agent_id=current_user.id).all()
    return render_template('my_ads.html', title='My Ads', properties=properties)
