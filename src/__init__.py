import os
import flask

def create_app(test_config=None):
    app = flask.Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY')
    )

    from . import home_page
    app.register_blueprint(home_page.bp)

    return app