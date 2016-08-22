#!/usr/bin python
# Battleship

from random import randint

board = []
opponent_board = []

for x in range(5):
    board.append(["O"] * 5)

for x in range(5):
    opponent_board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def print_opponent_board(opponent_board):
    for row in opponent_board:
        print " ".join(row)

#Introduction
print "============================="
print "====Welcome to Battleship===="
print "============================="
print "You are competing against a computer opponent"
print "Each player has a battleship on their respective boards"
print "Your objective is to guess the location of your opponents battleship"
print "You will be asked to guess a row and column"
print "Please keep your guess between 0 and 4"
print "You have 10 rounds of ammunition. Use them wisely!"
print "============================="
user_name = raw_input("What is your name? ")
opponent_name = raw_input("What would you like to name your opponent? ")
print "============================="
print "Hi " + str(user_name) + " Let's play Battleship!"
print "============================="
print "The Great Battle Between " + user_name + " And " + opponent_name
print "============================="
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#Opponents Ship Location
opponent_ship_row = random_row(opponent_board)
opponent_ship_col = random_col(opponent_board)

#User's Ship Location
user_ship_row = random_row(board)
user_ship_col = random_col(board)

print "Your Ship is located at: (" + str(user_ship_row) + "," + str(user_ship_col) + ")"

#Time For Battle
for turn in range(10):

#User's Turn
    print ""
    print user_name + "'s Shot"
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == opponent_ship_row and guess_col == opponent_ship_col:
        print "Congratulations! You sunk opponent's battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed opponent's battleship!"
            board[guess_row][guess_col] = "X"
        print "Round", turn + 1
        print_board(board)
        if turn == 10:
            print "Game Over"


#Opponent's Turn
    print ""
    print opponent_name + "'s Shot"
    opponent_guess_row = randint(0, len(board) - 1)
    opponent_guess_col = randint(0, len(board) - 1)
    if opponent_guess_row == user_ship_row and opponent_guess_col == user_ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (opponent_guess_row < 0 or opponent_guess_row > 4) or (opponent_guess_col < 0 or opponent_guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[opponent_guess_row][opponent_guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            opponent_board[opponent_guess_row][opponent_guess_col] = "X"
        print "Round", turn + 1
        print "Opponent Guessed: " + "(" + str(opponent_guess_row) + "," + str(opponent_guess_col) + ")"
        print_board(opponent_board)
        if turn == 10:
            print "Game Over"

print opponent_name + "'s Ship was located at: (" + str(opponent_ship_row) + "," + str(opponent_ship_col) + ")"
