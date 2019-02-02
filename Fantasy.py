#import myExample makes it run that PY code

class User:
	def __init__(self,userName):
		self.name = userName
		self.storage = []

def main():
	print("Please choose one of the following:")
	print("1. Create")
	print("2. Load")
	dataNumber = int (input("1 or 2"))
	if dataNumber == 1:
		savingData()
	elif dataNumber == 2:
		loadingData()
	else:
		print("error")

def savingData():
	import pickle

	userStorage = []

	inputNumberOfUsers = int (input('How many players: '))
	for i in range(0, inputNumberOfUsers):
		inputUserName = input('Enter name: ')
		userStorage.append(User(inputUserName))	
	realPoolStorage = pool()
	picking(inputNumberOfUsers, userStorage, realPoolStorage)

	outputFile = 'test.data'
	fw = open(outputFile, 'wb')
	pickle.dump(userStorage, fw)
	fw.close()

def loadingData():
	import pickle
	inputFile = 'test.data'
	fd = open(inputFile, 'rb')
	userStorage = pickle.load(fd)

	for l in range(0, len(userStorage)):
		print(userStorage[l].name, "'s final foster is: ")
		for m in range(0, 8):
			print(userStorage[l].storage[m].name)
	print("Fully Complete")

class Player:
	def __init__(self,playerName):
		self.name = playerName
		self.kills = 0
		self.deaths = 0
		self.assists = 0

def pool():
	poolStorage = []
	poolStorage.append(Player("Khan"))
	poolStorage.append(Player("Clid"))
	poolStorage.append(Player("Faker"))
	poolStorage.append(Player("Teddy"))
	poolStorage.append(Player("Mata"))
	poolStorage.append(Player("Impact"))
	poolStorage.append(Player("Xmithie"))
	poolStorage.append(Player("Jensen"))
	poolStorage.append(Player("DoubleLift"))
	poolStorage.append(Player("CoreJJ"))
	poolStorage.append(Player("Wunder"))
	poolStorage.append(Player("Jankos"))
	poolStorage.append(Player("Caps"))
	poolStorage.append(Player("Perkz"))
	poolStorage.append(Player("Mikyx"))
	poolStorage.append(Player("garylala918"))
	poolStorage.append(Player("cwlau"))
	return poolStorage		

def picking(userNum1, user1, pool1):
	z = 0
	for k in range(0, 1):#8):
		for i in range(0, userNum1):
			for j in range(0, len(pool1)):
				print(j+1, ": ", pool1[j].name)
			choosingPlayer = int (input(user1[i].name + " pick your Player: "))-1
			user1[i].storage.append(pool1.pop(choosingPlayer))
			print (user1[i].name, " has chosen: ",user1[i].storage[z].name)
		z +=1
	print("Complete")
	for l in range(0, userNum1):
		print(user1[l].name, "'s final foster is: ")
		for m in range(0, 1):#8):
			print(user1[l].storage[m].name)
	print("Fully Complete")

main()




