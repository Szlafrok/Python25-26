import unittest
from funkcje import *

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 12), 17) # dwa wyrażenia są sobie równe
        self.assertNotEqual(add(4, 5), 10) # dwa wyrażenia są różne

        self.assertTrue(add(5, 6) == 11) # wyrażenie logiczne jest spełnione
        self.assertFalse(add(5, 7) == 18) # wyrażenie logiczne jest niespełnione

if __name__ == '__main__':
    unittest.main()