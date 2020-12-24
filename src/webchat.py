# Entry point for the application.
import os

from . import app    # For application discovery by the 'flask' command.
app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY')
)

from . import home_page  # For import side-effects of setting up routes.
app.register_blueprint(home_page.bp)