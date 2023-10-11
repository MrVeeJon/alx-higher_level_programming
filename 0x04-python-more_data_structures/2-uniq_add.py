#!/usr/bin/python3
#  a function that adds all unique integers in a list
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    new_num = 0

    for i in uniq_list:
        new_num += i

    return (new_num)
