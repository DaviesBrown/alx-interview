#!/usr/bin/python3
"""
rotate 2d matrix
"""


def rotate_2d_matrix(matrix):
    """ rotate 2d matrix"""
    new_matrix = [tuple(i) for i in matrix]
    mat_len = len(matrix)
    length = mat_len - 1
    for i in range(mat_len):
        print(length)
        for j in range(len(matrix[i])):
            matrix[i][j] = new_matrix[length][i]
            length -= 1
        length = mat_len - 1
