from ..models import User
from .base_repository import BaseRepository


class UserRepository(BaseRepository):
    model_class = User
