#!/usr/bin/python3
"""
Script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv

    args = {'email': argv[2]}
    body = parse.urlencode(args)
    req = request.Request(argv[1], body)
    with request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
