Perms_List=[[a,b],[a,c],[a,d],[a,e],[a,f],[b,c],[b,d],[b,e],[b,f],[c,d],[c,e],[c,f],[d,e],[d,f],[e,f]]
Week=[]
int Weeks = W
int Users = 6
remList = Perms_List
for i in range(0,W)	#No of Weeks
	for j in range(0,2) #No of Games = (Users/2 - 1) only needs to pick games 2 & 3
		if len(Week[i])==0 #Takes care of first game of the week
			Week[i].append(remList[0])
			remPerm.pop(0)
		else #Picks remainder games for the week 
			for k in range(0,len(remPerm)) #Runs through all remaining games
				int Check = 0
				for l in range(0,len(Week[i][l]))
					if remPerm[k][1] != Week[i][l][1] &&  #Checks the elements individually
						remPerm[k][2] != Week[i][l][1] &&
						remPerm[k][1] != Week[i][l][2] &&
						remPerm[k][2] != Week[i][l][2]
							Check++
				if Check==2
					Week[i].append(remList[k])
					remList.pop(k)

					

