print(__name__)
print(__package__)
from . import app

@app.route("/")
def home():
    return "Chatting WebPage"