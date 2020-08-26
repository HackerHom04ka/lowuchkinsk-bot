from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask('lovushkinsk')

group_config = {
    "id": 193840305,
    "secret": "mjeynofbopn7t1j5aipm9ggxivjnxvq9",
    "confirm": os.environ['CONFIRM'],
    "token": "3a11ee2eef165b831ea31253e369bfd4377f12fee98dcfbc11054655de7538485133a773c55cb1521aaae"
}

app.config['DEBUG'] = False

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)