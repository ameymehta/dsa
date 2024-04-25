/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  memo = [nums[0]];
  maxSum = nums[0];
  for (let i = 1; i < nums.length; i++) {
    const curMax = Math.max(memo[i - 1] + nums[i], nums[i]);
    memo.push(curMax);
    maxSum = Math.max(maxSum, curMax);
  }
  return maxSum;
};
