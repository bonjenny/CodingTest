const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', (line) => {
  if (!line) rl.close();

  let line_input = [];
  line_input = line.split(' ');
  input.push(line_input);
});

rl.on('close', () => {
  input.forEach((elmns) => {
    elmns.forEach((el) => {
      console.log(el);
    });
  });
  process.exit();
});
