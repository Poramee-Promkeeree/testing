from coe_number.fizz_buzz import fizz_buzz

import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_3_in_FizzBuzz(self): 
        self.assertEqual(fizz_buzz(3), 'Fizz')

    def test_20_in_FizzBuzz(self):
        self.assertEqual(fizz_buzz(20), 'Buzz')

    def test_15_in_FizzBuzz(self):
        self.assertEqual(fizz_buzz(15), 'FizzBuzz')

    def test_7_not_in_FizzBuzz(self):
        self.assertIsNone(fizz_buzz(7))

    def test_zero_in_FizzBuzz(self):
        self.assertEqual(fizz_buzz(0), 'FizzBuzz')

