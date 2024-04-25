/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let productOfAll = 1;
  let zeroCount = 0;
  for (const n of nums) {
    if (n === 0) {
      zeroCount++;
    } else {
      productOfAll *= n;
    }
  }
  let result = [];
  if (zeroCount > 1) {
    // Array(size).fill(x) initializes array of size n and fills it with x element
    return Array(nums.length).fill(0);
  }
  for (const n of nums) {
    if (n != 0) {
      if (zeroCount === 1) {
        // push is append equivalent
        result.push(0);
      } else {
        result.push(productOfAll / n);
      }
    } else {
      result.push(productOfAll);
    }
  }
  return result;
};
