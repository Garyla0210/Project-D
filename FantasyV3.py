#import myExample makes it run that PY code
import pandas as pd

class User:
	def __init__(self,userName):
		self.name = userName
		self.players = [] # player storage
		self.score = [] # win/loss
		self.points = [] # total points per week

class Player:
	def __init__(self,playerName):
		self.name = playerName
		self.team = teamName
		self.stats = [[]] # array of - list of K,D,A,weekly points

def main():
	userStorage = [] # storage of users
	poolStorage = [] # storage of players
	print("Please choose one of the following:")
	print("1. Create")
	print("2. Load")
	dataNumber = int (input())
	if dataNumber == 1:
		userStorage, poolStorage, match = creatingData() # create date
		print("data saved.")
	elif dataNumber == 2:
		userStorage, poolStorage, match = loadingData() # load data
		print("data loaded.")
	else:
		print("error")

	print("Please choose one of the following:")
	print("1. Overview")
	print("2. Roster")
	print("3. Matchup")
	print("4. Trade")
	print("5. Save")
	print("6. Quit")
	dataNumber = int (input())
	while dataNumber != 6:
		if dataNumber == 1:
			overview(userStorage) # summary of standings/latest matchup
		elif dataNumber == 2:
			roster(userStorage) # player roster
		elif dataNumber == 3:
			matchup(match) # all matchups
		elif dataNumber == 4:
			userStorage, poolStorage = trade(userStorage, poolStorage) # trade players
		elif dataNumber == 5:
			savingData(userStorage, poolStorage, match) # save data
		print("Please choose one of the following:")
		print("1. Overview")
		print("2. Roster")
		print("3. Matchup")
		print("4. Trade")
		print("5. Save")
		print("6. Quit")
		dataNumber = int (input())

def createMatchup(userStorage): # create permutations of matchups
	week = []
	match = {}
	
	players = userStorage
	row_1 = []
	row_2 = []
	# scheduling algorithm
	for i in range(0,int(len(players)/2)):
		row_1.append(players[i].name)
	for i in range(int(len(players)-1),int(len(players)/2)-1, -1):
		row_2.append(players[i].name)

	for i in range (0,int(len(players)/2)):
		match["Match " + str(i+1)]=[row_1[i],row_2[i]]
		print(match)
	week.append(match)

	temp = ""
	counter = int(len(players)-1)
	weekCounter = 2
	totalWeeks = 9
	match = {}
	for i in range(0,totalWeeks-1): 
		match = {}
		temp = row_1.pop()
		row_1.insert(1,players[counter].name)
		row_2.pop(0)
		row_2.append(temp)
		counter-=1
		if counter<=0:
			counter = int(len(players)-1)
		else:
			""	

		for i in range(0,int(len(players)/2)):
			match["Match " + str(i+1)]=[row_1[i],row_2[i]]
		week.append(match)
	return week

def overview(userStorage):
	print("standings")
	#standings

def roster(userStorage):
	for l in range(0, len(userStorage)):
		print(userStorage[l].name, "'s current roster is: ")
		for m in range(0, 1):
			print(userStorage[l].players[m])

def matchup(match):
	print(match)
	#view matchup
	# scheduling algorithm round robin
	#display current matchup, and option to see other weeks

def trade(userStorage, poolStorage):
	print("Choose user number: ")
	for i in range (0, len(userStorage)):
		print(str(i+1)+") "+str(userStorage[i].name)) # display users
	choose = int (input())-1
	playerRoster(userStorage, choose) # displayer user player pool
	currentPool(poolStorage) # display player pool
	print("Choose options: ")
	print("1: Trade")
	print("2: Cancel")
	inputFile = int (input(""))
	if inputFile == 1:
		print("Select player you want to swap")
		playerRoster(userStorage, choose)
		inputFile1 = int (input(""))
		print("Select player you want to trade")
		currentPool(poolStorage)
		inputFile2 = int (input(""))
		userStorage, poolStorage = swap(userStorage,poolStorage,inputFile1,inputFile2, choose)
	elif inputFile == 2:
		print("Cancelled")
	print("update")
	playerRoster(userStorage, choose)
	currentPool(poolStorage)
	return userStorage, poolStorage

def swap(userStorage, poolStorage, inputFile1, inputFile2, choose):
	poolStorage.append(userStorage[choose].players.pop(inputFile1-1))
	userStorage[choose].players.append(poolStorage.pop(inputFile2-1))
	return userStorage, poolStorage

def currentPool(poolStorage):
	print("Remaining pool are: ")
	for i in range(0, len(poolStorage)):
		print(str(i+1) + ": " + str(poolStorage[i]))

	#user old list of players for trade, to add and remove

def playerRoster(userStorage, choose):
	print(str(userStorage[choose].name) + "'s current roster is: ")
	for m in range(0, len(userStorage[choose].players)):
		print(str(m+1) + ": " + userStorage[choose].players[m])

def savingData(userStorage,poolStorage, match):
	import pickle

	outputFile = 'test.data'
	fw = open(outputFile, 'wb')
	pickle.dump((userStorage, poolStorage, match), fw)
	fw.close()

def creatingData():
	import pickle

	userStorage = []

	inputNumberOfUsers = int (input('How many players: '))
	for i in range(0, inputNumberOfUsers):
		inputUserName = input('Enter name: ')
		userStorage.append(User(inputUserName))	
	poolStorage = pool()
	poolStorage = picking(inputNumberOfUsers, userStorage, poolStorage)
	match = createMatchup(userStorage)

	outputFile = 'test.data'
	fw = open(outputFile, 'wb')
	pickle.dump((userStorage, poolStorage, match), fw)
	fw.close()

	return userStorage, poolStorage, match

def loadingData():
	import pickle
	inputFile = 'test.data'
	fd = open(inputFile, 'rb')
	userStorage, poolStorage, match = pickle.load(fd)
	return userStorage, poolStorage, match

def pool(): # needs fixing 
	tempStorage = []
	article_read = pd.read_csv('2019.csv', delimiter = ',')
	counter = 0
	for i in range(60):
		counter +=1
		if counter == 11:
			tempStorage.append(article_read.iloc[i][12])
		elif counter == 12:
			tempStorage.append(article_read.iloc[i][12])
			counter = 0
		else:
			tempStorage.append(article_read.iloc[i][11])
	return tempStorage		

def picking(inputNumberOfUsers, userStorage, poolStorage):
	z = 0
	for k in range(0, 1): 										# need to change to 8 for selecting total of 8 players
		for i in range(0, inputNumberOfUsers):
			for j in range(0, len(poolStorage)):
				print(j+1, ": ", poolStorage[j])
			choosingPlayer = int (input(userStorage[i].name + " pick your Player: "))-1
			userStorage[i].players.append(poolStorage.pop(choosingPlayer))
			print (userStorage[i].name, " has chosen: ",userStorage[i].players[z])
		z +=1
	print("Complete picking")
	return poolStorage

#print(combo2(list('ABCDEF'),2))

print("Hello Good Sir/Madam")
main()
print("Good Bye Sir/Madam")


