#!/usr/bin/python3

"""Print the alphabet in lowercase, not followed by a new line."""
for lower_letter in range(97, 123):
    print("{}".format(chr(lower_letter)), end="")
