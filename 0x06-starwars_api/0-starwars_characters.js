#!/usr/bin/node

const request = require('request');

const getCharacters = (urls, index) => {
  if (index === urls.length) {
    return;
  }
  request(urls[index], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const character = JSON.parse(body);
      console.log(character.name);
      getCharacters(urls, index + 1);
    } else {
      console.error(error);
    }
  });
};

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;
    getCharacters(characterUrls, 0);
  } else {
    console.error(error);
  }
});
