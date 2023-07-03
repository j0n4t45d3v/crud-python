import os
from controllers.UserController import UserController
from database.db import Database
from flask import Flask, request

from services.UserService import UserService
from routes import app_route, connection


app = Flask(__name__)
app.register_blueprint(app_route)

if not os.path.isfile('./database/database.sqlite3'):
    connection.connect_db()

if __name__ == "__main__":
  app.run()
