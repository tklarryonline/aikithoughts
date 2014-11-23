from flask import Flask
from flask.ext.wtf.csrf import CsrfProtect


app = Flask(__name__)
csrf = CsrfProtect()
