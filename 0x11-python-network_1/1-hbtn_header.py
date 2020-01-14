#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv

    req = request.Request(argv[1])
    with request.urlopen(req) as res:
        print(res.headers.get('X-Request-Id'))
