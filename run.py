#!venv/bin/python
__author__ = 'alisonbnt'

from app import app
from routes import set_routes
from db import set_admin

if __name__ == "__main__":
    set_routes()
    set_admin()
    app.run()
