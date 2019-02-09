#import myExample makes it run that PY code

class User:
	def __init__(self,userName):
		self.name = userName
		self.storage = []

def main():
	userStorage1 = []
	print("Please choose one of the following:")
	print("1. Create")
	print("2. Load")
	dataNumber = int (input("1 or 2"))
	if dataNumber == 1:
		userStorage1 = savingData()
		print("data saved.")
	elif dataNumber == 2:
		userStorage1 = loadingData()
		print("data loaded.")
	else:
		print("error")

	print("Please choose one of the following:")
	print("1. Overview")
	print("2. Roster")
	print("3. Matchup")
	print("4. Trade")
	dataNumber = int (input("1,2,3,4: "))
	if dataNumber == 1:
		overview(userStorage1)
	elif dataNumber == 2:
		roster(userStorage1)
	elif dataNumber == 3:
		matchup(userStorage1)
	elif dataNumber == 4:
		trade(userStorage1)
	#print(permutation(userStorage1,2)) - prints all permutations 

def overview(userStorage1):
	print("standings")
	#standings

def roster(userStorage1):
	for l in range(0, len(userStorage1)):
		print(userStorage1[l].name, "'s current foster is: ")
		for m in range(0, 1):
			print(userStorage1[l].storage[m].name)

def matchup(userStorage1):
	print("matchups")
	#display current matchup, and option to see other weeks

def trade(userStorage1):
	print("Choose user number: ")
	for i in range (0, len(userStorage1)):
		print(str(i+1)+") "+str(userStorage1[i].name))
	choose = int (input())
	playerRoster(userStorage1, choose)
	#user old list of players for trade, to add and remove

def playerRoster(userStorage1, choose):
	choose -= 1
	print (choose)
	print(len(userStorage1))
	for m in range(0, len(userStorage1[choose].storage)):
		print(userStorage1[choose].storage[m].name)

def savingData():
	import pickle

	userStorage = []

	inputNumberOfUsers = int (input('How many players: '))
	for i in range(0, inputNumberOfUsers):
		inputUserName = input('Enter name: ')
		userStorage.append(User(inputUserName))	
	realPoolStorage = pool()
	realPoolStorage = picking(inputNumberOfUsers, userStorage, realPoolStorage)

	outputFile = 'test.data'
	fw = open(outputFile, 'wb')
	pickle.dump(userStorage, fw)
	fw.close()

	return userStorage
	''', realPoolStorage'''

def loadingData():
	import pickle
	inputFile = 'test.data'
	fd = open(inputFile, 'rb')
	userStorage = pickle.load(fd)
	return userStorage
	'''
	for l in range(0, len(userStorage)):
		print(userStorage[l].name, "'s final foster is: ")
		for m in range(0, 1):
			print(userStorage[l].storage[m].name)
	print("Fully Complete")'''

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
	print("Complete picking")
	return pool1

def permutation(lst,n):
    if n==0:
        return [[]]
    l=[]
    for i in range(0,len(lst)):
        m=lst[i].name
        remLst=lst[i+1:]
        for p in combo2(remLst,n-1):
            l.append([m]+p)
    return l

#print(combo2(list('ABCDEF'),2))

print("start")
main()
print("end")


