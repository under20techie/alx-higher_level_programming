exports.esrever = function (list) {
  const newList = [];
  let j = list.length - 1;
  while (j >= 0) {
    newList.push(list[j]);
    j--;
  }
  return newList;
};
