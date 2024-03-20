import numpy as np
import time
from . import eee
from .analyse import has_win, near_wins, forks, plays, swap
from .show import show_board_ascii

__all__ = ['random_move', 'suggest_move', 'input_move']

def random_move(pq, player=0):
    """Choose a random move for the specified player.
    
    Args:
        pq (np.array): The game state
        player: The player to choose a move for; not used in this function

    Returns:
        If one of the players has already won, or if the board is full,
        returns None.  Otherwise, returns an integer in the range 0..8
        representing a randomly chosen position which is currently empty.
    """
    if has_win(pq) or len(plays(pq)) == 0:
        return None
    return np.random.choice(plays(pq, player))

def suggest_move(pq, player):
    """Suggest a move for the specified player in the specified game state.
    
    Args:
        pq (np.array): The game state
        player: The player to suggest a move for (0 or 1)

    Returns:
        If one of the players has already won, or if the board is full,
        returns None.  Otherwise, returns an integer in the range 0..8
        representing a suggested move for the specified player.
        The suggestions are optimal in the sense that a win or draw is 
        guaranteed if the suggestions are followed throughout the game.  
    """
    if player == 0:
        pq0 = pq.copy()
        qp0 = swap(pq0)
    else:
        qp0 = pq.copy()
        pq0 = swap(qp0)
    if has_win(pq0) or len(plays(pq0)) == 0:
        return None
    n = near_wins(pq0)
    if len(n) > 0: return n[0]
    m = near_wins(qp0)
    if len(m) > 0: return m[0]
    f = forks(pq0)
    if len(f) > 0: return f[0]
    g = forks(qp0)
    if len(g) == 1: return g[0]
    for i in g:
        pq1 = pq0 + eee[i, 0]
        qp1 = swap(pq1)
        if len(near_wins(pq1)) > 0 and len(forks(qp1)) > 0:
            return i
    if pq0[4, 0] == 0 and pq0[4, 1] == 0: return 4
    for i in [0, 2, 6, 8]:
        if pq0[i, 0] == 0 and pq0[i, 1] == 0 and pq0[8-i, 1] == 1:
            return i
    for i in [0, 2, 6, 8, 1, 3, 5, 7]:
        if pq0[i, 0] == 0 and pq0[i, 1] == 0:
            return i
    return None

def input_move(pq, player=0):
    """Prompt the user to enter a move for the specified player.

    Args:
        pq (np.array): The game state
        player: The player to prompt for (0 or 1)

    Returns:
        An integer in the range 0..8 representing the position
        where the specified player has chosen to play.  If the
        user enters a string that cannot be interpreted as an
        integer in this range, the function returns None.
        No checks are made to ensure that the chosen position
        is empty.
    """
    if player == 0:
        s = 'O'
    else:
        s = 'X'
    show_board_ascii(pq)
    time.sleep(1)
    prompt = 'Enter position (0-8) for next ' + s + ': '
    i = input(prompt)
    try:
        i = int(i)
    except ValueError:
        return None
    if i < 0 or i > 8:
        i = None
    return i

