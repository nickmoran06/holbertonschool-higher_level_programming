#!/usr/bin/node
const lenArgs = process.argv.length;
const integer = parseInt(process.argv[2]);

if (lenArgs <= 2) {
  console.log('Not a number');
} else if (lenArgs === 3) {
  if (Number.isInteger(integer)) {
    console.log('My number: ' + integer);
  } else {
    console.log('Not a number');
  }
}
