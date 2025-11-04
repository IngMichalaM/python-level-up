#  Write a Python function to find all prime factors
from typing import List
import unittest


def smallest_prime_number(n: int) -> int:
    """ Returns the smallest prime number of n. """

    for i in range(2, n + 1):
        if n % i == 0:
            return i


def get_prime_factor(n: int) -> List[int]:
    prime_factors = []

    while n > 1:
        current_factor = smallest_prime_number(n)
        prime_factors.append(current_factor)
        n = n // current_factor

    return prime_factors


class TestFindPrimeNumber(unittest.TestCase):
    def test_smallest_prime_number(self):
        self.assertEqual(5, smallest_prime_number(5))
        self.assertEqual(3, smallest_prime_number(15))
        self.assertEqual(53, smallest_prime_number(53))


class TestGetPrimeFactor(unittest.TestCase):
    def test_get_prime_factor_prime_number(self):
        self.assertEqual([5], get_prime_factor(5))

    def test_get_prime_factor_repeated_output_numbers(self):
        self.assertEqual([2, 5, 5, 5], get_prime_factor(250))

    def test_get_prime_factor_given_example_630(self):
        self.assertEqual([2, 3, 3, 5, 7], get_prime_factor(630))

    def test_get_prime_factor_given_example_13(self):
        self.assertEqual([13], get_prime_factor(13))


if __name__ == '__main__':
    unittest.main()