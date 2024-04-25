/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const visited = new Map();
    for (let i = 0; i < nums.length; i++) {
        pairValue = target - nums[i];
        if (visited.has(pairValue)) {
            pairIndex = visited.get(pairValue);
            return [pairIndex, i];
        }
        visited.set(nums[i], i);
    }
    return [-1, -1];
};
