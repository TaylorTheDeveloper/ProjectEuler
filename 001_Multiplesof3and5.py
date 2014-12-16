#!/usr/bin/env python

#Project Euler
# Problem 1: Multiples of 3 and 5
sum =0
for i in range (0,1000):
	if i%5==0 or i%3==0:
		print i
		sum+=i

print sum