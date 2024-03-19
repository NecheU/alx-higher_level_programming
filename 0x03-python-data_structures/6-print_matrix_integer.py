#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for y in row:
            print("{:d}".format(y), end=" ")
        print(matrix)
