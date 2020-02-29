from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector, request

from ..config import Config
from ..database import db, init_db
from ..helpers import SessionHelper
from ..repositories import UserRepository
from ..services import UserService
from ..views.api.routes import build_routes as api_build_routes
from ..views.frontend.routes import build_routes as frontend_build_routes


def create_app(config_mode: str = 'development') -> Flask:
    app = Flask(Config.NAME)
    app.config.from_object(Config)
    login_manager = SessionHelper.get_login_manager()

    CORS(app)
    init_db(app)
    login_manager.init_app(app)

    api_build_routes(app)
    frontend_build_routes(app)

    FlaskInjector(app=app, modules=[_bind])

    return app


def _bind(binder):
    user_repository = UserRepository(database=db)
    user_service = UserService(user_repository=user_repository)

    binder.bind(
        UserRepository,
        to=user_repository,
        scope=request,
    )

    binder.bind(
        UserService,
        to=user_service,
        scope=request,
    )
