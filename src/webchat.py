# Entry point for the application.
from . import app    # For application discovery by the 'flask' command.

from . import home_page  # For import side-effects of setting up routes.
app.register_blueprint(home_page.bp)