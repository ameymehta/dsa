/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let n = height.length;
  let maxArea = 0;
  let left = 0;
  let right = n - 1;
  while (left < right) {
    curArea = Math.min(height[left], height[right]) * (right - left);
    maxArea = Math.max(curArea, maxArea);
    if (height[left] < height[right]) left++;
    else right--;
  }
  return maxArea;
};
