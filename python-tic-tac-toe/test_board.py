import unittest
from unittest import TestCase
from board import GameBoard
from board import create_board

class TestBoardSize(TestCase):
    def test_create_board_makes_list_with_9_elements(self):
        create_board()
        self.assertEqual(GameBoard.the_board, [None, None, None, None, None, None, None, None, None])
'''
 class TestDisplayBoard(TestCase):
     def test_display_board_shows_blank_board(self):
         self.assertEqual(display_board(), )
'''
if __name__ == "__main__":
    unittest.main()
