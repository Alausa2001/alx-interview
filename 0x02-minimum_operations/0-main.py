#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = -1
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 13
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))