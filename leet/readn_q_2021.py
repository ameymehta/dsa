from collections import deque


class Solution:
    def __init__(self):
        self.q = deque()

    def read(self, buf, n):
        i = 0
        while i < n:
            if self.q:
                buf[i] = self.q.popleft()
                i += 1
            else:
                temp_buf = [' '] * 4
                size = read4(temp_buf)
                if not size:
                    break
                for j in range(size):
                    self.q.append(temp_buf[j])
        return i

