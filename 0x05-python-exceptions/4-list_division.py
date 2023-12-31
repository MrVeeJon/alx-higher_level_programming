#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for i in range(list_length):
        try:
            list_div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            list_div = 0
        except ZeroDivisionError:
            print("division by 0")
            list_div = 0
        except IndexError:
            print("out of range")
            list_div = 0
        finally:
            n_list.append(list_div)
    return n_list
