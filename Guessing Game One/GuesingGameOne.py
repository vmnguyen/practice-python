#!/usr/bin/python3
# Author: bob
import random

count = 0
while True:
	num = random.randInt(1,9)
	guess = input("What number did you guess: ")
	if guess = "exit":
		break
	guess = int(guess)
	count = count + 1
	if number == guess:
		print "Not same"

print ("You had taken " + str(count) + " times")