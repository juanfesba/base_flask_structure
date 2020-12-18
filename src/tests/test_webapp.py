from src import routing
import unittest

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(routing.home(), 4)

if __name__ == '__main__':
    unittest.main()