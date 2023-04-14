#!/usr/bin/node
//working with argv.

const [arg] = process.argv.slice(2);

if (!arg) {
  console.log('No argument');

//  Otherwise, we print arg using console.log(...)
} else {
  console.log(arg);
}
