#!/usr/bin/python3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# This is the code for basic problem
'''
for i in a:
	if i < 5:
		print (i)
'''

# This is the code for problem Extra 1 - Use a result array to hold all elements are less than 5
'''
result = []
for i in a:
	if i > 5:
		result.append(i)
print result
'''

# This code for problem Extra 2 - Write in only one line
# Useful link to use lambda, map, filter and reduce: http://www.python-course.eu/lambda.php

print (filter(lambda x: x > 5, a))


# This code for problem Extra 3 - Ask the user for a number and return a list that contains only elements 
# from the original list that are smaller than a number given by user 
num = input("Give me a number: ")
print ("List of numbers smaller than " + str(num) + " are: ")
print (filter(lambda x: x > num, a))