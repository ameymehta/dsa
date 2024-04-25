/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
  let left = 0;
  let right = nums.length - 1;
  while (left < right) {
    // in python num//2 rounds result down to an int
    // in JS you need to use Math.floor(num/2)
    // in this case simple division operator works
    let mid = left + (right - left) / 2;
    if (nums[mid] > nums[right]) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }
  return nums[right];
};
