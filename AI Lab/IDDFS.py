from collections import defaultdict

def dls(graph, src, target, limit, path, visited):
    path.append(src)
    visited.add(src)

    if src == target:
        return True
    if limit <= 0:
        path.pop()
        visited.remove(src)
        return False

    for neighbor in graph[src]:
        if neighbor not in visited:
            if dls(graph, neighbor, target, limit - 1, path, visited):
                return True

    path.pop()
    visited.remove(src)
    return False

def iddfs(graph, src, target, max_depth):
    for depth in range(max_depth + 1):
        path = []
        visited = set()
        if dls(graph, src, target, depth, path, visited):
            return path
    return None

# Main block
if __name__ == "__main__":
    graph = defaultdict(list)
    graph[0].extend([1, 2])
    graph[1].extend([3, 4])
    graph[2].extend([5, 6]) 
    graph[3].extend([7])
    graph[4].extend([7])
    graph[5].extend([7])
    graph[6].extend([7])
    src = 0
    target = 7
    max_depth = 3

    path = iddfs(graph, src, target, max_depth)
    if path:
        print("Path found:", path)
    else:
        print(f"Target {target} not reachable within depth {max_depth}")
