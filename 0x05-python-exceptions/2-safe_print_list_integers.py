#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for k in range(x):
        try:
            if type(my_list[k]) == int:
                print("{:}".format(my_list[k], end''))
                counter += 1
        except IndexError:
            break
        print()
        return counter
