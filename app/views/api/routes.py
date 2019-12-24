import logging
import os

from flask import Blueprint, redirect, request
from injector import inject

from ...helpers import FileHelper
from ...services import UserService
from .responses import Error, User, Users

app = Blueprint('api', __name__)


@app.route('/users', methods=["GET"])
@inject
def index(user_service: UserService):
    offset = request.args.get('offset', default=0, type=int)
    limit = request.args.get('limit', default=10, type=int)
    users = user_service.get_jobs(offset, limit)

    return Users(users).response(), 200


@app.route('/users', methods=["POST"])
@inject
def create(user_service: UserService):
    user = user_service.create_user({
        "data": request.form.get('data'),
    })

    [os.remove(str(path.resolve())) for path in temporary_paths]

    return User(user).response(), 201


@app.route('/users/<int:user_id>', methods=["GET"])
@inject
def get(user_id: int, user_service: UserService):
    user = user_service.get_job(user_id)
    if user is None:
        return Error("User Not Found").response(), 404

    return User(user).response(), 200
