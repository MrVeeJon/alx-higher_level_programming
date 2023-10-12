#!/usr/bin/python3
# a function that prints a dictionary by ordered keys.
def print_sorted_dictionary(a_dictionary):
    key_ord = list(a_dictionary.keys())
    key_ord.sort()
    for i in key_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))
