const readline = require('readline')
const Calculator = require('./Calculator');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const runCalculator = (a, b) => {
    console.log("NWD: " + Calculator.getGreatestCommonDivisor(a, b));
    console.log("NWW: " + Calculator.getLeastCommonMultiple(a, b));
};

const prompt = () => {
    rl.question('Input first number: ', (a) => {
        rl.question('Input second number: ', (b) => {
            try {
                runCalculator(a, b)
            } catch (e) {
                console.error(e);
            }
            prompt();
        });
    });
}

prompt();
