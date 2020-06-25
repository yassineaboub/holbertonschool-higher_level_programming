#!/usr/bin/node
const list = require('./100-data').list;
const nlist = list.map(function (i, n) {
  return i * n;
});
console.log(list);
console.log(nlist);
