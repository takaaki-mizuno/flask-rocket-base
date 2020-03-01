import unittest
import urllib.parse
from app.bootstrap import create_app
from app.config import Config
from app.database import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import url_for
import pytest

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('database', MigrateCommand)


@manager.command
def run():
    app.run(host=Config.APP_HOST, port=Config.APP_PORT)


@manager.command
def test():
    """Runs the tests."""
    pytest.main(["-s", "tests"])


@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


if __name__ == '__main__':
    manager.run()
