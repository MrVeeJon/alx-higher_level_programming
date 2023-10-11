#!/usr/bin/python3
# a function that computes the square value of all integers of a matrix.
def square_matrix_simple(matrix=[]):
    my_matrix = matrix.copy()
    for i in range(len(matrix)):
        my_matrix[i] = list(map(lambda x: x**2, matrix[i]))
    return (my_matrix)
