#!/usr/bin/python3
def no_c(my_string):
    my_str = [item for item in my_string if item not in 'cC']
    return ("".join(my_str))
