#!/usr/bin/node
const l1 = require('./100-data').list;
/* const me = [2, 4, 5, 6, 7]; */
const map1 = l1.map((x, y) => x * y);
console.log(l1);
console.log(map1);
