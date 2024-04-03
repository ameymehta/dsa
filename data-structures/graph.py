import Queue


class Node:
    def __init__(self, id):
        self.id = id
        self.adjacent = []


class Graph:
    def __init__(self):
        self.node_lookup = {}

    def get_node(id):
        return self.node_lookup[id]

    def add_edge(source, dest):
        s = get_node(source)
        d = get_node(dest)
        s.adjacent.append(d)

    def has_path_dfs(src, dest):
        source = get_node(source)
        destination = get_node(dest)
        visited = set()
        return has_path_dfs(source, destination, visited)

    def has_path_dfs(source, destination, visited):
        if source.id in visited:
            return False
        visited.add(source.id)
        if source.id == destination.id:
            return True
        for child in source.adjacent:
            if has_path_dfs(child, destination, visited):
                return True
        return False

    def has_path_bfs(src, dest):
        source = get_node(source)
        destination = get_node(dest)
        visited = set()
        return has_path_bfs(source, destination, visited)

    def has_path_bfs(source, destination, visited):
        next_to_visit = Queue.Queue()
        next_to_visit.put(source)
        while not next_to_visit.empty():
            node = next_to_visit.get()
            if node.id == destination.id:
                return True
            if source.id in visited:
                continue
            visited.add(source.id)
            for child in node.adjacent:
                next_to_visit.put(child)
        return False
