import sqlite3


class Database:

    def __init__(self) -> None:
        pass

    def connect_db(self):
        connect = self.db.open_connection()
        cur = connect.cursor()
        cur.execute(
            'CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, age INTEGER, email TEXT, password TEXT)')
        self.db.confirm_operation(connect)
        self.db.close_connection(connect)

    def open_connection(self):
        return sqlite3.connect("./database/database.sqlite3")

    def close_connection(self, connect):
        return connect.close()

    def confirm_operation(self, connect):
        return connect.commit()
