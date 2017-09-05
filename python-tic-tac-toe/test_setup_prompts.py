import unittest
from unittest.mock import patch
from unittest import TestCase
from setup_prompts import SetupChoices
from setup_prompts import user_letter_choice 
from setup_prompts import who_goes_first
from setup_prompts import game_mode_selection

class Test(TestCase):
    @patch('setup_prompts.get_user_input', return_value = 'X')
    def test_choice_X(self, input):
        self.assertEqual(user_letter_choice(), 'X')
    @patch('setup_prompts.get_user_input', return_value = 'O') 
    def test_choice_O(self, input):
        self.assertEqual(user_letter_choice(), 'O')
    
    @patch('setup_prompts.who_goes_first', return_value = "1")
    def test_player_1_goes_first(self, input):
        self.assertEqual(who_goes_first(), "1")
    
    @patch('setup_prompts.who_goes_first', return_value = "2")
    def test_player_2_goes_first(self, input):
        self.assertEqual(who_goes_first(), "2")
    
    @patch('setup_prompts.game_mode_selection', return_value = "1")
    def test_game_mode_selection_1_returns_playerVplayer(self, input):
        self.assertEqual(game_mode_selection(), "Player V Player")

    @patch('setup_prompts.game_mode_selection', return_value = "2")
    def test_game_mode_selection_2_returns_playerVcomputer(self, input):
        self.assertEqual(game_mode_selection(), "Player V Computer")
    
    @patch('setup_prompts.game_mode_selection', return_value = "3")
    def test_game_mode_selection_3_returns_computerVcomputer(self, input):
        self.assertEqual(game_mode_selection(), "Computer V Computer")

if __name__ == "__main__":
    unittest.main()
