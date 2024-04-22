graph = {}
num_nodes = int(input("Enter the number of nodes in the graph: "))
for i in range(num_nodes):
    node_str = input(f"Enter the neighbors for node {i}: ")
    neighbors = [int(x) for x in node_str.split()]
    graph[i] = neighbors

print(graph)