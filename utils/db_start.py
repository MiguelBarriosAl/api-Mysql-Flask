from flask import Flask
from sqlalchemy import create_engine, text

app = Flask(__name__)


class DB_start:
    def __init__(self, dbdir: str):
        self.dbdir = dbdir
        app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.engine = create_engine(dbdir)

    def query_sim(self, query: str):
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(query))
                for r in result:
                    rows = r[0]
        except Exception as e:
            print('Error Connection: {}'.format(e))
            rows = "Error"
        data = {
            "Result": rows
        }
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
            count_rows = "Error"
        data = {
            "Result": list_dict
        }
        return data