#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('An error occurred while fetching the URL:', error);
    return;
  }

  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error('An error occurred while writing to the file:', err);
      return;
    }
    console.log(`Content from ${url} has been successfully written to ${filePath}`);
  });
});
