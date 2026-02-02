const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question("How old are you? ", (age) => {
    console.log("Before parsing, type of age:", typeof age);
  age = parseInt(age);
    console.log("After parsing, type of age:", typeof age);
  if (age >= 18) {
    console.log("You can drive!");
  } else if (age >= 15) {
    console.log("You can get a learner's permit.");
  } else {
    console.log("Too young to drive.");
  }
  readline.close();
});