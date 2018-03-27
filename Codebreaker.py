###########################
##     A Simple Game    ###
### --- CODEBREAKER --- ###
##  Nope--Close--Match   ##
###########################

print("--- CODEBREAKER ---")
print("The game goes like this:")
print("1. The computer will think of 3 digit number that has no repeating digits.")
print("2. You will then guess a 3 digit number.")
print("3. The computer will then give back clues, the possible clues are:")
print("     Close: You've guessed a correct number but in the wrong position")
print("     Match: You've guessed a correct number in the correct position")
print("     Nope: You haven't guess any of the numbers correctly")
print("4. Based on these clues you will guess again until you break the code with a perfect match!")

import random
digits = list(range(10))
random.shuffle(digits)
dlist=digits[:3]
# print(dlist)

while 1:
	guess = input("What is your guess? ")
	g1=list(map(int,guess))
	m=0
	c=0
	n=0
	if dlist==g1:
		print("You Won!")
		break
	for i in range(3):
		if dlist[i]==g1[i]:
			m=1
		elif dlist[i] in g1:
			c=1
		else:
			n=1
	if m==1:
		print("Match")
	elif c==1:
		print("Close")
	else:
		print("Nope")