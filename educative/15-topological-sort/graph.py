from collections import deque


def topological_sort(vertices, edges):
    sortedOrder = []
    if vertices == 0:
        return sortedOrder

    # initialize the graph
    inDegree = {i: 0 for i in range(vertices)}
    adjacencyList = {i: [] for i in range(vertices)}

    # build the graph
    for e in edges:
        parent, child = e[0], e[1]
        adjacencyList[parent].append(child)
        inDegree[child] += 1

    # find sources, add to sorted order
    # remove them from graph i.e. decrement inDegree from child
    # if inDegree becomes 0, it becomes a source, add to sources
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    while sources:
        src = sources.popleft()
        sortedOrder.append(src)
        for child in adjacencyList[src]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    return sortedOrder


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
