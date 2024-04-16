#!/usr/bin/python3

"""Python Input and Output
Python program to write a text in a file.
"""


def write_file(filename="", text=""):
    """Python to write on a file"""
    chr_count = 0
    with open(filename, 'w',  encoding='utf-8') as file:
        chr_count = file.write(text)

    return chr_count
