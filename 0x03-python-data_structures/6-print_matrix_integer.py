#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for m in row:
            print("{:d}".format(m), end=' ')
        print()
