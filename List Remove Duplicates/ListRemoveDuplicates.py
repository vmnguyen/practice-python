#!/usr/bin/python3
#Author: bob
def removeDuplicatesUsingSet(list):
	return set(list)
def removeDuplicatesUsingForLoop(list):
	result = []
	for i in list:
		if i in result:
			result
		else:
			result.append(i)
	return result

a = [1,1,5,6,2,4,5,2,8,5,10]
print (removeDuplicatesUsingSet(a))
print (removeDuplicatesUsingForLoop(a))