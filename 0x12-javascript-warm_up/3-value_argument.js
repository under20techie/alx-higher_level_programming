#!/usr/bin/node
const args = process.argv.slice(2);
if (!args[0]) {
  console.log('No argument');
} else {
  for (const i of args) {
    console.log(i);
  }
}
