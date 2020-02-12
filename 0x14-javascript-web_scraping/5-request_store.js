#!/usr/bin/node

/*
Script that gets the contents of a webpage and stores it in a file.

- The first argument is the URL to request
- The second argument the file path to store the body response
*/

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const pathFile = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFileSync(pathFile, body, 'utf-8');
  }
});
