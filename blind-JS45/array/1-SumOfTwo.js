/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  // use Map initializer, instead of m = {}, it initializes as an object
  const visited = new Map();
  for (let i = 0; i < nums.length; i++) {
    pairValue = target - nums[i];
    // has function to check if map contains that key
    if (visited.has(pairValue)) {
      // get value by key
      pairIndex = visited.get(pairValue);
      return [pairIndex, i];
    }
    // set key value
    visited.set(nums[i], i);
  }
  return [-1, -1];
};
