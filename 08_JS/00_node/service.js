const utility = require('./utility.js');

const accountA = 100;
const accountB = 200;
const accountC = 400;
const totalBalance = utility.addAll([accountA, accountB, accountC]);

console.log(totalBalance)

