from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector, request

from ..config import Config
from ..database import db, init_db
from ..repositories import UserRepository
from ..services import UserService
from ..views.api.routes import app as api_app
from ..views.frontend.routes import app as frontend_app


def create_app(config_mode='development'):
    app = Flask(Config.NAME)
    app.config.from_object(Config)

    CORS(app)
    init_db(app)

    app.register_blueprint(api_app, url_prefix='/api/')
    app.register_blueprint(frontend_app, url_prefix='/')

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
