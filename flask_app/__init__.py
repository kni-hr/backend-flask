from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# use env variables in prod
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123'

db = SQLAlchemy(app)

from .views import *