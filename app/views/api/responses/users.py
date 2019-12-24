from .base_list import BaseList
from .user import User


class Users(BaseList):
    _target = User
