#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, j;
    let myVar = '';
    for (i = 0; i < this.height; i++) {
      myVar = '';
      for (j = 0; j < this.width; j++) {
        myVar += 'X';
      }
      console.log(myVar);
    }
  }
} module.exports = Rectangle;
