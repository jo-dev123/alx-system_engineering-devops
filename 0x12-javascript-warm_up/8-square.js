#!/usr/bin/node

const squareSize = process.argv[2];

for (let i = 0; i < squareSize; i++) {
  for (let j = 0; j < squareSize; j++) {
    process.stdout.write('X');
  }
  console.log('X');
}
