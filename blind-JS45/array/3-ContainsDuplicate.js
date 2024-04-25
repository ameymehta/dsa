/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  let visited = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (visited.has(nums[i])) {
      return true;
    } else {
      visited.set(nums[i], i);
    }
  }
  return false;
};
