import unittest

import os.path

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from models import data_simulations, DB_sqlite3

app = Flask(__name__)
dbdir = "sqlite:///" + os.path.abspath((os.getcwd()) + "/data.db")
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class InputData(unittest.TestCase):
    def setUp(self):
        self.dbdir = dbdir
        self.engine = create_engine(dbdir)

    def test_successful_input_data(self):
        data_test = [
            (1000, 'demo'),
            (2000, 'demo'),
            (3000, 'demo')]
        db_dbdir = DB_sqlite3(dbdir)
        result = db_dbdir.insert_data_simulations(data_simulations)
        self.assertEqual(bool, type(result))


