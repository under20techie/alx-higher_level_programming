#!/usr/bin/node
const Square1 = require('./5-square');
class Square extends Square1 {
   charPrint(c) {
    if (c == undefined) {
      c = 'X'
    }
    let i = 0;
    let j = 0;
    while (i < this.height) {
      j = 0;
      while (j < this.width) {
        process.stdout.write(c);
        j++;
      }
      console.log('');
      i++;
    }
   }
}
module.exports = Square;
