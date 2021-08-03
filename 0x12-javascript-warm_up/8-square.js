#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  let i, j;
  let myVar = '';
  const size = process.argv[2];
  for (i = 0; i < size; i++) {
    myVar = '';
    for (j = 0; j < size; j++) {
      myVar += 'X';
    }
    console.log(myVar);
  }
}
