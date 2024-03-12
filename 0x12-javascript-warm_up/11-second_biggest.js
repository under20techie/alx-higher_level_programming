#!/usr/bin/node
const args = process.argv.splice(2);
if (args.length < 0) {
  console.log(0);
} else {
  let i = 1;
  let secBig = 0;
  let max = Number(args[0]);
  while (i < args.length) {
    const num = Number(args[i]);
    if (num > max) {
      secBig = max;
      max = num;
    } else if (num > secBig && num !== max) {
      secBig = num;
    }
    i++;
  }
  console.log(secBig);
}
