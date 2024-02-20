#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (!err) {
    const todos = JSON.parse(body);
    console.log(todos.reduce((obj, todo) => {
      obj[todo.userId] = (obj[todo.userId] || 0) + (todo.completed ? 1 : 0);
      return obj;
    }, {}));
  }
});
