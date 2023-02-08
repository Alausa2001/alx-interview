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
    var = 'H'
    target = n * 'H'
    prev = 'None'
    ops = 0
    while len(var) < len(target):
        if len(var) == 1:
            pre = var
            var *= 2
            ops += 2
        if len(target) % len(var) == 0 and n > 0:
            pre = var
            var *= 2
            ops += 2
        elif len(target) % len(var) != 0 and n > 0:
            var += pre
            ops += 1
    return ops
