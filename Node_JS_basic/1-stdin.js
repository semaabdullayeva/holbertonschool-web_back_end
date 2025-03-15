const readline = require("readline")

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

function ask(question){
  rl.question(question, (answer) => {
    rl.write(`Your name is: ${answer}\n`)
    rl.write(`This important software is now closing\n`)
    rl.close()
  })
}

ask("Welcome to Holberton School, what is your name?\n")
// process.stdout.write(`Welcome to Holberton School, what is your name?\n`);

// process.stdin.on("data", (data) => {
//   const name = data.toString("utf8").trim();

//   process.stdout.write(`Your name is: ${name}\n`);

//   process.stdout.write(`This important software is now closing\n`);

//   process.exit(0);
// });
