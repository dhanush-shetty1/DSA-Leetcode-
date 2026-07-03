/**
 * @param {number} n
 * @return {Function}
 */
var createCounter = function(n) {

    // Return a function (closure)
    return function() {

        // Return current value of n,
        // then increase n by 1
        return n++;
    };

};

/**
 * Driver Code
 */

// const counter = createCounter();

// console.log(counter()); // 10
// console.log(counter()); // 11
// console.log(counter()); // 12
// console.log(counter()); // 13
// console.log(counter()); // 14