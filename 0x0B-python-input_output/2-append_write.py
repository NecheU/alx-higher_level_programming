#!/usr/bin/python3

"""Python Input and Output
Programm ti append a text to a file
"""


def append_write(filename="", text=""):
    """Python program to append a text in a file"""

    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)

    return len(text)
