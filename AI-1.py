import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    priority_queue = [(heuristic[start], start, [start])]
    visited = set()
    while priority_queue:
        _, current_node, path = heapq.heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)
        if current_node == goal:
            return path
        for neighbor, cost in graph.get(current_node, {}).items():
            if neighbor not in visited:
                new_path = path + [neighbor]
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, new_path))
    return None

if __name__ == "__main__":
    # Example 1
    graph = {
        'A': {'B': 1, 'C': 5},
        'B': {'D': 3, 'E': 6},
        'C': {'F': 2},
        'D': {'G': 4},
        'E': {'G': 2},
        'F': {'G': 7},
        'G': {}
    }
    heuristic = {
        'A': 7,
        'B': 6,
        'C': 3,
        'D': 4,
        'E': 2,
        'F': 1,
        'G': 0
    }
    start_node = 'A'
    goal_node = 'G'
    path_found = greedy_best_first_search(graph, start_node, goal_node, heuristic)
    if path_found:
        print(f"Path from {start_node} to {goal_node}: {path_found}")
    else:
        print(f"No path found from {start_node} to {goal_node}")

    # Example 2
    graph2 = {
        'S': {'A': 1, 'B': 5},
        'A': {'C': 2, 'D': 3},
        'B': {'E': 4},
        'C': {},
        'D': {'G': 2},
        'E': {'G': 1},
        'G': {}
    }
    heuristic2 = {
        'S': 7,
        'A': 6,
        'B': 4,
        'C': 3,
        'D': 2,
        'E': 1,
        'G': 0
    }
    start_node2 = 'S'
    goal_node2 = 'G'
    path_found2 = greedy_best_first_search(graph2, start_node2, goal_node2, heuristic2)
    if path_found2:
        print(f"Path from {start_node2} to {goal_node2}: {path_found2}")
    else:
        print(f"No path found from {start_node2} to {goal_node2}")
