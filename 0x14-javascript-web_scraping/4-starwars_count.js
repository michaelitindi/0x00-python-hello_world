#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch the movies. Please ensure the API URL is correct.');
    return;
  }

  const moviesData = JSON.parse(body);
  const wedgeId = 'https://swapi-api.alx-tools.com/api/people/18/';
  const moviesWithWedge = moviesData.results.filter(movie => movie.characters.includes(wedgeId));

  console.log(`${moviesWithWedge.length}`);
});
