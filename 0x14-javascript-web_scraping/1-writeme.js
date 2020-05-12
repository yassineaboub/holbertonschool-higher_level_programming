#!/usr/bin/node
const fs = require('fs');
let text = process.argv[3];
let data = process.argv[2];

fs.writeFile(data, text, function(err) {
  if(err) {
   console.log(err);
  }
});
