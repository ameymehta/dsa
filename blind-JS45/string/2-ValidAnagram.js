/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length != t.length) return false;
  let charMap = new Map();
  for (let i = 0; i < s.length; i++) {
    // if(!charMap.has(s[i])) charMap.set(s[i], 0);
    charMap.set(s[i], (charMap.get(s[i]) ?? 0) + 1);
    // if(!charMap.has(t[i])) charMap.set(t[i], 0);
    charMap.set(t[i], (charMap.get(t[i]) ?? 0) - 1);
  }
  for (let [key, value] of charMap) {
    if (value != 0) return false;
  }
  return true;
};
