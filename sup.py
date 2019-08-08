import random
max=6
min=1
account=0
a="Y"
while(a=="YES" or a=="Y"):
	credit=int(input("Enter your bidding amount:-"))
	print("--------------------------------Fun Games-----------------------------------\n");
	print("1:7 Up\n");
	print("2:Equals 7\n");
	print("3:7 Down\n");
	print("--------------------------------Fun Games-----------------------------------\n");
	a=random.randint(min,max)
	b=random.randint(min,max)
	c=a+b
	ch=int(input("Enter Your Choice:-"))
	print("Dice is rolling..................")
	print("The answer is: ",c)
	if(ch==1):
	 if(c>7):
	  account=account+credit*2
	  print("Conrats! You won\n")
	 else:
	  account=account-credit
	  print("Sorry You Lose\n")

	elif(ch==2):
	 if(c==7):
	  account=account+credit*5
	  print("Conrats! You won\n")
	 else:
	  account=account-credit
	  print("Sorry You Lose\n")


	elif(ch==3):
	 if(c<7):
	  account=account+credit*2
	  print("Conrats! You won\n")
	 else:
	  account=account-credit
	  print("Sorry You Lose\n")

	else:
		print("wrong input\n")
	print("The balance is\n",account)
	a=input("Do you want to play more:").upper()



