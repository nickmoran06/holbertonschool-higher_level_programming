#!/usr/bin/python3
"""
fetches with requests library https://intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import requests
    req = requests.get('https://intranet.hbtn.io/status')
    text = req.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
