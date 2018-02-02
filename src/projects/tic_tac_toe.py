# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 11:41:33 2017

Tic Tac Toe developped based on the instruction from the Harvard online class:
    PH526x Using Python for Research Harvard class

@link https://courses.edx.org/courses/course-v1:HarvardX+PH526x+3T2016/info
@author: Sylhare

"""

import numpy
import random
import time
import matplotlib.pyplot as plt


def create_board():
    """
    Returns an 3x3 matrix (numpy.array) full of zeros

    """
    return numpy.zeros(shape=(3, 3))


def place(board, player, position):
    """
    Place the value of the player (1 or 2) at the position (x, y) in the board
    board is a numpy.array

    Returns the modified board

    """
    if board[position] == 0:
        board[position] = player
    else:
        print("player {} is already on that position".format(board[position]))


def possibilities(board):
    """
    Check for possibile empty position in the board
    if board[(x, y)] == 0 then (x, y) an empty position

    Returns a list of tuples: [(x1, y1), (x2, y2), ...]

    """
    (x, y) = numpy.where(board == 0)  # returns a tuple of 2 arrays ([x's], [y's])
    p = [(x[i], y[i]) for i in range(0, len(x))]  # creates a list of (x, y)

    return p


def random_place(board, player):
    """
    An empty position in the board is randomly filler with player (1 or 2)

    Returns the modified board

    """
    p = possibilities(board)
    place(board, player, p[random.randint(0, len(p) - 1)])

    return board


def row_win(board, player):
    """
    Check if a player is 3 times on the same row,

    Returns True if player wins, False otherwise

    """

    for i in range(0, 3):
        j = 0
        while board[i, j] == player:
            j += 1
            if j == 3:
                return True

    return False


def col_win(board, player):
    """
    Transpose the board so the column are now rows and then use the row_win
    method.

    Returns True if player wins, False otherwise

    """
    board = numpy.transpose(board)
    return row_win(board, player)


def diag_win(board, player):
    """
    Check the two diagonals for player.

    Returns True if player wins, False otherwise

    """
    if board[0, 0] == board[1, 1] == board[2, 2] == player:
        return True
    elif board[0, 2] == board[1, 1] == board[2, 0] == player:
        return True
    else:
        return False


def evaluate(board):
    """
    Evaluate the board for a potential winner,
    i.e. rows or colunms or diagonals contains 3 times the same player

    Returns -1 for a draw,
             1 for player 1's victory,
             2 for player 2's victory.

    """
    score = 0

    for player in [1, 2]:
        if (row_win(board, player)
                or col_win(board, player)
                or diag_win(board, player)):
            score = player

    if numpy.all(board != 0) and score == 0:
        score = -1

    return score


def play_game():
    """
    Player 1 starts to play, each player plays randomly.

    Returns the score, see evaluate().

    """
    board = create_board()
    win = evaluate(board)

    while win == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            win = evaluate(board)
            if win != 0:
                break

    return win


def play_strategic_game():
    """
    Player 1 starts to play, each player plays randomly.
    First move of player 1 is to go in the middle (1,1)

    Returns the score, see evaluate()

    """
    board, win = create_board(), 0
    board[1, 1] = 1

    while win == 0:
        for player in [2, 1]:
            board = random_place(board, player)
            win = evaluate(board)
            if win != 0:
                break
    return win


def test_play(func, games=1000):
    """
    Play multiple games with the specified fonction in the tic tac toe:
        - play_game()
        - play_startegic_game()

    Returns a list with all the games' scores

    """
    scores = []

    t = time.time()
    for i in range(0, games):
        scores.append(func())
    t = time.time() - t

    print("Execution's time: {} of {}".format(t, func))

    return scores


# -- Demo -- #
sp1 = plt.subplot(121)
plt.title('play_game')
plt.hist(test_play(play_game))

plt.subplot(122, sharey=sp1)
plt.title('play_strategic_game')
plt.hist(test_play(play_strategic_game), facecolor='green')
plt.show()
