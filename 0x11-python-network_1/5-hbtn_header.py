#!/usr/bin/python3
"""Displaying the X-Request-Id header variable of a request to a taken url"""
import sys
import requests

if __name__ == "__main__":
    taken_url = sys.argv[1]

    req = requests.get(taken_url)
    print(req.headers.get("X-Request-Id"))
