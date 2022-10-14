#!/usr/bin/node

if (process.argv.length > 3) {
  console.log(+process.argv[2] + +process.argv[3]);
} else {
  console.log(NaN);
}
