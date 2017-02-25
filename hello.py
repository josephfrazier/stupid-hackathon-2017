from flask import Flask, request
import json

app = Flask(__name__)

def shock_logic(magnitude):
    return 'TODO'


@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"


@app.route("/shock", methods=['POST'])
def shock():
    payload = request.get_json()
    magnitude = payload['magnitude']
    shock_logic(magnitude)
    return 'Shocked with magnitude of {}'.format(magnitude)


if __name__ == "__main__":
    app.run()
