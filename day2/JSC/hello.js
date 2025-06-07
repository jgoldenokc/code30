console.log("Hello, World!");

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question("What's your name? ", (name) => {
  console.log(`Nice to meet you, ${name}!`);
  readline.close();
});
// This code prints "Hello, World!" to the console and then prompts the user for their name.