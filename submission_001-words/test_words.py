import unittest
import word_processor

class TestFunctions(unittest.TestCase):
    def test_convert_to_word_list_function(self):
        text = 'These are indeed interesting, an obvious understatement, times. What say you?'
        results = word_processor.convert_to_word_list(text)
        expected_results = ['these','are','indeed','interesting','an','obvious','understatement','times','what','say','you']
        self.assertEqual(results, expected_results)

    def test_words_longer_than(self):
        text = 'These are indeed interesting, an obvious understatement, times. What say you?'
        results = word_processor.words_longer_than(10, text)
        expected_results = ['interesting','understatement']
        self.assertEqual(results, expected_results) 
        
    def test_words_lengths_map(self):
        text = 'These are indeed interesting, an obvious understatement, times. What say you?'
        results = word_processor.words_lengths_map(text)
        expected_results = {2: 1, 3: 3, 4: 1, 5: 2, 6: 1, 7: 1, 11: 1, 14: 1}
        self.assertEqual(results,expected_results)
    
    def test_letters_count_map(self):
        text = 'These are indeed interesting, an obvious understatement, times. What say you?'
        results = word_processor.letters_count_map(text)
        expected_results = {'a':5, 'b': 1, 'c':0, 'd': 3, 'e': 11, 'f': 0, 'g':\
             1, 'h': 2, 'i': 5, 'j': 0, 'k': 0, 'l': 0, 'm': 2, 'n': 6, 'o': 3, 'p':\
                  0, 'q': 0, 'r': 3, 's': 6, 't': 8, 'u': 3, 'v': 1, 'w': 1, 'x': 0, 'y': 2, 'z': 0}
        self.assertEqual(results,expected_results)
    
    def test_most_used_character(self):
         text = 'These are indeed interesting, an obvious understatement, times. What say you?'
         results = word_processor.most_used_character(text)
         expected_results = "e"
         self.assertEqual(results, expected_results)
