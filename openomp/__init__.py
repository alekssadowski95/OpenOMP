from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Create app instance
app = Flask(__name__)

# Add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# change public db credentials
db = SQLAlchemy(app)

# !!!This key needs to be changed!!!
app.config['SECRET_KEY'] = '59f063a2e5406614813c5b07e129fdrb'

# Add login
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Add routes to app
from openomp import routes