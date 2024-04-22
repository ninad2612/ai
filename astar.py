import heapq

def astar(graph, start, goal, heuristic):
    open_set = [(0, start)]  
    came_from = {} 
    g_score = {node: float('inf') for node in graph} 
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}  
    f_score[start] = heuristic[start]

    while open_set:
        current_f_score, current = heapq.heappop(open_set)

        if current == goal:
            path = reconstruct_path(came_from, current)
            return path

        for neighbor, cost in graph.get(current, {}).items():
            tentative_g_score = g_score[current] + cost
            tentative_f_score = tentative_g_score + heuristic[neighbor]

            if tentative_f_score < f_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_f_score
                heapq.heappush(open_set, (tentative_f_score, neighbor))

    return None

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return list(reversed(total_path))


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {'G': 1},
    'E': {'G': 3},
    'F': {'G': 2},
    'G': {}
}


heuristic = {
    'A': 9,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 5,
    'F': 4,
    'G': 0
}

start_node = 'A'
goal_node = 'G'

path = astar(graph, start_node, goal_node, heuristic)

if path:
    print(f"Path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}")
