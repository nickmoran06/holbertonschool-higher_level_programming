#!/usr/bin/python3
"""
Script that takes in a string and sends a search request to the Star Wars API
"""
if __name__ == '__main__':
    import requests
    from sys import argv

    req = requests.get('https://swapi.co/api/people', {'search': argv[1]})
    charac = req.json()
    print("Number of results: {}".format(charac.get('count')))
    for person in charac.get('results'):
        print(person.get('name'))
