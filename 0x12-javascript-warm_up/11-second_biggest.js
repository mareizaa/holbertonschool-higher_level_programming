#!/usr/bin/node
if (process.argv.length === 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  const aSet = process.argv.slice(2);
  const aSet1 = aSet.sort();
  const len = aSet1.length - 1;
  const second = len - 1;
  console.log(aSet1[second]);
}
