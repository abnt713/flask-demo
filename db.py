__author__ = 'alisonbnt'

from flask_admin import Admin

from flask_admin.contrib.mongoengine import ModelView
from app import app
from models import *


def set_admin():
    admin = Admin(app, name='quotes', template_mode='bootstrap3')
    admin.add_view(ModelView(Quote))
