#!/usr/bin/node
const Squar = require('./5-square');

class Square extends Squar {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let i, j;
      let myVar = '';
      for (i = 0; i < this.height; i++) {
        myVar = '';
        for (j = 0; j < this.width; j++) {
          myVar += c;
        }
        console.log(myVar);
      }
    }
  }
} module.exports = Square;
