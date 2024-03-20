import numpy as np
from . import wins, eee, empty_board

def add_o(pq, i): pq[i, 0] = 1
def add_x(pq, i): pq[i, 1] = 1

def has_win(pq, player=None):
    """Check whether the game has been won.

    Args:
        pq (np.array): The game state
        player: The player to check for. Expected to be 0, 1 or None.
           player 0 is O and player 1 is X.

    Returns:
        bool: True if the specified player has won, False otherwise
        if player is None, returns True if either player has won
    """
    w = [np.max(np.matmul(wins, pq[:, j])) >= 3 for j in [0, 1]]
    if player is None:
        return w[0] or w[1]
    else:
        return w[player]

def plays(pq, player=0):
    """List the available moves for the next player.

    Args:
        pq (np.array): The game state
        player: The player to check for; not used in this function

    Returns:
        list: A list of integers in the range 0..8 representing 
           the places where no counter has yet been placed.
    """
    n = []
    for i in range(9):
        if pq[i, 0] == 0 and pq[i, 1] == 0:
            n.append(i)
    return n

def near_wins(pq, player=0):
    """List the moves that would win the game for the specified player.
    
    Args:
        pq (np.array): The game state
        player: The player to check for (0 or 1)

    Returns:
        list: A list of integers in the range 0..8 representing 
           the places where the specified player could play and 
           thereby complete a winning line.
    """
    n = []
    for i in range(9):
        if pq[i, 0] == 0 and pq[i, 1] == 0 and has_win(pq + eee[i, player], player):
            n.append(i)
    return n

def forks(pq, player=0):
    """List the moves that would create two near-wins for the specified player.
    
    Args:
        pq (np.array): The game state
        player: The player to check for (0 or 1)

    Returns:
        list: A list of integers in the range 0..8 representing 
           the places where the specified player could play and 
           thereby create two near-wins.
    """
    f = []
    for i in range(9):
        if pq[i, player] == 0 and pq[i, 1-player] == 0 and \
                len(near_wins(pq + eee[i, player], player)) > 1:
            f.append(i)
    return f

def swap(pq):
    """Swap the players in the game state.

    Args:
        pq (np.array): The game state

    Returns:
        np.array: The game state with the players swapped
    """
    return np.array(pq)[:,::-1]

def board_from_moves(moves):
    """Create a game state from a list of moves.
    
    Args:
        moves (list): A list of two lists, moves_o and moves_x, 
           representing the moves taken by the two players.
           These are expected to consist of integers in the 
           range 0..8, and no entries should appear in both lists.

    Returns:
        np.array: The game state as an array of shape (9, 2)
    """
    s = empty_board.copy()
    s[0, moves[0]] = 1
    s[1, moves[1]] = 1
    return s