from queue import Queue

def greedy_bfs(graph, start, goal, heuristic):
    visited = set()
    queue = Queue()
    queue.put((start, [start]))

    while not queue.empty():
        node, path = queue.get()
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            neighbors = graph.get(node, [])
            
           
            neighbors.sort(key=lambda n: heuristic[n])
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.put((neighbor, path + [neighbor]))
                    
    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}


heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 4,
    'F': 2,
    'G': 0
}

start_node = 'A'
goal_node = 'G'

path = greedy_bfs(graph, start_node, goal_node, heuristic)

if path:
    print(f"Path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}")


Initialize a set to track visited nodes and a queue (imported from the queue module) to store nodes to be visited along with their paths from the start node.
Enqueue the start node along with a list containing only the start node (the initial path).
While the queue is not empty:
Dequeue a node along with its path from the front of the queue.
If the dequeued node is the goal node, return the path to the goal.
If the node has not been visited:
Mark the node as visited.
Get the list of neighbors of the current node from the graph.
Sort the neighbors based on their heuristic values (ascending order).
Enqueue each unvisited neighbor along with the updated path (current path + neighbor) to the queue.
If the goal node is not found after exploring all reachable nodes, return None to indicate that no path was found.
