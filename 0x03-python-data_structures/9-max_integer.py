#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    max_n = my_list[0]
    for nbr in my_list:
        if nbr > max_n:
            max_n = nbr
    return (max_n)
