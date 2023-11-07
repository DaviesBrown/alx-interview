#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

function getCharacters (movieId) {
  const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(filmUrl, (error, response, body) => {
    if (error) {
      console.error(`Error: ${error}`);
    } else if (response.statusCode === 200) {
      const filmData = JSON.parse(body);

      const charactersUrls = filmData.characters;
      let count = 0;

      function fetchCharacter (characterUrl) {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error(`Error fetching character data: ${error}`);
          } else if (response.statusCode === 200) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
            count++;

            if (count < charactersUrls.length) {
              fetchCharacter(charactersUrls[count]);
            }
          }
        });
      }

      if (charactersUrls.length > 0) {
        fetchCharacter(charactersUrls[0]);
      }
    } else {
      console.error(`Failed to fetch film data for movie ID ${movieId}`);
    }
  });
}

getCharacters(movieId);
