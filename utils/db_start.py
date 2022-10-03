from flask import Flask
from sqlalchemy import create_engine, text

app = Flask(__name__)


class DB_start:
    def __init__(self, dbdir: str):
        self.dbdir = dbdir
        app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.engine = create_engine(dbdir)

    def query(self, query: str):
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(query))
                for r in result:
                    count_rows = r[0]
                    print(count_rows)
        except Exception as e:
            print('Error Connection: {}'.format(e))
            count_rows = "Error"
        data = {
            "Result": count_rows
        }
        return data