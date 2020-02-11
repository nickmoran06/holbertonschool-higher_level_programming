#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  for (let count = 0; count < list.length; count++) {
    revList.unshift(list[count]);
  }
  return revList;
};
