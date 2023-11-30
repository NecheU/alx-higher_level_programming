#!/usr/bin/python3

#importing funtion add with from
#to perforn addition operation of two numbers

if __name__ == "__main__":
    from add_0.py import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
