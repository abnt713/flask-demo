__author__ = 'alisonbnt'

from app import db


class Quote(db.Document):
    author = db.StringField()
    message = db.StringField()