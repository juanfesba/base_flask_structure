import unittest

from flask import render_template
from src import app, home_page

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        with app.test_request_context(): #with app.app_context(), app.test_request_context():
            self.assertEqual(home_page.home(), render_template("home_page.html", name=None))

if __name__ == '__main__':
    unittest.main()
