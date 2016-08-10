#!/usr/bin/python2
#Author: bob
def fib(n):
	f = lambda x,_: x + [x[-1] + x[-2]]
	return reduce(f,range(n-2), [1,1])
def getInt(msg="Give me a number: "):
	return int(input(msg))
n = getInt()
print fib(n)
