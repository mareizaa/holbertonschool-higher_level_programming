#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      let i, j;
      let myVar = '';
      for (i = 0; i < this.height; i++) {
        myVar = '';
        for (j = 0; j < this.width; j++) {
          myVar += c;
        }
        console.log(myVar);
      }
    } else {
      this.print();
    }
  }
} module.exports = Square;
