import unittest
import super_algos
from unittest.mock import patch
from io import StringIO



class TestFunctions(unittest.TestCase):
    def test_find_min(self):
        my_list = [3,6,8,9,3,11]
        min_num = min(my_list)
        min_num_ = super_algos.find_min(my_list)
        self.assertEqual(min_num_,min_num)

    def test_sum_all(self):
        my_list = [1,2,3,4,5]
        sum_all = sum(my_list)
        sum_all_ = super_algos.sum_all(my_list)
        self.assertEqual(sum_all_,sum_all)
    
    def test_find_possible_strings(self):
        character_set = ["a","b"]
        test_re = ['aa', 'ab', 'ba', 'bb']
        n = 2
        results = super_algos.find_possible_strings(character_set, n)
        self.assertEqual(results,test_re)


