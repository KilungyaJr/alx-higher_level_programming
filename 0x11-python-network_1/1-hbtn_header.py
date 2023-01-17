#!/usr/bin/python3
"""
This module is used to fetch the value of the X-Request-Id
from the header of a URL using the package urllib and sys
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get("X-Request-Id")
        print(x_request_id)
