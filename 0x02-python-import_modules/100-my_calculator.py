#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    a = int(argv[1])
    b = int(argv[3])
    math_func = [add, sub, mul, div]
    math_oper = ["+", "-", "*", "/"]

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    else:
        for i, operat in enumerate(math_oper):
            if argv[2] == operat:
                print("{} {} {} = {}".format(a, operat, b, math_func[i](a, b)))
                break
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            quit(1)
