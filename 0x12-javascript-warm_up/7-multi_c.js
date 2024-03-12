#!/usr/bin/node
const args = process.argv.slice(2);

if (isNaN(Number(args[0]))) {
  console.log('Missing number of occurrences');
} else {
  const num = Math.floor(Number(args[0]));
  let i = 0;
  while (i < num) {
    console.log('C is fun');
    i++;
  }
}
