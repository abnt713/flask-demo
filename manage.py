from flask_script import Manager, Server
from app import app
from routes import set_routes

manager = Manager(app)
set_routes()

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

if __name__ == "__main__":
    manager.run()