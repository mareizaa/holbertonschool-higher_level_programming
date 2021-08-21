#!/usr/bin/python3
"""displays the value of the X-Request-Id"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    h = response.info()
    print(h['X-Request-Id'])
