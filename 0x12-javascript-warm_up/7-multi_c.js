#!/usr/bin/node
let x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  while (x) {
    console.log('C is fun');
    x--;
  }
}
