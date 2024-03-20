from . import empty_board, eee, ee
from .analyse import plays, has_win
from .players import suggest_move

__all__ = ['make_all_states', 'states', 'all_states', 'all_states_suggestions']

def make_all_states():
    """Set various global variables for all game states.

    states[i] is the list of all game states that could be seen
    by player 0 after i moves (with player 0 starting the game).  
    It only includes the states in which player 0 is required to
    respond; states are excluded if either player has already won.

    all_states is the union of all the states in states[i] for 
    i in 0..8.

    all_states_suggestions is the corresponding list of suggested
    moves, as computed by suggest_move.  In other words, if the
    suggestion for state all_states[i] is to play in position j,
    then all_states_suggestions[i] is the basis vector ee[j].
    """
    global states, all_states, all_states_suggestions
    all_states = []
    states = [[empty_board.copy()]]
    for i in range(1,9):
        states.append([])
        for s in states[i-1]:
            p = plays(s)
            k = 8
            while s[k, i % 2] == 0 and k >= 0: 
                k = k-1
            for j in p:
                s1 = s + eee[j, i % 2]
                if j > k and not has_win(s1):
                    states[i].append(s1)
        all_states += states[i]
    
    all_states_suggestions = list(map(
        lambda pq: ee[suggest_move(pq, 1)], 
        all_states
    ))

    return all_states
