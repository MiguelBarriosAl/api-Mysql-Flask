import datetime
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import ForeignKey

app = Flask(__name__)

dbdir = "sqlite:///" + os.path.abspath((os.getcwd()) + "/database.db")
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Simulations(db.Model):
    id_simulation = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(20))
    created_at = db.Column(db.DATETIME)
    updated_at = db.Column(db.DATETIME)


class Fixtures(db.Model):
    id_fixture = db.Column(db.Integer, primary_key=True)
    fixture = db.Column(db.String(100), ForeignKey("simulations.id_simulation"))
    created_at = db.Column(db.DATETIME,  onupdate=datetime.datetime.now)
    updated_at = db.Column(db.DATETIME, onupdate=datetime.datetime.now)


db.create_all()
