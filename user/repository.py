from database.db import Database
from user.models import User

class UserRepository:
    def __init__(self, db: Database):
        self.db = db

    def new_id(self):
        size = len(self.get_all())
        return size + 1

    def get(self, id):
        connect = self.db.open_connection()
        cur = connect.cursor()
        cur.execute('SELECT * FROM users WHERE id = ?', (id,))
        row = cur.fetchone()
        selected_user = User(id=row[0], name=row[1], age=row[2], email=row[3], password=row[4])
        self.db.close_connection(connect)
        return selected_user

    def get_all(self):
        connect = self.db.open_connection()
        cur = connect.cursor()
        cur.execute('SELECT * FROM users')
        rows = cur.fetchall()
        users = []
        for user in rows:
           print(user)
           selected_user = User(id=user[0], name=user[1], age=user[2], email=user[3], password=user[4])
           users.append(selected_user)
        self.db.close_connection(connect)
        return users

    def insert(self, user: User):
        connect = self.db.open_connection()
        cur = connect.cursor()
        cur.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?)', (
            self.new_id(),
            user.name,
            user.age,
            user.email,
            user.password,
        ))
        self.db.confirm_operation(connect)
        self.db.close_connection(connect)

    def update(self, id, user: User):
        connect = self.db.open_connection()
        cur = connect.cursor()
        cur.execute('UPDATE users SET name = ?, age = ?, email = ?, password = ? WHERE id = ?', (
            user.name,
            user.age,
            user.email,
            user.password,
            id
        ))
        self.db.confirm_operation(connect)
        self.db.close_connection(connect)

    def delete(self, id):
        connect = self.db.open_connection()
        cur = connect.cursor()
        cur.execute('DELETE FROM users WHERE id = ?', (id,))
        self.db.confirm_operation(connect)
        self.db.close_connection(connect)
