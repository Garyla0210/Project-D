#import myExample makes it run that PY code

class User:
	def __init__(self,name):
		self.name = name
		self.storage = []

inputNumberOfUsers = int (input('How many players: '))
userStorage = []
for i in range(0, inputNumberOfUsers):
	inputUserName = input('Enter name: ')
	print (i)
	userStorage.append(inputUserName)	
	inputUserName = User(inputUserName)
	print (userStorage[i])


#for(int i = 0, i<inputerNumberOfUsers, i++)



