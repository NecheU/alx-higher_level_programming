#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for m in row:
            print("{:3}".format(m), end="")
        print()
