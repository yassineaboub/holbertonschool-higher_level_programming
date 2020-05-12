#!/usr/bin/node
const fs = require('fs');
const text = process.argv[3];
const data = process.argv[2];

fs.writeFile(data, text, function(err) {
  if(err) {
    console.log(err);
  }
});
