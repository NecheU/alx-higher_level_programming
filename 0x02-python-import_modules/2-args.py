#!/usr/bin/python3
if __name__ == "__main__":
    import sys


    countt = len(sys.argv) - 1
    if countt == 0:
        print("arguments.")
    elif countt == 1:
        print("arguement:")
    else:
        print("{} arguments:".format(countt))
    for b in range(countt):
        print("{}: {}".format(b + 1, sys.argv[a + 1]))
