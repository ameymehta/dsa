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
