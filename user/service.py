from user.models import User
from user.repository import UserRepository


class UserService:

    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def get(self):
        select_all = self.repository.get_all()
        return [user.serialize() for user in select_all]

    def get_one(self, id):
        select_one = self.repository.get(id)
        return select_one.serialize()

    def insert(self, user: User):
        self.repository.insert(user)
        return {
            'message': 'usuario inserido'
        }

    def update(self, user: User, id):
        self.repository.update(id, user)
        return {
            'message': 'usuario atualizado'
        }

    def delete(self, id):
        self.repository.delete(id)
        return {
            'message': 'usuario deletado'
        }
