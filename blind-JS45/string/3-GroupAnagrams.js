/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const result = [];
  const groups = new Map();

  for (const s of strs) {
    const signature = getSignature(s);
    if (!groups.has(signature)) groups.set(signature, []);
    groups.get(signature).push(s);
  }

  groups.forEach((value) => result.push(value));

  return result;
};

const getSignature = (str) => {
  const count = Array(26).fill(0);
  for (const c of str) {
    // tricky part
    count[c.charCodeAt(0) - "a".charCodeAt(0)]++;
  }
  let result = "";
  count.forEach((n) => (result += `${n}`));
  return result;
};
