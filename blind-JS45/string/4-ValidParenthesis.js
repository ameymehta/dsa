/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let stack = [];
  for (const ch of s) {
    if (ch === "(" || ch === "{" || ch === "[") stack.push(ch);
    else {
      if (
        !stack.length ||
        (ch === ")" && stack[stack.length - 1] !== "(") ||
        (ch === "}" && stack[stack.length - 1] !== "{") ||
        (ch === "]" && stack[stack.length - 1] !== "[")
      ) {
        // since closing bracket didn't match with opening bracket in the stack
        return false;
      }
      // pop the opening bracket
      stack.pop();
    }
  }
  return !stack.length;
};
