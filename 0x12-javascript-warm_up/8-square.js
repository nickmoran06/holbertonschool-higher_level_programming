#!/usr/bin/node
const size = process.argv[2];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let counter = 0; counter < size; counter++) {
    console.log('X'.repeat(size));
  }
}
