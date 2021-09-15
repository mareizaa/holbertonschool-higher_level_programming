#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = 'https://swapi-api.hbtn.io/api/people/' + '18/';

request(url, (error, data, body) => {
  if (error) {
    return console.error(error);
  }
  const obj = JSON.parse(body);
  const films = obj.results;
  let num = 0;
  for (let i = 0; i < films.length; i++) {
    if (films[i].characters.includes(id)) {
      num += 1;
    }
  }
  console.log(num);
});
