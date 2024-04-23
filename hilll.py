import random

def generate_neighbors(solution):
  neighbors = []
  for i in range(len(solution)):
    for j in range(i + 1, len(solution)):
        neighbor = solution.copy()
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        neighbors.append(neighbor)
        return neighbors
    

def calculate_distance(solution, distances):
  total_distance = 0
  for i in range(len(solution) - 1):
    city1 = solution[i]
    city2 = solution[i + 1]
    total_distance += distances[city1][city2]
    total_distance += distances[solution[-1]][solution[0]]  # Return to starting point
    return total_distance
  

def tsp_hill_climbing(cities, distances):

  current_solution = random.sample(cities, len(cities))
  current_distance = calculate_distance(current_solution, distances)


  while True:
    neighbors = generate_neighbors(current_solution)
    best_neighbor = min(neighbors, key=lambda x: calculate_distance(x, distances))

    if calculate_distance(best_neighbor, distances) < current_distance:
        current_solution = best_neighbor
        current_distance = calculate_distance(best_neighbor, distances)
    else:
        return current_solution, current_distance





# Example usage
cities = [1, 2, 3, 4, 5]
distances = {
  1: {1: 0, 2: 10, 3: 15, 4: 20, 5: 25},
  2: {1: 10, 2: 0, 3: 35, 4: 25, 5: 20},
  3: {1: 15, 2: 35, 3: 0, 4: 30, 5: 10},
  4: {1: 20, 2: 25, 3: 30, 4: 0, 5: 40},
  5: {1: 25, 2: 20, 3: 10, 4: 40, 5: 0}
}

solution, distance = tsp_hill_climbing(cities, distances)
print("Optimal solution:", solution)
print("Optimal distance:", distance)

# OUTPUT can vary bc random fucntion is used
# Optimal solution: [5, 1, 2, 4, 3]
# Optimal distance: 35

generate_neighbors(solution): This function generates neighboring solutions by swapping the positions of two cities in the current solution. It returns a list of all possible neighbors.
calculate_distance(solution, distances): This function calculates the total distance of the given solution based on the distances between cities provided in the distances dictionary.
tsp_hill_climbing(cities, distances): This function implements the Hill Climbing algorithm for the TSP. It starts with a random initial solution, calculates its distance, and then iteratively generates neighboring solutions, selecting the one with the shortest distance. The process continues until no better neighbor can be found.
It utilizes generate_neighbors() to generate neighboring solutions.
It selects the neighbor with the shortest distance and updates the current solution and distance if it improves upon the current best solution.
Example usage: It provides an example of using the algorithm with a set of cities and their distances. It prints the optimal solution (order of cities) and the optimal distance found by the Hill Climbing algorithm.
