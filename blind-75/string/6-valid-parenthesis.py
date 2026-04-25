class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif c == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif c == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            elif c == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False
    
    # using map to remember pairs
    def is_valid_parentheses(self, s):
        stack = []
        pairs = { '(' : ')', '{' : '}', '[' : ']'}
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            elif ch in pairs.values():
                if not stack or pairs[stack.pop()] != ch:
                    return False
            # ignore other chars

        # stack should be empty at the end of for loop for s to be valid
        return len(stack) == 0

    def test_cases(self):
        print(self.is_valid_parentheses("()[]{}"))   # True
        print(self.is_valid_parentheses("([)]"))     # False
        print(self.is_valid_parentheses("{[]}"))     # True
        print(self.is_valid_parentheses("("))        # False