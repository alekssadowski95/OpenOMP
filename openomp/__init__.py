from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Create app instance
app = Flask(__name__)

# Add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# change public db credentials
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qqyaamzzkvorvh:f480ce43646794c02d634ee386b6e6f17b50e5addb59cc1e5dce172010b3052f@ec2-54-72-155-238.eu-west-1.compute.amazonaws.com:5432/d3fo6sk91rc21s'
db = SQLAlchemy(app)

# Add secret key for forms
app.config['SECRET_KEY'] = '59f063a2e5406614813c5b07e129fdrb'

# Add login
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Add routes to app
from openomp import routes