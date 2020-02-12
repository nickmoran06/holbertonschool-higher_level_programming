#!/usr/bin/node

/*
Script that computes the number of tasks completed by user id.

- The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
*/

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const myDict = {};
    const myBody = JSON.parse(body);

    for (const data of myBody) {
      if (data.completed === true) {
        if (data.userId in myDict) {
          myDict[data.userId] += 1;
        } else {
          myDict[data.userId] = 1;
        }
      }
    }
    console.log(myDict);
  }
});
