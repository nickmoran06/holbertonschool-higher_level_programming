#!/usr/bin/node
let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);

console.log(add(a, b));

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return (NaN);
  } else {
    return (a + b);
  }
}