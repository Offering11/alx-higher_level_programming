#!/usr/bin/node
const Squ = require('./5-square');

class Square extends Squ {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let k = '';
      for (let j = 0; j < this.width; j++) {
        k += c;
      }
      console.log(k);
    }
  }
}

module.exports = Square;
