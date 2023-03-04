from coe_number.staircase import staircase

import unittest

class TestStaircase(unittest.TestCase):
    def test_give_negative_1_to_staircase(self):
        # arrange
        n = -1
        pattern = '#'
        expected_output = ''

        # act
        result = staircase(n, pattern)

        # assert
        self.assertEqual(result, expected_output)

    def test_give_0_to_staircase(self):
        # arrange
        n = 0
        pattern = '#'
        expected_output = ''

        # act
        result = staircase(n, pattern)

        # assert
        self.assertEqual(result, expected_output)

    def test_give_1_to_staircase(self):
        # arrange
        n = 1
        pattern = '#'
        expected_output = '#'

        # act
        result = staircase(n, pattern)

        # assert
        self.assertEqual(result, expected_output)

    def test_give_5_to_staircase(self):
        # arrange
        n = 5
        pattern = '#'
        expected_output = '    #\n   ##\n  ###\n ####\n#####\n'

        # act
        result = staircase(n, pattern)

        # assert
        self.assertEqual(result, expected_output)

    def test_give_10_to_staircase(self):
        # arrange
        n = 10
        pattern = '*'
        expected_output = '         *\n        **\n       ***\n      ****\n     *****\n    ******\n   *******\n  ********\n *********\n**********\n'

        # act
        result = staircase(n, pattern)

        # assert
        self.assertEqual(result, expected_output)
