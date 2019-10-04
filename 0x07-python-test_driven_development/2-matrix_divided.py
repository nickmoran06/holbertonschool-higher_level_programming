#!/usr/bin/python3
def matrix_divided(matrix, div):
    lenght = None

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if lenght is None:
            lenght = len(row)
        elif lenght is not len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for line in row:
            if type(line) is not int and type(line) is not float:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    return list(list(round(line / div, 2) for line in row) for row in matrix)
