#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map((x, ind) => x * ind);
console.log(list);
console.log(newList);
