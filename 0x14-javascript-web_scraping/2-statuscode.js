#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) return console.log('Error: ', err);
  console.log('code: %d', res.statusCode);

});
