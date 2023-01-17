#!/usr/bin/python3
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read()
    print("Body response:\n\t- type:", type(body), "\n\t- content:", body, "\n\t- utf8 content:", body.decode('utf-8'))
