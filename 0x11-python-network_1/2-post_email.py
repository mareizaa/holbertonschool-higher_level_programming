#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')

    req = request.Request(url, data)

    with request.urlopen(req) as response:
        result = response.read()
        print(result.decode('utf-8'))
