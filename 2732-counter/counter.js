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

