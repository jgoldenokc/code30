// Define an array of tasks
const tasks = ["Wake up", "Code", "Eat", "Music", "Sleep"];

console.log("This is a FOR loop with indexes, somehow:");
for (let i = 0; i < tasks.length; i++) {
  console.log(`Task ${i + 1}: ${tasks[i]}`);
}
 
console.log("\n🔁 For-of loop with task names:");
for (let task of tasks) {
  console.log("Task:", task);
}

console.log("\n🔁 While loop with counter:");
let count = 0;
while (count < tasks.length) {
  console.log("While loop task:", tasks[count]);
  count++;
}