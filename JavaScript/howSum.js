#!/usr/bin/node

const howSum = (target, arr, memo={}) => {
    if (target in memo) return memo[target];
    if (target == 0) {
        return [];
    }
    if (target < 0) return null;

    for (let num of arr) {
        const remainder = target - num;
        const result = howSum(remainder, arr);
        if (result !== null) {
            memo[target] = [...result, num];
            return memo[target];
        }
    }
    memo[target] = null;
    return null;
};

console.log(howSum(7, [2, 3]));
console.log(howSum(7, [5, 4, 3, 7]));
console.log(howSum(8, [2, 3, 4, 5, 6, 7, 8, 8, 9, 0]));
console.log(howSum(5, [6]))

