/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  let result = [];
  let set = new Set();
  n = nums.length;
  if (n == 0) return [];
  nums.sort();
  for (let i = 0; i < n; i++) {
    let left = i + 1;
    let right = n - 1;
    while (left < right) {
      let sum = nums[i] + nums[left] + nums[right];
      if (sum == 0) {
        const s = `${nums[i]}-${nums[left]}-${nums[right]}`;
        if (!set.has(s)) {
          set.add(s);
          result.push([nums[i], nums[left], nums[right]]);
        }
        left++;
        right--;
        // approach to remove duplicate didn't work
        // while(nums[left] === nums[left+1]) left++;
        // while(nums[right] === nums[right - 1]) right--;
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }
  return result;
};
