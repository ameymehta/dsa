/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let charsMap = new Map();
  let left = 0;
  let maxSubStr = 0;
  for (let right = 0; right < s.length; right++) {
    const ch = s[right];
    if (charsMap.has(ch)) {
      left = charsMap.get(ch) + 1;
      charsMap.set(ch, right);
    } else {
      charsMap.set(ch, right);
      maxSubStr = Math.max(maxSubStr, right - left + 1);
    }
  }
  return maxSubStr;
};
