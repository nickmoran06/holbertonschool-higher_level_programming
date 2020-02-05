#!/usr/bin/node
let num = 0;
num = parseInt(process.argv[2]);

console.log(factorial(parseInt(num)));

function factorial (num) {
  if (isNaN(num) || num === 1) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}
