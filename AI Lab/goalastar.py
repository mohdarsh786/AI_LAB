import heapq

def heuristic(node, goal):
   
    return 0

def goal_astar(graph, start, goal):
    queue = []
    heapq.heappush(queue, (0 + heuristic(start, goal), 0, start, [start]))
    visited = set()

    while queue:
        est_total_cost, cost_so_far, current, path = heapq.heappop(queue)
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for neighbor, weight in graph.get(current, {}).items():
            if neighbor not in visited:
                new_cost = cost_so_far + weight
                est = new_cost + heuristic(neighbor, goal)
                heapq.heappush(queue, (est, new_cost, neighbor, path + [neighbor]))
    return None

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1}
}

# Example usage:
start_node = "A"
goal_node = "D"
path = goal_astar(graph, start_node, goal_node)
print("Path from", start_node, "to", goal_node, ":", path)