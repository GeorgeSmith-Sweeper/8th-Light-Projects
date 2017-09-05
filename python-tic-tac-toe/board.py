class GameBoard:
    the_board = [] 

def create_board():
    GameBoard.the_board = [" "] * 9

def display_board():
    print(GameBoard.the_board[0], GameBoard.the_board[1], GameBoard.the_board[2])
    print("===", "===", "===")
    print(GameBoard.the_board[3], GameBoard.the_board[4], GameBoard.the_board[5])
    print("===", "===", "===")
    print(GameBoard.the_board[6], GameBoard.the_board[7], GameBoard.the_board[8])

create_board()
display_board()
