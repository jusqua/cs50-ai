"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def unused_rooms(board):
    return [room for row in board for room in row].count(EMPTY)


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    return X if unused_rooms(board) % 2 == 1 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if i < 0 or j > 2 or board[i][j] != EMPTY:
        raise IndexError("Action cannot be performed: Invalid room")

    mark = player(board)
    state = deepcopy(board)
    state[i][j] = mark
    return state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for c in range(3):
        if board[c][0] != EMPTY and board[c][0] == board[c][1] and board[c][1] == board[c][2]:
            return board[c][0]
        elif board[0][c] != EMPTY and board[0][c] == board[1][c] and board[1][c] == board[2][c]:
            return board[0][c]

    if board[1][1] != EMPTY:
        for c in range(0, 3, 2):
            if board[0][c] == board[1][1] and board[1][1] == board[2][2 - c]:
                return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or unused_rooms(board) == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    mark = winner(board)
    if mark is None:
        return 0

    return 1 if mark == X else -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
