from flask import Flask,url_for,request, flash,redirect
from app.config import Config
from app.app_funcs.login_form import LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate=Migrate(app,db)

from app import routes,models