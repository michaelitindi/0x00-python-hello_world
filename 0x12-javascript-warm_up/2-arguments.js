#!/usr/bin/node
const agno = process.argv.length;
console.log(agno === 2 ? 'No argument' : agno == 3 ? 'Argument found' : 'Arguments found');
