from collections import deque
stack = deque()
s = '[[[[][]]]]'
print(stack[-1])
stack.append(s[0])
for i in range(1, len(s)):
    if s[i] == ']' and stack[-1] == '[':
        print(stack.pop())
    elif s[i] == '}' and stack[-1] == '{':
        print(stack.pop())
    elif s[i] == ')' and stack[-1] == '(':
        print(stack.pop())
    else:
        stack.append(s[i])

print(len(stack))
