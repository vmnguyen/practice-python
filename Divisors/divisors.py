#!/usr/bin/python2
#Author: bob
num = int(input("Give me a number: "))
print filter((lambda x: num % x == 0), range(2,num))