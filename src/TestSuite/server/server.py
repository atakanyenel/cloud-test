from .. import TestSuite
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/tests")
def hello():
    results = []
    for t in TestSuite.getTests():
        results.append(t.__str__())
    return jsonify(results=results)


def start():
    app.run()