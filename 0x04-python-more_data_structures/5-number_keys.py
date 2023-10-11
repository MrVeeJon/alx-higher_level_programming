#!/usr/bin/python3
# a function that returns the number of keys in a dictionary.
def number_keys(a_dictionary):
    num_key = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        num_key += 1

    return (num_key)
