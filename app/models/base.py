import datetime

from ..database import db


class Base(db.Model):
    __tablename__ = ''
    id = db.Column('id', db.BigInteger, primary_key=True)
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
