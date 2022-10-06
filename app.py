import os

from flask import Flask, jsonify, request
from sqlalchemy import insert
from middleware import middleware
from models import Simulations, Fixtures
from utils.db_start import DB_start
from utils.graphs import graphs
from utils.queries import query_total_count, query_by_state, query_graph_loss, query_order_by, query_list_fixtures

app = Flask(__name__)
dbdir = "sqlite:///" + os.path.abspath((os.getcwd()) + "data.db")
app.wsgi_app = middleware(app.wsgi_app)


@app.route("/count", methods=['GET'])
def count_simulations():
    db_start = DB_start(dbdir)
    query = query_total_count()
    data = db_start.query_sim("Total", query)
    return jsonify(data)


@app.route("/state", methods=['GET'])
def state():
    data = request.get_json()
    state = data['state']
    db_start = DB_start(dbdir)
    query = query_by_state(state)
    data = db_start.query_sim("State", query)
    return jsonify(data)


@app.route("/order_by/<term>", methods=['GET'])
def orderby(term):
    db_start = DB_start(dbdir)
    query = query_order_by(term)
    data = db_start.query_sim("Total", query)
    return jsonify(data)


@app.route("/fixtures", methods=['GET'])
def fixture():
    db_start = DB_start(dbdir)
    query = query_list_fixtures()
    data = db_start.query_fix(query)
    return jsonify(data)


@app.route("/insert", methods=['POST'])
def insert_data():
    data = request.get_json()
    id_simulations = data['id']
    state = data['state']
    fixture = data['fixture']
    insert(Simulations).values(
        id_simulation=id_simulations,
        state=state
    )
    insert(Fixtures).values(
        id_simulation=id_simulations,
        fixture=fixture
    )
    data = {
        "id Inserted": id_simulations
    }
    return jsonify(data)


@app.route("/graph", methods=['GET'])
def graph():
    data = request.get_json()
    id_simulations = data['id']
    db_start = DB_start(dbdir)
    query = query_graph_loss(id_simulations)
    data = db_start.query_loss(query)
    graphs(data['Result'])
    return jsonify(data)


if __name__ == "__main__":
    app.run('127.0.0.1', '5000', debug=True)

