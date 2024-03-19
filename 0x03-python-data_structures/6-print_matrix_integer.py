#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for y in row:
            print("{:d}".format(matrix[row][y]), end=" ")
        print()
