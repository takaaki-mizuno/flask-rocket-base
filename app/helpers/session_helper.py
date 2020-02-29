from ..session import login_manager
from flask_login import LoginManager


class SessionHelper(object):
    @classmethod
    def get_login_manager(cls) -> LoginManager:
        return login_manager
