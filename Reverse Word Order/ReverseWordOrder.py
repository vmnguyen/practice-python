#!/usr/bin/python3
#Author: bob
def revertString(strInput):
	return " ".join((strInput.split(" "))[::-1])
strInput = input("Give me a string: ")
print (revertString(strInput))