import datetime

from sqlalchemy import event
from werkzeug.security import check_password_hash, generate_password_hash

from ..database import db
from .base import Base


class User(Base):
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


def encrypt_password(target, value, old_value, initiator):
    generate_password_hash(value)


event.listen(User.password, 'set', encrypt_password, retval=True)
