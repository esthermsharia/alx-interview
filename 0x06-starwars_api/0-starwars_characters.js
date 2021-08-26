#!/usr/bin/node

const request = require('request');

const film_num = process.argv[2] + '/';
const film_url = 'https://swapi-api.hbtn.io/api/films/';

request(film_url + film_num, async function (err, res, body) {
  if (err) return console.error(err);
  const char_list = JSON.parse(body).characters;

  for (const charURL of char_list) {
    await new Promise(function (resolve, reject) {
      request(charURL, function (err, res, body) {
        if (err) return console.error(err);
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
