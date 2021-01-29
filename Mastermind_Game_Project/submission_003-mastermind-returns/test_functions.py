import unittest
import mastermind
from unittest.mock import patch
from io import StringIO


class TestFunctions(unittest.TestCase):


    def test_create_code(self):
        for i in range(100):
            code = mastermind.create_code()
            self.assertEqual(len(code),4)
            for x in code:
                self.assertNotEqual(x,0)
                self.assertNotEqual(x,9)


    def test_check_correctness(self):
        turns = 1
        correct = False
        
        correct_digits_and_position = 0
        
        x = correct_digits_and_position
        while x < 9:
            
            if x == 4:
                correct = mastermind.check_correctness(turns, correct, x)
                self.assertTrue(correct)
            else:
                correct = mastermind.check_correctness(turns, correct, x)
                self.assertFalse(correct)
            x += 1

  
    @patch("sys.stdin", StringIO("1234\n1234\n"))
    def test_get_answer_input(self):

        answer = mastermind.get_answer_input()
        self.assertEqual(type(answer), str)
        self.assertEqual(len(answer), 4)


    @patch("sys.stdin", StringIO("1234\n1234\n1234\n1234\n"))
    def test_take_turn_vs_user_input(self):
    
        answer = mastermind.take_turn([1,2,3,4])
        self.assertEqual(answer,(4,0))
        answer = mastermind.take_turn([1,2,3,5])
        self.assertEqual(answer,(3,0))
        answer = mastermind.take_turn([1,2,4,3])
        self.assertEqual(answer,(2,2))
        answer = mastermind.take_turn([4,3,2,1])
        self.assertEqual(answer,(0,4))
        