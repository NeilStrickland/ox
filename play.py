from . import empty_board, eee
from .analyse import add_o, add_x, has_win, plays
from .players import random_move

__all__ = ['play_game', 'step']

def play_game(player_o, player_x, return_moves=False):
    """Play a game of noughts and crosses (with player O starting).

    Args:
        player_o: A function that chooses moves for player O
          This should be a function like random_move, suggest_move
          or input_move, that accepts a game state and a player 
          index and returns an integer in the range 0..8.
        player_x: A function that chooses moves for player X
          This should be of the same form as player_o.
        return_moves: a boolean value which controls what 
          information is returned.

    Returns:
        If return_moves is False, returns a tuple (pq, winner)
          where pq is the final game state and winner is the 
          index of the winning player (0 for O, 1 for X, or None
          for a draw).  If return_moves is True, returns a tuple
          (pq, winner, moves) where moves is a list of two lists,
          moves_o and moves_x, representing the moves taken by 
          the two players.
    """
    pq = empty_board.copy()
    winner = None
    moves_o = []
    moves_x = []
    while True:
        if len(plays(pq)) == 0:
            break
        i = player_o(pq, 0)
        moves_o.append(i)
        if i is None or pq[i, 0] == 1 or pq[i, 1] == 1:
            winner = 1
            break
        add_o(pq, i)
        if has_win(pq, 0):
            winner = 0
            break
        if has_win(pq, 1):
            winner = 1
            break
        if len(plays(pq)) == 0:
            break
        i = player_x(pq, 1)
        moves_x.append(i)
        if i is None or pq[i, 0] == 1 or pq[i, 1] == 1:
            winner = 0
            break
        add_x(pq, i)
        if has_win(pq, 0):
            winner = 0
            break
        if has_win(pq, 1):
            winner = 1
            break
    if return_moves:
        return pq, winner, [moves_o, moves_x]
    else:
        return pq, winner

def step(pq, i, player=0):
    """Returns information intended for use when training a 
      neural network to play noughts and crosses.

    Args:
        pq (np.array): The game state
        i: The position where the specified player has chosen to play
        player: The player who has chosen to play (0 or 1)

    Returns:
        A tuple containing:
        - a boolean value to indicate whether the game has now finished
        - the reward
        - the new game state
        - the position where the opponent played, if applicable

    If it is illegal for the specified player to play in the specified
    position, the game ends with no change to the game state and a reward
    of -5.  Otherwise, we update the game state with the chosen move.
    If this does not lead to an immediate win and there is still some
    blank space, then we update again with a randomly selected move
    by the opponent.  The reward is now set to be +1 for a win, -1
    for a loss, and 0 if neither player has won.
    """
    if i is None or pq[i, 0] == 1 or pq[i, 1] == 1:
        return True, -5, pq, None
    pq1 = pq + eee[i, player]
    if has_win(pq1, player):
        return True, 1, pq1, None
    if len(plays(pq1)) == 0:
        return True, 0, pq1, None
    j = random_move(pq1, 1-player)
    pq2 = pq1 + eee[j, 1-player]
    if has_win(pq2, 1-player):
        return True, -1, pq1, j
    if len(plays(pq2)) == 0:
        return True, 0, pq2, j
    return False, 0, pq2, j
