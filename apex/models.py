from datetime import datetime
from apex import db,login_manager
from flask_login import UserMixin
from flask import current_app

@login_manager.user_loader
def load_agent(agent_id):
    return Agent.query.get(int(agent_id))

class Agent(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  profile_pic = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), nullable=False)
  description = db.Column(db.Text, nullable=False, default='some description')
  phone_number = db.Column(db.String(20), nullable=False, default='some phone number')

  def __repr__(self):
      return f"Agent('{self.username}', '{self.email}', '{self.profile_pic}')"

class PropertyImage(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
  image_path = db.Column(db.String(255), nullable=False)

  def __repr__(self):
      return f"PropertyImage('{self.property_id}', '{self.image_path}')"

class Property(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  address = db.Column(db.String(255), nullable=False)
  city = db.Column(db.String(100), nullable=False)
  property_size = db.Column(db.Integer, nullable=False)
  num_bedrooms = db.Column(db.Integer, nullable=False)
  num_bathrooms = db.Column(db.Integer, nullable=False)
  num_carspaces = db.Column(db.Integer, nullable=False)
  description = db.Column(db.Text, nullable=True)

  # Define the one-to-many relationship between Property and PropertyImage
  images = db.relationship('PropertyImage', backref='property', lazy=True)
  # Define the one-to-one relationship between Property and Agent
  agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=False)
  agent = db.relationship('Agent', backref='properties')

  def __repr__(self):
      return f"Property('{self.address}', '{self.city}')"

class ListingType(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(100), nullable=False)

  def __repr__(self):
      return f"ListingType('{self.description}')"

class ListingStatus(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(100), nullable=False)

  def __repr__(self):
      return f"ListingStatus('{self.description}')"

class Feature(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  feature_name = db.Column(db.String(100), nullable=False)

  def __repr__(self):
      return f"Feature('{self.feature_name}')"

class PropertyFeature(db.Model):
  property_id = db.Column(db.Integer, db.ForeignKey('property.id'), primary_key=True)
  feature_id = db.Column(db.Integer, db.ForeignKey('feature.id'), primary_key=True)

class Listing(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
  agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=False)
  listing_status_id = db.Column(db.Integer, db.ForeignKey('listing_status.id'), nullable=False)
  listing_type_id = db.Column(db.Integer, db.ForeignKey('listing_type.id'), nullable=False)
  price = db.Column(db.Integer, nullable=False)
  created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __repr__(self):
      return f"Listing('{self.id}', '{self.property_id}', '{self.agent_id}')"

class PropertyAgent(db.Model):
  property_id = db.Column(db.Integer, db.ForeignKey('property.id'),     
    primary_key=True)
  agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'), primary_key=True)
