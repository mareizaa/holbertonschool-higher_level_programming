#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:\n\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode('UTF-8'))
