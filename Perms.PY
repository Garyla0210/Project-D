def main():
	week1 = {}
	week1["match_1"]=[1,2]
	week1["match_2"]=[3,4]

	week = []
	week1 = {}
	week2 = {}
	week3 = {}
	
	players = ['A','B','C','D','E','F']
	row_1 = []
	row_2 = []
	#first week
	print(int(len(players))/2)
	for i in range(0,int(len(players)/2)):
		row_1.append(players[i])
	for i in range(int(len(players)-1),int(len(players)/2)-1, -1):
		row_2.append(players[i])

	print(row_1)
	print(row_2)

	for i in range (0,int(len(players)/2)):
		week1["Match " + str(i+1)]=[row_1[i],row_2[i]]

	print("Week 1: ")
	print(week1)
	print("DONE")

	counter1 = 1
	counter2 = len(players)
	for i in range (0,int(len(players)/2)):
		row_1.pop()
		row_1.append(players[counter2-1])
		row_2.pop(0)
		print(counter1)
		row_2.append(players[counter1])
		for i in range (0,int(len(players)/2)):	
			week1["Match " + str(i+1)]=[row_1[i],row_2[i]]
		counter1+=2
		counter2-=1
		print(week1)
		print("DONE")

'''
	row_1.pop()
	row_1.append(players[3])
	row_2.pop(0)
	row_2.append(players[1])

	print(row_1)
	print(row_2)

	for i in range (0,2):
		week2["Match " + str(i+1)]=[row_1[i],row_2[i]]

	print("Week 2: ")
	print(week2)

	row_1.pop()
	row_1.append(players[2])
	row_2.pop(0)
	row_2.append(players[3])

	print(row_1)
	print(row_2)

	for i in range (0,2):
		week3["Match " + str(i+1)]=[row_1[i],row_2[i]]

	print("Week 3: ")
	print(week3)
'''
main()