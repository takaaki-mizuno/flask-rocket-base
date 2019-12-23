import unittest
from app.bootstrap import create_app
from app.config import Config
from flask_script import Manager

app = create_app()
manager = Manager(app)


@manager.command
def run():
    app.run(host=Config.APP_HOST, port=Config.APP_PORT)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
