#23110058 Abdul Hannan Chaudhry
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
	"""
	This class outlines the structure of a search problem, but doesn't implement
	any of the methods (in object-oriented terminology: an abstract class).

	You do not need to change anything in this class, ever.
	"""

	def getStartState(self):
		"""
		Returns the start state for the search problem.
		"""
		util.raiseNotDefined()

	def isGoalState(self, state):
		"""
		  state: Search state

		Returns True if and only if the state is a valid goal state.
		"""
		util.raiseNotDefined()

	def getSuccessors(self, state):
		"""
		  state: Search state

		For a given state, this should return a list of triples, (successor,
		action, stepCost), where 'successor' is a successor to the current
		state, 'action' is the action required to get there, and 'stepCost' is
		the incremental cost of expanding to that successor.
		"""
		util.raiseNotDefined()

	def getCostOfActions(self, actions):
		"""
		 actions: A list of actions to take

		This method returns the total cost of a particular sequence of actions.
		The sequence must be composed of legal moves.
		"""
		util.raiseNotDefined()


def tinyMazeSearch(problem):
	"""
	Returns a sequence of moves that solves tinyMaze.  For any other maze, the
	sequence of moves will be incorrect, so only use this for tinyMaze.
	"""
	from game import Directions
	s = Directions.SOUTH
	w = Directions.WEST
	return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
	"""
	Search the deepest nodes in the search tree first.

	Your search algorithm needs to return a list of actions that reaches the
	goal. Make sure to implement a graph search algorithm.

	To get started, you might want to try some of these simple commands to
	understand the search problem that is being passed in:
		"""
	# print("Start:", problem.getStartState())
	# print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
	# print("Start's successors:", problem.getSuccessors(problem.getStartState()))
			
	"Start of Your Code"

	coordinates = problem.getStartState()
	frontier = util.Stack()
	frontier.push((coordinates,[]))
	explored = []

	while frontier.isEmpty() == False:
		node,path = frontier.pop()

		if problem.isGoalState(node) == False:
			successors = problem.getSuccessors(node)
			explored.append(node)

			for i,j,k in successors:

				if(i not in explored):
					frontier.push((i,path+[j]))
		elif problem.isGoalState(node) == True:
			return path

	"End of Your Code"

# ________________________________________________________________

class _RecursiveDepthFirstSearch(object):
	'''
		=> Output of 'recursive' dfs should match that of 'iterative' dfs you implemented
		above. 
		Key Point: Remember in tutorial you were asked to expand the left-most child 
		first for dfs and bfs for consistency. If you expanded the right-most
		first, dfs/bfs would be correct in principle but may not return the same
		path. 

		=> Useful Hint: self.problem.getSuccessors(node) will return children of 
		a node in a certain "sequence", say (A->B->C), If your 'recursive' dfs traversal 
		is different from 'iterative' traversal, try reversing the sequence.  

	'''
	def __init__(self, problem):
		" Do not change this. " 
		# You'll save the actions that recursive dfs found in self.actions. 
		self.actions = [] 
		# Use self.explored to keep track of explored nodes.  
		self.explored = set()
		self.problem = problem

	def RecursiveDepthFirstSearchHelper(self, node):
		'''
		args: start node 
		outputs: bool => True if path found else Fasle.
		'''
		"Start of Your Code"
  
		successors = self.problem.getSuccessors(node)
		successors = successors[::-1]

		if self.problem.isGoalState(node) == True:
			return True

		elif self.problem.isGoalState(node) == False:

			for x in range(0,len(successors)):
				leaf = successors[x][0]
				if leaf not in self.explored:

					self.explored.add(leaf)

					if self.RecursiveDepthFirstSearchHelper(leaf) == True:
						action = successors[x][1]
						self.actions.append(action)
						return True

		"End of Your Code"


def RecursiveDepthFirstSearch(problem):
	" You need not change this function. "
	# All your code should be in member function 'RecursiveDepthFirstSearchHelper' of 
	# class '_RecursiveDepthFirstSearch'."

	node = problem.getStartState() 
	rdfs = _RecursiveDepthFirstSearch(problem)
	path_found = rdfs.RecursiveDepthFirstSearchHelper(node)
	return list(reversed(rdfs.actions)) # Actions your recursive calls return are in opposite order.
# ________________________________________________________________


def depthLimitedSearch(problem, limit = 129): #BIG MAZE LIMIT = 228

	"""
	Search the deepest nodes in the search tree first as long as the
	nodes are not not deeper than 'limit'.

	For medium maze, pacman should find food for limit less than 130. 
	If your solution needs 'limit' more than 130, it's bogus.
	Specifically, for:
	'python pacman.py -l mediumMaze -p SearchAgent -a fn=dls', and limit=130
	pacman should work normally.  

	Your search algorithm needs to return a list of actions that reaches the
	goal. Make sure to implement a graph search algorithm.
	Autograder cannot test this function.  

	Hints: You may need to store additional information in your frontier(queue).

		"""

	"Start of Your Code"
 
	state = problem.getStartState()
	frontier = util.Stack()
	frontier.push((state, [],0))
	explored = []
	explored.append(state)

	while frontier.isEmpty() == False :
		node, actions, depth = frontier.pop()

		if problem.isGoalState(node) == False:

			explored.append(node)
			successors = problem.getSuccessors(node)

			for i,j,k in successors:
				if i not in explored:
					frontier.push((i,actions + [j], depth+1))

		elif problem.isGoalState(node) == True:
			return actions

		if depth>limit+1:
			return explored

	"End of Your Code"

# ________________________________________________________________

class _RecursiveDepthLimitedSearch(object):
	'''
		=> Output of 'recursive' dfs should match that of 'iterative' dfs you implemented
		above. 
		Key Point: Remember in tutorial you were asked to expand the left-most child 
		first for dfs and bfs for consistency. If you expanded the right-most
		first, dfs/bfs would be correct in principle but may not return the same
		path. 

		=> Useful Hint: self.problem.getSuccessors(node) will return children of 
		a node in a certain "sequence", say (A->B->C), If your 'recursive' dfs traversal 
		is different from 'iterative' traversal, try reversing the sequence.  

	'''
	def __init__(self, problem):
		" Do not change this. " 
		# You'll save the actions that recursive dfs found in self.actions. 
		self.actions = [] 
		# Use self.explored to keep track of explored nodes.  
		self.explored = set()
		self.problem = problem
		self.current_depth = 0
		self.depth_limit = 204 # For medium maze, You should find solution for depth_limit not more than 204.

	def RecursiveDepthLimitedSearchHelper(self, node):
		'''
		args: start node 
		outputs: bool => True if path found else Fasle.
		'''

		"Start of Your Code"
  
		successors = self.problem.getSuccessors(node)
		successors.reverse()
  		
		if self.depth_limit >= self.current_depth:

			if self.problem.isGoalState(node) == False:
				if node not in self.explored:
					self.explored.add(node)

					for i,j,k in successors:

						if i not in self.explored:

							if self.RecursiveDepthLimitedSearchHelper(i) == True:
								self.actions.append(j)
								self.current_depth += self.current_depth
								return True

			elif self.problem.isGoalState(node) == True:
				return True

			return False
		"End of Your Code"


def RecursiveDepthLimitedSearch(problem):
	"You need not change this function. All your code in member function RecursiveDepthLimitedSearchHelper"
	node = problem.getStartState() 
	rdfs = _RecursiveDepthLimitedSearch(problem)
	path_found = rdfs.RecursiveDepthLimitedSearchHelper(node)
	return list(reversed(rdfs.actions)) # Actions your recursive calls return are in opposite order.
# ________________________________________________________________


def breadthFirstSearch(problem):
	"""Search the shallowest nodes in the search tree first."""

	"Start of Your Code"
 
	coordinates = problem.getStartState()
	frontier = util.Queue()
	frontier.push((coordinates,[]))
	explored = []
	explored.append(coordinates)

	while frontier.isEmpty() == False:
		node,path = frontier.pop()

		if problem.isGoalState(node) == False:
			successors = problem.getSuccessors(node)
			
			for i,j,k in successors:

				if not i in explored:
					explored.append(i)
					frontier.push((i,path+[j]))

		elif problem.isGoalState(node) == True:
			return path

		"End of Your Code"


def uniformCostSearch(problem):
	"""Search the node of least total cost first.
	   You may need to pay close attention to util.py.
	   Useful Reminder: Note that problem.getSuccessors(node) returns "step_cost". 

	   Key Point: If a node is already present in the queue with higher path cost 
	   (or higher priority), you'll update its cost (or priority) 
	   (Similar to pseudocode in figure 3.14 of your textbook.). 
	   Be careful, autograder cannot catch this bug.
	"""

	"Start of Your Code"
 
	coordinates = problem.getStartState()
	frontier = util.PriorityQueue()
	frontier.push((coordinates,[]),0)
	explored = []

	while frontier.isEmpty() == False:
		node,path = frontier.pop()

		if problem.isGoalState(node[0]) == False:

			if node[0] not in explored:
				successors = problem.getSuccessors(node[0])
				explored.append(node[0])

				for i,j,k in successors:
					if i not in explored:
						cost = problem.getCostOfActions(node[1] + [j])
						frontier.push((i,node[1]+[j]), cost)
		elif problem.isGoalState(node[0]) == True:
			return node[1]

	"End of Your Code"

def nullHeuristic(state, problem=None):
	"""
	A heuristic function estimates the cost from the current state to the nearest
	goal in the provided SearchProblem.  This heuristic is trivial.
	"""
	return 0

def aStarSearch(problem, heuristic=nullHeuristic):
	'''
	Pay clos attention to util.py- specifically, args you pass to member functions. 

	Key Point: If a node is already present in the queue with higher path cost 
	(or higher priority), you'll update its cost (or priority) 
	(Similar to pseudocode in figure 3.14 of your textbook.). 
	Be careful, autograder cannot catch this bug.

	'''
	"Start of Your Code"
 
	coordinates = problem.getStartState()
	frontier = util.PriorityQueue()
	frontier.push((coordinates,[]),0)
	explored = []

	while frontier.isEmpty() == False:
		node,path = frontier.pop()

		if problem.isGoalState(node[0]) == False:

			if node[0] not in explored:
				successors = problem.getSuccessors(node[0])
				explored.append(node[0])

				for i,j,k in successors:
					if i not in explored:
						cost = problem.getCostOfActions(node[1] + [j])
						h_stic = heuristic(i,problem)
						heuristic_cost = cost + h_stic
						frontier.push((i,node[1]+[j]),heuristic_cost)
		elif problem.isGoalState(node[0]) == True:
			return node[1]

	"End of Your Code"


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
rdfs = RecursiveDepthFirstSearch
dls = depthLimitedSearch
rdls = RecursiveDepthLimitedSearch
astar = aStarSearch
ucs = uniformCostSearch
