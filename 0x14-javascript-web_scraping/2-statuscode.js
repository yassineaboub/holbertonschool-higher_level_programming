#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: %d', res.statusCode);
}
});
