#!/bin/bash
# Sends a request to url and displays the size of the body of response
curl -s "$1" | wc -c
