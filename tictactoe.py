# https://fellowship.hackbrightacademy.com/materials/serft13/exercises/oo-practice-melons/

class Player:

    def __init__(self, name):
        self.player = name


class Move:
    pass


class Board:

    def __init__(self):
        self.board_placement = {1: ' X ', 2: ' X ', 3: " X ", 4: " X ",
                                5: " X ", 6: " X ", 7: " X ", 8: " X ", 9: " X "}

    def display(self):
        board_keys = list(self.board_placement.keys())
        board_keys.sort()
        # [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print("------------")
        for board_key in board_keys:
            print(f"|{self.board_placement[board_key]}", end="")
            if board_key % 3 == 0:
                print("|")
                print("------------")

    def add_move(self, move, letter):
        self.board_placement[move] = letter


class Game:

    def play_game(self):
        self.player1_name = input('Player 1, input your name: ')
        self.player2_name = input('Player 2, input your name: ')

        player1 = Player()
        player2 = Player()
        board = Board()

        while True:
            board.display()
            player1.add_move()


board.add_move(1, " O ")
board.display()

# if __name__ == '__main__':


# Set up players
# Ask Player 1 name, assign x
# Ask Player 2 name, assign o

# Play game: loop --> game starts
# Show board
# Player 1 move
# Ask Player 1 where to place x
# Check if move is possible
# If not possible --> try again
# If possible --> break
# Show board
# Check for win
# if win conditions met --> break
# Check if board is full
# if yes --> break
# Player 2 move
# Ask Player 2 where to place o
# Check if move is possible
# If not possible --> try again
# If possible --> break
# Show board
# Check for win
# if win conditions met --> break
# Check if board is full
# if yes --> break

# when loop breaks --> game ends
# Announce winner OR draw
# Ask if play again


# 1 2 3
# 4 5 6
# 7 8 9

# move dictionary: key = name of square, value = blank, x, o

# board = {1: 'blank', 2: 'blank', 3:"X"}


# iterate through board dictionary
# turn keys into list
# sort list
# for loop through sorted list
# print corresponding value (X, O, or blank): " X |"
# if key % 3 == 0
# print ------

""""
------------
|   | O | X |
------------
| X | O | X |
------------
| X | O | X |
------------
"""
