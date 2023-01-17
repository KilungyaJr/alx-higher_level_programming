#!/usr/bin/python3
"""
This module is used to fetch the body of a URL response (decoded in utf-8)
using the package urllib and sys, also manage the HTTPError exception.
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except urllib.error.HTTPError as err:
        print("Error code:", err.code)
