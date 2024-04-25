from collections import defaultdict
from collections import deque


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        count = 0
        visited = set()
        for node in range(n):
            if node not in visited:
                visited.add(node)
                self.bfs(node, graph, visited)
                count += 1
        return count

    def bfs(self, node, graph, visited):
        queue = deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
