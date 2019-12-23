from flask import Blueprint

app = Blueprint('frontend', __name__)


@app.route('/')
def hello():
    return 'hello'
