from models.User import User
from services.UserService import UserService
from flask import make_response, jsonify


class UserController:
    def __init__(self, user_service:UserService) -> None:
        self.user_service = user_service

    def get(self):
        select = self.user_service.get()

        make_json = jsonify({
            'users': select
        })

        response = make_response(make_json, 200)
        return response

    def get_one(self, id):
        select_one = self.user_service.get_one(id)
        response = make_response(select_one, 200)
        return response

    def insert(self, request):
        name = request['name']
        email = request['email']
        age = request['age']
        password = request['password']

        new_user = User(id=None, age=age, name=name, email=email, password=password)

        user_created = self.user_service.insert(new_user)
        response = make_response(user_created, 201)
        return response

    def update(self, request, id):
        name = request['name']
        email = request['email']
        age = request['age']
        password = request['password']

        new_user = User(id=id, age=age, name=name, email=email, password=password)

        user_updated = self.user_service.update(new_user, id)
        response = make_response(user_updated, 200)
        return response

    def delete(self, id):
        user_deleted = self.user_service.delete(id)
        response = make_response(user_deleted, 200)
        return response
