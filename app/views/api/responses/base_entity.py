from flask import jsonify

from ....database import db


class BaseEntity(object):
    def __init__(self, model: db.Model):
        self._model = model

    def build_from_model(self):
        return {"id": self._model.id}

    def response(self):
        return jsonify(self.build_from_model())
