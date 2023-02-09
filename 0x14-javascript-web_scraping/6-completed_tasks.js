#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const tasks = JSON.parse(body);
  const completedTasks = {};
  tasks.forEach((task) => {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId]++;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  });

  console.log(completedTasks);
});
