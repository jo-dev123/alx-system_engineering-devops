#!/usr/bin/node

const factorial = (num = +process.argv[2]) => {
  if (isNaN(num)) {
    return 1;
  }
  if (num === 1) {
    return 1;
  }
  return (num * factorial(num - 1));
};

console.log(factorial());
