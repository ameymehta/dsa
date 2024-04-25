# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque


class Solution(object):
    # Amey preferred
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        # dict for storing and referencing cloned graph
        m = dict()
        # visited so that we don't go through that node when it comes in queue again
        visited = set()
        # queue for BFS
        queue = deque()
        queue.append(node)

        while queue:
            cur = queue.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            # cloning part
            # create clone of the current node, put in map
            if cur not in m:
                m[cur] = Node(cur.val)
            # create clone of each neighbor, put them in map
            for n in cur.neighbors:
                if n not in m:
                    m[n] = Node(n.val)
                # add each neighbor to the cloned current node's neighbors[]
                m[cur].neighbors.append(m[n])
                # add each neighbor (child in trees) to the queue
                queue.append(n)
        return m[node]

    def cloneGraphDFS(self, node):
        if not node:
            return node
        m, visited = dict(), set()
        self.dfs(node, m, visited)
        return m[node]

    def dfs(self, n, m, visited):
        if n in visited:
            return
        visited.add(n)
        if n not in m:
            m[n] = Node(n.val)
        for neigh in n.neighbors:
            if neigh not in m:
                m[neigh] = Node(neigh.val)
            m[n].neighbors.append(m[neigh])
            self.dfs(neigh, m, visited)
