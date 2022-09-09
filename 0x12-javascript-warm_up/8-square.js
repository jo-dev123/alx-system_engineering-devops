#!/usr/bin/node

const squareSize = +process.argv[2];
if (Number.isInteger(squareSize)) {
  for (let i = 0; i < squareSize; i++) {
    console.log('X'.repeat(squareSize));
  }
} else {
  console.log('Missing size');
}
