from collections import deque

def bfs_search(graph, start, target):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        if node == target:
            print(f"\nFound target node: {target}")
            return True

        if node not in visited:
            visited.add(node)
            queue.extend(
                neighbor for neighbor in graph[node]
                if neighbor not in visited
            )

    print(f"Target node {target} not found in the graph.")
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['A','D', 'E'],
    'C': ['A','F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C', 'E']
}

hello = bfs_search(graph, start='A', target='F')
print("Search completed:", hello)
