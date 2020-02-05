#!/usr/bin/node
let counter = 0;
if (process.argv.length === 3) {
  while (counter < parseInt(process.argv[2])) {
    console.log('C is fun');
    counter++;
  }
} else {
  console.log('Missing number of occurrences');
}
