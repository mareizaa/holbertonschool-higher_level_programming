#!/usr/bin/node
let mynumber;
if (process.argv.length === 2) {
  console.log('Not a number');
} else if (typeof (process.argv[2]) === 'string') {
  mynumber = parseInt(process.argv[2]);
  if (isNaN(mynumber)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + mynumber);
  }
} else {
  console.log('My number: ' + process.argv[2]);
}
