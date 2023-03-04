from coe_number.Two_Characters import twoCharacter

import unittest

class TestTwoCharacter(unittest.TestCase):
    def test_repeated_characters_to_two_character(self):
        text = 'aaaaa'
        expected_output = 0
        result = twoCharacter(text)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    def test_single_character_to_two_character(self):
        text = 'a'
        expected_output = 0
        result = twoCharacter(text)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    def test_alternating_characters_to_two_character(self):
        text = 'ababab'
        expected_output = 6
        result = twoCharacter(text)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
        
    def test_give_longtext_187_to_two_character(self):
        text = 'tlymrvjcylhqifsqtyyzfaugtibkkghfhyzxqbsizkjguqlqwwetyofqihtpkmpdlgthfybfhhmjerjdkybwppwrdapirukcshkpngayrdruanjtziknnwxmsjpnuswllymhkmztsrcwwzmlbcoakswwffveobbvzinkhnmvwqhpfednhsuzmffaebi'
        expected_output = 0
        result = twoCharacter(text)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_beabeefeab_to_two_character(self):
        text = 'beabeefeab'
        expected_output = 5
        result = twoCharacter(text)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')