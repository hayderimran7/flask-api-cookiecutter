from flask import Blueprint

home = Blueprint('hello', __name__)


@home.route("/")
def hello():
    return "Hello World!"


@home.route("/<name>")
def hello_name(name):
    return f"Hello, {name.title()}."
