import logging

from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector, request

from ..config import Config
from ..database import db, init_db
from ..repositories import JobFileRepository, JobRepository
from ..services import JobService, StorageService
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
    job_repository = JobRepository(db)
    job_file_repository = JobFileRepository(db)
    storage_service = StorageService()
    job_service = JobService(job_repository, job_file_repository,
                             storage_service)

    binder.bind(
        JobRepository,
        to=job_repository,
        scope=request,
    )

    binder.bind(
        JobFileRepository,
        to=job_file_repository,
        scope=request,
    )

    binder.bind(
        StorageService,
        to=storage_service,
        scope=request,
    )

    binder.bind(
        JobService,
        to=job_service,
        scope=request,
    )
