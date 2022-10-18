#!/usr/bin/python3
"""program that solves the N queens problem
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard
"""
from sys import argv


if __name__ == '__main__':
    """solves the N queens problem"""
    ac = len(argv)
    if ac != 2:
        print("Usage: nqueens N")
        exit(1)
    elif argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    elif int(argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    a = []
    size = int(argv[1])

    # initializes the answer list
    for i in range(size):
        a.append([i, None])

    def already_exists(y):
        """checks that a queen does not exist in y value"""
        for x in range(size):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y):
        """determines whether or not to reject the solution"""
        if (already_exists(y)):
            return False
        i = 0
        while (i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """clears the answers from the point of failure"""
        for i in range(x, size):
            a[i][1] = None

    def nqueens(x):
        """recursive backtracking function to find the solution"""
        for y in range(size):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if (x == size - 1):  # accepts the solution
                    print(a)
                else:
                    nqueens(x + 1)  # moves on to next x value to continue

    # starts the recursive process at 0
    nqueens(0)
