module.exports = class Calculator {
    static getGreatestCommonDivisor(a, b) {
        Calculator.throwIfBothZeros(a, b);
        return a == 0 ? b : Calculator.getGreatestCommonDivisor(b % a, a);
    }

    static getLeastCommonMultiple(a, b) {
        Calculator.throwIfNonUniqueInput(a, b);
        return Math.abs(a * b) / Calculator.getGreatestCommonDivisor(a, b);
    }

    static throwIfBothZeros(a, b) {
        if (a == 0 && b == 0) {
            throw "Provided numbers can't be both zeros!"
        }
    }

    static throwIfNonUniqueInput(a, b) {
        if (a == b) {
            throw "Enter two unique numbers";
        }
    }
}