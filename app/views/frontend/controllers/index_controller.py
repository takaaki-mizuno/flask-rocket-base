from flask import Blueprint, render_template

app = Blueprint('frontend', __name__)


@app.route('/')
def index():
    return render_template('pages/index.html', title="Flask")
