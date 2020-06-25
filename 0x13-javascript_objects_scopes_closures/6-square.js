#!/usr/bin/node
const Ns = require('./5-square');
class Square extends Ns {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.height));
    }
  }
};
module.exports = Square;
