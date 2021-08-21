#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
import urllib.request
from sys import argv


with urllib.request.urlopen(argv[1]) as response:
    header = response.info()
    print(header['X-Request-Id'])
