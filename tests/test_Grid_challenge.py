from coe_number.Grid_challenge import gridChallenge

import unittest

class TestGridChallenge(unittest.TestCase):
    def test_give_exampleList_1_to_grid(self):
        lst = ['eabcd','fghij','olkmn','trpqs','xywuv']
        expected_output = 'YES'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')
        
    def test_sorted_rows_grid_to_grid(self):
        lst = ['abcde','fghij','klmno','pqrst','uvwxy']
        expected_output = 'YES'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')
        
    def test_single_row_grid_to_grid(self):
        lst = ['abcde']
        expected_output = 'YES'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')
        
    def test_single_column_grid_to_grid(self):
        lst = ['a','b','c','d','e']
        expected_output = 'YES'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output, f'Shoud be {expected_output}')
    
    def test_identical_rows_grid_to_grid(self):
        lst = ['aaaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaa']
        expected_output = 'YES'
        result = gridChallenge(lst)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    
