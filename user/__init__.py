from user.repository import UserRepository
from user.service import UserService
from user.views import UserController


def user_module(connection):
    repository = UserRepository(connection)
    service = UserService(repository)
    controller = UserController(service)

    return controller
