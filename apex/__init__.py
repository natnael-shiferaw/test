from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from apex.config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
#login_manager = LoginManager()
#login_manager.login_view = 'agents.login'
#login_manager.login_message_category = 'info'

def create_app(config_class=Config):

  app = Flask(__name__)
  app.config.from_object(Config)
  #bcrypt.init_app(app)
  #login_manager.init_app(app)

  from apex.main.routes import main
  from apex.agents.routes import agents

  app.register_blueprint(main)
  app.register_blueprint(agents)

  return app

