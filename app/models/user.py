import datetime

from sqlalchemy import event
from werkzeug.security import check_password_hash, generate_password_hash

from ..database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column('id', db.BigInteger, primary_key=True)
    email = db.Column('email', db.String(64), nullable=False)
    password = db.Column('password', db.String(64), nullable=False)
    created_at = db.Column('created_at',
                           db.TIMESTAMP,
                           default=datetime.datetime.utcnow,
                           nullable=False)
    updated_at = db.Column('updated_at',
                           db.TIMESTAMP,
                           onupdate=datetime.datetime.utcnow,
                           nullable=False)

    def __repr__(self):
        return "<{name} '{id}'>".format(name=self.__class__.__name__,
                                        id=self.id)

    @staticmethod
    def is_authenticated() -> bool:
        return True

    @staticmethod
    def is_active() -> bool:
        return True

    @staticmethod
    def is_anonymous(self) -> bool:
        return False

    def get_id(self) -> int:
        return self.id


def encrypt_password(target, value, old_value, initiator):
    generate_password_hash(value)


event.listen(User.password, 'set', encrypt_password, retval=True)
