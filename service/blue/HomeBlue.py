from flask import Blueprint

app = Blueprint(__name__, __name__)


@app.route('/')
def index():
    return open('data/data.json', encoding='utf-8').read()
