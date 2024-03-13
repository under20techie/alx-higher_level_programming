#!/usr/bin/node
function log () {
  let i = 0;
  return function (item) {
    console.log(`${i}: ${item}`);
    i++;
  };
}
exports.logMe = log();
