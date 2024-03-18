from datetime import datetime
from apex import db

class Agent(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  profile_pic = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), nullable=False)
  description = db.Column(db.Text, nullable=False)
  phone_number = db.Column(db.String(20), nullable=False)

  def __repr__(self):
      return f"Agent('{self.username}', '{self.email}', '{self.profile_pic}')"