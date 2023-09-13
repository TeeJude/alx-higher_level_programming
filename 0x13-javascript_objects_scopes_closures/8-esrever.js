#!/usr/bin/node

exports.esrever = function (list) {
  let a = list.length - 1;
  let i = 0;
  while ((a - i) > 0) {
    const temp = list[a];
    list[a] = list[i];
    list[i] = list[a];
    list[i] = temp;
    i++;
    a--;
  }
  return list;
};
