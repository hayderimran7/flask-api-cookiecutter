from flask import Blueprint, jsonify, make_response

api = Blueprint('api', __name__)


@api.route("/", methods=["GET"])
def hello():
    return make_response("Hello World!", 200)


@api.route("/<name>", methods=["GET"])
def hello_name(name):
    return make_response(jsonify({"name": name}), 200)
