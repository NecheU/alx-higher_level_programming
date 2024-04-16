#!/usr/bin/python3

"""Python Input and Output
Python program to read text from a file
"""


def read_file(filename=""):
    """Python program to open and read from a file"""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
