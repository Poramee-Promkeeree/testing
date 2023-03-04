from coe_number.cat_and_mouse import cat_and_mouse

import unittest

class TestCatMouse(unittest.TestCase):

    def test_1_2_3_in_CatMouse(self): 
        result = cat_and_mouse(1,2,3)
        self.assertEqual(result, 'Cat B')
        
    def test_5_2_8_in_CatMouse(self):
        result = cat_and_mouse(5,2,8)
        self.assertEqual(result, 'Cat A')
        
    def test_1_1_2_in_CatMouse(self):
        result = cat_and_mouse(1,1,2)
        self.assertEqual(result, 'Cat B')
        
    def test_10_5_15_in_CatMouse(self):
        result = cat_and_mouse(10,5,15)
        self.assertEqual(result, 'Mouse C')
