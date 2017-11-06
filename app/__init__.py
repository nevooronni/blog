from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail#extension provides a simpole interface to setup smtop with your app send messages from your views and scripts
from flask_simplemde import SimpleMDE#extension that helps flask intergrate simpleMDE markdown editor to your flask appliation 

#initializing flask extension
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

	app = Flask(__name__)

	#app configurations
	app.config.from_object(config_options[config_name])
	db.init_app(app)

	#initializing bootstrap
	bootstrap.init_app(app)

	return app