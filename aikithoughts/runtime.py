from flask import Flask
from flask.ext.assets import Environment
from flask.ext.security.core import Security
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf.csrf import CsrfProtect


app = Flask(__name__)

csrf = CsrfProtect()

db = SQLAlchemy()

security = Security()

assets = Environment()