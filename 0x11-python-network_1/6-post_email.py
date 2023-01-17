#!/usr/bin/python3
"""
This module is used to send a POST request to a URL with an email
as a parameter using the package requests and sys
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
