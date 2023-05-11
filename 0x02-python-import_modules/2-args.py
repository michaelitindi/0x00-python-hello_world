#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    number = len(args)

    if number == 0:
        print("{} arguments.".format(number))
    else:
        if number == 1:
            print("{} argument:".format(number))
        else:
            print("{} arguments:".format(number))
        for i in range(number):
            print("{} : {}".format(i + 1, args[i]))
