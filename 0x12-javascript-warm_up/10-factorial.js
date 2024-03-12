#!/usr/bin/node
const args = process.argv.slice(2);

function factorial (num) {
  if (num === 1) {
    return 1;
  }
  return (num * factorial(num - 1));
}

if (args.length < 1) {
  console.log(1);
} else if (isNaN(Number(args[0]))) {
  console.log('NaN');
} else {
  console.log(factorial(Number(args[0])));
}
