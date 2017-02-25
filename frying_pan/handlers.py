from frying_pan.api import app
from frying_pan import logic
from flask import request


@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"


@app.route("/shock", methods=['POST'])
def shock():
    payload = request.get_json()
    magnitude = payload['magnitude']
    logic.shock(magnitude)
    return 'Shocked with magnitude of {}'.format(magnitude)
