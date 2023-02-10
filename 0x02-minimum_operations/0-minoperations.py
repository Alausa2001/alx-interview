#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

    n = 9

    H => Copy All => Paste => HH => Paste =>HHH =>
    Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

    Number of operations: 6
"""


def minOperations(n):
    """calculates the fewest number of operations needed to
    reach a target length of a character if only one of that
    character is provided and all you can do is copy all and paste
    """
    chars = 1
    # target = n * 'H'
    last_copy_op = int()
    no_ops = 0
    while chars < n:
        if n % chars == 0:
            last_copy_op = chars
            chars *= 2
            no_ops += 2
        if n % chars != 0:
            chars += last_copy_op
            no_ops += 1
    return no_ops
