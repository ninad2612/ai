def dfs(graph, start):
    # Create a set to track visited nodes
    visited = set()

    # Define a helper function for recursive DFS
    def dfs_helper(node):
        # Mark the node as visited
        visited.add(node)
        print(node, end=" ")  # Print the node (for visualization)

        # Explore unvisited neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    # Call the helper function with the start node
    dfs_helper(start)

if __name__ == '__main__':
    # Define the graph as a dictionary
    graph = {
        0: [1, 2],
        1: [3],
        2: [5,6],
        3: [],
        5:[],
        6:[]
    }

    # Call the DFS function with the start node
    print("Following is the Depth-First Search traversal:")
    dfs(graph, 0)

Initialize a set to track visited nodes.
Define a recursive helper function dfs_helper that takes a node as an argument:
Mark the current node as visited.
Print the value of the current node (for visualization purposes).
Explore all unvisited neighbors of the current node recursively by calling dfs_helper on each neighbor.
Call the dfs_helper function with the start node to initiate the DFS traversal.
