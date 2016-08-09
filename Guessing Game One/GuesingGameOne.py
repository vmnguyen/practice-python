#!/usr/bin/python3
# Author: bob
import random

count = 0
num = random.randint(1,9)
flag = True
while flag:
	while True:
		guess = input("What number did you guess: ")
		if guess == "exit":
			flag = False
			break
		guess = int(guess)
		count = count + 1
		if num == guess:
			print ("Exactly\n")
			print ("Type 'exit' to exit this game\n")
			break
		else:
			if num < guess: 
				print ("Too high")
			if num > guess : 
				print ("Too low")

print ("You had taken " + str(count) + " times")	