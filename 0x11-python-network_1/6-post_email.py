#!/usr/bin/python3
"""takes in a URL and an email address
    sends a POST request to the passed URL with the email
    displays the body of the response
"""
import sys
import requests

if __name__ == "__main__":
    taken_url = sys.argv[1]
    value = {"email": sys.argv[2]}

    req = requests.post(taken_url, data=value)
    print(req.text)
