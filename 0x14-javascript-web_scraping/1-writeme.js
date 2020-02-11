#!/usr/bin/node
const fs = require('fs');
const string = process.argv[3];

fs.writeFile(process.argv[2], string, (err, data) => {
  if (err) {
    console.log(err);
  }
});
