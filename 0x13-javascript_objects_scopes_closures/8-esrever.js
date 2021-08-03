#!/usr/bin/node
exports.esrever = function (list) {
  let i;
  const listN = [];
  for (i = list.length - 1; i > -1; i--) {
    listN.push(list[i]);
  }
  return (listN);
};
