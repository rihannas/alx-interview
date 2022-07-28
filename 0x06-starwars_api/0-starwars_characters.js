#!/usr/bin/node

// Require request which includes put() function
const request = require('request');
// To request, we need to concatenate the api with the endpoint
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (error, response, values) => {
  if (error) {
    console.log(error);
  } else {
    // Store the results
    const results = JSON.parse(values).characters;
    showResults(results, 0);
  }
});

function showResults (results, index) {
  if (index === results.length) {
    return;
  }
  request(results[index], async (error, response, values) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(values).name);
      index += 1;
      showResults(results, index);
    }
  });
}