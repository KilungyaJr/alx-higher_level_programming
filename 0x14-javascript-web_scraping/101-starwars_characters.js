#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  body.characters.forEach((character) => {
    request(character, { json: true }, (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      }

      console.log(body.name);
    });
  });
});
