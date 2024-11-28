import unittest
import numpy as np
from project1 import normal_distribution_array, solve_cramers_rule, generate_and_index

class TestProject1(unittest.TestCase):
    def test_normal_distribution_array(self):
        result = normal_distribution_array((2, 2), 0, 1)
        self.assertEqual(result.shape, (2, 2))
    
    def test_solve_cramers_rule(self):
        coeffs = [[2, -1], [1, 1]]
        constants = [1, 3]
        self.assertEqual(solve_cramers_rule(coeffs, constants), [2, 1])
    
    def test_generate_and_index(self):
        shape = (2, 3)
        array, evens, odds = generate_and_index(shape)
        self.assertEqual(array.shape, shape)
        self.assertTrue(all(array[tuple(idx)] % 2 == 0 for idx in evens))
        self.assertTrue(all(array[tuple(idx)] % 2 != 0 for idx in odds))

if __name__ == "__main__":
    unittest.main()

