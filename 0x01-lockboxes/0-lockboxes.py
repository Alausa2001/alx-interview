#!/usr/bin/python3
"""You have n number of locked boxes in front of you. Each box is
numbered sequentially from 0 to n - 1 and each box may contain
keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False"""


def canUnlockAll(boxes):
    """returns True if all boxes can be unlocked else false"""
    if type(boxes) is not list:
        return false
    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    return (len(unlocked) == len(boxes))
