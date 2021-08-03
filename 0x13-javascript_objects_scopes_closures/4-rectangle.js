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

  rotate () {
    const new_w = this.width;
    this.width = this.height;
    this.height = new_w;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
} module.exports = Rectangle;
