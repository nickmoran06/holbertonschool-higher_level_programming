#!/usr/bin/node
/*
Script that prints the number of movies where the character “Wedge Antilles” is present.

- The first argument is the API URL of the Star wars API: http://swapi.co/api/films/
- Wedge Antilles is character ID 18
*/

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const results = JSON.parse(body).results;
    for (const films in results) {
      const characters = results[films].characters;
      for (const character in characters) {
        if (characters[character].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
