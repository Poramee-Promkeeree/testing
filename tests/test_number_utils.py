from coe_number.number_utils import is_prime_list
import unittest


class PrimeListTest(unittest.TestCase):
    
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_11_17_19_is_prime(self):
        prime_list = [11, 17, 19]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_all_in_list_is_non_primes(self):
        prime_list = [2, 4, 6]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_even_composite_numbers(self):
        prime_list = [4, 6, 8 ]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_single_prime_number(self):
        prime_list = [5]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)





