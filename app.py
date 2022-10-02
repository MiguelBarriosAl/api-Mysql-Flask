from flask import Flask

app = Flask(__name__)


@app.route("/")
def count_simulations():
    return "<p>Hello, World!</p>"


@app.route("/")
def state():
    return "<p>Hello, World!</p>"


@app.route("/")
def listing():
    return "<p>Hello, World!</p>"


@app.route("/")
def fixtures_id():
    return "<p>Hello, World!</p>"


@app.route("/")
def fixtures_info():
    return "<p>Hello, World!</p>"


@app.route("/")
def graph():
    return "<p>Hello, World!</p>"