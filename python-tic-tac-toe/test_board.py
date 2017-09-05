import unittest
from unittest import TestCase
from board import GameBoard

class TestBoardSize(TestCase):
    def test_the_board_is_an_empty_list_inititally(self):
        self.assertEqual(GameBoard.the_board, [])

if __name__ == "__main__":
    unittest.main()
