#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    """Fucntion that returns the length of a string and its first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
