import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text

app = Flask(__name__)

dbdir = "sqlite:///" + os.path.abspath((os.getcwd()) + "data.db")
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
engine = create_engine(dbdir)


@app.route("/count", methods=['GET'])
def count_simulations():
    try:
        with engine.connect() as conn:
            result = conn.execute(text('select COUNT(*) from Simulations'))
            for r in result:
                count_rows = r[0]
    except Exception as e:
        print('Error Connection: {}'.format(e))
        count_rows = "Error"
    data = {
        "Total": count_rows
    }
    return jsonify(data)


@app.route("/state", methods=['GET'])
def state():
    data = request.get_json()
    id_simulations = data['id']
    try:
        with engine.connect() as conn:
            result = conn.execute(text("select * from Simulations WHERE id_simulation = {}".format(id_simulations)))
            for r in result:
                count_rows = r[0]
                fixture = r[1]
    except Exception as e:
        print('Error Connection: {}'.format(e))
        count_rows = "Error"
    data = {
        "Id": count_rows,
        "fixture": fixture
    }
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
