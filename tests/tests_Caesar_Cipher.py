from coe_number.Caesar_Cipher import caesarCipher

import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_abcdefghijklmnopqrstuvwxyz_in_caesarcipher(self):
        x = 'abcdefghijklmnopqrstuvwxyz'
        result = caesarCipher(x, 3)
        self.assertEqual(result, 'defghijklmnopqrstuvwxyzabc')
        
    def test_hello_world_in_caesarcipher(self):
        x = 'hello world'
        result = caesarCipher(x, 5)
        self.assertEqual(result, 'mjqqt btwqi')
        
    def test_emptyString_in_caesarcipher(self):
        x = ''
        result = caesarCipher(x, 7)
        self.assertEqual(result, '')
        
    def test_singleLetterString_in_caesarcipher(self):
        x = 'a'
        result = caesarCipher(x, 4)
        self.assertEqual(result, 'e')
