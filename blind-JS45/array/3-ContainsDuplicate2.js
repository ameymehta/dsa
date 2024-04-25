/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
  let visited = new Map();
  for (let i = 0; i < nums.length; i++) {
    if (visited.has(nums[i]) && i - visited.get(nums[i]) <= k) {
      return true;
    } else {
      visited.set(nums[i], i);
    }
  }
  return false;
};
