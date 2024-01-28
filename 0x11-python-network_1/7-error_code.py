#!/usr/bin/python3
"""displays the body of the response
    after sending a request to the URL
"""
import sys
import requests

if __name__ == "__main__":
    taken_url = sys.argv[1]

    req = requests.get(taken_url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
