#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('Missing number of occurrences');
} else {
  const x = process.argv[2];
  let i;
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
