#!/usr/bin/python3

name = input("Give me your name: ")
age = int(input("Enter your age: "))
repeat = int(input("How many time you want to copy messeges "))
year = (2016-age) + 100
for i in range(0,repeat):
	print ("In the " + str(year) + ", you'll be 100 years old")
