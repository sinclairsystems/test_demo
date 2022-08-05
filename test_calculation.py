import unittest
import calculation

class MyTestCase(unittest.TestCase):

    def test_add(self):
        actual_result = calculation.add(5, 6)
        expected_result = 11
        self.assertEqual(expected_result, actual_result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
