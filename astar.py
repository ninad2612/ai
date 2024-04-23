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



Initialize the open set with the start node, setting its g-score (the cost of getting from the start node to that node) to 0 and its f-score (the sum of g-score and the heuristic estimate) to the heuristic value for the start node.
While the open set is not empty:
Pop the node with the lowest f-score from the open set.
If the popped node is the goal node, reconstruct the path and return it.
Otherwise, for each neighbor of the current node:
Calculate the tentative g-score for the neighbor by adding the cost of the current node to the neighbor's g-score.
Calculate the tentative f-score for the neighbor by adding its tentative g-score to the heuristic estimate.
If the tentative f-score is lower than the current f-score for the neighbor:
Update the came_from dictionary to remember the path.
Update the g-score and f-score of the neighbor.
Add the neighbor to the open set with its updated f-score.
If the open set becomes empty and the goal node hasn't been reached, return None, indicating that there's no path from the start node to the goal node.
