#!/usr/bin/node
let b = 0;
exports.logMe = function (item) {
  const state = b;
  console.log(state + ': ' + item);
  b += 1;
};
