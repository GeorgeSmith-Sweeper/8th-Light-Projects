import unittest
from unittest import TestCase
from board import GameBoard
from board import create_board

class TestBoardSize(TestCase):
    def test_create_board_makes_list_with_9_elements(self):
        create_board()
        self.assertEqual(GameBoard.the_board, [None, None, None, None, None, None, None, None, None])

if __name__ == "__main__":
    unittest.main()
