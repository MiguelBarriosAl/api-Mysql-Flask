import os
from flask import Flask, jsonify, request
from middleware import middleware
from utils.db_start import DB_start
from utils.queries import query_total_count, query_state

app = Flask(__name__)
dbdir = "sqlite:///" + os.path.abspath((os.getcwd()) + "data.db")

app.wsgi_app = middleware(app.wsgi_app)


@app.route("/count", methods=['GET'])
def count_simulations():
    db_start = DB_start(dbdir)
    query = query_total_count()
    data = db_start.query(query)
    return jsonify(data)


@app.route("/state", methods=['GET'])
def state():
    data = request.get_json()
    id_simulations = data['id']
    db_start = DB_start(dbdir)
    query = query_state(id_simulations)
    data = db_start.query(query)
    return jsonify(data)

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

if __name__ == "__main__":
    app.run('127.0.0.1', '5000', debug=True)
