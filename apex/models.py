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