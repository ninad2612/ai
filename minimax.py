# A simple Python3 program to find
# maximum score that
# maximizing player can get
import math

def minimax (curDepth, nodeIndex,
			maxTurn, scores, 
			targetDepth):

	# base case : targetDepth reached
	if (curDepth == targetDepth): 
		return scores[nodeIndex]
	
	if (maxTurn):
		return max(minimax(curDepth + 1, nodeIndex * 2, 
					False, scores, targetDepth), 
				minimax(curDepth + 1, nodeIndex * 2 + 1, 
					False, scores, targetDepth))
	
	else:
		return min(minimax(curDepth + 1, nodeIndex * 2, 
					True, scores, targetDepth), 
				minimax(curDepth + 1, nodeIndex * 2 + 1, 
					True, scores, targetDepth))
	
# Driver code
scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(scores), 2)

print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))

# This code is contributed
# by rootshadow

minimax: This is the main function implementing the Minimax algorithm. It takes several parameters:
curDepth: The current depth in the game tree.
nodeIndex: The current node index.
maxTurn: A boolean flag indicating whether it's the maximizing player's turn (True) or the minimizing player's turn (False).
scores: A list containing the scores associated with each leaf node in the game tree.
targetDepth: The depth of the game tree.
The function recursively traverses the game tree and returns the maximum score achievable by the maximizing player if maxTurn is True, or the minimum score achievable by the minimizing player if maxTurn is False.
Base Case: When the curDepth equals the targetDepth, the function returns the score associated with the current node index.
In each recursive step:
If it's the maximizing player's turn (maxTurn == True), it selects the maximum score between the scores of its left and right child nodes.
If it's the minimizing player's turn (maxTurn == False), it selects the minimum score between the scores of its left and right child nodes.
treeDepth: The depth of the game tree is calculated using logarithm base 2 of the number of scores provided.
Example Usage: The code provides an example of using the Minimax algorithm with a list of scores representing the leaf nodes of the game tree. It prints the optimal value (maximum score achievable by the maximizing player) found by the Minimax algorithm.
