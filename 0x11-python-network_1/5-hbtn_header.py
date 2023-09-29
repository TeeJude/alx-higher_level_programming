#!/usr/bin/python3
"""
Script that displays the X-Request-Id header variable 
"""
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
