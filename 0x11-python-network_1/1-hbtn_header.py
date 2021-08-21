#!/usr/bin/python3
"""displays the value of the X-Request-Id"""
import urllib.request
from sys import argv


with urllib.request.urlopen(argv[1]) as response:
    h = response.info()
    print(h['X-Request-Id'])
