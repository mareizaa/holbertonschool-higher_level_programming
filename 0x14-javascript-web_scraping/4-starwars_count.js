#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = '18';
const char = 'https://swapi-api.hbtn.io/api/people/'.concat(id, '/');

request(url, (error, data, body) => {
  if (error) {
    return console.error(error);
  }
  const obj = JSON.parse(body);
  const films = obj.results;
  let num = 0;
  for (let i = 0; i < films.length; i++) {
    const character = films[i].characters;
    if (character.includes(char)) {
      num += 1;
    }
  }
  console.log(num);
});
