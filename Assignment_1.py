import itertools

morse_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
              '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
              '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
              '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
              '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'}

import re

def morseDecode(inputStringList):
    """
    	This method should take a list of strings as input. Each string is equivalent to one letter
    	(i.e. one morse code string). The entire list of strings represents a word.

    	This method should convert the strings from morse code into english, and return the word as a string.

    	"""
    # Please complete this method to perform the above described function
    word = []
    for element in inputStringList:
        word.append(morse_dict.get(element))
    return "".join(word)



def morsePartialDecode(inputStringList):
	"""
	This method should take a list of strings as input. Each string is equivalent to one letter
	(i.e. one morse code string). The entire list of strings represents a word.

	However, the first character of every morse code string is unknown (represented by an 'x' (lowercase))
	For example, if the word was originally TEST, then the morse code list string would normally be:
	['-','.','...','-']

	However, with the first characters missing, I would receive:
	['x','x','x..','x']

	With the x unknown, this word could be TEST, but it could also be EESE or ETSE or ETST or EEDT or other permutations.

	We define a valid words as one that exists within the dictionary file provided on the website, dictionary.txt
	When using this file, please always use the location './dictionary.txt' and place it in the same directory as
	the python script.

	This function should find and return a list of strings of all possible VALID words.
	"""

	dictionaryFileLoc = './dictionary.txt'
	# Please complete this method to perform the above described function

	with open(dictionaryFileLoc, "r") as f:
		file = f.read()
	dict = set(re.split(r'\n', file.upper()))  # after reading the file, we have to split it and store each word in uppercase an store it into a set
	options = []

	for element in inputStringList:
		"""We have to check each element of the list and get the two options (dash and point), sotre the into a list
        and make all possible combinations to get all the valid/non valid words"""
		letters = [morse_dict.get(re.sub('x', '-', element)), morse_dict.get(re.sub('x', '.', element))]
		options.append(letters)
	words = list(itertools.product(*options))
	valid_words = []
	for word in words:
		"""Now let's check which of the words are valid"""
		if "".join(word) in dict:
			valid_words.append("".join(word))

	return valid_words

class Maze:
	def __init__(self):
		"""
		Constructor - You may modify this, but please do not add any extra parameters
		"""
		self.mylist = None
		self.opens = []

	def createlist(self, x, y, createx, createy, blockType):

		if createx is None and createy is None:
			''' Create the maze filled with walls and just the designates open spot '''
			mylist = [['1']] * (x + 1)
			for i in range(0, x + 1):
				mylist[i] = ['1'] * (y + 1)
			mylist[x][y] = blockType
			self.mylist = mylist


		elif createx is not None and createy is None:
			''' Make an extention to the current maze when needed '''
			self.maze_width = x # store new width
			lastx = len(self.mylist)
			self.mylist = self.mylist + ([['1'] * (y + 1)] * createx)
			for i in range(lastx, lastx + createx - 1):
				self.mylist[i] = ['1'] * (y + 1)
			self.mylist[x][y] = blockType

		elif createx is None and createy is not None:
			self.maze_heihg = y # store new heigh
			for i in range(0, len(self.mylist)):
				self.mylist[i] = self.mylist[i] + (['1'] * createy)
			self.mylist[x][y] = blockType

		elif createx is not None and createx is not None:
			self.maze_width = x # store new width and heigh
			self.maze_heihg = y
			lastx = len(self.mylist)
			self.mylist = self.mylist + ([['1'] * (y + 1)] * createx)
			for i in range(0, x):
				self.mylist[i] = self.mylist[1] + (['1'] * createy)
			self.mylist[x][y] = blockType

	def addCoordinate(self,x,y,blockType):
		"""
		Add information about a coordinate on the maze grid
		x is the x coordinate
		y is the y coordinate
		blockType should be 0 (for an open space) of 1 (for a wall)
		"""
		# Please complete this method to perform the above described function


		if (blockType == 0):
			''' Store the open spaces '''
			self.opens.append((x,y))

		''' Check if there is no list yet created '''
		if self.mylist is None:
			self.createlist(x, y, None, None, str(blockType))
			self.maze_width = x # Store the size of the maze
			self.maze_heihg = y
		else:
			''' If there is one, then only extend the existent one  but checking if we have to  add columns, rows or both '''
			createx = x - len(self.mylist) + 1
			createy = y - len(self.mylist[0]) + 1
			if createx <= 0:
				createx = None
			if createy <= 0:
				createy = None
			if createx is None and createy is None:
				self.mylist[x][y] = str(blockType)
			else:
				self.createlist(x, y, createx=createx, createy=createy, blockType=str(blockType))

		''' Store the size of the maze '''




	def printMaze(self):
		"""
		Print out an ascii representation of the maze.
		A * indicates a wall and a empty space indicates an open space in the maze
		"""
		printer = list(itertools.zip_longest(*self.mylist))
		for i in range(len(printer)):
			temp = ' '.join(printer[i])
			temp = re.sub('1', '*', temp)
			temp = re.sub('0', ' ', temp)
			print(temp)


	def adjacent_cell(self, x, y):
		''' Looks for the open adjacent cells of coord (x,y) '''
		cells = []
		if (x + 1, y) in self.opens:
			cells.append((x + 1, y))
		if (x, y - 1) in self.opens:
			cells.append((x, y - 1))
		if (x - 1, y) in self.opens:
			cells.append((x-1,y))
		if (x, y + 1) in self.opens:
			cells.append((x,y + 1))

		return cells

	def redo_path(self, cameFrom, current):
		''' Go back on all the visited path and return the list '''
		total_path = [current]
		while current in cameFrom.keys():
			current = cameFrom[current] # for each cell, find the previous one
			total_path.insert(0, current) # insert it at the beginning to print it orderly
		return total_path

	def manh_dist(self, point, goal):
		''' Compute manhattan distance '''
		dist = abs(point[0] - goal[1]) + abs(point[1] - goal[1])
		return dist


	def findRoute(self,x1,y1,x2,y2):
		"""
		This method should find a route, traversing open spaces, from the coordinates (x1,y1) to (x2,y2)
		It should return the list of traversed coordinates followed along this route as a list of tuples (x,y),
		in the order in which the coordinates must be followed
		If no route is found, return an empty list
		"""
		start = (x1,y1)
		goal = (x2,y2)

		closedSet = set()
		openSet = {start}
		cameFrom = {}

		tuple_key = []
		for col in range(self.maze_width):
			for row in range(self.maze_heihg):
				tuple_key.append((col, row))

		# Create a dictionary with all the inicial weights

		gScore = dict(zip(tuple_key, [1000000000] * len(tuple_key)))
		fScore = dict(zip(tuple_key, [1000000000] * len(tuple_key)))

		gScore[start] = 0
		fScore[start] = self.manh_dist(start, goal)

		while openSet:
			'''Get the node in open set with the minimum fScore'''
			min_value = 2000000000
			for cell in openSet:
				if fScore[cell] < min_value:
					min_value = fScore[cell]
					current = cell
			if current == goal: # if current node is the goal, we are done
				return self.redo_path(cameFrom, current) # return all the path

			openSet.pop() # take out the current node from the options to evaluate
			closedSet.add(current) # and add it to the visited ones
			adjacent_nodes = self.adjacent_cell(current[0], current[1]) # check for all the possible next steps (adjacent and open spots)
			for neighbor in adjacent_nodes:
				if neighbor in closedSet: # if the point has been visited, continue to the next one
					continue
				tentative_gScore = gScore[current] + 1

				if neighbor not in openSet:
					openSet.add(neighbor) # possible next step
				elif tentative_gScore >= gScore[neighbor]:
					continue  # Not a better path

				cameFrom[neighbor] = current #store the path
				gScore[neighbor] = tentative_gScore
				fScore[neighbor] = gScore[neighbor] + self.manh_dist(neighbor, goal)
		return []


def morseCodeTest():
	"""
	This test program passes the morse code as a list of strings for the word
	HELLO to the decode method. It should receive a string "HELLO" in return.
	This is provided as a simple test example, but by no means covers all possibilities, and you should
	fulfill the methods as described in their comments.
	"""

	hello = ['....','.','.-..','.-..','---']
	print(morseDecode(hello))

def partialMorseCodeTest():

	"""
	This test program passes the partial morse code as a list of strings
	to the morsePartialDecode method. This is provided as a simple test example, but by
	no means covers all possibilities, and you should fulfill the methods as described in their comments.
	"""

	# This is a partial representation of the word TEST, amongst other possible combinations
	test = ['x','x','x..','x']
	print(morsePartialDecode(test))

	# This is a partial representation of the word DANCE, amongst other possible combinations
	dance = ['x..','x-','x.','x.-.','x']
	print(morsePartialDecode(dance))

def mazeTest():
	"""
	This sets the open space coordinates for the example
	maze in the assignment.
	The remainder of coordinates within the max bounds of these specified coordinates
	are assumed to be walls
	"""
	myMaze = Maze()
	myMaze.addCoordinate(1,0,0)
	myMaze.addCoordinate(1,1,0)
	myMaze.addCoordinate(7,1,0)
	myMaze.addCoordinate(1,2,0)
	myMaze.addCoordinate(2,2,0)
	myMaze.addCoordinate(3,2,0)
	myMaze.addCoordinate(4,2,0)
	myMaze.addCoordinate(6,2,0)
	myMaze.addCoordinate(7,2,0)
	myMaze.addCoordinate(4,3,0)
	myMaze.addCoordinate(7,3,0)
	myMaze.addCoordinate(4,4,0)
	myMaze.addCoordinate(7,4,0)
	myMaze.addCoordinate(3,5,0)
	myMaze.addCoordinate(4,5,0)
	myMaze.addCoordinate(7,5,0)
	myMaze.addCoordinate(1,6,0)
	myMaze.addCoordinate(2,6,0)
	myMaze.addCoordinate(3,6,0)
	myMaze.addCoordinate(4,6,0)
	myMaze.addCoordinate(5,6,0)
	myMaze.addCoordinate(6,6,0)
	myMaze.addCoordinate(7,6,0)
	myMaze.addCoordinate(5,7,0)
	myMaze.printMaze()
	print(myMaze.findRoute(1,0,7,2))
	print(myMaze.findRoute(1,0,7,1))

def main():
	morseCodeTest()
	partialMorseCodeTest()
	mazeTest()

if(__name__ == "__main__"):
	main()
