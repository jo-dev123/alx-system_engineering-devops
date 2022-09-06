#!/usr/bin/node

if (isNaN(process.argv[2]) === false) {
  console.log('My number: ' + +process.argv[2]);
} else {
  console.log('Not a number');
}
