#!/usr/bin/python3
"""
This module is used to get the id of a GitHub user using their credentials
and the GitHub API using the package requests and sys
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    res = requests.get("https://api.github.com/user", auth=(username, token))
    json_response = res.json()
    print(json_response.get("id"))
