import json
from flask import Flask, request, Response, jsonify

app = Flask(__name__)


@app.route("/")
def input_example():
    dictinput = request.get_json()
    resp = Response(json.dumps(dictinput))
    resp.headers['Content-Type'] = 'application/json'
    return resp


@app.route("/jsonify")
def input_example_jsonify():
    dictinput = request.get_json()
    return jsonify(dictinput), 200


app.run("localhost", 8080)
