#!/usr/bin/python2
#Author: bob
import random
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
'''
a = random.sample(range(1,100), random.randint(5,20))
b = random.sample(range(1,100), random.randint(5,20))
result = [i for i in set(a) if i in b]
print result