/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  sums = [nums[0]];
  maxSum = nums[0];
  for (let i = 1; i < nums.length; i++) {
    curMax = Math.max(sums[i - 1] + nums[i], nums[i]);
    sums.push(curMax);
    maxSum = Math.max(maxSum, curMax);
  }
  return maxSum;
};
