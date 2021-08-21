#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            result = response.read()
            print(result.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code:", e.code)
