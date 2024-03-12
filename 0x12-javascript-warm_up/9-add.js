#!/usr/bin/node
const args = process.argv.slice(2);

function add (a, b) {
  console.log(a + b);
}

if (args.length < 2 || isNaN(Number(args[0])) || isNaN(Number(args[1]))) {
  console.log('NaN');
} else {
  add(Number(args[0]), Number(args[1]));
}
