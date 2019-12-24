import time
from typing import Dict, List, Optional

from ..models import User
from ..repositories import UserRepository


class UserService(object):
    def __init__(self, user_repository: UserRepository, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_repository = user_repository

    def get_users(self, offset: int, limit: int) -> List[User]:
        return self.user_repository.get(offset, limit, User.created_at.desc())

    def get_user(self, id_: int) -> Optional[User]:
        return self.user_repository.find(id_)

    def create_user(self, fields: Dict) -> Optional[User]:
        user_fields = {
            'email': fields['email'],
            'password': fields['password'],
        }
        user = self.user_repository.create(user_fields)

        return user
