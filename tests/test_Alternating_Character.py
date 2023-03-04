from coe_number.Alternating_Characters import AlternatingCharacter

import unittest

class TestAlternatingCharacter(unittest.TestCase):
    def test_BABABA_in_alternating(self):
        x = 'BABABA'
        result = AlternatingCharacter(x)
        self.assertEqual(result, 0)
        
    def test_ABAABBAABBABA_in_alternating(self):
        x = 'ABAABBAABBABA'
        result = AlternatingCharacter(x)
        self.assertEqual(result, 4)
        
    def test_BBBB_in_alternating(self):
        x = 'BBBB'
        result = AlternatingCharacter(x)
        self.assertEqual(result, 3)
    
    def test_ABABABAB_in_alternating(self):
        x = 'ABABABAB'
        result = AlternatingCharacter(x)
        self.assertEqual(result, 0)

    