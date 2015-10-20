#!venv/bin/python
__author__ = 'alisonbnt'

from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config')

db = MongoEngine(app)


