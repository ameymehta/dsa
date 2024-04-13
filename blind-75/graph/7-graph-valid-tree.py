from collections import deque


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False
        neighbors = {}
        for i in range(n):
            neighbors[i] = []

        for a, b in edges:
            neighbors[a] += [b]
            neighbors[b] += [a]

        queue = deque([0])

        while queue:
            # changed this sugar syntax to simple code
            # queue.extend(neighbors.pop(queue.popleft(), []))
            cur = queue.popleft()
            if cur in neighbors:
                queue.extend(neighbors[cur])
                del neighbors[cur]

        return not neighbors
