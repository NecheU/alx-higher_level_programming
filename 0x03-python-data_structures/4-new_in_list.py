#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list[:]
    elif idx >= my_list:
        return my_list[:]
    else:
        my_list[idx] = element
