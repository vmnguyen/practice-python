#!/usr/bin/python2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Basic problem
for i in set(a):
	if i in b:
		print i,

print 

# Only one line problem
result = [ x for x in set(a) if x in b ]
print result