class User:
    def __init__(self,id, name, age, email, password):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.password = password

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'password': self.password
        }
