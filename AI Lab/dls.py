def DLS(graph, node, goal, depth):
    if node == goal:
        return True
    if depth <= 0:
        return False
    for child in graph.get(node, []):
        if DLS(graph, child, goal, depth - 1):
            return True
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': []
}

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")
max_depth = int(input("Enter the maximum depth limit: "))

found = DLS(graph, start, goal, max_depth)
print("Goal found within limit:", found)