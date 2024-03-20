#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for h in range(len(matrix)):
        new_row = []
        for k in range(len(matrix[h])):
            new_row.append(matrix[h][k] ** 2)
        new_mat.append(new_mat)
    return new_mat
