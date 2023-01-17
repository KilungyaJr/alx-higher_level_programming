#!/usr/bin/python3
"""
This module is used to fetch the status of https://alx-intranet.hbtn.io/status
using the package requests
"""
import requests

if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
