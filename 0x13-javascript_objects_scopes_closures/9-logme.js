#!/usr/bin/node

let varLog = 0;
exports.logMe = function (item) {
  console.log(varLog + ': ' + item);
  varLog++;
};
