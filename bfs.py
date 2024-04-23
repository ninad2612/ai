import collections

# BFS algorithm with goal node
def bfs(graph, start, goal):
    # Create a queue for BFS
    queue = collections.deque()

    # Create a set to track visited nodes
    visited = set()

    # Mark the start node as visited and enqueue it
    visited.add(start)
    queue.append(start)

    # Loop until the queue is empty
    while queue:
        # Dequeue a vertex from the front of the queue
        node = queue.popleft()

        # If the dequeued node is the goal node, return
        if node == goal:
            print(f"Goal node {goal} reached!")
            return

        # If not, print the current node
        print(node, end=" ")

        # Enqueue all unvisited neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # If the goal node is not found, print a message
    print(f"\nGoal node {goal} not found.")

if __name__ == '__main__':
    # Define the graph as a dictionary
    graph = {
        0: [1, 2],
        1: [2],
        2: [3],
        3: [1, 2]
    }

    # Call the BFS function with the start node and goal node
    print("Following is the Breadth-First Search traversal:")
    bfs(graph, 0, 3)

Initialize a queue to store nodes to be visited and a set to track visited nodes.
Add the start node to the queue and mark it as visited.
While the queue is not empty:
Dequeue a node from the front of the queue.
If the dequeued node is the goal node, return, indicating that the goal node has been reached.
Print the value of the dequeued node.
Enqueue all unvisited neighbors of the dequeued node and mark them as visited.
If the goal node is not found after exploring all reachable nodes, print a message indicating that the goal node was not found.
