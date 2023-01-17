#!/usr/bin/python3
"""
This module is used to send a POST request to a URL with an email
as a parameter using the package urllib and sys
"""
import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode()
    req = urllib.request.Request(url, data=data)
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))
