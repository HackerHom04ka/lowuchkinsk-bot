from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from vk_api import vk

app = Flask('lovushkinsk')

try:
    confirm = os.environ['CONFIRM']
except:
    confirm = '00000000'

group_config = {
    "id": 193840305,
    "secret": "",
    "confirm": confirm,
    "token": ""
}

app.config['DEBUG'] = False

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
try:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
except:
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

db = SQLAlchemy(app)

session = vk(group_config['token'])