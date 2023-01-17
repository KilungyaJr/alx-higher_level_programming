#!/usr/bin/python3
"""
This module is used to fetch the value of the X-Request-Id from
the header of a URL using the package requests and sys
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    x_request_id = response.headers.get("X-Request-Id")
    print(x_request_id)
