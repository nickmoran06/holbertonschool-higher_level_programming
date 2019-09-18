#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(0, len(matrix)):
        for line in range(0, len(matrix[row])):
            if line == (len(matrix[row]) - 1):
                print("{:d}".format(matrix[row][line]), end="")
            else:
                print("{:d}".format(matrix[row][line]), end=" ")
        print()
