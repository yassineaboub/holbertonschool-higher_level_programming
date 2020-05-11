#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let r = 0;
    for (r = 0; r < this.height; r++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    let temp;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
