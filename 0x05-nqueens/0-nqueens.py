#!/usr/bin/python3
"""
N queens puzzle
"""


def isvalid(board, row, col, n):
    """
    checks if a position is safe for placing a value
    """
    for i in range(n):
        if board[row][i] == 'q':
            return False
    for j in range(n):
        if board[j][col] == 'q':
            return False
    for i in range(n):
        if row - i >= 0 and col - i >= 0 and board[row-i][col-i] == 'q':
            return False
        if row - i >= 0 and col + i < n and board[row-i][col+i] == 'q':
            return False
        if row + i < n and col - i >= 0 and board[row+i][col-i] == 'q':
            return False
        if row + i < n and col + i < n and board[row+i][col+i] == 'q':
            return False
    return True


def place(board, row, n):
    """
    places a quuen on a valid position
    It also handle printing the queen indices
    """
    if row == n:
        answer = []

        for i in range(n):
            queen_position = []
            for j in range(n):
                if board[i][j] == 'q':
                    queen_position.append(i)
                    queen_position.append(j)
            answer.append(queen_position)
        print(answer)
        return

    for col in range(n):
        if isvalid(board, row, col, n):
            board[row][col] = 'q'
            place(board, row + 1, n)
        # backtracking
        board[row][col] = '.'


def nqueens(n):
    """
    solution
    """
    board = [['.' for i in range(n)] for j in range(n)]
    place(board, 0, n)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)
    nqueens(n)
