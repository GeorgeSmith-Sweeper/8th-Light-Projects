import unittest
from unittest import TestCase
from board import GameBoard
from board import create_board
from board import display_board
from board import update_board 

class TestBoardSize(TestCase):
    def test_create_board_makes_list_with_9_elements(self):
        create_board()
        self.assertEqual(GameBoard.the_board, [" ", " ", " ", " ", " ", " ", " ", " ", " "])

class TestBoardUpdate(TestCase):
    def test_update_board_places_X_on_index_0(self):
        spot = 1
        playerLetter = "X"
        update_board(spot, playerLetter)
        print(GameBoard.the_board)
        display_board()
        self.assertEqual(GameBoard.the_board, ["X", " ", " ", " ", " ", " ", " ", " ", " "])

if __name__ == "__main__":
    unittest.main()
