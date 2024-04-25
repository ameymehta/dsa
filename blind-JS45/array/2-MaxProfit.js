/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let indexOfLowest = 0;
  let highestDiff = 0;
  for (let i = 0; i < prices.length; i++) {
    if (prices[i] - prices[indexOfLowest] > highestDiff) {
      highestDiff = prices[i] - prices[indexOfLowest];
    }
    if (prices[i] < prices[indexOfLowest]) {
      indexOfLowest = i;
    }
  }
  return highestDiff;
};
