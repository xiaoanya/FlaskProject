from flask_script import Manager
from flask import Flask
from blueapp.blueview import blue

app = Flask(__name__)
app.register_blueprint(blueprint=blue)

app.config['secret_key'] = '123456'

manager = Manager(app)



if __name__ == '__main__':
    manager.run()
