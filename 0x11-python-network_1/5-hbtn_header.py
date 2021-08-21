#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get(argv[1])
    res = response.headers
    print(res.get('X-Request-Id'))
