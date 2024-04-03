#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_of_elem = 0
    try:
        while True:
            print(my_list[num_of_elem], end="")
            num_of_elem += 1
            if num_of_elem == x:
                break
    except IndexError:
        pass
    print()
    return num_of_elem
