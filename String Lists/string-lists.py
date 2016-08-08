#!/usr/bin/python3
# Author: bob

str1 = input("Give me a string: ")

if str1.replace(' ','') == str1[::-1].replace(' ',''):
	print (str1)