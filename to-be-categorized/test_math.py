import unittest
import math


class TestMath(unittest.TestCase):

    def test_add(self):
        result = math.add(10, 5)
        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main()
