#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request(url, (error, data, body) => {
  if (error) {
    return console.error(error);
  }

  fs.writeFile(file, body, 'utf-8', function (err) {
    if (err) {
      return console.error(error);
    }
  });
});
