# A perfect Tic Tac Toe player using the strategy in Newell and Simon's 1972 tic-tac-toe program.

# Initial Variable
gameBoard = [[0,0,0],[0,0,0],[0,0,0]]	#Testing
count = 0	# Keep track of the filling progress
log=[]	# The log of the coordinate
isComputerFirst = 0 # 0 for User go first and 1 for computer go first
Undetermined, User, Computer = range(3)

# Subject to removal #
# Board Function
def printBoard():
	print ''
	print "    1   2   3"
	print "  +-----------+"
	for row in range(3):
		rowPrint = str(row+1) + " |"
		for element in gameBoard[row]:
			if element == Undetermined:	# Empty Space
				rowPrint += "   |"
			elif element == User:	# User's Mark
				rowPrint += " X |"
			elif element == Computer:	# Program's Mark
				rowPrint += " O |"
			else:
				print "Something Wrong!!!!"
		print rowPrint
		print "  +-----------+"
	print ''

# why the hell is and else have the same instruction??? #
# A log for gaming progress
def logInput(activePlayer, coordinate):
	if activePlayer:
		log.append(coordinate)
	else:
		log.append(coordinate)

# Put down a mark
def putMark(isUser, coordinate):
	global count 
	count += 1
	logInput(isUser, coordinate)
	gameBoard[coordinate[0]-1][coordinate[1]-1]= 1 if isUser else 2

# Check every possible solution, but might be able to improve
# Give number for each cell and then we can sum each colum or row or diagno to check win.

# Potential optimization: only check the three potential win options surrounding the last moved slot #

def winCheck():
	# Add 4 for program
	# Add 1 for user
	columWin = [0,0,0]

	# Check row and colum
	for i in range(3):
		# Check Row
		if gameBoard[i] == [User,User,User]:
			return User
		elif gameBoard[i] == [Computer,Computer,Computer]:
			return Computer
		# Mark Column
		for j in range(3):
			if gameBoard[i][j] == User:
				columWin[j] += 1
			elif gameBoard[i][j] == Computer:
				columWin[j] += 4

	# Check Colum
	for x in columWin:
		if x == 3:
			return User
		elif x == 12:
			return Computer

	# Check diagonal:
	PlayerAtCenter = gameBoard[1][1]
	if(gameBoard[0][0] == PlayerAtCenter and PlayerAtCenter == gameBoard[2][2]) \
			or(gameBoard[0][2] == PlayerAtCenter and PlayerAtCenter == gameBoard[2][0]):
		# Will return 0 when both diagonal is not occupied
		return PlayerAtCenter

	return 0 

# Check if the program win by putting one mark, or if the user can win by putting one mark
# If User=True, check if the user can win
def potentialWinCheck(isUser):
	# 4 for program
	# 1 for user
	if isUser:
		test = 1
	else:
		test = 4

	# Counting for winning
	columWin=[0,0,0]
	rowWin = [0,0,0]

	# Counting for row and column
	for i in range(3):
		for j in range(3):
			if gameBoard[i][j] == Computer:
				rowWin[i] += 4
				columWin[j] += 4
			elif gameBoard[i][j] == User:
				rowWin[i] += 1
				columWin[j] += 1

	# Check row
	for i in range(3):
		if(rowWin[i]==2*test):
			for j in range(3):
				if(gameBoard[i][j]==Undetermined):
					return (i,j)
	# Check column
	for j in range(3):
		if(columWin[j]==2*test):
			for i in range(3):
				if(gameBoard[i][j]==Undetermined):
					return (i,j)

	# Check diagonal series
	if(gameBoard[0][0]==gameBoard[1][1] and gameBoard[2][2]==Undetermined and gameBoard[1][1]==(test+1)/2):
		return (2,2)
	if(gameBoard[1][1]==gameBoard[2][2] and gameBoard[0][0]==Undetermined and gameBoard[2][2]==(test+1)/2):
		return (0,0)
	if(gameBoard[0][2]==gameBoard[1][1] and gameBoard[2][0]==Undetermined and gameBoard[1][1]==(test+1)/2):
		return (2,0)
	if(gameBoard[1][1]==gameBoard[2][0] and gameBoard[0][2]==Undetermined and gameBoard[2][0]==(test+1)/2):
		return (0,2)
	if(gameBoard[0][0]==gameBoard[2][2] and gameBoard[1][1]==Undetermined and gameBoard[2][2]==(test+1)/2) \
			or (gameBoard[0][2]==gameBoard[2][0] and gameBoard[1][1]==Undetermined and gameBoard[2][0]==(test+1)/2):
		return (1,1)

	# If no win
	return False

# check the possibility for forking
def fork(isUser):
	# threat
	threat=[]

	# 2 for program
	# 1 for user
	if isUser:
		test = 1
	else:
		test = 2

	# Counting for winning
	columWin=[0,0,0]
	rowWin = [0,0,0]

	# Counting for row and column
	for i in range(3):
		for j in range(3):
			if gameBoard[i][j]==Undetermined:
				rowWin[i] += 1
				columWin[j] += 1

	# Check row
	for i in range(3):
		if(rowWin[i]==2):
			for j in range(3):
				if(gameBoard[i][j]==test):
					threat.append((i,(j+1)%3))
					threat.append((i,(j+2)%3))
	# Check column
	for j in range(3):
		##### Why is this twice test instead of 4??? #####
		if(columWin[j]==2*test):
			for i in range(3):
				if(gameBoard[i][j]==test):
					threat.append(((i+1)%3,j))
					threat.append(((i+2)%3,j))

	# Check diagonal series
	if(gameBoard[0][0]==gameBoard[1][1] and gameBoard[2][2]==test and gameBoard[1][1]==Undetermined):
		threat.append((0,0))
		threat.append((1,1))
	if(gameBoard[0][0]==gameBoard[2][2] and gameBoard[1][1]==test and gameBoard[2][2]==Undetermined):
		threat.append((0,0))
		threat.append((2,2))
	if(gameBoard[1][1]==gameBoard[2][2] and gameBoard[0][0]==test and gameBoard[2][2]==Undetermined):
		threat.append((1,1))
		threat.append((2,2))
	if(gameBoard[0][2]==gameBoard[1][1] and gameBoard[2][0]==test and gameBoard[1][1]==Undetermined):
		threat.append((0,2))
		threat.append((1,1))
	if(gameBoard[0][2]==gameBoard[2][0] and gameBoard[1][1]==test and gameBoard[2][0]==Undetermined):
		threat.append((0,2))
		threat.append((2,0))
	if(gameBoard[1][1]==gameBoard[2][0] and gameBoard[0][2]==test and gameBoard[2][0]==Undetermined):
		threat.append((1,1))
		threat.append((2,0))

	for i in range(len(threat)-1):
		for j in range(i+1,len(threat)):
			if(threat[i]==threat[j]):
				return threat[i]

	# If no fork
	return False

# return the key right next to the current key
def rightNext(n):
	if (n==2):
		return 1
	else:
		return n+1

# causing a two in a row situation to threat away the fork
# this is basically the fork function but without storing the possible threat
def twoInARow():
	# Counting for winning
	columWin=[0,0,0]
	rowWin = [0,0,0]

	# Counting for row and column
	for i in range(3):
		for j in range(3):
			if gameBoard[i][j]==Undetermined:
				rowWin[i] += 1
				columWin[j] += 1

	# Check row
	for i in range(3):
		if(rowWin[i]==2):
			for j in range(3):
				if(gameBoard[i][j]==Computer):
					return(i,rightNext(j))
	# Check column
	for j in range(3):
		if(columWin[j]==2*Computer):
			for i in range(3):
				if(gameBoard[i][j]==Computer):
					return (rightNext(i),j)

	#Check diagonal series
	if(gameBoard[0][0]==gameBoard[1][1] and gameBoard[2][2]==Computer and gameBoard[1][1]==Undetermined):
		return (1,1)
	if(gameBoard[0][0]==gameBoard[2][2] and gameBoard[1][1]==Computer and gameBoard[2][2]==Undetermined):
		return (2,2)
	if(gameBoard[1][1]==gameBoard[2][2] and gameBoard[0][0]==Computer and gameBoard[2][2]==Undetermined):
		return (1,1)
	if(gameBoard[0][2]==gameBoard[1][1] and gameBoard[2][0]==Computer and gameBoard[1][1]==Undetermined):
		return (1,1)
	if(gameBoard[0][2]==gameBoard[2][0] and gameBoard[1][1]==Computer and gameBoard[2][0]==Undetermined):
		return (2,0)
	if(gameBoard[1][1]==gameBoard[2][0] and gameBoard[0][2]==Computer and gameBoard[2][0]==Undetermined):
		return (1,0)

	# If no two in a row
	return False


# User Moving Function
def checkCoordinateRange(coordinate):
	return len(coordinate)==2 and coordinate[0]<=3 and coordinate[1]<=3 and coordinate[0]>0 and coordinate[1]>0 and gameBoard[coordinate[0]-1][coordinate[1]-1]==0

# Get the coordinate from user
def readCoordinate():
	coordinate = input("Please Give the coordinate of your mark in the form of (row, column) -->")
	if(checkCoordinateRange(coordinate)):
		return coordinate
	else:
		print ("Please make sure the input coordinate is in range and empty. Try again :)")
		return readCoordinate()

# Get user input and putmark
def userMove():
	coordinate = readCoordinate()
	putMark(True, coordinate)


# Program Moving Function
def programMove():
	# 1st check if the program can win
	win = potentialWinCheck(False)
	if (win!=False):
		putMark(False,programCoordinate(win))
		return
	# 2nd block user's win
	block = potentialWinCheck(True)
	if (block!=False):
		putMark(False,programCoordinate(block))
		return
	# 3rd try to fork
	programFork = fork(False)
	if (programFork!=False):
		putMark(False,programCoordinate(programFork))
		return

	# 4th try to block fork by threatening with a two in a row
	userFork = fork(True)
	if (userFork!=False):
		tryBlock = twoInARow()
		if(tryBlock!=False):
			putMark(False,programCoordinate(tryBlock))
		return

	# 5th put in the center
	if (center()):
		putMark(False,(2,2))
		return
	# 6th try opponent corner
	programOppoCorner = oppoCorner()
	if (programOppoCorner!=False):
		putMark(False,programCoordinate(programOppoCorner))
		return
	# 7th get the corner
	programCorner = getCorner()
	if (programCorner!=False):
		putMark(False,programCoordinate(programCorner))
		return
	# 8th get the side
	programSide = getSide()
	if (programSide!=False):
		putMark(False,programCoordinate(programSide))
		return

def getSide():
	if gameBoard[1][0]==Undetermined:
		return (1,0)
	elif gameBoard[2][1]==Undetermined:
		return (2,1)
	elif gameBoard[1][2]==Undetermined :
		return (1,2)
	elif gameBoard[0][1]==Undetermined:
		return (0,1)
	else:
		return False

def getCorner():
	if gameBoard[2][2]==Undetermined:
		return (2,2)
	elif gameBoard[0][0]==Undetermined:
		return (0,0)
	elif gameBoard[2][0]==Undetermined :
		return (2,0)
	elif gameBoard[0][2]==Undetermined:
		return (0,2)
	else:
		return False

def oppoCorner():
	if(gameBoard[0][0]==User and gameBoard[2][2]==Undetermined):
		return (2,2)
	elif(gameBoard[2][2]==User and gameBoard[0][0]==Undetermined):
		return (0,0)
	elif(gameBoard[0][2]==User and gameBoard[2][0]==Undetermined):
		return (2,0)
	elif(gameBoard[2][0]==User and gameBoard[0][2]==Undetermined):
		return (0,2)
	else:
		return False

def center():
	return gameBoard[1][1]==Undetermined

# the purMark are optimized for user, so we need to increment the coor that program generate
def programCoordinate(coor):
	return (coor[0]+1,coor[1]+1)

# Main Function
def main():
	# Prepare
	winner = Undetermined

	# Starter
	print "Welcome to the tic tac toe game!"

	# Loop
	while (winner == Undetermined and count!=9):
		if(count%2==isComputerFirst):
			printBoard()
			userMove()
		else:
			programMove()
		winner = winCheck()

	if winner != Undetermined:
		print ''
		print "You Win! And please report you strategy to the author!" if winner == User else "The Computer Wins!"
	else:
		print ''
		print "It's a tie!"
	printBoard()

if __name__ == '__main__':
	main()
