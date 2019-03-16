from .. import TestSuite
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/tests")
def hello():
    return jsonify(results=getTests())


@app.route("/rerun", methods=["POST"])
def rerun():
    TestSuite.rerun()
    return jsonify(results=getTests())


def getTests():
    results = []
    for t in TestSuite.getTests():
        results.append({
            "name": t.name, "status": t.status, "elapsed": t.elapsed})
    return results


def start():
    app.run()
