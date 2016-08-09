#!/usr/bin/python2
# 1 - Rock
# 2 - Scissors
# 3 - Paper
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
def whoIsTheWinner(player1, player2):
	if player1 = player2:
		return 0
	if player1 = 1: # Rock
		if player2 = 2:
			return 1
		else:
			if player2 = 3:
				return 2
	if player1 = 2: # Scissors
		if player2 = 1:
			return 2
		else:
			if player2 = 3:
				return 1
	if player1 = 3: # Paper
		if player2 = 2:
			return 2
		else:
			if player2 = 1:
				return 1

	
