#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request as request
    req = request.Request('https://intranet.hbtn.io/status')
    with request.urlopen(req) as res:
        Page = res.read()
        print('Body response:')
        print("\t- type: {}".format(type(Page)))
        print("\t- content: {}".format(Page))
        print("\t- utf8 content: {}".format(Page.decode('utf-8')))
