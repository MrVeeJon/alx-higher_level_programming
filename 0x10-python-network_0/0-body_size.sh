#!/bin/bash
# Sends a request to a URL and displays the size of the body of the response

# Check if URL is provided
if [ -z "$1" ]; then
	    echo "Usage: $0 <URL>"
	        exit 1
fi

# Use curl to get the response and display the size
curl -sI "$1" | grep -i Content-Length | awk '{print "Size of the body of the response: " $2 " bytes"}' | tr -d '\r\n'

