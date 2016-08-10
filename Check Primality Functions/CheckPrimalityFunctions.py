#!/usr/bin/python2
#Author: bob
def isPrimality(num):
	if filter((lambda x: num % x == 0), range(2,num)) == []:
		return True
	return False
def getInt(msg="Give me a number: "):
	return int(input(msg))
num = getInt()
if isPrimality(num):
	print str(num) + " is prime number."
else:
	print str(num) + " isn't prime number."