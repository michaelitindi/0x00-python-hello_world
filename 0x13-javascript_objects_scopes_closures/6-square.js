#!/usr/bin/node
const SquareZero = require('./5-square');
module.exports = class Square extends SquareZero {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
