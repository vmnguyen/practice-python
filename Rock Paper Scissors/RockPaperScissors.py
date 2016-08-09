#!/usr/bin/python3
# 1 - Rock
# 2 - Scissors
# 3 - Paper
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
def whoIsTheWinner(player1, player2):
	if player1 == player2:
		return 0
	if player1 == 1: # Rock
		if player2 == 2:
			return 1
		else:
			if player2 == 3:
				return 2
	if player1 == 2: # Scissors
		if player2 == 1:
			return 2
		else:
			if player2 == 3:
				return 1
	if player1 == 3: # Paper
		if player2 == 2:
			return 2
		else:
			if player2 == 1:
				return 1


flag = True

while flag:
	while True:
		print ("1 - Rock")
		print ("2 - Scissors")
		print ("3 - Paper\n")
		player1 = int(input("Player1, would you like to choise: "))
		player2 = int(input("Player2, would you like to choise: "))
		if  player1 > 0 and player1 < 4 and player2 > 0 and player2 < 4:
			break
		print ("\n*****You should choise in range 1-3*****")
	result = whoIsTheWinner(player1,player2)
	if result == 0:
		print ("Two player choise same things")
	else:
		print ("Congratulation player " + str(result) + ", you are the winner")
	continues = input("Would you like to play again? [Y/n] \n")
	if continues == 'n':
		flag = False