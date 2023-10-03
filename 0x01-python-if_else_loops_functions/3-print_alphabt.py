#!/usr/bin/python3
for lower_letter in range(97, 123):
    if chr(lower_letter) is not 'q' and chr(lower_letter) is not 'e':
        print("{}".format(chr(lower_letter)), end="")
