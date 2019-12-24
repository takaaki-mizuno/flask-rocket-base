from typing import List

from flask import jsonify

from ....database import db
from .base_entity import BaseEntity


class BaseList(object):
    _target = BaseEntity

    def __init__(self, models: List[db.Model]):
        self._models = models

    def build_from_models(self):
        lists = [
            self._target(model).build_from_model() for model in self._models
        ]
        return {"list": lists}

    def response(self):
        return jsonify(self.build_from_models())
