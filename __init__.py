import numpy as np

__all__ = ['analyse', 'players', 'show', 'play', 'states']

def setup():
    global board, wins, ee, eee, corners, edges, opposite, empty_board

    board = range(9)

    wins = np.array([
        [1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0]
    ])

    # ee[i] is the vector of length 9 with a single 1 in position i
    # eee[i, j] is the array of shape (9, 2) with a single 1 in position (i, j)
    ee = np.eye(9)
    eee = np.zeros([9, 2, 9, 2])

    for i in range(9):
        for j in range(2):
            eee[i, j, i, j] = 1

    # corners[i] is 1 iff position i is a corner of the board
    # edges[i] is 1 iff position i is the middle of one edge of the board
    corners = np.array([1, 0, 1, 0, 0, 0, 1, 0, 1])
    edges   = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0])

    # opposite[i] is the position opposite position i
    opposite = [8, 7, 6, 5, 4, 3, 2, 1, 0]

    empty_board = np.zeros([9, 2])

setup()

from .analyse import near_wins, forks, swap, board_from_moves
from .show import show_board, show_board_ascii
from .players import random_move, suggest_move, input_move
from .play import play_game, step
from .states import make_all_states