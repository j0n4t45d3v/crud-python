from flask import Blueprint, request
from user import user_module
from database.db import Database

app_route = Blueprint('routes', __name__)

connection = Database()
user_controller = user_module(connection)

@app_route.route("/", methods=['GET'])
def index():
    return user_controller.get()

@app_route.route('/', methods=['POST'])
def post():
    req_data = request.get_json()
    return user_controller.insert(request=req_data)

@app_route.route('/<int:id>', methods=['GET'])
def get_one(id):
    return user_controller.get_one(id=id)

@app_route.route('/<int:id>', methods=['PUT'])
def put(id):
    req_data = request.get_json()
    return user_controller.update(request=req_data, id=id)

@app_route.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return user_controller.delete(id=id)
