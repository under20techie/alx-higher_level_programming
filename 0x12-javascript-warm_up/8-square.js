#!/usr/bin/node
const args = process.argv.slice(2);

if (isNaN(Number(args[0]))) {
  console.log('Missing size');
} else {
  const num = Math.floor(Number(args[0]));
  let i = 0;
  let j = 0;
  while (i < num) {
    j = 0;
    while (j < num) {
      process.stdout.write('X');
      j++;
    }
    console.log('');
    i++;
  }
}
