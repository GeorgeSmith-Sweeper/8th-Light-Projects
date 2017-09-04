import unittest
from unittest.mock import patch
from unittest import TestCase
from setup_prompts import SetupChoices
from setup_prompts import get_user_input 
from setup_prompts import user_choice 

class Test(TestCase):
    @patch('setup_prompts.get_user_input', return_value = 'X')
    def test_choice_X(self, input):
        self.assertEqual(user_choice(), 'X')
    @patch('setup_prompts.get_user_input', return_value = 'O') 
    def test_choice_O(self, input):
        self.assertEqual(user_choice(), 'O')
        
if __name__ == "__main__":
    unittest.main()
