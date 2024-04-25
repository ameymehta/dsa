/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
  memo = [nums[0]];
  maxProd = nums[0];
  for (let i = 1; i < nums.length; i++) {
    const curMax = Math.max(memo[i - 1] * nums[i], nums[i]);
    memo.push(curMax);
    maxProd = Math.max(maxProd, curMax);
  }
  return maxProd;
};
