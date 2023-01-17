#!/usr/bin/python3
"""
This module is used to send a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter using the package requests and sys
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    data = {'q': q}
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        json_res = response.json()
        if json_res:
            print("[{}] {}".format(json_res.get('id'), json_res.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
