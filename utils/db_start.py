from flask import Flask
from sqlalchemy import create_engine, text

app = Flask(__name__)


class DB_start:
    def __init__(self, dbdir: str):
        self.dbdir = dbdir
        app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.engine = create_engine(dbdir)

    def query_sim(self, key, query) -> list:
        rows = []
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(query))
                for row in result:
                    data = data_output(key, row)
                    rows.append(data)
                return rows
        except Exception as e:
            print('Error Connection: {}'.format(e))
            rows = ["Error"]
        data = rows
        return data

    def query_fix(self, query) -> list:
        rows = []
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(query))
                for row in result:
                    data = {
                        "id_simulation": row[0],
                        "fixture": row[1]
                    }
                    rows.append(data)
                return rows
        except Exception as e:
            print('Error Connection: {}'.format(e))
            rows = ["Error"]
        data = rows
        return data

    def query_loss(self, query: str):
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(query))
                list_dict = []
                for r in result:
                    seconds = r[0]
                    loss = r[1]
                    data = {
                        "seconds": seconds,
                        "loss": loss
                    }
                    list_dict.append(data)

        except Exception as e:
            print('Error Connection: {}'.format(e))
            list_dict = {"Error"}
        data = {
            "Result": list_dict
        }
        return data


def data_output(key: str, row: str) -> dict:
    key = "{}".format(key)
    return {
        key: row[0]
    }


def data_by_state(row: tuple) -> dict:
    return {
        "Simulations_id": row[0],
        "State": row[1]
    }


def data_output_loss(row: tuple) -> dict:
    return {
        "seconds": row[0],
        "loss": row[1]
    }
