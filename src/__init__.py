import os
import flask
from flask_socketio import SocketIO

'''
def create_app(test_config=None):
    app = flask.Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY')
    )

    from . import home_page
    app.register_blueprint(home_page.bp)
    #socketio = SocketIO(app)
    #socketio.run(app)

    return app
'''

app = flask.Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY')
)

from . import home_page
app.register_blueprint(home_page.bp)

socketio = SocketIO(app)
socketio.run(app)
#if __name__ == '__main__':
    #socketio.run(app)
print(2)