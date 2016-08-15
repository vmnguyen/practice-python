#!/usr/bin/python3
#Author: bob
import random
def createPassword(strong = 1):
	result = ""
	arr  = "abcdefghijklmnopqrtuvwxyz1234567890!@#$%^&*()"
	

	if strong == 1:
		ranLen = random.randint(12,20)
		for i in range(1,ranLen):
			result = result + arr[random.randint(1,len(arr)-1)]
	else:
		ranLen = random.randint(8,16)
		for i in range(1,ranLen):
			result = result + arr[random.randint(1,len(arr) - 11)]
	return result
print ("1 - Strong Password")
print ("2 - Weak Password")
choise = int(input("How strong do you want with your password: "))
print (createPassword(choise%2))