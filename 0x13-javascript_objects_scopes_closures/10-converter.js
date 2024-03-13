#!/usr/bin/node
exports.converter = function (base) {
  return function myConverter (num) {
    if (num < 1) {
      return ('');
    }
    if (base === 16 && (num % base) > 9) {
      return (myConverter(Math.floor(num / base)) + String.fromCharCode(87 + (num % base)));
    } else {
      return (myConverter(Math.floor(num / base)) + String.fromCharCode(48 + (num % base)));
    }
  };
};
