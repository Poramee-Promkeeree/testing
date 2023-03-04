from coe_number.Funny_string  import funnyString

import unittest

class TestFunnyString(unittest.TestCase):
    def test_4554koko_in_FunnyString(self):
        x = '4554koko'
        result = funnyString(x)
        self.assertEqual(result, 'Not Funny')
        
    def test_zz_in_FunnyString(self):
        x = 'zz'
        result = funnyString(x)
        self.assertEqual(result, 'Funny')
        
    def test_numbers_in_FunnyString(self):
        x = '12345'
        result = funnyString(x)
        self.assertEqual(result, 'Funny')

    def test_ab_in_FunnyString(self):
        x = 'ab'
        result = funnyString(x)
        self.assertEqual(result, 'Funny')

