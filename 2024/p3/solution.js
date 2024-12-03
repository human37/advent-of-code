const fs = require("fs");
const input = fs.readFileSync("input.txt", "utf8");

let sum = 0;
const mulPattern = /mul\((\d+),(\d+)\)/g;
const matches = input.match(mulPattern);
if (matches) {
  sum += matches.reduce((acc, match) => {
    const [_, num1, num2] = match.match(/mul\((\d+),(\d+)\)/);
    return acc + parseInt(num1) * parseInt(num2);
  }, 0);
}

console.log("sum: ", sum);
