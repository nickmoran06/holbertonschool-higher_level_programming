#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
        else:
            print("{:d} ".format(i), end="")
    print("Buzz", end="")
