import datetime
import os.path
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import ForeignKey, insert, create_engine

"""
    Script to quickly create a small db to test 
    the different views created in the app.
    To do this, you only have to uncomment lines 126 to 130. 
    In this way you create the db locally and insert test data.
"""

app = Flask(__name__)
dbdir = "sqlite:///" + os.path.abspath((os.getcwd()) + "/data.db")
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Simulations(db.Model):
    id_simulation = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(100))
    created_at = db.Column(db.DATETIME, onupdate=datetime.datetime.now)
    updated_at = db.Column(db.DATETIME, onupdate=datetime.datetime.now)


class Fixtures(db.Model):
    id_fixture = db.Column(db.Integer,  ForeignKey("simulations.id_simulation"))
    fixture = db.Column(db.String(100), primary_key=True)
    created_at = db.Column(db.DATETIME, onupdate=datetime.datetime.now)
    updated_at = db.Column(db.DATETIME, onupdate=datetime.datetime.now)


class Loss(db.Model):
    id_loss = db.Column(db.Integer, primary_key=True)
    id_simulation = db.Column(db.Integer, ForeignKey("simulations.id_simulation"))
    seconds = db.Column(db.Integer())
    loss = db.Column(db.FLOAT(100))
    created_at = db.Column(db.DATETIME, onupdate=datetime.datetime.now)
    updated_at = db.Column(db.DATETIME, onupdate=datetime.datetime.now)


class DB_sqlite3:
    def __init__(self, dbdir: str):
        self.dbdir = dbdir
        self.engine = create_engine(dbdir)

    def insert_data_simulations(self, data: list):
        for d in data:
            try:
                with self.engine.connect() as conn:
                    query = insert(Simulations).values(
                        id_simulation=d[0],
                        state=d[1]
                    )
                    conn.execute(query)
                    print("Data Inserted", query)
                return True
            except Exception as e:
                print('Error Connection: {}'.format(e))
            finally:
                conn.close()

    def insert_data_fixtures(self, data: list):
        for d in data:
            try:
                with self.engine.connect() as conn:
                    query = insert(Fixtures).values(
                        id_fixture=d[0],
                        fixture=d[1]
                    )
                    conn.execute(query)
                print("Data Inserted", query)
            except Exception as e:
                print('Error Connection: {}'.format(e))
            finally:
                conn.close()

    def insert_data_loss(self, data: list):
        for d in data:
            try:
                with self.engine.connect() as conn:
                    query = insert(Loss).values(
                        id_loss=d[0],
                        id_simulation=d[1],
                        seconds=d[2],
                        loss=d[3]
                    )
                    conn.execute(query)
                print("Data Inserted", query)
            except Exception as e:
                print('Error Connection: {}'.format(e))
            finally:
                conn.close()


try:
    data_simulations = [
        (1, 'pending'),
        (2, 'pending'),
        (3, 'running'),
        (4, 'finished'),
        (5, 'finished')]

    data_fixtures = [
        (1, 'fixtures_001vwf'),
        (1, 'fixtures_002rtb'),
        (1, 'fixtures_003wer'),
        (2, 'fixtures_004qwe'),
        (2, 'fixtures_005owe'),
        (3, 'fixtures_006qrt'),
        (4, 'fixtures_007xqw'),
        (5, 'fixtures_008yuh'),
        (5, 'fixtures_009rth')]

    data_loss = [
        (1, 3, 10, 0.8),
        (2, 3, 40, 0.61),
        (3, 3, 70, 0.58),
        (4, 3, 100, 0.56),
        (5, 3, 130, 0.551),
        (6, 3, 160, 0.552),
        (7, 3, 190, 0.55)]
    """
    Uncomment the lines to create the base and enter the data
    """
    if not path.exists(os.path.abspath((os.getcwd()) + "/data.db")):
        db.create_all()
        db_dbdir = DB_sqlite3(dbdir)
        db_dbdir.insert_data_simulations(data_simulations)
        db_dbdir.insert_data_fixtures(data_fixtures)
        db_dbdir.insert_data_loss(data_loss)
    else:
        print('Database already created', dbdir)
except Exception as e:
    print('Error Connection: {}'.format(e))
