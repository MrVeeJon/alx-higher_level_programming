#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Function that find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    big_int = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big_int:
            big_int = my_list[i]

    return (big_int)
