#!/usr/bin/python3
"""
This module is used to fetch the body of a URL response
using the package requests and sys, also manage the HTTP status code.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
