from flask import Flask
from .views.api import api

app = Flask(__name__)

app.register_blueprint(api)
