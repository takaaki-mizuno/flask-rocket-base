from flask import Blueprint, Flask, redirect, request

from .controllers import user_controller


def build_routes(app: Flask) -> None:
    app.register_blueprint(user_controller, url_prefix='/api/users')
