import os
from flask import Flask
from uris import app_route, connection


app = Flask(__name__)
app.register_blueprint(app_route)

if not os.path.isfile('./database/database.sqlite3'):
    connection.connect_db()

if __name__ == "__main__":
    app.run(debug=True)
