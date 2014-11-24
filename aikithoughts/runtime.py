from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf.csrf import CsrfProtect


app = Flask(__name__)
csrf = CsrfProtect()
db = SQLAlchemy()
