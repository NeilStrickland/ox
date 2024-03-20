import matplotlib.pyplot as plt
import matplotlib.lines

__all__ = ['show_board', 'show_board_ascii']

def show_board(pq, winner=None):
    """Display the game state as an image using matplotlib.
    
    Args:
        pq (np.array): The game state
        winner: The player who has won the game (0 or 1), or None
           if the game is still in progress.

    Os are shown in red, Xs in blue.  If the winner is specified,
    the losing player's counters are shown in a lighter shade.
    """
    col_o = 'red'
    col_x = 'blue'
    if winner == 0: col_x = 'lightblue'
    if winner == 1: col_o = 'lightcoral'
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_axis_off()
    ax.set_xlim((0, 3))
    ax.set_ylim((0, 3))
    ax.add_line(matplotlib.lines.Line2D([1, 1], [0, 3], color='grey'))
    ax.add_line(matplotlib.lines.Line2D([2, 2], [0, 3], color='grey'))
    ax.add_line(matplotlib.lines.Line2D([0, 3], [1, 1], color='grey'))
    ax.add_line(matplotlib.lines.Line2D([0, 3], [2, 2], color='grey'))
    for i in range(3):
        for j in range(3):
            k = i+3*j
            if pq[k, 0] == 1:
                ax.add_patch(matplotlib.patches.Circle([i + 0.5, 2.5 - j], 0.3, color=col_o, fill=False))
            if pq[k, 1] == 1:
                ax.add_line(matplotlib.lines.Line2D([i + 0.2, i + 0.8], [2.8 - j, 2.2 - j], color=col_x))
                ax.add_line(matplotlib.lines.Line2D([i + 0.2, i + 0.8], [2.2 - j, 2.8 - j], color=col_x))

# This function prints an ASCII art representation of the specified game state
def show_board_ascii(pq, winner=None):
    """Display the game state as an ASCII art string.
    
    Args:
        pq (np.array): The game state
        winner: The player who has won the game (0 or 1), or None
           if the game is still in progress.

    Os are shown as 'O', Xs as 'X'.  If the winner is specified,
    the losing player's counters are shown in lower case.
    """
    sym_o = 'O'
    sym_x = 'X'
    if winner == 0: sym_x = 'x'
    if winner == 1: sym_o = 'o'
    s = '---\n'
    for j in range(3):
        for i in range(3):
            k = i+3*j
            t = '#'
            if pq[k, 0] == 1: t = sym_o
            if pq[k, 1] == 1: t = sym_x
            s = s + t
        s = s + '\n'
    s = s + '---'
    print(s)