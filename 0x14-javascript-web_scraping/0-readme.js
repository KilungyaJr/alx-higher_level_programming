#!/usr/bin/node

var fs = require('fs');
var filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
