#!/usr/bin/python3
"""
a program that solves the N queens problem.
"""

import sys


if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if num < 4:
    print("N must be at least 4")
    sys.exit(1)


def solveNQueens(n):
    """
    Places N non-attacking queens on an NxN chessboard.
    """
    col, pos, neg = set(), set(), set()
    current_board = [[] for n in range(n)]
    solved_board = []

    def backtrack(row):
        """
        Tool for solving constraint satisfaction problems.
        """
        if row == n:
            copy = current_board.copy()
            solved_board.append(copy)
            return

        for c in range(n):
            if c in col or (row + c) in pos or (row - c) in neg:
                continue

            col.add(c)
            pos.add(row + c)
            neg.add(row - c)

            current_board[row] = [row, c]

            backtrack(row + 1)

            col.remove(c)
            pos.remove(row + c)
            neg.remove(row - c)
            current_board[row] = []

    backtrack(0)

    return solved_board


if __name__ == "__main__":
    boards = solveNQueens(num)
    for board in boards:
        print(board)
