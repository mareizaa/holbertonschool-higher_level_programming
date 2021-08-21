#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import requests


if __name__ == '__main__':
    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type:", type(response.text))
    print("\t- content:", response.text)
